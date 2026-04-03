from dotenv import load_dotenv
load_dotenv()

from flask import Flask
from routes.synergy import synergy_bp
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.register_blueprint(synergy_bp, url_prefix="/api/synergy")

if __name__ == "__main__":
    app.run(port=5001, debug=True)