import { useState } from 'react'
import './ProfileSection.css'

export default function ProfileSection({ user, onUpdate, onShowChat }) {
  const [message, setMessage] = useState(null)

  const sarah = {
    name: 'Sarah',
    email: 'sarah.johnson@dxc.com',
    company: 'DXC',
    availability: 'available',
    image: 'https://middaymatesa.blob.core.windows.net/images/Sarah.png'
  }

  const jake = {
    name: 'Jake',
    email: 'jake.thompson@techcorp.com',
    company: 'Tech Corp',
    availability: 'available',
    image: 'https://middaymatesa.blob.core.windows.net/images/Jake.jpg'
  }

  const handleMatchClick = () => {
    setMessage(true)
    onShowChat()
    setTimeout(() => setMessage(null), 5000)
  }

  return (
    <section className="profile-section">
      <div className="container">
        <div className="profiles-header">
          <h3>Available Professionals</h3>
          <p className="profiles-subtitle">Connect with professionals in your network</p>
        </div>

        {message && (
          <div className="success-card">
            <img
              src="https://middaymatesa.blob.core.windows.net/images/CoffeeFirstDate.png"
              alt="Meeting"
              className="success-image"
            />
            <div className="success-content">
              <h4>Meeting Arranged</h4>
              <p>Sarah & Jake are meeting at The Espresso Bar</p>
            </div>
          </div>
        )}

        <div className="profiles-grid">
          <div className="profile-card">
            <div className="profile-image-wrapper">
              <img
                src={sarah.image}
                alt={sarah.name}
                className="profile-image"
              />
            </div>
            <div className="profile-info">
              <h4>{sarah.name}</h4>
              <p className="company-name">{sarah.company}</p>
              <p className="email">{sarah.email}</p>
              <span className="availability-badge available">● Available</span>
            </div>
          </div>

          <div className="profile-card">
            <div className="profile-image-wrapper">
              <img
                src={jake.image}
                alt={jake.name}
                className="profile-image"
              />
            </div>
            <div className="profile-info">
              <h4>{jake.name}</h4>
              <p className="company-name">{jake.company}</p>
              <p className="email">{jake.email}</p>
              <span className="availability-badge available">● Available</span>
            </div>
          </div>
        </div>

        <div className="action-section">
          <button
            className="btn btn-primary btn-large"
            onClick={handleMatchClick}
          >
            ⚡ M2-Match&Meet
          </button>
        </div>
      </div>
    </section>
  )
}
