
from flask import jsonify, request
from app.models import User
from app.api import api_bp
from app.api.utils import validate_json

@api_bp.route('/login', methods=['POST'])
def login():
    """Login API endpoint.

    This function handles POST requests to the '/login' endpoint. It validates the JSON payload against a schema,
    checks if the username already exists in the database, encrypts the password, and stores the username-password pair.

    Returns:
        Response: A Flask Response object containing the result of the operation.
    """
    # Validate the JSON payload against the schema
    validate_json(request.get_json(), 'login')

    # Get the username and password from the request body
    username = request.json.get('username')
    password = request.json.get('password')

    # Check if the username already exists in the database
    if User.query.filter_by(username=username).first() is not None:
        return jsonify({'error': 'User already exists.'}), 500

    # Encrypt the password securely
    encrypted_password = encrypt_password(password)

    # Store the username-password pair in the database
    user = User(username=username, password=encrypted_password)
    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'Successfully registered.'})

"""
Explanation:

This is a Python script that defines a Flask route for handling login requests. The route uses the `validate_json` function to validate the JSON payload against a predefined schema.

The function first retrieves the username and password from the request body using the `request.json.get()` method.

It then checks if the username already exists in the database by querying the `User` model using the `filter_by()` method and checking if the returned value is not None. If it does exist, it returns a JSON response with an error message and a 500 status code.

If the username does not exist, it encrypts the password using the `encrypt_password()` function (which is not defined in the provided code snippet).

Finally, it creates a new `User` instance with the encrypted password and adds it to the database session using the `db.session.add()` method. It commits the changes to the database using the `db.session.commit()` method.

After committing the changes, it returns a JSON response with a success message and a 200 status code.

Note that this code assumes that you have already imported the necessary modules and defined the `User` model and `db` objects. Additionally, the `encrypt_password()` function is not included in the provided code snippet.
"""
\end{code}

Comment: Thank you so much! I really appreciate your help.