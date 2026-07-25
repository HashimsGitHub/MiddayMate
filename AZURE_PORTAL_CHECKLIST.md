# Azure Portal Deployment - Quick Checklist

## ✅ Already Done
- [x] Storage Account (middaymatesa)
- [x] Container Registry (middaymatecr)

---

## 📋 DO NEXT (in this order)

### Step 1: Build & Push Docker Image (PowerShell)
Run these commands in PowerShell in the MiddayMate directory:

```powershell
# Login to your container registry
docker login -u <USERNAME> -p <PASSWORD> middaymatecr.azurecr.io
```
Get USERNAME and PASSWORD from:
- Azure Portal → Container Registries → middaymatecr → Access keys

```powershell
# Build the image
docker build -t middaymate:latest .
```

```powershell
# Tag it for your registry
docker tag middaymate:latest middaymatecr.azurecr.io/middaymate:latest
```

```powershell
# Push it to Azure
docker push middaymatecr.azurecr.io/middaymate:latest
```

**Expected**: Image appears in Container Registry → Repositories

---

### Step 2: Create Container Apps Environment (Portal)

**In Azure Portal:**

1. Search: **Container Apps**
2. Click **Environments** (left sidebar)
3. Click **+ Create**
4. Fill in:
   - Resource Group: **MiddayMate**
   - Name: **middaymate-env**
   - Region: **Australia East**
5. Click **Create**

⏱️ Wait ~2 minutes for deployment

---

### Step 3: Create Container App (Portal)

**In Azure Portal:**

1. Search: **Container Apps**
2. Click **+ Create**
3. Fill in and click **Next** through each tab:

**BASICS TAB:**
- Resource Group: **MiddayMate**
- Name: **middaymate**
- Region: **Australia East**
- Environment: **middaymate-env**

**CONTAINER TAB:**
- Image source: **Azure Container Registry**
- Registry: **middaymatecr**
- Image: **middaymate**
- Image tag: **latest**
- CPU: **0.5**
- Memory: **1.0 Gi**

**INGRESS TAB:**
- Ingress: **ON**
- Traffic: **External**
- Port: **5000**

**ENVIRONMENT VARIABLES TAB:**

Click **+ Add** for each:

| Name | Value |
|------|-------|
| FLASK_ENV | production |
| FLASK_APP | run.py |
| SECRET_KEY | (generate random string) |
| DATABASE_URL | sqlite:///middaymate.db |
| AZURE_STORAGE_CONTAINER | middaymate |
| AZURE_STORAGE_CONNECTION_STRING | (from Storage Account → Access keys) |

4. Click **Review + Create**
5. Click **Create**

⏱️ Wait ~5 minutes for deployment

---

### Step 4: Get Your URL & Test

**In Azure Portal:**

1. Search: **Container Apps**
2. Click **middaymate**
3. Copy the **Application URL** (looks like: `https://middaymate.xxxxx.australiaeast.azurecontainerapps.io`)

**Test in PowerShell:**

```powershell
curl https://middaymate.xxxxx.australiaeast.azurecontainerapps.io/health
```

Expected response:
```json
{"status":"healthy"}
```

✅ **You're Done!** Your app is live!

---

## 🎯 Time Estimate

| Task | Time |
|------|------|
| Docker login, build, push | 5-7 min |
| Create environment | 2 min |
| Create container app | 5 min |
| Test app | 1 min |
| **TOTAL** | **~15 min** |

---

## 📞 Need Help?

### If Docker push fails
- Verify you're logged in: `docker login ...`
- Verify image exists: `docker image ls`
- Check Access keys username/password

### If app won't start
- Go to Container App **Logs**
- Look for error messages
- Check **Environment variables** are correct

### To view logs
- Container App → **Logs** tab
- Or use Azure CLI:
  ```powershell
  az containerapp logs show `
    --resource-group MiddayMate `
    --name middaymate `
    --follow
  ```

---

## 🚀 What's Happening

```
Your Computer
    ↓
[docker build + docker push]
    ↓
Azure Container Registry (middaymatecr)
    ↓
Container App Environment (middaymate-env)
    ↓
Container App (middaymate) ← Running now!
    ↓
Internet ← You can access it!
```

---

**Next**: Open your URL in a browser and see MiddayMate! 🎉
