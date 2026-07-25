# MiddayMate - Quick Start (5 Minutes)

## Option 1: Run Locally 🖥️

```bash
# 1. Setup
cd D:\MiddayMate
python -m venv venv
venv\Scripts\activate

# 2. Install
pip install -r requirements.txt

# 3. Seed database
python scripts/seed_database.py

# 4. Run
python run.py
```

**Open**: http://localhost:5000

Done! 🎉

---

## Option 2: Deploy to Azure ☁️

### Windows
```powershell
.\scripts\azure_setup.ps1
```

### macOS/Linux
```bash
bash scripts/azure_setup.sh
```

**Wait 5-10 minutes**, then you'll get your application URL.

Done! 🎉

---

## What's Ready?

✅ **Full Backend API** - 7 route modules, 6 models  
✅ **Responsive Frontend** - HTML/CSS/JavaScript  
✅ **Database & ORM** - SQLAlchemy with SQLite  
✅ **Tests** - pytest with coverage  
✅ **Docker** - Production-ready container  
✅ **Azure** - Automated deployment  
✅ **Docs** - Complete guides  

---

## Next: OAuth Setup

To enable real OAuth sign-in:

1. Get credentials from [Google](https://console.cloud.google.com) or [Microsoft](https://portal.azure.com)
2. Add to `.env`:
   ```env
   MICROSOFT_CLIENT_ID=your_id
   MICROSOFT_CLIENT_SECRET=your_secret
   ```
3. Update `app/routes/auth.py` with real OAuth flow
4. Restart app

---

## Need Help?

- **Local setup**: See [DEVELOPMENT.md](DEVELOPMENT.md)
- **Azure deployment**: See [AZURE_SETUP.md](AZURE_SETUP.md)  
- **Full project info**: See [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)
- **Azure quick ref**: See [AZURE_QUICK_REFERENCE.md](AZURE_QUICK_REFERENCE.md)

---

**That's it! You're ready to build.** 🚀
