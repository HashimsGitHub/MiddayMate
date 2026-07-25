import { useState } from 'react'
import './AuthSection.css'

export default function AuthSection({ onAuthSuccess }) {
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

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

  return (
    <section className="auth-section">
      <div className="auth-card">
        <h3>Sign In to MiddayMate</h3>
        {error && <div className="error-message">{error}</div>}
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
      </div>
    </section>
  )
}
