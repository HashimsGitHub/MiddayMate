#!/usr/bin/env python
"""Comprehensive CRUD tests for MongoDB migration"""

import os
import sys
from datetime import datetime, timedelta
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

from app import create_app, db
from app.models import User, Venue, Vendor, Promotion, Invitation, Message, UserRole, AvailabilityStatus, InvitationStatus

def print_section(title):
    """Print a section header"""
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}")

def print_test(name, status):
    """Print test result"""
    symbol = "✅" if status else "❌"
    print(f"{symbol} {name}")

def test_connection():
    """Test MongoDB connection"""
    print_section("1. Testing MongoDB Connection")
    try:
        app = create_app('testing')
        with app.app_context():
            # Try to access the database
            user_count = User.objects.count()
            print(f"✅ Connected to MongoDB successfully")
            print(f"   Current users in database: {user_count}")
            return True
    except Exception as e:
        print(f"❌ Connection failed: {str(e)}")
        return False

def test_user_crud():
    """Test User CREATE, READ, UPDATE, DELETE"""
    print_section("2. Testing User CRUD Operations")

    app = create_app('testing')

    with app.app_context():
        try:
            # CREATE
            user = User(
                oauth_id='test_user_001',
                oauth_provider='microsoft',
                email='testuser@example.com',
                name='Test User',
                role=UserRole.PROFESSIONAL.value,
                availability_status=AvailabilityStatus.AVAILABLE.value,
                bio='Test bio'
            )
            user.save()
            user_id = str(user.id)
            print_test("CREATE User", True)

            # READ
            fetched = User.objects.get(id=user_id)
            assert fetched.email == 'testuser@example.com'
            print_test("READ User", True)

            # UPDATE
            fetched.bio = 'Updated bio'
            fetched.availability_status = AvailabilityStatus.BUSY.value
            fetched.save()

            updated = User.objects.get(id=user_id)
            assert updated.bio == 'Updated bio'
            assert updated.availability_status == AvailabilityStatus.BUSY.value
            print_test("UPDATE User", True)

            # DELETE
            User.objects.get(id=user_id).delete()
            remaining = User.objects(id=user_id).first()
            assert remaining is None
            print_test("DELETE User", True)

            return True
        except Exception as e:
            print_test("User CRUD", False)
            print(f"   Error: {str(e)}")
            return False

def test_vendor_crud():
    """Test Vendor CREATE, READ, UPDATE, DELETE"""
    print_section("3. Testing Vendor CRUD Operations")

    app = create_app('testing')

    with app.app_context():
        try:
            # CREATE
            vendor = Vendor(
                name='Test Cafe',
                email='cafe@example.com',
                company_name='Test Cafe Company',
                address='123 Main St, Sydney',
                phone='02-1234-5678',
                is_approved=False
            )
            vendor.save()
            vendor_id = str(vendor.id)
            print_test("CREATE Vendor", True)

            # READ
            fetched = Vendor.objects.get(id=vendor_id)
            assert fetched.email == 'cafe@example.com'
            print_test("READ Vendor", True)

            # UPDATE
            fetched.is_approved = True
            fetched.phone = '02-9876-5432'
            fetched.save()

            updated = Vendor.objects.get(id=vendor_id)
            assert updated.is_approved == True
            assert updated.phone == '02-9876-5432'
            print_test("UPDATE Vendor", True)

            # DELETE
            Vendor.objects.get(id=vendor_id).delete()
            remaining = Vendor.objects(id=vendor_id).first()
            assert remaining is None
            print_test("DELETE Vendor", True)

            return True
        except Exception as e:
            print_test("Vendor CRUD", False)
            print(f"   Error: {str(e)}")
            return False

