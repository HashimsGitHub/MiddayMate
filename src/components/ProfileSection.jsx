import { useState } from 'react'
import './ProfileSection.css'

export default function ProfileSection({ user, onUpdate, onShowChat }) {
  const [formData, setFormData] = useState({
    name: user.name || '',
    bio: user.bio || '',
    availability: user.availability_status || 'available'
  })
  const [loading, setLoading] = useState(false)
  const [message, setMessage] = useState(null)

  const handleChange = (e) => {
    const { name, value } = e.target
    setFormData(prev => ({ ...prev, [name]: value }))
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    setLoading(true)
    // Mock update - no API call in mockup mode
    setTimeout(() => {
      const updatedUser = { ...user, ...formData }
      onUpdate(updatedUser)
      setMessage('Profile updated successfully!')
      setLoading(false)
      setTimeout(() => setMessage(null), 3000)
    }, 500)
  }

  return (
    <section className="profile-section">
      <div className="container">
        <div className="profile-card">
          <h3>My Profile</h3>
          {message && <div className="success-message">{message}</div>}
          <form onSubmit={handleSubmit}>
            <div className="form-group">
              <label htmlFor="name">Name:</label>
              <input
                type="text"
                id="name"
                name="name"
                value={formData.name}
                onChange={handleChange}
                required
              />
            </div>
            <div className="form-group">
              <label htmlFor="bio">Bio:</label>
              <textarea
                id="bio"
                name="bio"
                value={formData.bio}
                onChange={handleChange}
                rows="4"
              />
            </div>
            <div className="form-group">
              <label htmlFor="availability">Availability:</label>
              <select
                id="availability"
                name="availability"
                value={formData.availability}
                onChange={handleChange}
              >
                <option value="available">Available</option>
                <option value="busy">Busy</option>
                <option value="away">Away</option>
              </select>
            </div>
            <div className="form-actions">
              <button type="submit" className="btn btn-primary" disabled={loading}>
                {loading ? 'Saving...' : 'Save Profile'}
              </button>
              {onShowChat && (
                <button type="button" className="btn btn-secondary" onClick={onShowChat}>
                  💬 View Sample Chat
                </button>
              )}
            </div>
          </form>
        </div>
      </div>
    </section>
  )
}
