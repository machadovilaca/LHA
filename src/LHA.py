import logging
from flask import Flask
from Web.Routes import web_app

logging_format = '%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s'
logging.basicConfig(level=logging.DEBUG, format=logging_format)


if __name__ == '__main__':
    app = Flask(__name__)
    app.register_blueprint(web_app)

    app.run(debug=True, port=5000)
