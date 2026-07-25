# Project Structure - Reorganized

Your project is now organized into logical directories for easy navigation.

---

## 📁 Complete Project Structure

```
MiddayMate/
│
├── 📄 README.md                 ← Start here! Project overview
├── 📄 QUICKSTART.md             ← 5-minute setup guide
├── 📄 LICENSE
│
├── 🔧 Configuration Files
│   ├── Dockerfile               ← Container configuration
│   ├── docker-compose.yml       ← Local Docker setup
│   ├── requirements.txt          ← Python dependencies
│   ├── .env.example             ← Environment template
│   ├── .gitignore               ← Git ignore rules
│   ├── pytest.ini               ← Test configuration
│   └── run.py                   ← Application entry point
│
├── 📚 docs/                     ← ALL DOCUMENTATION
│   ├── README.md                ← Docs directory guide
│   ├── INDEX.md                 ← Complete documentation index ⭐
│   │
│   ├── 📖 Architecture & Design (Reference)
│   │   ├── 01_Project_Vision.md
│   │   ├── 02_Business_Model.md
│   │   ├── 03_Product_Requirements.md
│   │   ├── 04_System_Architecture.md
│   │   ├── 05_Database_Design.md
│   │   ├── 06_API_Specification.md
│   │   ├── 07_UI_UX_Guidelines.md
│   │   ├── CONTRIBUTING.md
│   │   └── DECISIONS.md
│   │
│   ├── 📖 guides/               ← Development & Usage Guides
│   │   ├── INDEX.md             ← Guide navigation
│   │   ├── PROJECT_SUMMARY.md   ← Complete project overview
│   │   ├── DEVELOPMENT.md       ← Local development setup
│   │   ├── SESSION_SUMMARY.md   ← Session progress tracker
│   │   └── FRONTEND_UPDATE_GUIDE.md ← How to deploy changes
│   │
│   └── 🚀 deployment/           ← Azure Deployment Guides
│       ├── INDEX.md             ← Deployment navigation
│       ├── AZURE_SETUP.md       ← Complete Azure setup guide
│       ├── AZURE_DEPLOYMENT.md  ← Deployment checklist
│       ├── AZURE_PORTAL_STEP_BY_STEP.md
│       ├── AZURE_PORTAL_CHECKLIST.md
│       ├── AZURE_PORTAL_EXISTING_ENV.md
│       ├── FINAL_DEPLOYMENT.md
│       ├── GITHUB_ACTIONS_SETUP.md
│       └── AZURE_QUICK_REFERENCE.md
│
├── 🐍 app/                      ← Flask Application (Backend)
│   ├── __init__.py              ← App factory
│   ├── config.py                ← Configuration (dev/test/prod)
│   ├── models.py                ← Database models (6 models)
│   ├── utils.py                 ← Utility functions
│   └── routes/                  ← API Blueprints (7 modules)
│       ├── __init__.py
│       ├── auth.py              ← OAuth login/logout
│       ├── users.py             ← User profiles
│       ├── venues.py            ← Venue discovery
│       ├── promotions.py        ← Browse offers
│       ├── invitations.py       ← Meetup requests
│       ├── messages.py          ← In-app messaging
│       └── vendors.py           ← Vendor management
│
├── 🎨 frontend/                 ← Web Interface (Frontend)
│   ├── index.html               ← Main HTML page
│   ├── css/
│   │   └── style.css            ← Responsive styling
│   └── js/
│       └── app.js               ← Client-side logic
│
├── 🧪 tests/                    ← Test Suite
│   ├── __init__.py
│   ├── test_models.py           ← Model unit tests
│   └── test_routes.py           ← API integration tests
│
├── 🔧 scripts/                  ← Utility Scripts
│   ├── README.md                ← Script documentation
│   ├── seed_database.py         ← Database seeding
│   ├── azure_setup.ps1          ← Azure automation (Windows)
│   └── azure_setup.sh           ← Azure automation (macOS/Linux)
│
├── 📋 ai/                       ← Project Specifications
│   ├── 00_Code_Instructions.md  ← Coding guidelines
│   ├── 01_Project_Context.md    ← Project context
│   ├── 02_MVP_Features.md       ← MVP feature list
│   ├── 03_Technical_Requirements.md
│   ├── 04_UI_Screens.md         ← Screen descriptions
│   ├── 05_Database_Schema.md    ← Schema overview
│   ├── 06_API_Requirements.md   ← API requirements
│   └── TODO.md                  ← Project TODO list
│
├── ⚙️ .github/
│   └── workflows/
│       └── deploy.yml           ← GitHub Actions CI/CD
│
└── .claude/
    └── settings.local.json      ← Claude Code settings
```

---

## 🎯 Where to Find What

