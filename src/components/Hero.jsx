import './Hero.css'

export default function Hero({ onGetStarted }) {
  return (
    <section className="hero">
      <div className="hero-content">
        <h2>Meet Someone New During Your Break</h2>
        <p>Discover nearby venues, browse exclusive promotions, and connect with professionals in your network.</p>
        <div className="hero-buttons">
          <button className="btn btn-primary" onClick={onGetStarted}>Explore Now</button>
        </div>
      </div>
    </section>
  )
}
