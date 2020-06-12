import logging

from flask import Flask
from flask_cors import CORS

logging_format = '%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s'
logging.basicConfig(level=logging.DEBUG, format=logging_format)

if __name__ == '__main__':
    from web.routes import web_app

    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(web_app)
    app.run(debug=False, port=5000)
