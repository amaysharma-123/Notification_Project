from flask import Flask
from routes.api import api_bp
from routes.web import web_bp
from services.queue_manager import start_queue_processor

app = Flask(__name__)
app.register_blueprint(api_bp, url_prefix='/api')
app.register_blueprint(web_bp)

if __name__ == '__main__':
    start_queue_processor()
    app.run(debug=True, port=5000)