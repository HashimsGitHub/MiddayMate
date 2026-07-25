// Mock data for demo - hardcoded venues and users
export const mockVenues = [
  {
    id: 1,
    name: 'The Espresso Bar',
    address: 'Level 5, 123 King Street, Sydney CBD',
    latitude: -33.8688,
    longitude: 151.2093,
    description: 'Premium espresso bar with specialty coffee and fresh pastries'
  },
  {
    id: 2,
    name: 'Urban Lunch Co',
    address: 'Shop 2, 456 Pitt Street, Sydney CBD',
    latitude: -33.8701,
    longitude: 151.2087,
    description: 'Modern lunch spot with healthy bowls and wraps'
  },
  {
    id: 3,
    name: 'The Boardroom Cafe',
    address: 'Level 12, 789 George Street, Sydney CBD',
    latitude: -33.8674,
    longitude: 151.2099,
    description: 'Corporate cafe with premium WiFi and meeting spaces'
  },
  {
    id: 4,
    name: 'Market Street Bistro',
    address: '101 Market Street, Sydney CBD',
    latitude: -33.8685,
    longitude: 151.2072,
    description: 'French-inspired bistro perfect for business lunches'
  },
  {
    id: 5,
    name: 'Chase Bar & Kitchen',
    address: 'Level 2, 321 Clarence Street, Sydney CBD',
    latitude: -33.8695,
    longitude: 151.2055,
    description: 'Contemporary bar and kitchen with craft cocktails'
  },
  {
    id: 6,
    name: 'Green Leaf Organic Cafe',
    address: '34 Martin Place, Sydney CBD',
    latitude: -33.8650,
    longitude: 151.2112,
    description: 'Farm-to-table cafe with organic ingredients and sustainability focus'
  },
  {
    id: 7,
    name: 'The Meeting Room',
    address: 'Ground Floor, 654 Bourke Street, Sydney CBD',
    latitude: -33.8776,
    longitude: 151.2060,
    description: 'Exclusive lounge for professionals with premium seating'
  },
  {
    id: 8,
    name: 'Chai & Co',
    address: '125 Castlereagh Street, Sydney CBD',
    latitude: -33.8705,
    longitude: 151.2110,
    description: 'Trendy chai bar with Asian fusion snacks'
  },
];

export const mockPromotions = [
  { id: 1, venue_id: 1, title: 'Happy Hour Coffee Special', description: '20% off all espresso-based drinks from 2-4 PM', discount_percentage: 20 },
  { id: 2, venue_id: 1, title: 'Free Pastry with Coffee', description: 'Buy any coffee, get a free pastry (up to $8 value)', discount_percentage: null },
  { id: 3, venue_id: 2, title: 'Lunch Combo Deal', description: 'Get a bowl + drink + dessert for $15', discount_percentage: 35 },
  { id: 4, venue_id: 2, title: 'CBD Workers Special', description: '10% off with work ID for all lunch items', discount_percentage: 10 },
  { id: 5, venue_id: 3, title: 'Corporate Meeting Packages', description: 'Private meeting room + catering from $200', discount_percentage: null },
  { id: 6, venue_id: 4, title: 'Afternoon Tea Promo', description: 'Elegant afternoon tea service, normally $35, now $25', discount_percentage: 29 },
  { id: 7, venue_id: 5, title: 'Happy Hour Cocktails', description: 'Buy 1 cocktail, get 2nd at 50% off (4-6 PM)', discount_percentage: 50 },
  { id: 8, venue_id: 6, title: 'Organic Breakfast Bundle', description: 'Breakfast + fresh juice + smoothie for $18', discount_percentage: 22 },
  { id: 9, venue_id: 7, title: 'Executive Lounge Trial', description: 'Free day pass to the lounge with any purchase over $50', discount_percentage: null },
  { id: 10, venue_id: 8, title: 'Chai Lovers Festival', description: '25% off all chai varieties this month', discount_percentage: 25 },
];

export const mockUsers = [
  { id: 1, name: 'Sarah Johnson', email: 'sarah.johnson@dxc.com', availability_status: 'available' },
  { id: 2, name: 'Jake Thompson', email: 'jake.thompson@techcorp.com', availability_status: 'available' },
  { id: 3, name: 'Michael Chen', email: 'michael.chen@dxc.com', availability_status: 'available' },
  { id: 4, name: 'Emily Rodriguez', email: 'emily.rodriguez@dxc.com', availability_status: 'busy' },
  { id: 5, name: 'Lisa Wang', email: 'lisa.wang@financeplus.com', availability_status: 'away' },
  { id: 6, name: 'David Kumar', email: 'david.kumar@consulting.com', availability_status: 'available' },
];

// Default logged-in user for mockup
export const mockCurrentUser = {
  id: 1,
  name: 'Sarah Johnson',
  email: 'sarah.johnson@dxc.com',
  bio: 'Digital professional passionate about networking and exploring new venues',
  availability_status: 'available'
};
