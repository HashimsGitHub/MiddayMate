#!/bin/bash

# MiddayMate Azure Setup Automation Script
# This script automates the creation of all necessary Azure resources
# Usage: bash scripts/azure_setup.sh

set -e

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Configuration
RESOURCE_GROUP="MiddayMate"
REGION="australiaeast"
ACR_NAME="middaymatecr"
STORAGE_ACCOUNT="middaymatesa"
SQL_SERVER="middaymate-sql"
CONTAINER_APP_NAME="middaymate"
KEY_VAULT_NAME="middaymate-kv"
CONTAINER_APP_ENV="middaymate-env"

echo -e "${BLUE}=== MiddayMate Azure Setup ===${NC}\n"

# Function to print steps
print_step() {
    echo -e "${GREEN}✓${NC} $1"
}

print_info() {
    echo -e "${BLUE}ℹ${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}⚠${NC} $1"
}

print_error() {
    echo -e "${RED}✗${NC} $1"
}

# Check prerequisites
print_info "Checking prerequisites..."

if ! command -v az &> /dev/null; then
    print_error "Azure CLI not found. Install from: https://docs.microsoft.com/cli/azure/install-azure-cli"
    exit 1
fi

if ! command -v docker &> /dev/null; then
    print_error "Docker not found. Install from: https://www.docker.com/get-started"
    exit 1
fi

print_step "Prerequisites check passed"

# Login to Azure
print_info "Logging in to Azure..."
az login

# Check resource group
print_info "Verifying resource group..."
if ! az group show --name $RESOURCE_GROUP &> /dev/null; then
    print_warning "Resource group $RESOURCE_GROUP not found. Creating..."
    az group create --name $RESOURCE_GROUP --location $REGION
fi
print_step "Resource group verified: $RESOURCE_GROUP"

# 1. Create Container Registry
print_info "Creating Container Registry..."
if az acr show --resource-group $RESOURCE_GROUP --name $ACR_NAME &> /dev/null; then
    print_warning "Container Registry $ACR_NAME already exists"
else
    az acr create \
        --resource-group $RESOURCE_GROUP \
        --name $ACR_NAME \
        --sku Basic \
        --admin-enabled true
    print_step "Container Registry created: $ACR_NAME"
fi

# Get ACR credentials
ACR_USERNAME=$(az acr credential show --resource-group $RESOURCE_GROUP --name $ACR_NAME --query username -o tsv)
ACR_PASSWORD=$(az acr credential show --resource-group $RESOURCE_GROUP --name $ACR_NAME --query "passwords[0].value" -o tsv)
ACR_SERVER=$(az acr show --resource-group $RESOURCE_GROUP --name $ACR_NAME --query loginServer -o tsv)

print_info "ACR Server: $ACR_SERVER"
print_info "ACR Username: $ACR_USERNAME"

# 2. Create Storage Account
print_info "Creating Storage Account..."
if az storage account show --resource-group $RESOURCE_GROUP --name $STORAGE_ACCOUNT &> /dev/null; then
    print_warning "Storage Account $STORAGE_ACCOUNT already exists"
else
    az storage account create \
        --resource-group $RESOURCE_GROUP \
        --name $STORAGE_ACCOUNT \
        --location $REGION \
        --sku Standard_LRS
    print_step "Storage Account created: $STORAGE_ACCOUNT"
fi

# Create blob container
print_info "Creating blob container..."
az storage container create \
    --account-name $STORAGE_ACCOUNT \
    --name middaymate \
    --auth-mode login 2>/dev/null || print_warning "Container already exists"

# Get storage connection string
STORAGE_CONNECTION_STRING=$(az storage account show-connection-string \
    --resource-group $RESOURCE_GROUP \
    --name $STORAGE_ACCOUNT \
    --query connectionString -o tsv)

print_step "Storage Account configured"

# 3. Create SQL Database (Optional)
read -p "Create SQL Database? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    print_info "Creating SQL Server..."
    if az sql server show --resource-group $RESOURCE_GROUP --name $SQL_SERVER &> /dev/null; then
        print_warning "SQL Server $SQL_SERVER already exists"
    else
        SQL_ADMIN_PASSWORD=$(openssl rand -base64 32)

        az sql server create \
            --resource-group $RESOURCE_GROUP \
            --name $SQL_SERVER \
            --location $REGION \
            --admin-user sqladmin \
            --admin-password "$SQL_ADMIN_PASSWORD" \
            --enable-public-network true

        print_step "SQL Server created: $SQL_SERVER"
        print_warning "SQL Admin Password: $SQL_ADMIN_PASSWORD (save this!)"
    fi

    print_info "Creating SQL Database..."
    az sql db create \
        --resource-group $RESOURCE_GROUP \
        --server $SQL_SERVER \
        --name middaymate \
        --sku Basic \
        --backup-storage-redundancy Local 2>/dev/null || print_warning "Database already exists"

    print_step "SQL Database created"
