from flask import Flask

# Initialize Flask app
def create_app():
    app = Flask(__name__, template_folder="../frontend/templates", static_folder="../frontend/static")
    print(app.template_folder)

    # Register routes
    from src.backend.routes import api
    app.register_blueprint(api)

    return app
