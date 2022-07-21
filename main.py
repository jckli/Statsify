"""
This script runs the Statsify application using a development server.
"""

from os import environ
from Statsify import app

if __name__ == '__main__':
    app.config.from_pyfile('settings.py')
    HOST = environ.get('SERVER_HOST', 'localhost')
    DEBUG=False
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT, DEBUG, threaded=True)