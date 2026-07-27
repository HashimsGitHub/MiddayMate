import { useState, useEffect } from 'react'
import Navbar from './components/Navbar'
import Hero from './components/Hero'
import VenuesSection from './components/VenuesSection'
import MeetupsSection from './components/MeetupsSection'
import ProfileSection from './components/ProfileSection'
import VendorPortal from './pages/VendorPortal'
import ChatModal from './components/ChatModal'
import Footer from './components/Footer'
import { mockCurrentUser } from './mockData'
import './App.css'

function App() {
  const [currentUser, setCurrentUser] = useState(mockCurrentUser)
  const [activeSection, setActiveSection] = useState('home')
  const [venues, setVenues] = useState([])
  const [showChatModal, setShowChatModal] = useState(false)

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
        <Hero onGetStarted={handleGetStarted} />
      )}

      {activeSection === 'venues' && (
        <VenuesSection venues={venues} onRefresh={fetchVenues} />
      )}

      {activeSection === 'meetups' && (
        <MeetupsSection />
      )}

      {activeSection === 'profile' && (
        <ProfileSection
          user={currentUser}
          onUpdate={(updatedUser) => setCurrentUser(updatedUser)}
          onShowChat={() => setShowChatModal(true)}
        />
      )}

      {activeSection === 'vendor-portal' && (
        <VendorPortal />
      )}

      {showChatModal && (
        <ChatModal onClose={() => setShowChatModal(false)} currentUser={currentUser} />
      )}

      <Footer />
    </div>
  )
}

export default App
