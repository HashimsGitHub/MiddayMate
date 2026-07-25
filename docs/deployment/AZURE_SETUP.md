# Azure Setup Guide for MiddayMate

This guide walks you through creating all necessary Azure resources for MiddayMate deployment.

## Prerequisites

- Azure Visual Studio Subscription (you have this ✓)
- Resource Group: `MiddayMate` (already created ✓)
- Region: `australiaeast` ✓
- Azure CLI installed: https://docs.microsoft.com/en-us/cli/azure/install-azure-cli
- Docker installed locally

## Quick Setup (Recommended - Using Azure CLI)

If you prefer command-line setup, skip to the CLI section below. Otherwise, follow the Portal section.

### Setup Order
1. Azure Container Registry (for Docker images)
2. Azure Blob Storage (for user/venue images)
3. Azure SQL Database (future - currently using SQLite)
4. Azure Container Apps (to run the app)
5. Key Vault (for secrets management - optional but recommended)

---

## Option A: Azure CLI Setup (Fastest)

### 1. Login to Azure

```bash
az login
```

This opens your browser. Sign in with your Microsoft account associated with your Visual Studio Subscription.

Verify you're using the correct subscription:
```bash
az account show
```

### 2. Set Variables for Reuse

```bash
# Set these variables
RESOURCE_GROUP="MiddayMate"
REGION="australiaeast"
ACR_NAME="middaymatecr"  # Must be lowercase, no hyphens
STORAGE_ACCOUNT="middaymatesa"  # Must be lowercase, no hyphens
SQL_SERVER="middaymate-sql"
CONTAINER_APP_NAME="middaymate"
KEY_VAULT_NAME="middaymate-kv"

# Verify resource group exists
az group show -n $RESOURCE_GROUP
```

### 3. Create Azure Container Registry

```bash
az acr create \
  --resource-group $RESOURCE_GROUP \
  --name $ACR_NAME \
  --sku Basic \
  --admin-enabled true

# Get login credentials
az acr credential show \
  --resource-group $RESOURCE_GROUP \
  --name $ACR_NAME
```

**Save these credentials** - you'll need them for Docker login.

### 4. Create Azure Storage Account (Blob Storage)

```bash
az storage account create \
  --resource-group $RESOURCE_GROUP \
  --name $STORAGE_ACCOUNT \
  --location $REGION \
  --sku Standard_LRS

# Create container for images
az storage container create \
  --account-name $STORAGE_ACCOUNT \
  --name middaymate \
  --auth-mode login

# Get connection string (save this)
az storage account show-connection-string \
  --resource-group $RESOURCE_GROUP \
  --name $STORAGE_ACCOUNT \
  --query connectionString \
  -o tsv
```

### 5. Create Azure SQL Database (Optional - For Future)

```bash
# Create SQL Server
az sql server create \
  --resource-group $RESOURCE_GROUP \
  --name $SQL_SERVER \
  --location $REGION \
  --admin-user sqladmin \
  --admin-password "YourStrongPassword123!" \
  --enable-public-network true

# Create database
az sql db create \
  --resource-group $RESOURCE_GROUP \
  --server $SQL_SERVER \
  --name middaymate \
  --sku Basic \
  --backup-storage-redundancy Local

# Configure firewall to allow your IP
az sql server firewall-rule create \
  --resource-group $RESOURCE_GROUP \
  --server $SQL_SERVER \
  --name AllowMyIP \
  --start-ip-address YOUR_IP_ADDRESS \
  --end-ip-address YOUR_IP_ADDRESS

# Get connection string
az sql db show-connection-string \
  --server $SQL_SERVER \
  --name middaymate \
  --client sqlserver
```

### 6. Create Key Vault for Secrets

```bash
az keyvault create \
  --resource-group $RESOURCE_GROUP \
  --name $KEY_VAULT_NAME \
  --location $REGION \
  --enable-purge-protection true

# Add secrets
az keyvault secret set \
  --vault-name $KEY_VAULT_NAME \
  --name "DatabaseUrl" \
  --value "sqlite:///middaymate.db"

az keyvault secret set \
  --vault-name $KEY_VAULT_NAME \
  --name "SecretKey" \
  --value "your-secret-key-here"

az keyvault secret set \
  --vault-name $KEY_VAULT_NAME \
  --name "AzureStorageConnectionString" \
  --value "YOUR_CONNECTION_STRING"
```

### 7. Build and Push Docker Image

