# Final Deployment - Container App Creation

## ✅ You Have Everything Ready

- [x] Storage Account: `middaymatesa`
- [x] Container Registry: `middaymatecr`
- [x] Container Apps Environment: `middaymate-env`

---

## 📋 2 Final Steps

### Step 1: Build & Push Docker Image (PowerShell)

**Location**: D:\MiddayMate directory

```powershell
# Get login credentials
# Azure Portal → Container Registries → middaymatecr → Access keys
# Copy: Login server, Username, Password

docker login -u <USERNAME> -p <PASSWORD> middaymatecr.azurecr.io

docker build -t middaymate:latest .

docker tag middaymate:latest middaymatecr.azurecr.io/middaymate:latest

docker push middaymatecr.azurecr.io/middaymate:latest
```

**Time**: 5-7 minutes

**Verify**: Container Registry → Repositories → should see `middaymate:latest` ✓

---

### Step 2: Create Container App (Azure Portal)

**In Azure Portal:**

1. Search: **Container Apps**
2. Click **+ Create**

---

### BASICS TAB
Fill in:
- **Subscription**: Your Visual Studio Subscription
- **Resource Group**: `MiddayMate`
- **Container App name**: `middaymate`
- **Region**: `Australia East`
- **Container Apps Environment**: `middaymate-env` ← Your existing one!

Click **Next: Container →**

---

### CONTAINER TAB
Fill in:
- **Image source**: `Azure Container Registry`
- **Registry**: `middaymatecr`
- **Image**: `middaymate`
- **Image tag**: `latest`
- **CPU**: `0.5`
- **Memory**: `1.0 Gi`

Click **Next: Ingress →**

---

### INGRESS TAB
Fill in:
- **Ingress**: Toggle **ON**
- **Ingress traffic**: `External`
- **Target port**: `5000`

Click **Next: Environment variables →**

---

### ENVIRONMENT VARIABLES TAB

Click **+ Add** button and add these 6 variables:

**Variable 1:**
- Name: `FLASK_ENV`
- Value: `production`

**Variable 2:**
- Name: `FLASK_APP`
- Value: `run.py`

**Variable 3:**
- Name: `SECRET_KEY`
- Value: `Kx9mP2jQ7wL4vN8rT5bY3` (or generate your own)

**Variable 4:**
- Name: `DATABASE_URL`
- Value: `sqlite:///middaymate.db`

**Variable 5:**
- Name: `AZURE_STORAGE_CONTAINER`
- Value: `middaymate`

**Variable 6:**
- Name: `AZURE_STORAGE_CONNECTION_STRING`
- Value: Get from:
  - Azure Portal → Storage Accounts → middaymatesa → Access keys
  - Copy the "Connection string" value
  - Paste it here

Click **Next: Review + Create →**

---

### REVIEW + CREATE

Review all settings look correct:
- Name: `middaymate` ✓
- Environment: `middaymate-env` ✓
- Image: `middaymatecr.azurecr.io/middaymate:latest` ✓
- Port: `5000` ✓
- Ingress: External ✓

Click **Create**

**Time**: 5-7 minutes (wait for "Deployment succeeded")

---

## 🎉 Done! Get Your URL

Once deployment completes:

1. Go to **Container Apps** in Azure Portal
2. Click **middaymate**
3. On **Overview** page, find: **Application URL**

Copy this URL - it's your live app!

Example: `https://middaymate.xxxxx.australiaeast.azurecontainerapps.io`

---

## ✅ Test It

```powershell
# Test the health endpoint
curl https://middaymate.xxxxx.australiaeast.azurecontainerapps.io/health

# Should return:
# {"status":"healthy"}
```

Or open in browser:
```
https://middaymate.xxxxx.australiaeast.azurecontainerapps.io
```

---

## ⏱️ Timeline

| Task | Duration |
|------|----------|
| Docker build & push | 5-7 min |
| Create Container App | 5-7 min |
| App startup | 2-3 min |
| **Total** | **~15 min** |

---

## 🚀 You're Live!

Your MiddayMate MVP is now running on Azure!

**Next Steps:**
1. Open your application URL in a browser
2. Test the health endpoint
3. Check the logs if needed: Container App → Logs
4. Add OAuth credentials (Microsoft/Google) to enable real sign-in
5. Monitor performance: Container App → Metrics

---

**That's it! Happy deploying! 🎉**