def test_venue_with_vendor():
    """Test Venue CRUD with Vendor relationship"""
    print_section("4. Testing Venue CRUD with Vendor Relationship")

    app = create_app('testing')

    with app.app_context():
        try:
            # Create vendor first
            vendor = Vendor(
                name='Coffee Co',
                email='coffee@example.com',
                company_name='Coffee Company',
                address='456 King St, Sydney'
            )
            vendor.save()

            # CREATE Venue
            venue = Venue(
                name='Test Coffee Shop',
                address='123 Pitt St, Sydney',
                latitude=-33.8688,
                longitude=151.2093,
                description='A great coffee shop',
                vendor_id=vendor,
                phone='02-1111-1111'
            )
            venue.save()
            venue_id = str(venue.id)
            print_test("CREATE Venue with Vendor", True)

            # READ
            fetched = Venue.objects.get(id=venue_id)
            assert fetched.name == 'Test Coffee Shop'
            assert str(fetched.vendor_id.id) == str(vendor.id)
            print_test("READ Venue with Vendor relationship", True)

            # UPDATE
            fetched.description = 'Updated description'
            fetched.save()

            updated = Venue.objects.get(id=venue_id)
            assert updated.description == 'Updated description'
            print_test("UPDATE Venue", True)

            # DELETE Venue
            Venue.objects.get(id=venue_id).delete()
            assert Venue.objects(id=venue_id).first() is None
            print_test("DELETE Venue", True)

            # Cleanup vendor
            vendor.delete()

            return True
        except Exception as e:
            print_test("Venue CRUD", False)
            print(f"   Error: {str(e)}")
            return False

def test_promotion_crud():
    """Test Promotion CRUD with Venue relationship"""
    print_section("5. Testing Promotion CRUD with Venue Relationship")

    app = create_app('testing')

    with app.app_context():
        try:
            # Create vendor and venue first
            vendor = Vendor(
                name='Test Vendor',
                email='vendor@test.com',
                company_name='Test Company',
                address='789 George St'
            )
            vendor.save()

            venue = Venue(
                name='Test Venue',
                address='789 George St, Sydney',
                latitude=-33.8674,
                longitude=151.2099,
                vendor_id=vendor
            )
            venue.save()

            # CREATE Promotion
            promotion = Promotion(
                venue_id=venue,
                title='Happy Hour Special',
                description='20% off all drinks',
                discount_percentage=20,
                start_date=datetime.now(),
                end_date=datetime.now() + timedelta(days=30),
                is_featured=False
            )
            promotion.save()
            promotion_id = str(promotion.id)
            print_test("CREATE Promotion with Venue", True)

            # READ
            fetched = Promotion.objects.get(id=promotion_id)
            assert fetched.title == 'Happy Hour Special'
            assert fetched.discount_percentage == 20
            print_test("READ Promotion", True)

            # UPDATE
            fetched.discount_percentage = 25
            fetched.is_featured = True
            fetched.save()

            updated = Promotion.objects.get(id=promotion_id)
            assert updated.discount_percentage == 25
            assert updated.is_featured == True
            print_test("UPDATE Promotion", True)

            # DELETE
            Promotion.objects.get(id=promotion_id).delete()
            assert Promotion.objects(id=promotion_id).first() is None
            print_test("DELETE Promotion", True)

            # Cleanup
            venue.delete()
            vendor.delete()

            return True
        except Exception as e:
            print_test("Promotion CRUD", False)
            print(f"   Error: {str(e)}")
            return False

