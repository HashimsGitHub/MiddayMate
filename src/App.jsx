import { useState, useEffect } from 'react'
import Navbar from './components/Navbar'
import Hero from './components/Hero'
import AuthSection from './components/AuthSection'
import VenuesSection from './components/VenuesSection'
import ProfileSection from './components/ProfileSection'
import DemoMode from './components/DemoMode'
import Footer from './components/Footer'
import './App.css'

function App() {
  const [currentUser, setCurrentUser] = useState(null)
  const [activeSection, setActiveSection] = useState('home')
  const [venues, setVenues] = useState([])
  const [showDemo, setShowDemo] = useState(false)

  useEffect(() => {
    initializeApp()
  }, [])

  useEffect(() => {
    if (currentUser) {
      fetchVenues()
    }
  }, [currentUser])

  const initializeApp = async () => {
    // Try to seed database on first load
    try {
      await fetch('/api/seed/populate', { method: 'POST' })
    } catch (e) {
      console.log('Database already seeded or seed endpoint not available')
    }
    checkAuthStatus()
  }

  const checkAuthStatus = async () => {
    try {
      const response = await fetch('/api/auth/me')
      if (response.ok) {
        const user = await response.json()
        setCurrentUser(user)
        setActiveSection('venues')
      }
    } catch (error) {
      console.log('Not authenticated')
    }
  }

  const fetchVenues = async () => {
    try {
      const response = await fetch('/api/venues')
      if (response.ok) {
        const data = Array.isArray(response) ? response : response
        const venueList = Array.isArray(data) ? data : data.venues || []
        setVenues(venueList)
      }
    } catch (error) {
      console.error('Failed to fetch venues:', error)
    }
  }

  const handleLogout = () => {
    setCurrentUser(null)
    setActiveSection('home')
  }

  const handleGetStarted = () => {
    if (currentUser) {
      setActiveSection('venues')
    } else {
      setActiveSection('auth')
    }
  }

  return (
    <div className="app">
      <Navbar
        currentUser={currentUser}
        onLogout={handleLogout}
        activeSection={activeSection}
        onNavigate={setActiveSection}
      />

      {activeSection === 'home' && (
        <Hero
          onGetStarted={handleGetStarted}
          onDemoMode={() => setShowDemo(true)}
        />
      )}

      {activeSection === 'auth' && !currentUser && (
        <AuthSection onAuthSuccess={(user) => {
          setCurrentUser(user)
          setActiveSection('venues')
        }} />
      )}

      {activeSection === 'venues' && currentUser && (
        <VenuesSection venues={venues} onRefresh={fetchVenues} />
      )}

      {activeSection === 'profile' && currentUser && (
        <ProfileSection
          user={currentUser}
          onUpdate={(updatedUser) => setCurrentUser(updatedUser)}
        />
      )}

      {showDemo && (
        <DemoMode onClose={() => setShowDemo(false)} />
      )}

      <Footer />
    </div>
  )
}

export default App
