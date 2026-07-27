import { useState } from 'react'
import './VendorPortal.css'

export default function VendorPortal() {
  const [formData, setFormData] = useState({
    name: '',
    company_name: '',
    address: '',
    description: '',
    phone: '',
    website: '',
    email: ''
  })

  const [image, setImage] = useState(null)
  const [imagePreview, setImagePreview] = useState(null)
  const [loading, setLoading] = useState(false)
  const [message, setMessage] = useState('')
  const [messageType, setMessageType] = useState('') // 'success' or 'error'

  const handleInputChange = (e) => {
    const { name, value } = e.target
    setFormData(prev => ({
      ...prev,
      [name]: value
    }))
  }

  const handleImageChange = (e) => {
    const file = e.target.files[0]
    if (file) {
      setImage(file)
      const reader = new FileReader()
      reader.onloadend = () => {
        setImagePreview(reader.result)
      }
      reader.readAsDataURL(file)
    }
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    setLoading(true)
    setMessage('')

    try {
      // Step 1: Register/update vendor
      const vendorRes = await fetch('/api/vendors', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
      })

      if (!vendorRes.ok) {
        const error = await vendorRes.json()
        throw new Error(error.error || 'Failed to register vendor')
      }

      const vendorData = await vendorRes.json()
      const vendorId = vendorData.vendor.id

      // Step 2: Upload image if provided
      if (image) {
        const formDataImage = new FormData()
        formDataImage.append('image', image)

        const imageRes = await fetch(`/api/vendors/${vendorId}/upload-image`, {
          method: 'POST',
          body: formDataImage
        })

        if (!imageRes.ok) {
          const error = await imageRes.json()
          throw new Error(error.error || 'Failed to upload image')
        }
      }

      setMessageType('success')
      setMessage('Vendor portal submitted successfully! We will review and approve your registration.')

      // Reset form
      setFormData({
        name: '',
        company_name: '',
        address: '',
        description: '',
        phone: '',
        website: '',
        email: ''
      })
      setImage(null)
      setImagePreview(null)

    } catch (error) {
      setMessageType('error')
      setMessage(error.message || 'Failed to submit vendor portal')
      console.error('Error:', error)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="vendor-portal">
      <div className="container">
        <div className="vendor-portal-header">
          <h2>Vendor Portal</h2>
          <p>Register your business and showcase your venues to professionals</p>
        </div>

        {message && (
          <div className={`message-alert ${messageType}`}>
            {message}
          </div>
        )}

        <form onSubmit={handleSubmit} className="vendor-form">
          <div className="form-section">
            <h3>Business Information</h3>

            <div className="form-group">
              <label htmlFor="name">Contact Person Name *</label>
              <input
                type="text"
                id="name"
                name="name"
                value={formData.name}
                onChange={handleInputChange}
                placeholder="Enter your full name"
                required
              />
            </div>

            <div className="form-group">
              <label htmlFor="company_name">Company Name *</label>
              <input
                type="text"
                id="company_name"
                name="company_name"
                value={formData.company_name}
                onChange={handleInputChange}
                placeholder="Enter company name"
                required
              />
            </div>

            <div className="form-group">
              <label htmlFor="email">Email Address *</label>
              <input
                type="email"
                id="email"
                name="email"
                value={formData.email}
                onChange={handleInputChange}
                placeholder="Enter email address"
                required
              />
            </div>

            <div className="form-row">
              <div className="form-group">
                <label htmlFor="phone">Phone Number</label>
                <input
                  type="tel"
                  id="phone"
                  name="phone"
                  value={formData.phone}
                  onChange={handleInputChange}
                  placeholder="02-9999-0000"
                />
              </div>

              <div className="form-group">
                <label htmlFor="website">Website</label>
                <input
                  type="url"
                  id="website"
                  name="website"
                  value={formData.website}
                  onChange={handleInputChange}
                  placeholder="https://yourwebsite.com"
                />
              </div>
            </div>

            <div className="form-group">
              <label htmlFor="address">Business Address *</label>
              <input
                type="text"
                id="address"
                name="address"
                value={formData.address}
                onChange={handleInputChange}
                placeholder="Enter business address"
                required
              />
            </div>

            <div className="form-group">
              <label htmlFor="description">Business Description</label>
              <textarea
                id="description"
                name="description"
                value={formData.description}
                onChange={handleInputChange}
                placeholder="Tell us about your business..."
                rows="4"
              />
            </div>
          </div>

          <div className="form-section">
            <h3>Business Image</h3>
            <p className="form-helper-text">Upload a professional photo of your business (JPG, PNG, WebP - Max 5MB)</p>

            <div className="image-upload-area">
              {imagePreview ? (
                <div className="image-preview">
                  <img src={imagePreview} alt="Preview" />
                  <button
                    type="button"
                    className="btn-remove-image"
                    onClick={() => {
                      setImage(null)
                      setImagePreview(null)
                    }}
                  >
                    ✕ Remove
                  </button>
                </div>
              ) : (
                <label className="upload-label">
                  <input
                    type="file"
                    accept="image/*"
                    onChange={handleImageChange}
                    style={{ display: 'none' }}
                  />
                  <div className="upload-content">
                    <span className="upload-icon">🖼️</span>
                    <span className="upload-text">Click to upload image or drag and drop</span>
                  </div>
                </label>
              )}
            </div>
          </div>

          <div className="form-actions">
            <button
              type="submit"
              className="btn btn-primary"
              disabled={loading}
            >
              {loading ? 'Submitting...' : 'Submit Vendor Registration'}
            </button>
          </div>
        </form>
      </div>
    </div>
  )
}
