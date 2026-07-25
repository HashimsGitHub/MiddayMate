import { useState, useEffect } from 'react'
import './VenuesSection.css'

export default function VenuesSection({ venues, onRefresh }) {
  const [filteredVenues, setFilteredVenues] = useState(venues)
  const [searchTerm, setSearchTerm] = useState('')

  useEffect(() => {
    setFilteredVenues(
      venues.filter(v =>
        v.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
        v.description.toLowerCase().includes(searchTerm.toLowerCase())
      )
    )
  }, [searchTerm, venues])

  return (
    <section className="venues-section">
      <div className="container">
        <h3>Nearby Venues</h3>
        <div className="filters">
          <input
            type="text"
            placeholder="Search venues..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
          />
          <button className="btn btn-secondary" onClick={onRefresh}>Refresh</button>
        </div>
        <div className="venues-grid">
          {filteredVenues.length > 0 ? (
            filteredVenues.map(venue => (
              <div key={venue.id} className="venue-card">
                {venue.image_url && (
                  <img src={venue.image_url} alt={venue.name} className="venue-image" />
                )}
                <div className="venue-content">
                  <h4 className="venue-name">{venue.name}</h4>
                  <p className="venue-address">📍 {venue.address}</p>
                  <p className="venue-description">{venue.description}</p>
                  <div className="venue-actions">
                    <button className="btn btn-primary" style={{ flex: 1 }}>View</button>
                    <button className="btn btn-secondary" style={{ flex: 1 }}>Save</button>
                  </div>
                </div>
              </div>
            ))
          ) : (
            <div style={{ gridColumn: '1/-1', textAlign: 'center', padding: '2rem', color: 'var(--text-secondary)' }}>
              No venues found. Try adjusting your search.
            </div>
          )}
        </div>
      </div>
    </section>
  )
}