def test_invitation_crud():
    """Test Invitation CRUD with User and Venue relationships"""
    print_section("6. Testing Invitation CRUD with Relationships")

    app = create_app('testing')

    with app.app_context():
        try:
            # Create users
            user1 = User(
                oauth_id='user_1',
                oauth_provider='google',
                email='user1@test.com',
                name='User One'
            )
            user1.save()

            user2 = User(
                oauth_id='user_2',
                oauth_provider='google',
                email='user2@test.com',
                name='User Two'
            )
            user2.save()

            # Create venue
            vendor = Vendor(
                name='Test Vendor',
                email='vendor@test.com',
                company_name='Test Company',
                address='123 Test St'
            )
            vendor.save()

            venue = Venue(
                name='Test Venue',
                address='123 Test St, Sydney',
                latitude=-33.8688,
                longitude=151.2093,
                vendor_id=vendor
            )
            venue.save()

            # CREATE Invitation
            invitation = Invitation(
                sender_id=user1,
                recipient_id=user2,
                venue_id=venue,
                message='Want to grab coffee?',
                status=InvitationStatus.PENDING.value
            )
            invitation.save()
            invitation_id = str(invitation.id)
            print_test("CREATE Invitation with User and Venue", True)

            # READ
            fetched = Invitation.objects.get(id=invitation_id)
            assert fetched.message == 'Want to grab coffee?'
            assert str(fetched.sender_id.id) == str(user1.id)
            assert str(fetched.recipient_id.id) == str(user2.id)
            print_test("READ Invitation", True)

            # UPDATE
            fetched.status = InvitationStatus.ACCEPTED.value
            fetched.save()

            updated = Invitation.objects.get(id=invitation_id)
            assert updated.status == InvitationStatus.ACCEPTED.value
            print_test("UPDATE Invitation", True)

            # DELETE
            Invitation.objects.get(id=invitation_id).delete()
            assert Invitation.objects(id=invitation_id).first() is None
            print_test("DELETE Invitation", True)

            # Cleanup
            user1.delete()
            user2.delete()
            venue.delete()
            vendor.delete()

            return True
        except Exception as e:
            print_test("Invitation CRUD", False)
            print(f"   Error: {str(e)}")
            return False

def test_message_crud():
    """Test Message CRUD with Invitation relationship"""
    print_section("7. Testing Message CRUD with Invitation Relationship")

    app = create_app('testing')

    with app.app_context():
        try:
            # Setup: Create users, venue, vendor, and invitation
            user1 = User(
                oauth_id='user_msg_1',
                oauth_provider='google',
                email='msg1@test.com',
                name='Message User 1'
            )
            user1.save()

            user2 = User(
                oauth_id='user_msg_2',
                oauth_provider='google',
                email='msg2@test.com',
                name='Message User 2'
            )
            user2.save()

            vendor = Vendor(
                name='Message Test Vendor',
                email='msgvendor@test.com',
                company_name='Message Company',
                address='456 Message St'
            )
            vendor.save()

            venue = Venue(
                name='Message Venue',
                address='456 Message St, Sydney',
                latitude=-33.8701,
                longitude=151.2087,
                vendor_id=vendor
            )
            venue.save()

            invitation = Invitation(
                sender_id=user1,
                recipient_id=user2,
                venue_id=venue,
                status=InvitationStatus.ACCEPTED.value
            )
            invitation.save()

            # CREATE Message
            message = Message(
                invitation_id=invitation,
                sender_id=user1,
                content='See you at 3pm!',
                is_read=False
            )
            message.save()
            message_id = str(message.id)
            print_test("CREATE Message with Invitation", True)

            # READ
            fetched = Message.objects.get(id=message_id)
            assert fetched.content == 'See you at 3pm!'
            assert fetched.is_read == False
            print_test("READ Message", True)

            # UPDATE
            fetched.is_read = True
            fetched.save()

            updated = Message.objects.get(id=message_id)
            assert updated.is_read == True
            print_test("UPDATE Message", True)

            # DELETE
            Message.objects.get(id=message_id).delete()
            assert Message.objects(id=message_id).first() is None
            print_test("DELETE Message", True)

            # Cleanup
            invitation.delete()
            user1.delete()
            user2.delete()
            venue.delete()
            vendor.delete()

            return True
        except Exception as e:
            print_test("Message CRUD", False)
            print(f"   Error: {str(e)}")
            return False