```bash
# Login to ACR
az acr login --name $ACR_NAME

# Build image
docker build -t middaymate:latest .

# Tag image for ACR
docker tag middaymate:latest $ACR_NAME.azurecr.io/middaymate:latest

# Push to ACR
docker push $ACR_NAME.azurecr.io/middaymate:latest

# List images in ACR
az acr repository list --name $ACR_NAME
```

### 8. Create Azure Container Apps Environment

```bash
# Create environment
az containerapp env create \
  --resource-group $RESOURCE_GROUP \
  --name middaymate-env \
  --location $REGION

# Create Container App
az containerapp create \
  --resource-group $RESOURCE_GROUP \
  --name $CONTAINER_APP_NAME \
  --environment middaymate-env \
  --image $ACR_NAME.azurecr.io/middaymate:latest \
  --registry-server $ACR_NAME.azurecr.io \
  --registry-username $(az acr credential show -n $ACR_NAME --query username -o tsv) \
  --registry-password $(az acr credential show -n $ACR_NAME --query "passwords[0].value" -o tsv) \
  --target-port 5000 \
  --ingress external \
  --cpu 0.5 \
  --memory 1Gi \
  --env-vars \
    FLASK_ENV=production \
    SECRET_KEY="your-secret-key" \
    DATABASE_URL="sqlite:///middaymate.db" \
    AZURE_STORAGE_CONNECTION_STRING="your-storage-connection-string"

# Get the application URL
az containerapp show \
  --resource-group $RESOURCE_GROUP \
  --name $CONTAINER_APP_NAME \
  --query properties.latestRevisionFqdn
```

---

## Option B: Azure Portal Setup (Visual Steps)

### 1. Create Container Registry

1. Go to https://portal.azure.com
2. Click **Create a resource**
3. Search for "Container Registry"
4. Click **Create**
5. Fill in:
   - **Subscription**: Your Visual Studio Subscription
   - **Resource group**: MiddayMate
   - **Registry name**: `middaymatecr` (must be lowercase)
   - **Location**: Australia East
   - **SKU**: Basic
6. Click **Review + create** → **Create**

Wait for deployment to complete.

### 2. Create Storage Account

1. Click **Create a resource**
2. Search for "Storage account"
3. Click **Create**
4. Fill in:
   - **Subscription**: Your Visual Studio Subscription
   - **Resource group**: MiddayMate
   - **Storage account name**: `middaymatesa`
   - **Region**: Australia East
   - **Performance**: Standard
   - **Redundancy**: Locally-redundant storage (LRS)
5. Click **Review + create** → **Create**

Once created:
- Go to the storage account
- Click **Containers** (left sidebar)
- Click **+ Container**
- Name: `middaymate`
- Click **Create**

### 3. Create SQL Database (Optional)

1. Click **Create a resource**
2. Search for "SQL Database"
3. Click **Create**
4. Fill in:
   - **Subscription**: Your Visual Studio Subscription
   - **Resource group**: MiddayMate
   - **Database name**: `middaymate`
   - **Server**: Create new
     - **Server name**: `middaymate-sql`
     - **Location**: Australia East
     - **Authentication**: SQL authentication
     - **Admin login**: `sqladmin`
     - **Password**: Create a strong password
   - **Compute + storage**: Basic (for development)
5. Click **Review + create** → **Create**

Configure firewall:
- Go to the SQL Server (not database)
- Click **Networking**
- Click **Add your client IPv4 address**
- Click **Save**

### 4. Create Key Vault (Optional)

1. Click **Create a resource**
2. Search for "Key Vault"
3. Click **Create**
4. Fill in:
   - **Subscription**: Your Visual Studio Subscription
   - **Resource group**: MiddayMate
   - **Key Vault name**: `middaymate-kv`
   - **Location**: Australia East
   - **Pricing tier**: Standard
5. Click **Review + create** → **Create**

Once created:
- Click **Secrets** (left sidebar)
- Click **Generate/Import**
- Create secrets:
  - Name: `DatabaseUrl`, Value: `sqlite:///middaymate.db`
  - Name: `SecretKey`, Value: your secret key
  - Name: `AzureStorageConnectionString`, Value: your connection string

### 5. Build Docker Image Locally

```bash
cd D:\MiddayMate
docker build -t middaymate:latest .
```

### 6. Push to Container Registry

