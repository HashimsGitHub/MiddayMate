# MiddayMate - Demo & Prototype Setup

This guide explains how to set up and run MiddayMate with demo data for showcasing features without OAuth configuration.

## ✅ Quick Start for Demo

### 1. Populate Database with Dummy Data

The app includes a seed script that populates the SQLite database with realistic demo data:

```bash
# Activate Python virtual environment
.venv\Scripts\activate

# Run the seed script
python scripts/seed_database.py
```

This creates:
- **6 Demo Users**: Sarah Johnson, Michael Chen, Emily Rodriguez, James Thompson, Lisa Wang, David Kumar
- **8 CBD Venues**: The Espresso Bar, Urban Lunch Co, The Boardroom Cafe, Market Street Bistro, Chase Bar & Kitchen, Green Leaf Organic Cafe, The Meeting Room, Chai & Co
- **10 Active Promotions**: Happy Hour Coffee, Lunch Combos, Corporate Packages, Happy Hour Cocktails, etc.

### 2. Start the Application

**Development Mode:**
```bash
npm run dev      # Runs React dev server with HMR
# In another terminal:
python run.py    # Runs Flask backend
```

**Production Mode:**
```bash
npm run build    # Build React optimized bundle
# Then run Flask:
python run.py
```

### 3. Login as Demo User

On the login screen:
1. Click **"Demo Login"**
2. Select any user (e.g., Sarah Johnson)
3. Explore the app with full venue and promotion data

## 🎯 What to Demo

### Home Page
- Beautiful dark theme with silver chrome accents
- Hero section with premium business venue imagery
- Clear call-to-action: "Explore Now"

### Venues Discovery
- 8 realistic CBD Sydney venues
- Search and filter functionality
- Each venue shows description and location
- "View" and "Save" buttons (ready for implementation)

### Promotions Showcase
- Happy Hour specials
- Lunch combo deals
- Corporate meeting packages
- Discount percentages clearly displayed
- Active date ranges

### Profile Management
- Edit user availability status (Available/Busy/Away)
- Update bio and name
- Demo user data pre-populated

### Design Highlights
- **Sleek Black Theme**: #0f1117 background
- **Silver Chrome Accents**: #c0c0c0, #d0d0d0
- **Gold Gradient Buttons**: #b8956a to #d4af94
- **Glassmorphism Effects**: Backdrop-filter blur on cards
- **Smooth Animations**: Hover effects on buttons and cards
- **Responsive Layout**: Works perfectly on mobile and desktop

## 📁 Project Structure

```
MiddayMate/
├── app/                    # Flask backend
│   ├── models.py          # SQLAlchemy models (User, Venue, Promotion)
│   ├── routes/            # API endpoints
│   ├── config.py          # Configuration
│   └── __init__.py        # App factory
├── src/                   # React frontend source
│   ├── App.jsx            # Main app component
│   ├── App.css            # App styles
│   ├── components/        # React components
│   │   ├── Navbar.jsx
│   │   ├── Hero.jsx
│   │   ├── AuthSection.jsx
│   │   ├── VenuesSection.jsx
│   │   ├── ProfileSection.jsx
│   │   └── Footer.jsx
│   └── main.jsx           # React entry point
├── public/                # Static files
│   └── index.html         # HTML template
├── frontend/dist/         # Built React app (auto-generated)
├── scripts/
│   └── seed_database.py   # Database population script
├── package.json           # NPM dependencies
├── vite.config.js         # Vite configuration
├── Dockerfile             # Multi-stage build (Node + Python)
└── requirements.txt       # Python dependencies
```

## 🔧 Technical Stack

### Frontend
- **React 19** - Modern UI component framework
- **Vite** - Lightning-fast build tool with HMR
- **CSS3** - Custom styling with CSS variables

### Backend
- **Flask** - Lightweight Python web framework
- **SQLAlchemy** - ORM for database
- **SQLite** - Simple database (upgradeable to SQL Server/PostgreSQL)

### Deployment
- **Docker** - Multi-stage build (Node.js → React, Python → Flask)
- **Azure Container Apps** - Serverless container hosting

## 🚀 Resetting Demo Data

To reset and reload the database with fresh demo data:

```bash
python scripts/seed_database.py
```

This will:
1. Drop all existing tables
2. Create fresh schema
3. Populate with demo data
4. Show confirmation with list of users and venues

## 🔐 OAuth Configuration (When Ready)

Currently, the app supports demo login for prototyping. To enable OAuth:

1. **Microsoft Azure AD**:
   - Register app in Azure AD
   - Set `MICROSOFT_CLIENT_ID` and `MICROSOFT_CLIENT_SECRET` env vars

2. **Google OAuth**:
   - Create OAuth 2.0 credentials in Google Cloud Console
   - Set `GOOGLE_CLIENT_ID` and `GOOGLE_CLIENT_SECRET` env vars

3. Update Flask routes in `app/routes/auth.py` to handle OAuth flows

## 📝 Environment Variables

Create `.env` file (example):
```
FLASK_ENV=development
FLASK_DEBUG=1
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///instance/middaymate.db
AZURE_STORAGE_CONNECTION_STRING=your-azure-connection-string
```

## ✨ Key Features Showcased

✅ **Dark Theme UI** - Sleek, professional appearance
✅ **Responsive Design** - Works on all screen sizes
✅ **Venue Discovery** - Browse 8 CBD venues with details
✅ **Active Promotions** - Display discount offers and deals
✅ **User Profiles** - Edit availability and bio
✅ **Search/Filter** - Find venues by name or description
✅ **Demo Authentication** - Quick login without OAuth setup
✅ **SQLite Database** - Fully functional data persistence

## 🎓 Demo Talking Points

1. **Modern Frontend**: React + Vite provides fast, responsive experience
2. **Professional Design**: Dark theme with chrome accents appeals to business audience
3. **Location-based Concept**: Real Sydney CBD venues and coordinates
4. **Realistic Promotions**: Actual discount percentages and dates
5. **Scalable Architecture**: Flask backend easily connects to payment/messaging APIs
6. **Enterprise Ready**: Docker containerization, Azure deployment, OAuth-ready

## 📞 Support

For issues or questions during demo:
- Check database has been seeded: `python scripts/seed_database.py`
- Verify Flask backend is running on port 5000
- Clear browser cache if UI doesn't update
- Check browser console for any error messages

---

**Ready to demo!** 🚀

Start with: `python scripts/seed_database.py` then run the app and click "Demo Login"
