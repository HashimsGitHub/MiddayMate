# GitHub Actions CI/CD Setup (5 minutes)

Automatic deployment every time you push code!

---

## 🎯 What This Does

1. You edit `frontend/` files
2. You commit and push to GitHub
3. GitHub Actions automatically:
   - Builds Docker image
   - Pushes to Azure Container Registry
   - Updates your live app
4. Changes live in ~3 minutes ✅

---

## ⚙️ Setup (One-time - 5 minutes)

### Step 1: Create GitHub Repository

If not already on GitHub:

```powershell
cd D:\MiddayMate

# Initialize if needed
git init
git add .
git commit -m "Initial commit"

# Create repo on GitHub.com
# Then:
git remote add origin https://github.com/YOUR_USERNAME/MiddayMate.git
git branch -M main
git push -u origin main
```

---

### Step 2: Add GitHub Secrets

**Go to GitHub.com** → Your repo → **Settings** → **Secrets and variables** → **Actions**

Click **New repository secret** and add these 4 secrets:

#### Secret 1: `ACR_SERVER`
```
middaymatecr.azurecr.io
```

#### Secret 2: `ACR_USERNAME`
From Azure Portal:
- Container Registry → **middaymatecr** → **Access keys**
- Copy the **Username**

#### Secret 3: `ACR_PASSWORD`
From Azure Portal:
- Container Registry → **middaymatecr** → **Access keys**
- Copy the **password** (one of them)

#### Secret 4: `AZURE_CREDENTIALS`

Run this in PowerShell:

```powershell
# First, get your subscription ID
az account show --query id -o tsv

# Then run (replace {SUBSCRIPTION_ID}):
az ad sp create-for-rbac `
  --name "MiddayMateCI" `
  --role contributor `
  --scopes /subscriptions/{SUBSCRIPTION_ID}/resourceGroups/MiddayMate `
  --json-auth
```

This outputs JSON. Copy the entire JSON output and paste as the value for `AZURE_CREDENTIALS` secret.

---

### Step 3: Add Workflow File

The workflow file is already at: `.github/workflows/deploy.yml`

Just commit and push it:

```powershell
git add .github/workflows/deploy.yml
git commit -m "Add GitHub Actions deployment"
git push origin main
```

---

## ✅ That's It!

Your CI/CD is now set up!

---

## 🚀 Using It

### To deploy, just:

1. **Edit files** (e.g., `frontend/css/style.css`)
2. **Commit**:
   ```powershell
   git add .
   git commit -m "Update UI styles"
   ```
3. **Push**:
   ```powershell
   git push origin main
   ```
4. **Watch it deploy**:
   - Go to GitHub → **Actions** tab
   - You'll see your workflow running
   - Takes ~3-5 minutes total
   - Your live app updates automatically!

---

## 📊 Monitor Deployment

### In GitHub:
1. Go to repo → **Actions** tab
2. Click the latest workflow
3. See build and deployment progress in real-time

### Check your live app:
```powershell
# Your live URL:
curl https://middaymate.calmsand-7d615011.australiaeast.azurecontainerapps.io/health

# Should still return: {"status":"healthy"}
```

---

## 🧪 Test It

1. **Make a small change**:
   - Edit `frontend/css/style.css`
   - Change one color value

2. **Push to GitHub**:
   ```powershell
   git add frontend/css/style.css
   git commit -m "Test: change button color"
   git push origin main
   ```

3. **Watch GitHub Actions**:
   - Go to GitHub → **Actions** tab
   - Click your workflow
   - See it build and deploy
   - Takes 3-5 minutes

4. **Verify in your live app**:
   - Go to: `https://middaymate.calmsand-7d615011.australiaeast.azurecontainerapps.io`
   - Refresh browser
   - See your color change! ✅

---

## ⚡ Tips

**Development workflow:**
```powershell
# 1. Edit files locally
# 2. Test locally
python run.py
# Open http://localhost:5000

# 3. When happy, commit and push
git add .
git commit -m "Add new feature"
git push origin main

# 4. GitHub Actions automatically deploys!
# Check Actions tab to watch
```

**Skip deployment for small changes:**

If you don't want to deploy, just don't push to `main`:
```powershell
# Work on a branch instead
git checkout -b feature/new-ui
git add .
git commit -m "WIP: new UI"
git push origin feature/new-ui

# When ready, merge to main (triggers deploy):
git checkout main
git merge feature/new-ui
git push origin main
```

**Force a re-deployment:**
```powershell
# Just push to main again
git add .
git commit -m "Force redeploy"
git push origin main
```

---

## 🔍 Troubleshooting

### Actions not running?
- Check branch is `main`
- Check file paths in `deploy.yml` match your structure
- Click workflow to see detailed logs

### Deployment fails?
- Check secrets are correct
- Run locally first: `docker build -t middaymate:latest .`
- Check file changes are in `frontend/`, `app/`, or `Dockerfile`

### App doesn't update?
- Wait 2-3 minutes (app takes time to restart)
- Check Container App logs: `az containerapp logs show --resource-group MiddayMate --name middaymate`

---

## 📋 Secrets Checklist

- [ ] `ACR_SERVER` = `middaymatecr.azurecr.io`
- [ ] `ACR_USERNAME` = username from Access keys
- [ ] `ACR_PASSWORD` = password from Access keys
- [ ] `AZURE_CREDENTIALS` = JSON from `az ad sp create-for-rbac`
- [ ] Workflow file at `.github/workflows/deploy.yml`

---

## 🎉 You're Done!

Now you have automatic CI/CD! Every push to main deploys your changes.

**Next:**
1. Test it with a small change
2. Push to main
3. Watch it deploy automatically!

---

## 📞 Need Help?

- See: [FRONTEND_UPDATE_GUIDE.md](FRONTEND_UPDATE_GUIDE.md) for all update options
- GitHub Actions docs: https://docs.github.com/actions
- Azure Container Apps docs: https://learn.microsoft.com/azure/container-apps/

**Happy deploying! 🚀**
