from flask import Flask
from routes import register_routes

import coverage


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key_this_is_not_safe_for_production'

cov = coverage.Coverage(
    source=["src"],
    omit=["*/routes.py", "*/app.py", "*/templates/*", "*/tests/*"]
)
cov.start()

register_routes(app, cov)

if __name__ == '__main__':
    app.run(debug=True)
