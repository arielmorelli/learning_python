from flask import Flask
from flask import jsonify
from flask import request
from sqlalchemy import exc

import models

app = Flask(__name__)


@app.route('/get_users', methods=['GET'])
def get_users():
    all_users = models.User.query.all()
    all_users_json = {'objects': []}
    all_users_details = []
    for user in all_users:
        details = {
            'username': user.username,
            'id': user.id,
            'email': user.email,
            'image_link': user.image_link,
        }
        all_users_details.append(details)
    all_users_json['objects'] = all_users_details

    response = jsonify(all_users_json)
    response.headers['Content-type'] = 'application/json'
    return response


@app.route('/new_user', methods=['POST'])
def insert_user():
    """
    Insert new users to DB. This method is called after a POST request,
    so all the data is inside the request object.
    """

    user_username = request.get_json()['username']
    user_email = request.get_json()['email']
    user_image_link = request.get_json()['image_link']

    new_user = models.User(username=user_username, email=user_email,
                           image_link=user_image_link)

    message = ""

    try:
        new_user.insert()
        success = True
        message = "Ok"
        content = {
            'username': user_username,
            'email': user_email,
            'image_link': user_image_link
        }
    except exc.IntegrityError:
        message = "Error: email field must be unique!"
        success = False
        content = {}

    response_json = {
        'success': success,
        'message': message,
        'content': content
    }

    response = jsonify(response_json)
    response.headers['Content-type'] = 'application/json'

    return response


if __name__ == '__main__':
    models.db.create_all()
    app.run(port=8090)
