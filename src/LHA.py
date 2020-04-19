import logging

from flask import Flask

logging_format = '%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s'
logging.basicConfig(level=logging.DEBUG, format=logging_format)

if __name__ == '__main__':
    from src.web.routes import web_app

    app = Flask(__name__)
    app.register_blueprint(web_app)
    app.run(debug=False, port=5000)
