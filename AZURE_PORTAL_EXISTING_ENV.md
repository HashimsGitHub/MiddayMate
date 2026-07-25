# Azure Portal Deployment - Using Existing Environment

Since you already have the `vcnity-env` Container Apps environment, skip the environment creation step.

---

## ✅ Already Done

- [x] Storage Account (`middaymatesa`)
- [x] Container Registry (`middaymatecr`)
- [x] Container Apps Environment (`vcnity-env`)

---

## 📋 Remaining Steps

### Step 1: Build & Push Docker Image (PowerShell)

Run these commands in PowerShell in the `D:\MiddayMate` directory:

```powershell
# Get credentials from Azure Portal:
# Container Registry → middaymatecr → Access keys
# Copy: Login server, Username, Password

# Login
docker login -u <USERNAME> -p <PASSWORD> middaymatecr.azurecr.io
```

```powershell
# Build the image
docker build -t middaymate:latest .
```

```powershell
# Tag for your registry
docker tag middaymate:latest middaymatecr.azurecr.io/middaymate:latest
```

```powershell
# Push to Azure
docker push middaymatecr.azurecr.io/middaymate:latest
```

**Expected**: Image appears in Container Registry → Repositories → `middaymate:latest`

⏱️ Time: 5-7 minutes

---

### Step 2: Create Container App (Using Your Existing Environment)

**In Azure Portal:**

1. Search: **Container Apps**
2. Click **+ Create**

**BASICS TAB:**
- Subscription: Your Visual Studio Subscription
- Resource Group: **MiddayMate**
- Container App name: **`middaymate`**
- Region: **Australia East**
- **Container Apps Environment: `vcnity-env`** ← Use your existing one!

Click **Next: Container →**

**CONTAINER TAB:**
- Image source: **Azure Container Registry**
- Registry: **middaymatecr**
- Image: **middaymate**
- Image tag: **latest**
- CPU: **0.5**
- Memory: **1.0 Gi**

Click **Next: Ingress →**

**INGRESS TAB:**
- Ingress: Toggle **ON**
- Ingress traffic: **External**
- Target port: **5000**

Click **Next: Environment variables →**

**ENVIRONMENT VARIABLES TAB:**

Click **+ Add** and add these (one by one):

| Name | Value |
|------|-------|
| `FLASK_ENV` | `production` |
| `FLASK_APP` | `run.py` |
| `SECRET_KEY` | Generate random: `Kx9mP2jQ7wL4vN8rT5bY3` |
| `DATABASE_URL` | `sqlite:///middaymate.db` |
| `AZURE_STORAGE_CONTAINER` | `middaymate` |

**For the connection string:**
- Go to **Storage Account → Access keys**
- Copy the **Connection string** value
- Add it:

| Name | Value |
|------|-------|
| `AZURE_STORAGE_CONNECTION_STRING` | Paste connection string here |

Click **Next: Review + Create →**

**REVIEW + CREATE:**
- Review everything looks good
- Click **Create**

⏱️ Time: 5-7 minutes

---

## 🎯 Get Your URL & Test

Once deployment completes (you'll see "Deployment succeeded"):

1. Go to **Container Apps** → **middaymate**
2. On the **Overview** page, copy the **Application URL**

Example: `https://middaymate.xxxxx.australiaeast.azurecontainerapps.io`

**Test it:**

```powershell
curl https://middaymate.xxxxx.australiaeast.azurecontainerapps.io/health
```

Should return:
```json
{"status":"healthy"}
```

✅ **Done!** Your app is live!

---

## ⏱️ Total Time

| Task | Time |
|------|------|
| Docker build & push | 5-7 min |
| Create Container App | 5-7 min |
| **Total** | **~12 min** |

---

## 📝 What's Being Created

```
Your Computer (PowerShell)
    ↓
[docker build + docker push]
    ↓
Container Registry (middaymatecr)
    ↓
Existing Environment (vcnity-env) ← Uses this!
    ↓
Container App (middaymate) ← Creates this
    ↓
Internet - Your live app!
```

---

## 🚀 Quick Checklist

- [ ] PowerShell: `docker login` ✓
- [ ] PowerShell: `docker build -t middaymate:latest .` ✓
- [ ] PowerShell: `docker tag middaymate:latest middaymatecr.azurecr.io/middaymate:latest` ✓
- [ ] PowerShell: `docker push middaymatecr.azurecr.io/middaymate:latest` ✓
- [ ] Verify image in Container Registry ✓
- [ ] Azure Portal: Create Container App
- [ ] Select Environment: `vcnity-env` ✓
- [ ] Get Application URL ✓
- [ ] Test with `/health` endpoint ✓

---

## ❓ If Docker Push Fails

```powershell
# Check you're logged in
docker login -u <USERNAME> -p <PASSWORD> middaymatecr.azurecr.io
# Should say "Login Succeeded"

# Check image exists
docker image ls | findstr middaymate

# Try push again with verbose
docker push -v middaymatecr.azurecr.io/middaymate:latest
```

---

**That's it! You're ready to deploy!** 🎉

Start with the PowerShell commands in Step 1.
