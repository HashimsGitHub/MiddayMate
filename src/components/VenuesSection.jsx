import { useState, useEffect } from 'react'
import './VenuesSection.css'

export default function VenuesSection({ venues: initialVenues, onRefresh }) {
  const [venues, setVenues] = useState([])
  const [searchTerm, setSearchTerm] = useState('')
  const [loading, setLoading] = useState(true)
  const [venuePromotions, setVenuePromotions] = useState({})

  const promotions = [
    'Buy-1-Get-1',
    '20% Off Today',
    'First Date on Us',
    'Celebrate Success 50% Off',
    'MiddayMate Offer'
  ]

  const getRandomPromotion = () => {
    return promotions[Math.floor(Math.random() * promotions.length)]
  }

  useEffect(() => {
    fetchVenues()
  }, [])

  const fetchVenues = async () => {
    try {
      setLoading(true)
      const response = await fetch('/api/venues')

      if (response.ok) {
        const data = await response.json()
        setVenues(data)

        // Generate random promotions for each venue
        const promos = {}
        data.forEach(venue => {
          promos[venue.id] = getRandomPromotion()
        })
        setVenuePromotions(promos)
      } else {
        console.error('Failed to fetch venues')
        setVenues([])
      }
    } catch (error) {
      console.error('Error fetching venues:', error)
      setVenues([])
    } finally {
      setLoading(false)
    }
  }

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
                  <div className="venue-promotion">
                    <span className="promotion-badge">✨ {venuePromotions[venue.id]}</span>
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
