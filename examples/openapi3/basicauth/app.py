#!/usr/bin/env python3
'''
Basic example of a resource server
'''

import pointsecio

PASSWD = {
    'admin': 'secret',
    'foo': 'bar'
}


def basic_auth(username, password):
    if PASSWD.get(username) == password:
        return {'sub': username}
    # optional: raise exception for custom error response
    return None


def get_secret(user) -> str:
    return f"You are {user} and the secret is 'wbevuec'"


if __name__ == '__main__':
    app = pointsecio.FlaskApp(__name__)
    app.add_api('openapi.yaml')
    app.run(port=8080)
