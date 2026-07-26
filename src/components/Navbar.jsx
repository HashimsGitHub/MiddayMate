import './Navbar.css'

export default function Navbar({ activeSection, onNavigate }) {
  return (
    <nav className="navbar">
      <div className="navbar-container">
        <div className="navbar-brand" onClick={() => onNavigate('home')} style={{ cursor: 'pointer' }}>
          <h1>MiddayMate</h1>
          <p className="tagline">Find Someone New</p>
        </div>
        <div className="navbar-menu">
          <a href="#" onClick={(e) => { e.preventDefault(); onNavigate('home'); }} className="nav-link">Home</a>
          <a href="#" onClick={(e) => { e.preventDefault(); onNavigate('venues'); }} className="nav-link">Venues</a>
          <a href="#" onClick={(e) => { e.preventDefault(); onNavigate('profile'); }} className="nav-link">Profile</a>
          <a href="#" onClick={(e) => { e.preventDefault(); onNavigate('meetups'); }} className="nav-link">MeetUps</a>
        </div>
      </div>
    </nav>
  )
}
