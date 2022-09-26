from flask import Flask
from train_path_finder import path_finder_api
from flask_cors import CORS

app = Flask(__name__, static_url_path='/', static_folder='static')
cors = CORS(app, resources={r"/*": {"origins": "*"}})

base_prefix = "/api/v1"

app.register_blueprint(path_finder_api, url_prefix=f'{base_prefix}/path')

if __name__ == '__main__':
    app.run(debug=True)
