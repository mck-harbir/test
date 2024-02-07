import re
import string
from flask_restful import Resource, reqparse



class Login(Resource):
    ""
    A class representing the login resource.

    This class provides methods for validating and registering users. It uses a parser object to parse incoming requests and validate their parameters.

    Attributes:
        parser (reqparse.RequestParser): The request parser used to parse incoming requests.
    ""

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('username', required=True)
        self.parser.add_argument('password', required=True)

    @staticmethod
    def _validate_username(username):
        """
        Validates the given username.

        Args:
            username (str): The username to validate.

        Returns:
            bool: True if the username is valid; False otherwise.
        """
        # TODO: Implement this method
        pass

    @staticmethod
    def _validate_password(password):
        """
        Validates the given password.

        Args:
            password (str): The password to validate.

        Returns:
            bool: True if the password is valid; False otherwise.
        """
        # TODO: Implement this method
        pass

    def post(self):
        """
        Handles POST requests to register a new user.

        This method handles POST requests to the login endpoint by parsing the request body and validating the provided username and password.
        If the username or password are invalid, it returns a bad request response with an error message. Otherwise, it checks if the username already exists in the database.
        If the username does exist, it returns a server error response with an error message indicating that the user already exists.
        If the username doesn't exist, it encrypts the password and saves the username-password pair in the database. Finally, it returns a success response with a status code of 200.

        Returns:
            Response: The response containing the result of the operation.
        """
        args = self.parser.parse_args()
        username = args['username']
        password = args['password']

        if not self._validate_username(username):
            return {'message': 'Invalid username'}, 400

        if not self._validate_password(password):
            return {'message': 'Invalid password'}, 400

        if User.query.filter_by(username=username).first():
            return {'message': 'User already exists.'}, 500

        hashed_password = <PASSWORD>(password)
        user = User(username=username, password=<PASSWORD>)
        db.session.add(user)
        db.session.commit()

        return '', 200


if __name__ == '__main__':
    app.run(debug=True)