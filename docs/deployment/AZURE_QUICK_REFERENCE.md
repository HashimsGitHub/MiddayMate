# Azure Setup - Quick Reference

**Subscription**: Visual Studio Subscription  
**Resource Group**: MiddayMate  
**Region**: australiaeast  

## 5-Minute Checklist

- [ ] Install Azure CLI: `az login`
- [ ] Create Container Registry: `middaymatecr`
- [ ] Create Storage Account: `middaymatesa`
- [ ] Create SQL Database: `middaymate-sql` (optional, future)
- [ ] Build Docker image: `docker build -t middaymate:latest .`
- [ ] Push to registry: `docker push middaymatecr.azurecr.io/middaymate:latest`
- [ ] Create Container Apps environment
- [ ] Deploy Container App
- [ ] Test with health endpoint: `/health`

## Key Resource Names

| Resource | Name | Type |
|----------|------|------|
| Container Registry | `middaymatecr` | ACR |
| Storage Account | `middaymatesa` | Storage |
| SQL Server | `middaymate-sql` | SQL Server |
| SQL Database | `middaymate` | SQL Database |
| Container App | `middaymate` | App |
| Key Vault | `middaymate-kv` | Vault |
| Env: Container Apps | `middaymate-env` | Env |

## Connection Strings to Save

**Storage Account Connection String**
```
DefaultEndpointsProtocol=https;AccountName=middaymatesa;AccountKey=...
```

**SQL Connection String** (when using)
```
Server=tcp:middaymate-sql.database.windows.net,1433;Initial Catalog=middaymate;Persist Security Info=False;User ID=sqladmin;Password=...;Encrypt=True;Connection Timeout=30;
```

## Environment Variables to Set in Container Apps

```env
FLASK_ENV=production
FLASK_APP=run.py
SECRET_KEY=<generate-strong-secret>
DATABASE_URL=sqlite:///middaymate.db
AZURE_STORAGE_CONNECTION_STRING=<your-storage-connection-string>
AZURE_STORAGE_CONTAINER=middaymate
```

## Azure CLI One-Liners

**Check resources exist**
```bash
az resource list --resource-group MiddayMate --output table
```

**Delete resource group (caution!)**
```bash
az group delete --name MiddayMate --yes --no-wait
```

**Get Container App URL**
```bash
az containerapp show --resource-group MiddayMate --name middaymate --query properties.latestRevisionFqdn
```

**View logs**
```bash
az containerapp logs show --resource-group MiddayMate --name middaymate --follow
```

**Update Container App image**
```bash
az containerapp update \
  --resource-group MiddayMate \
  --name middaymate \
  --image middaymatecr.azurecr.io/middaymate:latest
```

## Estimated Costs (per month)

| Service | Cost |
|---------|------|
| Container Registry (Basic) | $5 |
| Storage Account | $0.50-2 |
| SQL Database (Basic) | $5 |
| Container Apps | $18-40 |
| **Total** | **~$30-50** |

## Docker Commands

```bash
# Build
docker build -t middaymate:latest .

# Login to ACR
az acr login --name middaymatecr

# Tag
docker tag middaymate:latest middaymatecr.azurecr.io/middaymate:latest

# Push
docker push middaymatecr.azurecr.io/middaymate:latest

# Test locally
docker run -p 5000:5000 middaymate:latest
```

## Port Mappings

| Service | Port | Notes |
|---------|------|-------|
| Flask App | 5000 | Internal |
| Container Apps | 80/443 | External HTTPS |
| SQL Server | 1433 | Azure only |
| Storage Blob | 443 | Azure only |

## Firewall Rules

**For SQL Database** - Allow your IP:
```bash
az sql server firewall-rule create \
  --resource-group MiddayMate \
  --server middaymate-sql \
  --name "AllowMyIP" \
  --start-ip-address <YOUR_IP> \
  --end-ip-address <YOUR_IP>
```

## Status Checks

**Is Container App running?**
```bash
curl https://<your-app-url>/health
```

**Check image in registry**
```bash
az acr repository list --name middaymatecr
```

**Check storage connectivity**
```bash
az storage account show-connection-string \
  --resource-group MiddayMate \
  --name middaymatesa
```

## Need Help?

- Azure CLI docs: `az --help`
- Container Apps: https://learn.microsoft.com/en-us/azure/container-apps/
- Full guide: See `AZURE_SETUP.md`