def test_queries():
    """Test complex queries"""
    print_section("8. Testing Complex Queries")

    app = create_app('testing')

    with app.app_context():
        try:
            # Setup test data
            vendor = Vendor(
                name='Query Test Vendor',
                email='query@test.com',
                company_name='Query Company',
                address='Query St'
            )
            vendor.save()

            # Create multiple venues
            venues_created = []
            for i in range(3):
                venue = Venue(
                    name=f'Venue {i+1}',
                    address=f'{i+1} Query St, Sydney',
                    latitude=-33.8 + (i * 0.01),
                    longitude=151.20 + (i * 0.01),
                    vendor_id=vendor
                )
                venue.save()
                venues_created.append(venue)

            # Create promotions for first venue
            for i in range(2):
                promotion = Promotion(
                    venue_id=venues_created[0],
                    title=f'Promo {i+1}',
                    description='Test promotion',
                    start_date=datetime.now(),
                    end_date=datetime.now() + timedelta(days=30)
                )
                promotion.save()

            # Test Query 1: Get all venues
            all_venues = list(Venue.objects(vendor_id=vendor))
            assert len(all_venues) == 3
            print_test("Query: Get all venues by vendor", True)

            # Test Query 2: Get active promotions
            active_promos = list(Promotion.objects(
                venue_id=venues_created[0],
                start_date__lte=datetime.now(),
                end_date__gte=datetime.now()
            ))
            assert len(active_promos) == 2
            print_test("Query: Get active promotions", True)

            # Test Query 3: Filter by status
            user1 = User(
                oauth_id='query_user_1',
                oauth_provider='google',
                email='quser1@test.com',
                name='Query User 1',
                availability_status=AvailabilityStatus.AVAILABLE.value
            )
            user1.save()

            user2 = User(
                oauth_id='query_user_2',
                oauth_provider='google',
                email='quser2@test.com',
                name='Query User 2',
                availability_status=AvailabilityStatus.BUSY.value
            )
            user2.save()

            available_users = list(User.objects(availability_status=AvailabilityStatus.AVAILABLE.value))
            assert len(available_users) >= 1
            print_test("Query: Filter users by availability status", True)

            # Cleanup
            Promotion.objects(venue_id__in=venues_created).delete()
            for venue in venues_created:
                venue.delete()
            vendor.delete()
            user1.delete()
            user2.delete()

            return True
        except Exception as e:
            print_test("Complex Queries", False)
            print(f"   Error: {str(e)}")
            return False

def main():
    """Run all tests"""
    print("\n" + "="*60)
    print("  MONGODB CRUD OPERATIONS TEST SUITE")
    print("="*60)

    # Check if MONGO_URI is set
    if not os.environ.get('MONGO_URI'):
        print("\n❌ ERROR: MONGO_URI environment variable not set!")
        print("   Please set your MongoDB connection string first.")
        sys.exit(1)

    results = []

    # Run tests
    results.append(("Connection Test", test_connection()))
    results.append(("User CRUD", test_user_crud()))
    results.append(("Vendor CRUD", test_vendor_crud()))
    results.append(("Venue CRUD", test_venue_with_vendor()))
    results.append(("Promotion CRUD", test_promotion_crud()))
    results.append(("Invitation CRUD", test_invitation_crud()))
    results.append(("Message CRUD", test_message_crud()))
    results.append(("Complex Queries", test_queries()))

    # Summary
    print_section("SUMMARY")
    passed = sum(1 for _, result in results if result)
    total = len(results)

    for name, result in results:
        status = "✅ PASSED" if result else "❌ FAILED"
        print(f"{status}: {name}")

    print(f"\nTotal: {passed}/{total} test groups passed")

    if passed == total:
        print("\n✅ All CRUD operations working correctly!")
        print("   Safe to deploy to production.")
        return 0
    else:
        print(f"\n❌ {total - passed} test group(s) failed!")
        print("   Fix issues before deploying.")
        return 1

if __name__ == '__main__':
    sys.exit(main())
