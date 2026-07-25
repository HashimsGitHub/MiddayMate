# Update Frontend UI/UX - Automatic Deployment Guide

Your app is live at: `https://middaymate.calmsand-7d615011.australiaeast.azurecontainerapps.io`

Here are 3 ways to update it:

---

## 🚀 Option 1: Quick Manual Update (Fastest - 5 minutes)

**Best for**: Quick CSS tweaks, small HTML changes, testing

### Steps:

1. **Edit files locally** in `frontend/` folder:
   - `frontend/index.html` - Update HTML
   - `frontend/css/style.css` - Update styling
   - `frontend/js/app.js` - Update JavaScript

2. **Test locally first**:
   ```powershell
   python run.py
   # Open: http://localhost:5000
   ```

3. **Rebuild Docker image**:
   ```powershell
   docker build -t middaymate:latest .
   ```

4. **Push to Azure**:
   ```powershell
   docker login -u middaymatecr -p <PASSWORD> middaymatecr.azurecr.io
   
   docker tag middaymate:latest middaymatecr.azurecr.io/middaymate:latest
   
   docker push middaymatecr.azurecr.io/middaymate:latest
   ```

5. **Update Container App** (auto-redeploys):
   ```powershell
   az containerapp update `
     --resource-group MiddayMate `
     --name middaymate `
     --image middaymatecr.azurecr.io/middaymate:latest
   ```

6. **Wait 2-3 minutes** for app to restart

✅ Done! Your changes are live!

---

## 🤖 Option 2: GitHub Actions CI/CD (Recommended - Automatic!)

**Best for**: Every commit automatically deploys

### 2.1 Create GitHub Repository

```powershell
# Initialize git (if not done)
cd D:\MiddayMate
git init
git add .
git commit -m "Initial commit"

# Create repo on GitHub.com
# Then push:
git remote add origin https://github.com/YOUR_USERNAME/MiddayMate.git
git branch -M main
git push -u origin main
```

### 2.2 Create GitHub Secrets

In GitHub:
1. Go to **Settings** → **Secrets and variables** → **Actions**
2. Click **New repository secret**

Add these secrets:

| Secret Name | Value |
|-------------|-------|
| `AZURE_CREDENTIALS` | See step 2.3 below |
| `ACR_USERNAME` | From Container Registry → Access keys |
| `ACR_PASSWORD` | From Container Registry → Access keys |
| `ACR_SERVER` | `middaymatecr.azurecr.io` |

**For AZURE_CREDENTIALS**, run in PowerShell:

```powershell
az ad sp create-for-rbac `
  --name "MiddayMateCI" `
  --role contributor `
  --scopes /subscriptions/{subscription-id}/resourceGroups/MiddayMate `
  --json-auth
```

Copy the JSON output → paste into GitHub secret `AZURE_CREDENTIALS`

### 2.3 Create GitHub Actions Workflow

Create file: `.github/workflows/deploy.yml`

```yaml
name: Deploy to Azure

on:
  push:
    branches: [ main ]
    paths:
      - 'frontend/**'
      - 'app/**'
      - 'Dockerfile'
      - 'requirements.txt'

env:
  ACR_SERVER: ${{ secrets.ACR_SERVER }}
  ACR_USERNAME: ${{ secrets.ACR_USERNAME }}
  ACR_PASSWORD: ${{ secrets.ACR_PASSWORD }}

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Build Docker image
      run: |
        docker build -t middaymate:latest .
        docker tag middaymate:latest $ACR_SERVER/middaymate:latest
    
    - name: Login to ACR
      run: |
        echo "$ACR_PASSWORD" | docker login -u "$ACR_USERNAME" --password-stdin $ACR_SERVER
    
    - name: Push to Container Registry
      run: |
        docker push $ACR_SERVER/middaymate:latest
    
    - name: Azure Login
      uses: azure/login@v1
      with:
        creds: ${{ secrets.AZURE_CREDENTIALS }}
    
    - name: Update Container App
      run: |
        az containerapp update \
          --resource-group MiddayMate \
          --name middaymate \
          --image $ACR_SERVER/middaymate:latest
```

### 2.4 That's It!

Now every time you:
1. Edit `frontend/` files
2. Commit and push to GitHub
3. GitHub Actions automatically:
   - Builds Docker image
   - Pushes to Container Registry
   - Updates your live app
   - Your changes are live in 2-3 minutes!

✅ Fully automatic!

---

## 📋 Option 3: Manual PowerShell Script

**Best for**: Scripting your deployment process

Create file: `scripts/deploy-to-azure.ps1`

```powershell
param(
    [string]$ImageTag = "latest"
)

