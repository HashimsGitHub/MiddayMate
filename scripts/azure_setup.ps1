# MiddayMate Azure Setup Automation Script (PowerShell)
# This script automates the creation of all necessary Azure resources
# Usage: .\scripts\azure_setup.ps1

param(
    [switch]$SkipSQLDatabase,
    [switch]$SkipKeyVault
)

# Configuration
$ResourceGroup = "MiddayMate"
$Region = "australiaeast"
$ACRName = "middaymatecr"
$StorageAccount = "middaymatesa"
$SQLServer = "middaymate-sql"
$ContainerAppName = "middaymate"
$KeyVaultName = "middaymate-kv"
$ContainerAppEnv = "middaymate-env"

# Color functions
function Write-Success {
    param([string]$Message)
    Write-Host "✓ $Message" -ForegroundColor Green
}

function Write-Info {
    param([string]$Message)
    Write-Host "ℹ $Message" -ForegroundColor Cyan
}

function Write-Warning {
    param([string]$Message)
    Write-Host "⚠ $Message" -ForegroundColor Yellow
}

function Write-Error {
    param([string]$Message)
    Write-Host "✗ $Message" -ForegroundColor Red
}

Write-Host "=== MiddayMate Azure Setup ===" -ForegroundColor Blue
Write-Host ""

# Check prerequisites
Write-Info "Checking prerequisites..."

$azFound = Get-Command az -ErrorAction SilentlyContinue
if (-not $azFound) {
    Write-Error "Azure CLI not found. Install from: https://docs.microsoft.com/cli/azure/install-azure-cli"
    exit 1
}

$dockerFound = Get-Command docker -ErrorAction SilentlyContinue
if (-not $dockerFound) {
    Write-Error "Docker not found. Install from: https://www.docker.com/get-started"
    exit 1
}

Write-Success "Prerequisites check passed"

# Login to Azure
Write-Info "Logging in to Azure..."
az login

# Verify resource group
Write-Info "Verifying resource group..."
$groupExists = az group exists --name $ResourceGroup | ConvertFrom-Json
if (-not $groupExists) {
    Write-Warning "Resource group $ResourceGroup not found. Creating..."
    az group create --name $ResourceGroup --location $Region
}
Write-Success "Resource group verified: $ResourceGroup"

# 1. Create Container Registry
Write-Info "Creating Container Registry..."
$acrExists = az acr show --resource-group $ResourceGroup --name $ACRName --query "id" -o tsv 2>$null
if ($acrExists) {
    Write-Warning "Container Registry $ACRName already exists"
} else {
    az acr create `
        --resource-group $ResourceGroup `
        --name $ACRName `
        --sku Basic `
        --admin-enabled true
    Write-Success "Container Registry created: $ACRName"
}

# Get ACR credentials
$ACRUsername = az acr credential show --resource-group $ResourceGroup --name $ACRName --query username -o tsv
$ACRPassword = az acr credential show --resource-group $ResourceGroup --name $ACRName --query "passwords[0].value" -o tsv
$ACRServer = az acr show --resource-group $ResourceGroup --name $ACRName --query loginServer -o tsv

Write-Info "ACR Server: $ACRServer"
Write-Info "ACR Username: $ACRUsername"

# 2. Create Storage Account
Write-Info "Creating Storage Account..."
$storageExists = az storage account show --resource-group $ResourceGroup --name $StorageAccount --query "id" -o tsv 2>$null
if ($storageExists) {
    Write-Warning "Storage Account $StorageAccount already exists"
} else {
    az storage account create `
        --resource-group $ResourceGroup `
        --name $StorageAccount `
        --location $Region `
        --sku Standard_LRS
    Write-Success "Storage Account created: $StorageAccount"
}

# Create blob container
Write-Info "Creating blob container..."
az storage container create `
    --account-name $StorageAccount `
    --name middaymate `
    --auth-mode login 2>$null
Write-Success "Storage Account configured"

# Get storage connection string
$StorageConnectionString = az storage account show-connection-string `
    --resource-group $ResourceGroup `
    --name $StorageAccount `
    --query connectionString -o tsv

