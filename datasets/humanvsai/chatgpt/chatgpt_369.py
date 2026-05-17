from flask import request, jsonify

def verify_oauth_token_and_set_current_user():
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return jsonify({'message': 'Authorization header missing'}), 400

    parts = auth_header.split()
    if parts[0].lower() != 'bearer':
        return jsonify({'message': 'Invalid token type'}), 400

    token = parts[1]
    # logic for verifying the token and fetching the current user
    current_user = fetch_current_user(token)

    # set the current user on the request stack
    request.current_user = current_user