$ACR_SERVER = "middaymatecr.azurecr.io"
$RESOURCE_GROUP = "MiddayMate"
$APP_NAME = "middaymate"

Write-Host "🔨 Building Docker image..." -ForegroundColor Green
docker build -t middaymate:$ImageTag .

Write-Host "🏷️ Tagging image..." -ForegroundColor Green
docker tag middaymate:$ImageTag $ACR_SERVER/middaymate:$ImageTag

Write-Host "📤 Pushing to ACR..." -ForegroundColor Green
docker push $ACR_SERVER/middaymate:$ImageTag

Write-Host "🚀 Updating Container App..." -ForegroundColor Green
az containerapp update `
  --resource-group $RESOURCE_GROUP `
  --name $APP_NAME `
  --image $ACR_SERVER/middaymate:$ImageTag

Write-Host "✅ Deployment complete!" -ForegroundColor Green
Write-Host "⏳ App will restart in 2-3 minutes" -ForegroundColor Yellow
```

**Usage:**
```powershell
.\scripts\deploy-to-azure.ps1

# Or with custom tag:
.\scripts\deploy-to-azure.ps1 -ImageTag "v1.1"
```

---

## 🔄 Workflow Comparison

| Option | Time | Automatic | Best For |
|--------|------|-----------|----------|
| **Option 1: Manual** | 5 min | ❌ No | Quick testing |
| **Option 2: GitHub Actions** | 3 min | ✅ Yes | Production |
| **Option 3: Script** | 3 min | ⚠️ Manual | Regular updates |

---

## 💡 Recommended Approach

### For Development:
1. Edit files locally
2. Test with `python run.py` (http://localhost:5000)
3. Use Option 1 (manual update) to deploy

### For Production:
1. Set up GitHub Actions (Option 2)
2. Just commit and push
3. Automatic deployment happens!

---

## 📝 Step-by-Step for GitHub Actions Setup

### 1. Commit your code
```powershell
git add .
git commit -m "Update frontend UI"
git push origin main
```

### 2. Go to GitHub.com

Your repo → **Settings** → **Secrets and variables** → **Actions**

### 3. Add secrets
- `AZURE_CREDENTIALS` (JSON from `az ad sp create-for-rbac`)
- `ACR_USERNAME` (from Azure Portal)
- `ACR_PASSWORD` (from Azure Portal)
- `ACR_SERVER` (`middaymatecr.azurecr.io`)

### 4. Create `.github/workflows/deploy.yml`

Copy the YAML file from Option 2 above

### 5. Push the workflow file
```powershell
git add .github/workflows/deploy.yml
git commit -m "Add GitHub Actions CI/CD"
git push origin main
```

### 6. Done!

Now every push to main branch automatically deploys!

---

## 🧪 Testing Your Setup

### Test Option 1 (Manual):

```powershell
# Make a small change
# Edit frontend/css/style.css (change a color)
# Run deployment script
.\scripts\deploy-to-azure.ps1
# Visit your URL, refresh browser
```

### Test Option 2 (GitHub Actions):

```powershell
# Make a small change
# Edit frontend/index.html
git add .
git commit -m "Test GitHub Actions"
git push origin main

# Go to GitHub → Actions tab
# Watch the workflow run
# Your app updates automatically!
```

---

## ⚡ Quick Tips

**Fastest feedback loop:**
1. Edit files locally
2. Test: `python run.py` locally
3. When ready: `.\scripts\deploy-to-azure.ps1`
4. Wait 2-3 minutes
5. Refresh your live URL

**See your changes immediately (local):**
```powershell
python run.py
# App reloads on file changes automatically in dev mode
```

**See deployment progress:**
```powershell
# Watch logs as your app updates
az containerapp logs show `
  --resource-group MiddayMate `
  --name middaymate `
  --follow
```

**Rollback if something breaks:**
```powershell
# Go back to previous image
az containerapp update `
  --resource-group MiddayMate `
  --name middaymate `
  --image middaymatecr.azurecr.io/middaymate:previous-tag
```

---

## 📊 Current URL

Your live app: `https://middaymate.calmsand-7d615011.australiaeast.azurecontainerapps.io`

Test it: 
```powershell
curl https://middaymate.calmsand-7d615011.australiaeast.azurecontainerapps.io/health
# Should return: {"status":"healthy"}
```

---

## 🎯 Recommendation

**Start with Option 1** (manual) to understand the flow, then **switch to Option 2** (GitHub Actions) for hands-free deployment.

---

## ❓ Next Steps

1. Choose your deployment method
2. For GitHub Actions: Set up secrets and workflow file
3. Make a test change and deploy
4. Refresh your live URL to see changes

**Questions?** See [FINAL_DEPLOYMENT.md](FINAL_DEPLOYMENT.md) for the manual process.
