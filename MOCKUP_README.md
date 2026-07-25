# MiddayMate - Mockup Phase

This is a **functional mockup/prototype** with hardcoded frontend data. All features are working with mock data - no real authentication or database required.

## Current Features (Mockup)

### Frontend
- **Hero Section** - Landing page with CTA buttons
- **Demo Mode** - Interactive walkthrough of Sarah & Jake meeting at a cafe (8-step story)
- **Venues Section** - Beautiful card-based display of 8 CBD Sydney cafes with search
- **Profile Section** - User profile display (Sarah Johnson demo user)
- **Navigation** - Working navbar with Home, Venues, and Profile links

### Design
- Sleek black theme (#0f1117) with silver chrome accents (#c0c0c0)
- Glassmorphism effects with backdrop filters
- Gold accent color (#b8956a)
- Fully responsive, mobile-friendly
- No external dependencies - everything is self-contained

## Data Structure

All data is **hardcoded in frontend** (`src/mockData.js`):

### Venues (8 mock cafes)
- The Espresso Bar
- Urban Lunch Co
- The Boardroom Cafe
- Market Street Bistro
- Chase Bar & Kitchen
- Green Leaf Organic Cafe
- The Meeting Room
- Chai & Co

### Users (6 demo users)
- Sarah Johnson (current logged-in user)
- Jake Thompson
- Michael Chen
- Emily Rodriguez
- Lisa Wang
- David Kumar

### Promotions (10 mock promotions)
- Various discounts and offers across venues

## Removed Features (For Later Development)

The following have been **removed for the mockup phase** and will be implemented in production:

- ❌ OAuth/Social Login
- ❌ Real Database (SQLite)
- ❌ API Authentication
- ❌ Real User Profiles
- ❌ Messaging System
- ❌ Vendor Management
- ❌ Invitations System

## Project Structure

```
MiddayMate/
├── src/                    # React Frontend
│   ├── App.jsx            # Main app component
│   ├── mockData.js        # Hardcoded mock data
│   ├── components/
│   │   ├── Navbar.jsx     # Navigation
│   │   ├── Hero.jsx       # Landing page
│   │   ├── DemoMode.jsx   # Interactive demo
│   │   ├── VenuesSection.jsx  # Venues display
│   │   ├── ProfileSection.jsx  # User profile
│   │   └── Footer.jsx     # Footer
│   └── index.css          # Global styles
│
├── app/                    # Flask Backend (minimal)
│   ├── __init__.py        # App factory
│   ├── config.py          # Configuration
│   ├── models.py          # Database models
│   ├── utils.py           # Utilities
│   └── routes/
│       ├── users.py       # User endpoints (for reference)
│       ├── venues.py      # Venue endpoints (for reference)
│       ├── promotions.py  # Promotion endpoints (for reference)
│       └── seed.py        # Database seeding (reference)
│
├── Dockerfile             # Container build
├── vite.config.js         # Vite build config
├── package.json           # Frontend dependencies
├── requirements.txt       # Backend dependencies
└── docs/                  # Documentation
```

## Deleted Files
- `tests/` - Removed test files
- `test_db.py` - Removed test script
- `src/components/AuthSection.jsx` - Removed OAuth component
- `app/routes/auth.py` - Removed authentication routes
- `app/routes/invitations.py` - Removed invitations routes
- `app/routes/messages.py` - Removed messaging routes
- `app/routes/vendors.py` - Removed vendor management routes

## Running the Mockup

### Local Development
```bash
# Install dependencies
npm install
pip install -r requirements.txt

# Build frontend
npm run build

# Run Flask server
python run.py
```

### Live Mockup
Visit: https://middaymate.calmsand-7d615011.australiaeast.azurecontainerapps.io/

## Next Steps (Production Development)

1. Implement real OAuth login/signup
2. Connect to real database
3. Implement actual user profiles
4. Build messaging system
5. Add venue owner/vendor features
6. Implement payment/promotions system
7. Add real geolocation features
8. Build mobile apps

---

**Note**: This mockup demonstrates the UI/UX and user flow. All data is hardcoded for demonstration purposes.