# 3. Create SQL Database (Optional)
if (-not $SkipSQLDatabase) {
    $createSQL = Read-Host "Create SQL Database? (y/n)"
    if ($createSQL -eq "y" -or $createSQL -eq "Y") {
        Write-Info "Creating SQL Server..."
        $sqlExists = az sql server show --resource-group $ResourceGroup --name $SQLServer --query "id" -o tsv 2>$null

        if ($sqlExists) {
            Write-Warning "SQL Server $SQLServer already exists"
        } else {
            $sqlPassword = -join ((33..126) | Get-Random -Count 32 | ForEach-Object {[char]$_})

            az sql server create `
                --resource-group $ResourceGroup `
                --name $SQLServer `
                --location $Region `
                --admin-user sqladmin `
                --admin-password $sqlPassword `
                --enable-public-network true

            Write-Success "SQL Server created: $SQLServer"
            Write-Warning "SQL Admin Password: $sqlPassword (save this!)"
        }

        Write-Info "Creating SQL Database..."
        az sql db create `
            --resource-group $ResourceGroup `
            --server $SQLServer `
            --name middaymate `
            --sku Basic `
            --backup-storage-redundancy Local 2>$null
        Write-Success "SQL Database created"
    }
}

# 4. Create Key Vault (Optional)
if (-not $SkipKeyVault) {
    $createKV = Read-Host "Create Key Vault? (y/n)"
    if ($createKV -eq "y" -or $createKV -eq "Y") {
        Write-Info "Creating Key Vault..."
        $kvExists = az keyvault show --resource-group $ResourceGroup --name $KeyVaultName --query "id" -o tsv 2>$null

        if ($kvExists) {
            Write-Warning "Key Vault $KeyVaultName already exists"
        } else {
            az keyvault create `
                --resource-group $ResourceGroup `
                --name $KeyVaultName `
                --location $Region `
                --enable-purge-protection true
            Write-Success "Key Vault created: $KeyVaultName"
        }
    }
}

# 5. Build Docker image
Write-Info "Building Docker image..."
docker build -t middaymate:latest . 2>&1 | Out-Null
if ($LASTEXITCODE -ne 0) {
    Write-Error "Docker build failed"
    exit 1
}
Write-Success "Docker image built"

# 6. Login to ACR and push image
Write-Info "Logging in to Azure Container Registry..."
$ACRPassword | docker login -u $ACRUsername --password-stdin $ACRServer 2>&1 | Out-Null

Write-Info "Tagging image for ACR..."
docker tag middaymate:latest "$ACRServer/middaymate:latest" 2>&1 | Out-Null

Write-Info "Pushing image to ACR..."
docker push "$ACRServer/middaymate:latest" 2>&1 | Out-Null
Write-Success "Image pushed to ACR"

# 7. Create Container Apps Environment
Write-Info "Creating Container Apps environment..."
$envExists = az containerapp env show --resource-group $ResourceGroup --name $ContainerAppEnv --query "id" -o tsv 2>$null

if ($envExists) {
    Write-Warning "Container Apps environment already exists"
} else {
    az containerapp env create `
        --resource-group $ResourceGroup `
        --name $ContainerAppEnv `
        --location $Region
    Write-Success "Container Apps environment created"
}

# 8. Create Container App
Write-Info "Creating Container App..."
$appExists = az containerapp show --resource-group $ResourceGroup --name $ContainerAppName --query "id" -o tsv 2>$null

if ($appExists) {
    Write-Warning "Container App already exists. Updating..."
    az containerapp update `
        --resource-group $ResourceGroup `
        --name $ContainerAppName `
        --image "$ACRServer/middaymate:latest"
} else {
    $secretKey = -join ((33..126) | Get-Random -Count 32 | ForEach-Object {[char]$_})

    az containerapp create `
        --resource-group $ResourceGroup `
        --name $ContainerAppName `
        --environment $ContainerAppEnv `
        --image "$ACRServer/middaymate:latest" `
        --registry-server $ACRServer `
        --registry-username $ACRUsername `
        --registry-password $ACRPassword `
        --target-port 5000 `
        --ingress external `
        --cpu 0.5 `
        --memory 1Gi `
        --env-vars `
            FLASK_ENV=production `
            SECRET_KEY=$secretKey `
            DATABASE_URL="sqlite:///middaymate.db" `
            AZURE_STORAGE_CONNECTION_STRING=$StorageConnectionString `
            AZURE_STORAGE_CONTAINER="middaymate"
    Write-Success "Container App created: $ContainerAppName"
}

# Get application URL
$AppFQDN = az containerapp show `
    --resource-group $ResourceGroup `
    --name $ContainerAppName `
    --query properties.latestRevisionFqdn -o tsv

# Summary
Write-Host ""
Write-Host "=== Setup Complete ===" -ForegroundColor Green
Write-Host ""

Write-Success "All Azure resources created successfully!"
Write-Host ""

Write-Host "Important Information:" -ForegroundColor Cyan
Write-Host "  Resource Group: $ResourceGroup"
Write-Host "  Region: $Region"
Write-Host "  Container Registry: $ACRServer"
Write-Host "  Storage Account: $StorageAccount"
Write-Host "  Container App: $ContainerAppName"
Write-Host ""

Write-Host "Application URL:" -ForegroundColor Cyan
Write-Host "  https://$AppFQDN" -ForegroundColor Yellow
Write-Host ""

Write-Host "Test Application:" -ForegroundColor Cyan
Write-Host "  curl https://$AppFQDN/health"
Write-Host ""

Write-Host "Save for future reference:" -ForegroundColor Yellow
Write-Host "  Storage Connection String: $StorageConnectionString"
Write-Host ""

Write-Host "Next Steps:" -ForegroundColor Cyan
Write-Host "  1. Wait 2-3 minutes for Container App to fully start"
Write-Host "  2. Test the application: curl https://$AppFQDN/health"
Write-Host "  3. View logs: az containerapp logs show --resource-group $ResourceGroup --name $ContainerAppName"
Write-Host "  4. Configure environment variables if needed"
Write-Host "  5. Set up custom domain (optional)"
