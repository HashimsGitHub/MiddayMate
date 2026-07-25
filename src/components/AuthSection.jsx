import { useState } from 'react'
import './AuthSection.css'

export default function AuthSection({ onAuthSuccess }) {
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)
  const [showDemo, setShowDemo] = useState(false)

  const demoUsers = [
    { id: 1, name: 'Sarah Johnson', email: 'sarah.johnson@dxc.com' },
    { id: 2, name: 'Michael Chen', email: 'michael.chen@dxc.com' },
    { id: 3, name: 'Emily Rodriguez', email: 'emily.rodriguez@dxc.com' },
    { id: 4, name: 'James Thompson', email: 'james.thompson@techcorp.com' },
  ]

  const handleLogin = async (provider) => {
    setLoading(true)
    setError(null)
    try {
      const response = await fetch(`/api/auth/login`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ provider })
      })

      if (response.ok) {
        const user = await response.json()
        onAuthSuccess(user)
      } else {
        setError('Login failed. Please try again.')
      }
    } catch (err) {
      setError('Login failed. Please try again.')
      console.error(err)
    } finally {
      setLoading(false)
    }
  }

  const handleDemoLogin = (user) => {
    onAuthSuccess(user)
  }

  return (
    <section className="auth-section">
      <div className="auth-card">
        <h3>Sign In to MiddayMate</h3>
        {error && <div className="error-message">{error}</div>}

        {!showDemo ? (
          <>
            <button
              className="btn btn-login btn-microsoft"
              onClick={() => handleLogin('microsoft')}
              disabled={loading}
            >
              {loading ? 'Signing in...' : 'Sign in with Microsoft'}
            </button>
            <button
              className="btn btn-login btn-google"
              onClick={() => handleLogin('google')}
              disabled={loading}
            >
              {loading ? 'Signing in...' : 'Sign in with Google'}
            </button>
            <div className="demo-divider">
              <span>OR</span>
            </div>
            <button
              className="btn btn-secondary"
              onClick={() => setShowDemo(true)}
              style={{ width: '100%' }}
            >
              Demo Login
            </button>
          </>
        ) : (
          <>
            <p className="demo-label">Select a demo user to explore:</p>
            {demoUsers.map(user => (
              <button
                key={user.id}
                className="btn btn-login"
                onClick={() => handleDemoLogin(user)}
              >
                {user.name}
              </button>
            ))}
            <button
              className="btn btn-secondary"
              onClick={() => setShowDemo(false)}
              style={{ width: '100%', marginTop: '1rem' }}
            >
              Back to OAuth
            </button>
          </>
        )}
      </div>
    </section>
  )
}