fi

# 4. Create Key Vault (Optional)
read -p "Create Key Vault? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    print_info "Creating Key Vault..."
    if az keyvault show --resource-group $RESOURCE_GROUP --name $KEY_VAULT_NAME &> /dev/null; then
        print_warning "Key Vault $KEY_VAULT_NAME already exists"
    else
        az keyvault create \
            --resource-group $RESOURCE_GROUP \
            --name $KEY_VAULT_NAME \
            --location $REGION \
            --enable-purge-protection true
        print_step "Key Vault created: $KEY_VAULT_NAME"
    fi
fi

# 5. Build Docker image
print_info "Building Docker image..."
docker build -t middaymate:latest . || {
    print_error "Docker build failed"
    exit 1
}
print_step "Docker image built"

# 6. Login to ACR and push image
print_info "Logging in to Azure Container Registry..."
echo $ACR_PASSWORD | docker login -u $ACR_USERNAME --password-stdin $ACR_SERVER

print_info "Tagging image for ACR..."
docker tag middaymate:latest $ACR_SERVER/middaymate:latest

print_info "Pushing image to ACR..."
docker push $ACR_SERVER/middaymate:latest
print_step "Image pushed to ACR"

# 7. Create Container Apps Environment
print_info "Creating Container Apps environment..."
if az containerapp env show --resource-group $RESOURCE_GROUP --name $CONTAINER_APP_ENV &> /dev/null; then
    print_warning "Container Apps environment already exists"
else
    az containerapp env create \
        --resource-group $RESOURCE_GROUP \
        --name $CONTAINER_APP_ENV \
        --location $REGION
    print_step "Container Apps environment created"
fi

# 8. Create Container App
print_info "Creating Container App..."
if az containerapp show --resource-group $RESOURCE_GROUP --name $CONTAINER_APP_NAME &> /dev/null; then
    print_warning "Container App already exists. Updating..."
    az containerapp update \
        --resource-group $RESOURCE_GROUP \
        --name $CONTAINER_APP_NAME \
        --image $ACR_SERVER/middaymate:latest
else
    az containerapp create \
        --resource-group $RESOURCE_GROUP \
        --name $CONTAINER_APP_NAME \
        --environment $CONTAINER_APP_ENV \
        --image $ACR_SERVER/middaymate:latest \
        --registry-server $ACR_SERVER \
        --registry-username $ACR_USERNAME \
        --registry-password $ACR_PASSWORD \
        --target-port 5000 \
        --ingress external \
        --cpu 0.5 \
        --memory 1Gi \
        --env-vars \
            FLASK_ENV=production \
            SECRET_KEY="$(openssl rand -base64 32)" \
            DATABASE_URL="sqlite:///middaymate.db" \
            AZURE_STORAGE_CONNECTION_STRING="$STORAGE_CONNECTION_STRING" \
            AZURE_STORAGE_CONTAINER="middaymate"
    print_step "Container App created: $CONTAINER_APP_NAME"
fi

# Get application URL
APP_FQDN=$(az containerapp show \
    --resource-group $RESOURCE_GROUP \
    --name $CONTAINER_APP_NAME \
    --query properties.latestRevisionFqdn -o tsv)

# Summary
echo -e "\n${GREEN}=== Setup Complete ===${NC}\n"
print_step "All Azure resources created successfully!"
echo -e "\n${BLUE}Important Information:${NC}"
echo "Resource Group: $RESOURCE_GROUP"
echo "Region: $REGION"
echo "Container Registry: $ACR_SERVER"
echo "Storage Account: $STORAGE_ACCOUNT"
echo "Container App: $CONTAINER_APP_NAME"
echo -e "\n${BLUE}Application URL:${NC}"
echo "https://$APP_FQDN"
echo -e "\n${BLUE}Test Application:${NC}"
echo "curl https://$APP_FQDN/health"
echo -e "\n${YELLOW}Save these for future reference:${NC}"
echo "Storage Connection String: $STORAGE_CONNECTION_STRING"
echo -e "\n${BLUE}Next Steps:${NC}"
echo "1. Wait 2-3 minutes for Container App to fully start"
echo "2. Test the application: curl https://$APP_FQDN/health"
echo "3. View logs: az containerapp logs show --resource-group $RESOURCE_GROUP --name $CONTAINER_APP_NAME"
echo "4. Configure environment variables if needed"
echo "5. Set up custom domain (optional)"
