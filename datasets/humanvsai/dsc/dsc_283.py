from functools import wraps
from flask import request, jsonify, current_app
import jwt

def has_access_api(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return jsonify({'message': 'Missing authorization header'}), 401

        try:
            token = auth_header.split(" ")[1]
            data = jwt.decode(token, current_app.config['SECRET_KEY'])
            user_id = data['sub']
            user = User.query.filter_by(id=user_id).first()

            if not user:
                return jsonify({'message': 'User not found'}), 401

            if not user.has_permission(f.__name__):
                return jsonify({'message': 'Unauthorized'}), 401

        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Signature expired. Please log in again.'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token. Please log in again.'}), 401

        return f(*args, **kwargs)

    return decorated_function