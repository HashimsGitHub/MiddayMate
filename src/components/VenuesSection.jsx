import { useState, useEffect } from 'react'
import { mockVenues } from '../mockData'
import './VenuesSection.css'

export default function VenuesSection({ venues: initialVenues, onRefresh }) {
  const [venues, setVenues] = useState(mockVenues)
  const [searchTerm, setSearchTerm] = useState('')
  const [loading, setLoading] = useState(false)

  useEffect(() => {
    // Use mock data for demo
    setVenues(mockVenues)
  }, [])

  const filteredVenues = venues.filter(v =>
    v.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
    v.description.toLowerCase().includes(searchTerm.toLowerCase()) ||
    v.address.toLowerCase().includes(searchTerm.toLowerCase())
  )

  return (
    <section className="venues-section">
      <div className="container">
        <div className="venues-header">
          <div>
            <h3>Nearby Venues</h3>
            <p className="venues-subtitle">Discover cafés and restaurants in your area</p>
          </div>
        </div>

        {searchTerm && (
          <div className="search-bar">
            <input
              type="text"
              placeholder="Search venues..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              className="search-input"
            />
            {searchTerm && (
              <button
                className="clear-search"
                onClick={() => setSearchTerm('')}
              >
                ✕
              </button>
            )}
          </div>
        )}

        {loading ? (
          <div className="loading">
            <p>Loading venues...</p>
          </div>
        ) : filteredVenues.length > 0 ? (
          <div className="venues-grid">
            {filteredVenues.map(venue => (
              <div key={venue.id} className="venue-card">
                <div className="venue-image-wrapper">
                  {venue.image_url ? (
                    <img src={venue.image_url} alt={venue.name} className="venue-image" />
                  ) : (
                    <div className="venue-image-placeholder">☕</div>
                  )}
                </div>
                <div className="venue-content">
                  <h4 className="venue-name">{venue.name}</h4>
                  <p className="venue-address">📍 {venue.address}</p>
                  <p className="venue-description">{venue.description}</p>
                  <div className="venue-actions">
                    <button className="btn btn-primary">View Promotions</button>
                    <button className="btn btn-secondary">♥ Save</button>
                  </div>
                </div>
              </div>
            ))}
          </div>
        ) : (
          <div className="empty-state">
            <p className="empty-icon">🏢</p>
            <p className="empty-text">
              {searchTerm ? 'No venues match your search.' : 'No venues found.'}
            </p>
            {searchTerm && (
              <button
                className="btn btn-secondary"
                onClick={() => setSearchTerm('')}
              >
                Clear Search
              </button>
            )}
          </div>
        )}
      </div>
    </section>
  )
}
