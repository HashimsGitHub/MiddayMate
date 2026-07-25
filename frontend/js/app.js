/**
 * MiddayMate Frontend Application
 * Main client-side logic for user interactions and API calls
 */

const API_BASE_URL = '/api';
let currentUser = null;

// Initialize app when DOM is loaded
document.addEventListener('DOMContentLoaded', async () => {
    setupEventListeners();
    await checkAuthStatus();
});

/**
 * Setup all event listeners for the application
 */
function setupEventListeners() {
    // Authentication buttons
    document.getElementById('microsoftLoginBtn')?.addEventListener('click', () => loginWithProvider('microsoft'));
    document.getElementById('googleLoginBtn')?.addEventListener('click', () => loginWithProvider('google'));
    document.getElementById('authBtn')?.addEventListener('click', showAuthSection);
    document.getElementById('logoutBtn')?.addEventListener('click', handleLogout);

    // Navigation
    document.getElementById('getStartedBtn')?.addEventListener('click', showAuthSection);

    // Profile form
    document.getElementById('profileForm')?.addEventListener('submit', handleProfileUpdate);

    // Venue search
    document.getElementById('searchInput')?.addEventListener('input', debounce(searchVenues, 300));
    document.getElementById('filterBtn')?.addEventListener('click', applyFilters);

    // Navigation links
    document.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', handleNavigation);
    });
}

/**
 * Check if user is already authenticated
 */
async function checkAuthStatus() {
    try {
        const response = await fetch(`${API_BASE_URL}/auth/me`);

        if (response.ok) {
            currentUser = await response.json();
            showAuthenticatedView();
            await loadVenues();
            await loadInvitations();
        } else {
            showAuthView();
        }
    } catch (error) {
        console.error('Auth check failed:', error);
        showAuthView();
    }
}

/**
 * Login with OAuth provider
 */
async function loginWithProvider(provider) {
    try {
        // In a real app, redirect to OAuth provider
        // For MVP, we'll use a simplified mock flow
        const mockOAuthData = {
            oauth_provider: provider,
            oauth_id: `${provider}-${Date.now()}`,
            email: `user-${Date.now()}@example.com`,
            name: `User ${Date.now()}`
        };

        const response = await fetch(`${API_BASE_URL}/auth/login`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(mockOAuthData)
        });

        if (response.ok) {
            const data = await response.json();
            currentUser = data.user;
            showAuthenticatedView();
            await loadVenues();
        } else {
            alert('Login failed');
        }
    } catch (error) {
        console.error('Login error:', error);
        alert('Login error. Please try again.');
    }
}

/**
 * Handle logout
 */
async function handleLogout() {
    try {
        await fetch(`${API_BASE_URL}/auth/logout`, {
            method: 'POST'
        });

        currentUser = null;
        showAuthView();
    } catch (error) {
        console.error('Logout error:', error);
    }
}

/**
 * Load venues from API
 */
async function loadVenues() {
    try {
        const response = await fetch(`${API_BASE_URL}/venues`);

        if (!response.ok) throw new Error('Failed to load venues');

        const venues = await response.json();
        displayVenues(venues);
    } catch (error) {
        console.error('Error loading venues:', error);
    }
}

/**
 * Display venues in the UI
 */
function displayVenues(venues) {
    const venuesList = document.getElementById('venuesList');

    if (!venuesList) return;

    if (venues.length === 0) {
        venuesList.innerHTML = '<p>No venues found</p>';
        return;
    }

    venuesList.innerHTML = venues.map(venue => `
        <div class="venue-card">
            <div class="venue-image" style="background-color: #e0e0e0;">
                ${venue.image_url ? `<img src="${venue.image_url}" alt="${venue.name}">` : ''}
            </div>
            <div class="venue-content">
                <div class="venue-name">${venue.name}</div>
                <div class="venue-address">${venue.address}</div>
                <div class="venue-description">${venue.description || 'No description'}</div>
                <div class="venue-actions">
                    <button class="btn btn-primary" onclick="viewVenueDetails(${venue.id})">
                        View Details
                    </button>
                    <button class="btn btn-secondary" onclick="inviteSomeone(${venue.id})">
                        Invite
                    </button>
                </div>
            </div>
        </div>
    `).join('');
}

/**
 * Load user invitations
 */
async function loadInvitations() {
    try {
        const response = await fetch(`${API_BASE_URL}/invitations`);

        if (!response.ok) throw new Error('Failed to load invitations');

        const invitations = await response.json();
        displayInvitations(invitations);
    } catch (error) {
        console.error('Error loading invitations:', error);
    }
}

/**
 * Display invitations in the UI
 */
function displayInvitations(invitations) {
    const invitationsList = document.getElementById('invitationsList');

    if (!invitationsList) return;

    if (invitations.length === 0) {
        invitationsList.innerHTML = '<p>No invitations yet</p>';
        return;
    }

    invitationsList.innerHTML = invitations.map(invitation => `
        <div class="invitation-item">
            <div class="invitation-sender">From: User ${invitation.sender_id}</div>
            <div class="invitation-venue">Venue: ${invitation.venue_id}</div>
            <div class="invitation-actions">
                <button class="btn btn-primary" onclick="acceptInvitation(${invitation.id})">
                    Accept
                </button>
                <button class="btn btn-secondary" onclick="declineInvitation(${invitation.id})">
                    Decline
                </button>
            </div>
        </div>
    `).join('');
}

