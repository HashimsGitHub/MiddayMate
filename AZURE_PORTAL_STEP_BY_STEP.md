# Azure Portal Setup - Step by Step Guide

## ✅ You've Completed

1. ✅ Storage Account (`middaymatesa`)
2. ✅ Container Registry (`middaymatecr`)

## 📋 Next Steps (in order)

1. **Build & Push Docker Image** (local command line)
2. **Create Container Apps Environment** (Azure Portal)
3. **Create Container App** (Azure Portal)

---

## Step 1: Build & Push Docker Image to Container Registry

### 1.1 Open Command Line / PowerShell

Navigate to your MiddayMate project:
```powershell
cd D:\MiddayMate
```

### 1.2 Get Container Registry Login Information

Go to **Azure Portal** → **Container Registries** → **middaymatecr**

**Left sidebar** → Click **Access keys**

You'll see:
- **Login server**: `middaymatecr.azurecr.io`
- **Username**: (something like `middaymatecr`)
- **Password**: (long string)

**Copy all three values** - you'll need them in the next step.

### 1.3 Login to Container Registry

In PowerShell, run:
```powershell
docker login -u <USERNAME> -p <PASSWORD> middaymatecr.azurecr.io
```

Replace:
- `<USERNAME>` with the username from Access keys
- `<PASSWORD>` with the password from Access keys

**Expected output**: `Login Succeeded`

### 1.4 Build Docker Image

Still in PowerShell, run:
```powershell
docker build -t middaymate:latest .
```

**Expected output**: Shows build steps, ends with `Successfully tagged middaymate:latest`

⏱️ **Time**: ~2-3 minutes

### 1.5 Tag Image for Registry

```powershell
docker tag middaymate:latest middaymatecr.azurecr.io/middaymate:latest
```

**No output** = success ✓

### 1.6 Push Image to Registry

```powershell
docker push middaymatecr.azurecr.io/middaymate:latest
```

**Expected output**: Shows upload progress, ends with `Digest: sha256:...`

⏱️ **Time**: ~1-2 minutes

### 1.7 Verify Image in Registry

Go to **Azure Portal** → **Container Registries** → **middaymatecr**

**Left sidebar** → Click **Repositories**

You should see: `middaymate` with tag `latest` ✓

---

## Step 2: Create Container Apps Environment

This is the hosting environment where your app will run.

### 2.1 Go to Container Apps

In **Azure Portal**, search for: **Container Apps**

Click **Container Apps** (the service, not a specific app)

### 2.2 Create Environment

**Left sidebar** → Click **Environments**

Click **+ Create** button

### 2.3 Fill in Environment Details

**Create Container Apps environment** page:

| Field | Value |
|-------|-------|
| **Resource Group** | MiddayMate |
| **Name** | `middaymate-env` |
| **Region** | Australia East |
| **Zone redundancy** | Disabled (for MVP) |

Click **Create**

⏱️ **Time**: ~1-2 minutes to deploy

Wait for "Deployment succeeded" message.

---

## Step 3: Create Container App

This is where your Flask app will actually run.

### 3.1 Go to Container Apps

Search for: **Container Apps** in Azure Portal

Click **+ Create**

### 3.2 Basics Tab

Fill in:

| Field | Value |
|-------|-------|
| **Subscription** | Your Visual Studio Subscription |
| **Resource Group** | MiddayMate |
| **Container App name** | `middaymate` |
| **Region** | Australia East |
| **Container Apps Environment** | middaymate-env |

Click **Next: Container →**

### 3.3 Container Tab

**Image source**: Select **Azure Container Registry**

**Registry**: Select `middaymatecr`

**Image**: Select `middaymate`

**Image tag**: Select `latest`

Under **Container name** section:
- Container name: `middaymate` (auto-filled)
- **CPU and memory**: 
  - **CPU**: 0.5
  - **Memory**: 1.0 Gi

Click **Next: Ingress →**

### 3.4 Ingress Tab

**Ingress**: Toggle **ON** (enabled)

**Ingress traffic**: Select **External** (so you can access from internet)

