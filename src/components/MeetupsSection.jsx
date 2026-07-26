import './MeetupsSection.css'

export default function MeetupsSection() {
  const meetup = {
    venue: 'The Espresso Bar',
    address: 'Queen Street, Brisbane CBD',
    user1: 'Sarah',
    user2: 'Jake',
    image: 'https://middaymatesa.blob.core.windows.net/images/CoffeeFirstDate.png',
    status: 'Connected'
  }

  return (
    <section className="meetups-section">
      <div className="container">
        <div className="meetups-header">
          <h3>Your MeetUps</h3>
          <p className="meetups-subtitle">View your upcoming and past connections</p>
        </div>

        <div className="meetups-grid">
          <div className="meetup-card">
            <div className="meetup-image-wrapper">
              <img
                src={meetup.image}
                alt={meetup.venue}
                className="meetup-image"
              />
            </div>
            <div className="meetup-content">
              <h4>{meetup.venue}</h4>
              <p className="meetup-address">📍 {meetup.address}</p>
              <div className="meetup-users">
                <span className="user-badge">{meetup.user1}</span>
                <span className="separator">&</span>
                <span className="user-badge">{meetup.user2}</span>
              </div>
              <div className="meetup-status">
                <span className="status-indicator">✓</span>
                <span className="status-text">{meetup.status}</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  )
}