/**
 * Handle profile form submission
 */
async function handleProfileUpdate(e) {
    e.preventDefault();

    const formData = {
        name: document.getElementById('name').value,
        bio: document.getElementById('bio').value,
        availability_status: document.getElementById('availability').value
    };

    try {
        const response = await fetch(`${API_BASE_URL}/users/profile`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        });

        if (response.ok) {
            const data = await response.json();
            currentUser = data.user;
            alert('Profile updated successfully');
        } else {
            alert('Failed to update profile');
        }
    } catch (error) {
        console.error('Error updating profile:', error);
        alert('Error updating profile');
    }
}

/**
 * Accept an invitation
 */
async function acceptInvitation(invitationId) {
    try {
        const response = await fetch(`${API_BASE_URL}/invitations/${invitationId}/accept`, {
            method: 'POST'
        });

        if (response.ok) {
            alert('Invitation accepted!');
            await loadInvitations();
        } else {
            alert('Failed to accept invitation');
        }
    } catch (error) {
        console.error('Error accepting invitation:', error);
    }
}

/**
 * Decline an invitation
 */
async function declineInvitation(invitationId) {
    try {
        const response = await fetch(`${API_BASE_URL}/invitations/${invitationId}/decline`, {
            method: 'POST'
        });

        if (response.ok) {
            alert('Invitation declined');
            await loadInvitations();
        } else {
            alert('Failed to decline invitation');
        }
    } catch (error) {
        console.error('Error declining invitation:', error);
    }
}

/**
 * View venue details (placeholder)
 */
function viewVenueDetails(venueId) {
    alert(`Viewing details for venue ${venueId}`);
}

/**
 * Invite someone to a venue (placeholder)
 */
function inviteSomeone(venueId) {
    if (!currentUser) {
        alert('Please sign in first');
        return;
    }
    alert(`Invite someone to venue ${venueId}`);
}

/**
 * Search venues
 */
async function searchVenues(query) {
    try {
        const response = await fetch(`${API_BASE_URL}/venues`);

        if (!response.ok) throw new Error('Failed to load venues');

        let venues = await response.json();

        // Client-side filtering
        venues = venues.filter(v =>
            v.name.toLowerCase().includes(query.toLowerCase()) ||
            v.address.toLowerCase().includes(query.toLowerCase())
        );

        displayVenues(venues);
    } catch (error) {
        console.error('Error searching venues:', error);
    }
}

/**
 * Apply filters
 */
function applyFilters() {
    const query = document.getElementById('searchInput').value;
    searchVenues(query);
}

/**
 * Navigation handler
 */
function handleNavigation(e) {
    const target = e.target.getAttribute('href');

    if (target === '#profile') {
        if (!currentUser) {
            showAuthSection();
            return;
        }
        showProfileSection();
    } else if (target === '#venues') {
        showVenuesSection();
    } else if (target === '#home') {
        showHomeSection();
    }
}

/**
 * UI Display Functions
 */

function showAuthView() {
    document.getElementById('authSection').style.display = 'block';
    document.getElementById('venuesSection').style.display = 'none';
    document.getElementById('profileSection').style.display = 'none';
    document.getElementById('authBtn').style.display = 'block';
    document.getElementById('logoutBtn').style.display = 'none';
    document.getElementById('profileLink').style.display = 'none';
}

function showAuthenticatedView() {
    document.getElementById('authSection').style.display = 'none';
    document.getElementById('authBtn').style.display = 'none';
    document.getElementById('logoutBtn').style.display = 'block';
    document.getElementById('profileLink').style.display = 'inline-block';
}

function showAuthSection() {
    document.getElementById('authSection').style.display = 'block';
    document.getElementById('venuesSection').style.display = 'none';
    document.getElementById('profileSection').style.display = 'none';
}

function showVenuesSection() {
    document.getElementById('authSection').style.display = 'none';
    document.getElementById('venuesSection').style.display = 'block';
    document.getElementById('profileSection').style.display = 'none';
}

function showProfileSection() {
    if (!currentUser) return;

    document.getElementById('authSection').style.display = 'none';
    document.getElementById('venuesSection').style.display = 'none';
    document.getElementById('profileSection').style.display = 'block';

    // Populate form with current user data
    document.getElementById('name').value = currentUser.name || '';
    document.getElementById('bio').value = currentUser.bio || '';
    document.getElementById('availability').value = currentUser.availability_status || 'away';
}

function showHomeSection() {
    document.getElementById('authSection').style.display = 'none';
    document.getElementById('venuesSection').style.display = 'none';
    document.getElementById('profileSection').style.display = 'none';
}

/**
 * Utility Functions
 */

function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}