### 📖 Documentation Sections

| Need | Location | File |
|------|----------|------|
| **Start here** | Root | [README.md](README.md) |
| **Quick start** | Root | [QUICKSTART.md](QUICKSTART.md) |
| **Doc index** | docs/ | [docs/INDEX.md](docs/INDEX.md) ⭐ |
| **Project overview** | docs/guides/ | [docs/guides/PROJECT_SUMMARY.md](docs/guides/PROJECT_SUMMARY.md) |
| **Local setup** | docs/guides/ | [docs/guides/DEVELOPMENT.md](docs/guides/DEVELOPMENT.md) |
| **Frontend updates** | docs/guides/ | [docs/guides/FRONTEND_UPDATE_GUIDE.md](docs/guides/FRONTEND_UPDATE_GUIDE.md) |
| **Azure setup** | docs/deployment/ | [docs/deployment/AZURE_SETUP.md](docs/deployment/AZURE_SETUP.md) |
| **GitHub Actions** | docs/deployment/ | [docs/deployment/GITHUB_ACTIONS_SETUP.md](docs/deployment/GITHUB_ACTIONS_SETUP.md) |
| **Architecture** | docs/ | [docs/04_System_Architecture.md](docs/04_System_Architecture.md) |
| **API reference** | docs/ | [docs/06_API_Specification.md](docs/06_API_Specification.md) |

### 💻 Source Code

| Component | Location | Purpose |
|-----------|----------|---------|
| **Backend** | `app/` | Flask REST API |
| **Routes** | `app/routes/` | 7 API modules |
| **Models** | `app/models.py` | Database models |
| **Frontend** | `frontend/` | HTML/CSS/JavaScript |
| **Tests** | `tests/` | Unit & integration tests |
| **Scripts** | `scripts/` | Utility scripts |

---

## 📍 Quick Navigation

### I'm New to the Project
1. [README.md](README.md) - Overview
2. [docs/guides/PROJECT_SUMMARY.md](docs/guides/PROJECT_SUMMARY.md) - Complete summary
3. [docs/04_System_Architecture.md](docs/04_System_Architecture.md) - Architecture

### I Want to Develop Locally
1. [QUICKSTART.md](QUICKSTART.md) - 5-minute setup
2. [docs/guides/DEVELOPMENT.md](docs/guides/DEVELOPMENT.md) - Full development guide

### I Want to Deploy/Update
1. [docs/guides/FRONTEND_UPDATE_GUIDE.md](docs/guides/FRONTEND_UPDATE_GUIDE.md) - Update frontend
2. [docs/deployment/AZURE_SETUP.md](docs/deployment/AZURE_SETUP.md) - Azure setup

### I Need Everything
→ **[docs/INDEX.md](docs/INDEX.md)** ⭐ Complete documentation index

---

## 🔑 Key Entry Points

### 📄 Root Level Files
These are essential and belong at root level:
- `README.md` - Project overview
- `QUICKSTART.md` - Quick setup guide
- `Dockerfile` - Container config
- `requirements.txt` - Dependencies
- `run.py` - Entry point

### 📚 Documentation
All guides and references moved to `docs/`:
- `docs/guides/` - Development guides
- `docs/deployment/` - Deployment guides
- `docs/` - Architecture and design specs

### 🐍 Source Code
Organized by function:
- `app/` - Backend logic
- `frontend/` - Frontend code
- `tests/` - Test suite
- `scripts/` - Utility scripts

---

## 📊 Directory Summary

| Directory | Files | Purpose |
|-----------|-------|---------|
| Root | 4 | Essential files |
| `docs/` | 20+ | All documentation |
| `docs/guides/` | 5 | Development guides |
| `docs/deployment/` | 9 | Deployment guides |
| `app/` | 9 | Backend (Flask) |
| `frontend/` | 3 | Frontend (HTML/CSS/JS) |
| `tests/` | 2 | Test suite |
| `scripts/` | 3 | Utility scripts |
| `ai/` | 8 | Project specs |

---

## ✅ Benefits of This Structure

✅ **Clear organization** - Each section has a purpose  
✅ **Easy navigation** - INDEX.md files guide you  
✅ **Documentation grouped** - All guides together  
✅ **Deployment separate** - Deployment docs isolated  
✅ **Source code clear** - Backend, frontend, tests organized  
✅ **Specifications available** - AI context and specs in `ai/`  
✅ **Scalable** - Easy to add more guides or modules  

---

## 🚀 Next Steps

1. **Start with [docs/INDEX.md](docs/INDEX.md)** for complete navigation
2. **Choose your task** from the Quick Navigation section above
3. **Follow the appropriate guide** for your work

---

**This structure keeps everything organized and easy to find!** 📚
