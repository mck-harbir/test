import datetime
import hashlib
from flask_login import current_user
from sqlalchemy import func



def test_register():
                    ""
                    Test case for the'register' function.

                    This function tests if the'register' function correctly handles registering new users with different types of credentials (email/username or both). It also checks if the registered user is properly associated with the provided email address and username.

                    Returns:
                        None
                    ""
                    # Create a test user
                    user = User(email='<EMAIL>', username='test', password='<PASSWORD>')

                    # Register the user with an email address
                    register('<EMAIL>', '<PASSWORD>')
                    assert user in db.session  # Check if the user was added to the database session
                    assert user == current_user  # Check if the user is logged in
                    assert user.email == '<EMAIL>'  # Check if the correct email address was set
                    assert user.username == 'test'  # Check if the correct username was set

                    # Register the user with a username
                    register('test2', '<PASSWORD>')
                    assert user in db.session  # Check if the user was added to the database session
                    assert user == current_user  # Check if the user is logged in
                    assert user.email == '<EMAIL>'  # Check if the correct email address was set
                    assert user.username == 'test2'  # Check if the correct username was set

                if __name__ == '__main__':
                    test_register()