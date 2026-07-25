import { useState, useEffect } from 'react'
import Navbar from './components/Navbar'
import Hero from './components/Hero'
import AuthSection from './components/AuthSection'
import VenuesSection from './components/VenuesSection'
import ProfileSection from './components/ProfileSection'
import Footer from './components/Footer'
import './App.css'

function App() {
  const [currentUser, setCurrentUser] = useState(null)
  const [activeSection, setActiveSection] = useState('home')
  const [venues, setVenues] = useState([])

  useEffect(() => {
    checkAuthStatus()
    if (currentUser) {
      fetchVenues()
    }
  }, [currentUser])

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
        const data = await response.json()
        setVenues(data.venues || [])
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
        <Hero onGetStarted={handleGetStarted} />
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

      <Footer />
    </div>
  )
}

export default App