In Azure Portal:
1. Go to your Container Registry (middaymatecr)
2. Click **Access keys** (left sidebar)
3. Enable **Admin user**
4. Copy the login server, username, and password

Then locally:
```bash
# Login to your registry
docker login -u <username> -p <password> <login-server>

# Tag image
docker tag middaymate:latest <login-server>/middaymate:latest

# Push image
docker push <login-server>/middaymate:latest
```

### 7. Create Container Apps

1. Click **Create a resource**
2. Search for "Container Apps"
3. Click **Create**
4. Fill in:
   - **Subscription**: Your Visual Studio Subscription
   - **Resource group**: MiddayMate
   - **Container App name**: `middaymate`
   - **Region**: Australia East
5. Click **Container Image**:
   - **Image source**: Azure Container Registry
   - **Registry**: middaymatecr
   - **Image**: middaymate
   - **Image tag**: latest
6. Click **Ingress**:
   - **Ingress**: Enabled
   - **Ingress traffic**: External
   - **Target port**: 5000
7. **Environment variables**:
   ```
   FLASK_ENV = production
   SECRET_KEY = your-secret-key
   DATABASE_URL = sqlite:///middaymate.db
   AZURE_STORAGE_CONNECTION_STRING = your-connection-string
   ```
8. Click **Review + create** → **Create**

Once created, get your application URL from the **Overview** tab.

---

## Verifying Your Setup

### Check Container Registry
```bash
az acr list --resource-group MiddayMate --query "[].name"
```

### Check Storage Account
```bash
az storage account list --resource-group MiddayMate --query "[].name"
```

### Check Container App is Running
```bash
az containerapp show \
  --resource-group MiddayMate \
  --name middaymate \
  --query properties.latestRevisionFqdn
```

### Test Your Application
```bash
# Get the FQDN from above and test it
curl https://<your-fqdn>/health
```

---

## Environment Variables for Container App

Create a `.env` file with:

```env
FLASK_ENV=production
FLASK_APP=run.py
SECRET_KEY=your-secure-secret-key-here
DATABASE_URL=sqlite:///middaymate.db
AZURE_STORAGE_CONNECTION_STRING=your-connection-string
AZURE_STORAGE_CONTAINER=middaymate
MICROSOFT_CLIENT_ID=your-client-id
MICROSOFT_CLIENT_SECRET=your-client-secret
GOOGLE_CLIENT_ID=your-client-id
GOOGLE_CLIENT_SECRET=your-client-secret
```

Set these in Container App **Environment variables** section.

---

## Cost Estimation

Approximate monthly costs (Australia East):
- **Container Registry (Basic)**: ~$5
- **Storage Account (Standard LRS)**: ~$0.50-2 depending on usage
- **SQL Database (Basic)**: ~$5 (if using)
- **Container Apps**: ~$18-40 depending on usage
- **Key Vault**: ~$0.60

**Total**: ~$30-50/month for MVP

---

## Scaling for Production

When ready to scale:
1. Container Registry: Upgrade to Standard/Premium
2. Storage Account: Enable geo-redundancy
3. SQL Database: Upgrade tier if needed
4. Container Apps: Increase CPU/memory, enable autoscaling
5. Application Insights: Add monitoring
6. Application Gateway: Add for advanced routing
7. Azure CDN: Cache static assets

---

## Troubleshooting

### Container App not starting
```bash
az containerapp logs show \
  --resource-group MiddayMate \
  --name middaymate \
  --follow
```

### Connection string issues
Verify in Azure Portal → Storage Account → Access keys

### Docker push fails
```bash
az acr login --name middaymatecr
docker logout
docker login -u <username> -p <password> <server>
```

### SQL connection issues
Check Networking → Firewall rules to ensure your IP is allowed

---

## Next Steps

1. ✅ Create resources (this guide)
2. Build and push Docker image
3. Deploy to Container Apps
4. Configure custom domain (optional)
5. Set up continuous deployment from GitHub (optional)
6. Monitor with Application Insights (optional)

---

## Useful Links

- [Azure Container Apps Documentation](https://learn.microsoft.com/en-us/azure/container-apps/)
- [Azure Container Registry](https://learn.microsoft.com/en-us/azure/container-registry/)
- [Azure Storage](https://learn.microsoft.com/en-us/azure/storage/)
- [Azure SQL Database](https://learn.microsoft.com/en-us/azure/azure-sql/database/)
- [Azure Key Vault](https://learn.microsoft.com/en-us/azure/key-vault/)
