import { useState, useEffect } from 'react'
import './DemoMode.css'

export default function DemoMode({ onClose }) {
  const [step, setStep] = useState(0)
  const [isAnimating, setIsAnimating] = useState(false)

  useEffect(() => {
    setIsAnimating(true)
  }, [step])

  const demoSteps = [
    {
      title: "👋 Welcome to MiddayMate",
      description: "Watch Sarah discover a new colleague and arrange a coffee meeting",
      action: "Let's Begin",
      image: "🎬"
    },
    {
      title: "📱 Sarah Logs In",
      description: "Sarah Johnson, a business analyst at DXC, opens the app during her lunch break",
      profile: {
        name: "Sarah Johnson",
        email: "sarah.johnson@dxc.com",
        status: "Available",
        avatar: "👩‍💼"
      },
      action: "Next"
    },
    {
      title: "☕ Discovers Nearby Venues",
      description: "Sarah browses nearby cafés and sees active promotions",
      venues: [
        { name: "The Espresso Bar", promo: "Happy Hour Coffee - 20% off" },
        { name: "Urban Lunch Co", promo: "Lunch Combo - 35% off" }
      ],
      action: "Continue"
    },
    {
      title: "🔍 Finds Jake Available",
      description: "Sarah sees Jake Thompson is also available nearby and interested in connecting",
      users: [
        {
          name: "Jake Thompson",
          company: "Tech Corp",
          status: "Available",
          avatar: "👨‍💻"
        }
      ],
      action: "Next"
    },
    {
      title: "💬 Sends Invitation",
      description: "Sarah sends Jake an invitation to meet at The Espresso Bar",
      message: "Hey Jake! Want to grab a coffee at The Espresso Bar? They have a great Happy Hour special right now! ☕",
      action: "Continue"
    },
    {
      title: "✅ Jake Accepts",
      description: "Jake sees the invitation and immediately accepts!",
      response: "Sounds perfect! I could use a break. See you in 5 minutes!",
      action: "Next"
    },
    {
      title: "📍 They Meet at The Espresso Bar",
      description: "Sarah and Jake connect in person, enjoy their coffee, and have a great conversation",
      meeting: {
        venue: "The Espresso Bar",
        users: ["Sarah Johnson", "Jake Thompson"],
        status: "Connected ✓",
        image: "https://middaymatesa.blob.core.windows.net/images/CoffeeFirstDate.png"
      },
      action: "Finish Demo"
    },
    {
      title: "🎉 Mission Accomplished!",
      description: "MiddayMate made it easy for two professionals to connect and enjoy a break together",
      stats: [
        "✓ Profile created",
        "✓ Venues discovered",
        "✓ Connection made",
        "✓ Meeting arranged"
      ],
      action: "Close"
    }
  ];

  const current = demoSteps[step];

  const handleNext = () => {
    if (step < demoSteps.length - 1) {
      setStep(step + 1)
    } else {
      onClose()
    }
  }

  return (
    <div className="demo-mode-overlay">
      <div className={`demo-mode-container ${isAnimating ? 'animate' : ''}`}>
        <button className="demo-close" onClick={onClose}>✕</button>

        <div className="demo-content">
          <div className="demo-image">{current.image}</div>
          <h2>{current.title}</h2>
          <p className="demo-description">{current.description}</p>

          {/* Step 2: Login */}
          {current.profile && (
            <div className="demo-card profile-card">
              <div className="profile-avatar">{current.profile.avatar}</div>
              <h3>{current.profile.name}</h3>
              <p>{current.profile.email}</p>
              <span className="status-badge available">● {current.profile.status}</span>
            </div>
          )}

          {/* Step 3: Venues */}
          {current.venues && (
            <div className="demo-venues">
              {current.venues.map((venue, idx) => (
                <div key={idx} className="venue-item">
                  <h4>☕ {venue.name}</h4>
                  <p className="promo-badge">{venue.promo}</p>
                </div>
              ))}
            </div>
          )}

          {/* Step 4: Available Users */}
          {current.users && (
            <div className="demo-users">
              {current.users.map((user, idx) => (
                <div key={idx} className="user-item">
                  <div className="user-avatar">{user.avatar}</div>
                  <div className="user-info">
                    <h4>{user.name}</h4>
                    <p>{user.company}</p>
                    <span className="status-badge available">● {user.status}</span>
                  </div>
                </div>
              ))}
            </div>
          )}

          {/* Step 5: Message */}
          {current.message && (
            <div className="demo-message sent">
              <p>{current.message}</p>
            </div>
          )}

          {/* Step 6: Response */}
          {current.response && (
            <div className="demo-message received">
              <p>{current.response}</p>
            </div>
          )}

          {/* Step 7: Meeting */}
          {current.meeting && (
            <div className="demo-meeting">
              {current.meeting.image && (
                <img src={current.meeting.image} alt="Meeting" className="meeting-image" />
              )}
              <h3>📍 {current.meeting.venue}</h3>
              <div className="meeting-users">
                {current.meeting.users.map((user, idx) => (
                  <span key={idx} className="meeting-user">
                    {user.split(' ')[0]}
                  </span>
                ))}
              </div>
              <p className="meeting-status">{current.meeting.status}</p>
            </div>
          )}

          {/* Step 8: Stats */}
          {current.stats && (
            <div className="demo-stats">
              {current.stats.map((stat, idx) => (
                <div key={idx} className="stat-item">{stat}</div>
              ))}
            </div>
          )}
        </div>

        <div className="demo-controls">
          <div className="demo-progress">
            {demoSteps.map((_, idx) => (
              <div
                key={idx}
                className={`progress-dot ${idx === step ? 'active' : ''} ${idx < step ? 'completed' : ''}`}
              />
            ))}
          </div>
          <button className="btn btn-primary" onClick={handleNext}>
            {current.action}
          </button>
        </div>
      </div>
    </div>
  )
}
