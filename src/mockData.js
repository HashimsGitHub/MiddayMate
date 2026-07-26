// Mock data for demo - hardcoded venues and users
export const mockVenues = [
  {
    id: 1,
    name: 'The Expresso Bar',
    address: 'Level 5, 123 Queen Street, Brisbane CBD',
    latitude: -27.4679,
    longitude: 153.0281,
    description: 'Premium espresso bar with specialty coffee and fresh pastries',
    image_url: 'https://middaymatesa.blob.core.windows.net/images/The_Expresso_Bar.jpg'
  },
  {
    id: 2,
    name: 'Urban Kitchen and Co',
    address: 'Shop 2, 456 Creek Street, Brisbane CBD',
    latitude: -27.4689,
    longitude: 153.0301,
    description: 'Modern lunch spot with healthy bowls and wraps',
    image_url: 'https://middaymatesa.blob.core.windows.net/images/Urban_Kitchen_and_Co.jpg'
  },
  {
    id: 3,
    name: 'The Boardroom Gaming Cafe',
    address: 'Level 12, 789 George Street, Brisbane CBD',
    latitude: -27.4700,
    longitude: 153.0315,
    description: 'Corporate cafe with premium WiFi and meeting spaces',
    image_url: 'https://middaymatesa.blob.core.windows.net/images/The_Boardroom_Gaming_Cafe.jpg'
  },
  {
    id: 4,
    name: 'Market Bistro',
    address: '101 Margaret Street, Brisbane CBD',
    latitude: -27.4670,
    longitude: 153.0270,
    description: 'French-inspired bistro perfect for business lunches',
    image_url: 'https://middaymatesa.blob.core.windows.net/images/Market_Bistro.jpg'
  },
  {
    id: 5,
    name: 'Chase Restaurant and Lounge',
    address: 'Level 2, 321 Eagle Street, Brisbane CBD',
    latitude: -27.4685,
    longitude: 153.0330,
    description: 'Contemporary bar and kitchen with craft cocktails',
    image_url: 'https://middaymatesa.blob.core.windows.net/images/Chase_Restaurant_and_Lounge.webp'
  },
  {
    id: 6,
    name: 'Green Leaf Cafe and Bar',
    address: '34 Alice Street, Brisbane CBD',
    latitude: -27.4750,
    longitude: 153.0280,
    description: 'Farm-to-table cafe with organic ingredients and sustainability focus',
    image_url: 'https://middaymatesa.blob.core.windows.net/images/Green_Leaf_Cafe_and_Bar.jpg'
  },
  {
    id: 7,
    name: 'The Meeting Place Cafe',
    address: 'Ground Floor, 654 Queen Street, Brisbane CBD',
    latitude: -27.4695,
    longitude: 153.0290,
    description: 'Exclusive lounge for professionals with premium seating',
    image_url: 'https://middaymatesa.blob.core.windows.net/images/The_Meeting_Place_Cafe.jpg'
  },
  {
    id: 8,
    name: 'Chai and Co',
    address: '125 Edward Street, Brisbane CBD',
    latitude: -27.4675,
    longitude: 153.0305,
    description: 'Trendy chai bar with Asian fusion snacks',
    image_url: 'https://middaymatesa.blob.core.windows.net/images/Chai_and_Co.jpg'
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
