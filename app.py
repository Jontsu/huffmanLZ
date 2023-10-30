from flask import Flask
from routes import register_routes


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key_this_is_not_safe_for_production'

register_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