**Target port**: `5000` (this is what Flask uses)

Click **Next: Environment variables →**

### 3.5 Environment Variables Tab

Click **+ Add** button and add these variables:

| Name | Value |
|------|-------|
| `FLASK_ENV` | `production` |
| `FLASK_APP` | `run.py` |
| `SECRET_KEY` | Generate a random string (e.g., `Kx9mP2jQ7wL4vN8rT5bY3`) |
| `DATABASE_URL` | `sqlite:///middaymate.db` |
| `AZURE_STORAGE_CONTAINER` | `middaymate` |

**For AZURE_STORAGE_CONNECTION_STRING:**

Go to your **Storage Account** → **Access keys** → Copy the **Connection string**

Then come back and add:

| Name | Value |
|------|-------|
| `AZURE_STORAGE_CONNECTION_STRING` | Paste your connection string |

### 3.6 Review + Create

Click **Next: Review + Create →**

Review all settings (should show):
- Container App name: `middaymate` ✓
- Image: `middaymatecr.azurecr.io/middaymate:latest` ✓
- Port: 5000 ✓
- Ingress: External ✓

Click **Create**

⏱️ **Time**: ~3-5 minutes to deploy

---

## Step 4: Get Your Application URL

Once deployment completes (you'll see "Deployment succeeded"):

### 4.1 Go to Your Container App

Search: **Container Apps** → Click **middaymate**

### 4.2 Find Your URL

On the **Overview** page, look for:

**Application URL**: `https://middaymate.xxxxx.australiaeast.azurecontainerapps.io`

**Copy this URL** - this is your live application! 🎉

### 4.3 Test It

Open in browser or curl:

```powershell
curl https://middaymate.xxxxx.australiaeast.azurecontainerapps.io/health
```

You should see:
```json
{"status": "healthy"}
```

---

## ⏱️ Troubleshooting If App Doesn't Start

### Check Logs

1. Go to **Azure Portal** → **Container Apps** → **middaymate**
2. **Left sidebar** → Click **Logs**
3. Look for errors

### Common Issues

**Error: Image not found**
- Go to Container Registry → Repositories
- Verify `middaymate:latest` exists
- May need to wait a few minutes after push

**Error: Environment variable missing**
- Go to Container App → Configuration
- Click **Environment variables**
- Check all required vars are there

**Error: Port 5000 connection refused**
- Make sure Docker image is built correctly
- Check Dockerfile exposes port 5000
- May need to wait 2-3 minutes for app to fully start

### View Logs (if needed)

1. Container App **Overview** page
2. Scroll down to **Recent activity** section
3. Click on the revision that's running
4. Click **Logs** tab

---

## 📊 Summary of What You Have Now

| Resource | Name | Status |
|----------|------|--------|
| Storage Account | `middaymatesa` | ✅ Created |
| Container Registry | `middaymatecr` | ✅ Created |
| Docker Image | `middaymate:latest` | ✅ Pushed |
| Container Apps Env | `middaymate-env` | ✅ Created |
| Container App | `middaymate` | ✅ Running |

**Your app is now LIVE!** 🚀

---

## 📝 Next Steps

Once app is running:

### 1. Update Environment Variables (if needed)

If you want to add OAuth credentials:

Container App **Configuration** → **Environment variables** → **Edit and save**

Add:
```
MICROSOFT_CLIENT_ID=your-id
MICROSOFT_CLIENT_SECRET=your-secret
```

Then Container App auto-redeploys.

### 2. Monitor Performance

Container App **Metrics** tab shows:
- CPU usage
- Memory usage
- Request count
- Error rates

### 3. View Real-time Logs

Container App **Logs** tab shows what's happening.

### 4. Set Custom Domain (Optional)

Container App **Custom domains** to use your own domain.

---

## 🎯 You're Done!

Your MiddayMate MVP is now:
- ✅ Built (Docker image)
- ✅ Stored (Container Registry)
- ✅ Running (Container App)
- ✅ Live (Accessible via HTTPS URL)

**Estimated Total Time**: 15-20 minutes

Next feature: Add OAuth sign-in or enable image uploads!
