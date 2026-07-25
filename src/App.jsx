import { useState, useEffect } from 'react'
import Navbar from './components/Navbar'
import Hero from './components/Hero'
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

  // Demo mode with hardcoded data - no authentication needed

  const fetchVenues = () => {
    // Mock venues already loaded in VenuesSection component
  }


  const handleGetStarted = () => {
    setActiveSection('venues')
  }

  return (
    <div className="app">
      <Navbar
        activeSection={activeSection}
        onNavigate={setActiveSection}
      />

      {activeSection === 'home' && (
        <Hero
          onGetStarted={handleGetStarted}
          onDemoMode={() => setShowDemo(true)}
        />
      )}

      {activeSection === 'venues' && (
        <VenuesSection venues={venues} onRefresh={fetchVenues} />
      )}

      {activeSection === 'profile' && (
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
