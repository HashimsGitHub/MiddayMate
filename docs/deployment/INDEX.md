# Azure Deployment Guides

Complete guides for deploying and managing MiddayMate on Azure.

## 🚀 Getting Started with Azure

### [AZURE_SETUP.md](AZURE_SETUP.md)
Complete Azure setup guide with 3 options:
- **Option A**: Azure CLI commands (fastest)
- **Option B**: Azure Portal click-ops (visual)
- **Option C**: Azure CLI manual (step-by-step)

**Start here** if you need to set up Azure resources from scratch.

---

### [AZURE_DEPLOYMENT.md](AZURE_DEPLOYMENT.md)
Complete deployment guide with pre/post deployment checklists, troubleshooting, and scaling info.

**Use this** as your main deployment reference.

---

## 📋 Azure Portal Click-Ops Guides

### [AZURE_PORTAL_STEP_BY_STEP.md](AZURE_PORTAL_STEP_BY_STEP.md)
Detailed step-by-step guide for Azure Portal UI with exact field values and navigation.

**Follow this** if using Azure Portal UI instead of CLI.

---

### [AZURE_PORTAL_CHECKLIST.md](AZURE_PORTAL_CHECKLIST.md)
Quick checklist format for Azure Portal deployment with minimal explanations.

**Use this** for quick reference while deploying.

---

### [AZURE_PORTAL_EXISTING_ENV.md](AZURE_PORTAL_EXISTING_ENV.md)
Simplified guide for users who already have a Container Apps environment.

**Use this** if you already created the environment yourself.

---

## 🔄 Deployment Methods

### [FINAL_DEPLOYMENT.md](FINAL_DEPLOYMENT.md)
Final 2-step deployment guide for the last phase of setup.

**Use this** when ready to create the Container App itself.

---

### [GITHUB_ACTIONS_SETUP.md](GITHUB_ACTIONS_SETUP.md)
Complete GitHub Actions CI/CD setup for automatic deployment on every push.

**Follow this** to enable hands-free deployments.

---

## 🎯 Quick Navigation

| Need | Document |
|------|----------|
| Fresh Azure setup | [AZURE_SETUP.md](AZURE_SETUP.md) |
| Using Azure Portal | [AZURE_PORTAL_STEP_BY_STEP.md](AZURE_PORTAL_STEP_BY_STEP.md) |
| Already have environment | [AZURE_PORTAL_EXISTING_ENV.md](AZURE_PORTAL_EXISTING_ENV.md) |
| Quick checklist | [AZURE_PORTAL_CHECKLIST.md](AZURE_PORTAL_CHECKLIST.md) |
| Final deployment steps | [FINAL_DEPLOYMENT.md](FINAL_DEPLOYMENT.md) |
| CI/CD automation | [GITHUB_ACTIONS_SETUP.md](GITHUB_ACTIONS_SETUP.md) |
| Full reference | [AZURE_DEPLOYMENT.md](AZURE_DEPLOYMENT.md) |
| Quick lookup | [AZURE_QUICK_REFERENCE.md](AZURE_QUICK_REFERENCE.md) |

---

## 🔍 Azure Quick Reference

### [AZURE_QUICK_REFERENCE.md](AZURE_QUICK_REFERENCE.md)
Quick lookup for:
- Azure CLI commands
- Resource names and configurations
- Connection strings
- Docker commands
- Firewall rules
- Troubleshooting

**Use this** when you need a quick command or configuration value.

---

## 📊 Current Status

| Resource | Status |
|----------|--------|
| Storage Account | ✅ Created |
| Container Registry | ✅ Created |
| Container App | ✅ Running |
| CI/CD Pipeline | ✅ Active |
| Live URL | ✅ Working |

---

## 🚀 Recommended Workflow

1. **First time**: Read [AZURE_SETUP.md](AZURE_SETUP.md) Option A or B
2. **Using Portal**: Follow [AZURE_PORTAL_STEP_BY_STEP.md](AZURE_PORTAL_STEP_BY_STEP.md)
3. **Already have resources**: Use [AZURE_PORTAL_EXISTING_ENV.md](AZURE_PORTAL_EXISTING_ENV.md)
4. **Quick checklist**: Reference [AZURE_PORTAL_CHECKLIST.md](AZURE_PORTAL_CHECKLIST.md)
5. **Automate deploys**: Setup [GITHUB_ACTIONS_SETUP.md](GITHUB_ACTIONS_SETUP.md)
6. **Need a command**: Check [AZURE_QUICK_REFERENCE.md](AZURE_QUICK_REFERENCE.md)

---

## 📞 Support

- For development setup: See [docs/guides/](../guides/)
- For architecture details: See [docs/](../)
- For project specifications: See [ai/](../../ai/)
