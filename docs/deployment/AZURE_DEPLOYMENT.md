# Azure Deployment - Complete Guide

This document provides all necessary information to deploy MiddayMate to Azure.

## Overview

MiddayMate will be deployed to **Azure Container Apps** running in the **australiaeast** region within your **MiddayMate** resource group.

### Architecture

```
┌─────────────────────────────────────────────┐
│         Internet / Browser                   │
└────────────────┬────────────────────────────┘
                 │
         ┌───────▼──────────┐
         │  Azure Container │
         │  Apps (Port 5000)│
         │  middaymate      │
         └───────┬──────────┘
                 │
    ┌────────────┼────────────┐
    │            │            │
┌───▼────┐  ┌───▼────┐  ┌───▼────┐
│ SQLite │  │ Storage│  │  Env   │
│ DB     │  │ Blob   │  │  Vars  │
└────────┘  └────────┘  └────────┘
```

## Deployment Methods

### Method 1: Automated (Recommended)

**Windows (PowerShell):**
```powershell
cd D:\MiddayMate
.\scripts\azure_setup.ps1
```

**macOS/Linux (Bash):**
```bash
cd MiddayMate
bash scripts/azure_setup.sh
```

What this does:
- ✅ Logs into Azure
- ✅ Creates Container Registry
- ✅ Creates Storage Account
- ✅ Optionally creates SQL Database
- ✅ Optionally creates Key Vault
- ✅ Builds Docker image
- ✅ Pushes image to registry
- ✅ Creates Container Apps environment
- ✅ Deploys Container App
- ✅ Provides application URL

**Time**: ~5-10 minutes

### Method 2: Azure Portal (Visual)

Follow the detailed steps in [AZURE_SETUP.md](AZURE_SETUP.md) - Option B section.

**Time**: ~20-30 minutes

### Method 3: Azure CLI Manual

Use the individual CLI commands from [AZURE_SETUP.md](AZURE_SETUP.md) - Option A section.

**Time**: ~15-20 minutes

---

## Pre-Deployment Checklist

- [ ] Azure CLI installed: `az --version`
- [ ] Docker installed: `docker --version`
- [ ] Logged into Azure: `az login`
- [ ] At the MiddayMate project root directory
- [ ] `.env` file created from `.env.example`
- [ ] Docker can build the image: `docker build -t middaymate:latest .`

---

## Step-by-Step (Automated Setup)

### 1. Open Terminal

**Windows**: Open PowerShell as Administrator
```powershell
cd D:\MiddayMate
```

**macOS/Linux**: Open Terminal
```bash
cd /path/to/MiddayMate
```

### 2. Run Setup Script

**Windows**:
```powershell
.\scripts\azure_setup.ps1
```

**macOS/Linux**:
```bash
bash scripts/azure_setup.sh
```

### 3. Answer Prompts

The script will ask:
- Do you want to create SQL Database? (y/n) → Choose based on your needs
- Do you want to create Key Vault? (y/n) → Recommended for production

### 4. Wait for Completion

The script will:
1. Check prerequisites
2. Log in to Azure (opens browser)
3. Create all resources
4. Build Docker image (~2 min)
5. Push to container registry (~1 min)
6. Deploy container app (~3 min)

### 5. Get Your Application URL

At the end, the script displays:
```
Application URL:
https://middaymate.xxx.australiaeast.azurecontainerapps.io
```

Save this URL!

### 6. Wait for App to Start

The container app takes 2-3 minutes to fully start. Monitor with:

```bash
# Watch logs
az containerapp logs show \
  --resource-group MiddayMate \
  --name middaymate \
  --follow
```

### 7. Test the Application

```bash
# Test health endpoint (should return 200 OK)
curl https://middaymate.xxx.australiaeast.azurecontainerapps.io/health

# Or open in browser
https://middaymate.xxx.australiaeast.azurecontainerapps.io
```

---

## Post-Deployment Tasks

### 1. Verify Resources in Azure Portal

Go to: https://portal.azure.com
- Search for "MiddayMate" resource group
- Verify all resources created:
  - Container Registry ✓
  - Storage Account ✓
  - Container App ✓
  - Key Vault (if created) ✓

### 2. Configure Environment Variables

If you need to add OAuth credentials:

```bash
az containerapp update \
  --resource-group MiddayMate \
  --name middaymate \
  --set-env-vars \
    MICROSOFT_CLIENT_ID="your-client-id" \
    MICROSOFT_CLIENT_SECRET="your-client-secret" \
    GOOGLE_CLIENT_ID="your-google-id" \
    GOOGLE_CLIENT_SECRET="your-google-secret"
```

### 3. View Logs

```bash
# Latest logs
az containerapp logs show \
  --resource-group MiddayMate \
  --name middaymate \
  --tail 50

# Follow logs live
az containerapp logs show \
  --resource-group MiddayMate \
  --name middaymate \
  --follow
```

### 4. Monitor Performance

In Azure Portal:
1. Go to MiddayMate resource group
2. Click on "middaymate" Container App
3. Check **Metrics** tab for:
   - CPU usage
   - Memory usage
   - Request count
   - Error rates

### 5. Set Up Custom Domain (Optional)

To use your own domain name:

1. Azure Portal → middaymate Container App
2. Click **Custom domains**
3. Add your domain
4. Update DNS records as instructed

---

## Redeploying After Changes

### Update Application Code

1. Make changes locally
2. Test: `python run.py`
3. Run tests: `pytest`
4. Commit changes: `git add . && git commit -m "..."`

### Push New Version

```bash
# Build new image
docker build -t middaymate:latest .

# Tag for ACR
docker tag middaymate:latest middaymatecr.azurecr.io/middaymate:latest

# Login to ACR
az acr login --name middaymatecr

# Push image
docker push middaymatecr.azurecr.io/middaymate:latest

# Update Container App (auto-redeploys)
az containerapp update \
  --resource-group MiddayMate \
  --name middaymate \
  --image middaymatecr.azurecr.io/middaymate:latest
```

---

## Troubleshooting

### Container App won't start

**Check logs:**
```bash
az containerapp logs show \
  --resource-group MiddayMate \
  --name middaymate \
  --tail 100
```

**Common issues:**
- Missing environment variables → Check `.env` values
- Port mismatch → Should be 5000
- Image not found → Verify Docker image pushed to ACR

### Can't push Docker image

```bash
# Verify ACR login
az acr login --name middaymatecr

# Check image exists
docker image ls | grep middaymate

# Try verbose push
docker push -v middaymatecr.azurecr.io/middaymate:latest
```

### Health check failing

```bash
# Test endpoint
curl -v https://YOUR_URL/health

# Should return:
# HTTP/1.1 200 OK
# {"status": "healthy"}
```

### Storage connection issues

```bash
# Verify storage account exists
az storage account show \
  --resource-group MiddayMate \
  --name middaymatesa

# Get connection string
az storage account show-connection-string \
  --resource-group MiddayMate \
  --name middaymatesa
```

---

## Cost Management

### Estimated Monthly Costs

| Service | Size | Cost |
|---------|------|------|
| Container Registry | Basic | $5 |
| Storage Account | Standard | $0.50-2 |
| Container Apps | 0.5 CPU | $18-40 |
| SQL Database | Basic | $5 (optional) |
| **Total** | | **$30-50** |

### Cost Optimization Tips

1. **Container Apps**: Currently set to 0.5 CPU/1GB RAM (minimum)
2. **Storage**: LRS (locally redundant) is cheapest option
3. **SQL Database**: Only create if needed (MVP uses SQLite)
4. **Monitoring**: Application Insights adds ~$0.60/month

### Stop Container App (to save costs)

```bash
# Scale down to zero (stops the app, saves ~$18/month)
az containerapp update \
  --resource-group MiddayMate \
  --name middaymate \
  --min-replicas 0 \
  --max-replicas 0
```

To restart:
```bash
az containerapp update \
  --resource-group MiddayMate \
  --name middaymate \
  --min-replicas 1 \
  --max-replicas 1
```

---

## Scaling for Growth

### When to Scale

**Scale up CPU/Memory:**
- Response times > 1 second
- Memory usage > 80%
- High error rates

**Scale to multiple replicas:**
- Traffic spikes
- Multiple concurrent users
- High availability needed

### Scale Container App

```bash
# Increase resources
az containerapp update \
  --resource-group MiddayMate \
  --name middaymate \
  --cpu 1.0 \
  --memory 2Gi

# Enable autoscaling
az containerapp update \
  --resource-group MiddayMate \
  --name middaymate \
  --min-replicas 2 \
  --max-replicas 5
```

### Upgrade SQL Database

```bash
# Change SKU if using SQL Database
az sql db update \
  --resource-group MiddayMate \
  --server middaymate-sql \
  --name middaymate \
  --set sku.name=S0  # Standard tier
```

---

## Backup & Recovery

### Backup Container App Configuration

```bash
# Export current config
az containerapp show \
  --resource-group MiddayMate \
  --name middaymate > backup.json
```

### Backup Database (if using SQL)

```bash
# Create point-in-time backup
az sql db restore \
  --resource-group MiddayMate \
  --server middaymate-sql \
  --name middaymate-backup \
  --time "2024-01-15T12:00:00Z" \
  --source-name middaymate
```

### Backup Storage Account

Azure automatically maintains backups. To access:
- Azure Portal → Storage Account → Snapshots

---

## Cleanup (Deleting Everything)

**WARNING**: This deletes all resources!

```bash
# Delete entire resource group
az group delete \
  --name MiddayMate \
  --yes \
  --no-wait
```

---

## Support & Resources

- **Azure Container Apps Docs**: https://learn.microsoft.com/azure/container-apps/
- **Azure CLI Reference**: `az containerapp --help`
- **Container App Troubleshooting**: https://learn.microsoft.com/azure/container-apps/troubleshooting
- **GitHub Issues**: Report issues in project repository

---

## Summary

| Task | Time | Command |
|------|------|---------|
| Setup (automated) | 5-10 min | `./scripts/azure_setup.ps1` |
| Setup (manual) | 20-30 min | Follow AZURE_SETUP.md |
| Test application | 1 min | `curl https://YOUR_URL/health` |
| View logs | 1 min | `az containerapp logs show ...` |
| Redeploy | 5 min | `docker push ... && az containerapp update ...` |

**You're ready to deploy! 🚀**
