import { useState } from 'react'
import './ChatModal.css'

export default function ChatModal({ onClose, currentUser }) {
  const [isVisible, setIsVisible] = useState(true)

  const handleClose = () => {
    setIsVisible(false)
    onClose()
  }

  const sarah = {
    name: 'Sarah Johnson',
    email: 'sarah.johnson@dxc.com',
    avatar: '👩‍💼'
  }

  const jake = {
    name: 'Jake Thompson',
    email: 'jake.thompson@techcorp.com',
    avatar: '👨‍💻'
  }

  const conversation = [
    {
      sender: 'sarah',
      message: 'Hi Jake! 👋 I saw you\'re also available for lunch today',
      timestamp: '12:15 PM'
    },
    {
      sender: 'jake',
      message: 'Hey Sarah! Yeah, I\'m taking a break from my current project. What did you have in mind?',
      timestamp: '12:16 PM'
    },
    {
      sender: 'sarah',
      message: 'There\'s a great cafe nearby - The Espresso Bar. They have amazing specialty coffee and it\'s perfect for a quick catch-up. Plus they have a Happy Hour special running!',
      timestamp: '12:17 PM'
    },
    {
      sender: 'jake',
      message: 'The Espresso Bar sounds perfect! I love their coffee. When were you thinking?',
      timestamp: '12:18 PM'
    },
    {
      sender: 'sarah',
      message: 'Maybe in about 10 minutes? I can walk over there now',
      timestamp: '12:19 PM'
    },
    {
      sender: 'jake',
      message: 'Perfect! I\'ll head over there now. See you in a few! ☕',
      timestamp: '12:20 PM'
    },
    {
      sender: 'system',
      message: 'Sarah and Jake are now connected and meeting at The Espresso Bar! ✓',
      timestamp: '12:21 PM'
    }
  ]

  if (!isVisible) return null

  return (
    <div className="chat-modal-overlay">
      <div className="chat-modal-container">
        <div className="chat-modal-header">
          <div className="chat-title">
            <h3>Sarah & Jake's Meeting</h3>
            <p className="chat-subtitle">The Espresso Bar - Queen Street, Brisbane CBD</p>
          </div>
          <button className="chat-close" onClick={handleClose}>✕</button>
        </div>

        <div className="chat-messages">
          {conversation.map((msg, idx) => (
            <div key={idx} className={`chat-message ${msg.sender}`}>
              {msg.sender !== 'system' && (
                <div className="message-avatar">
                  {msg.sender === 'sarah' ? sarah.avatar : jake.avatar}
                </div>
              )}
              <div className={`message-content ${msg.sender}`}>
                {msg.sender !== 'system' && (
                  <p className="message-sender">
                    {msg.sender === 'sarah' ? sarah.name : jake.name}
                  </p>
                )}
                <p className="message-text">{msg.message}</p>
                <span className="message-time">{msg.timestamp}</span>
              </div>
            </div>
          ))}
        </div>

        <div className="chat-modal-footer">
          <div className="meeting-status">
            <img
              src="https://middaymatesa.blob.core.windows.net/images/CoffeeFirstDate.png"
              alt="Meeting Arranged"
              className="meeting-status-image"
            />
          </div>
          <button className="btn btn-primary" onClick={handleClose}>
            Got it!
          </button>
        </div>
      </div>
    </div>
  )
}
