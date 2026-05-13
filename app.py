from flask import Flask, render_template
from config import SECRET_KEY, UPLOAD_FOLDER
from routes.auth_routes import auth_bp
from routes.exam_routes import exam_bp
from routes.result_routes import result_bp
from routes.history_routes import history_bp
from routes.ranking_routes import ranking_bp
from routes.admin_routes import admin_bp


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = SECRET_KEY
    app.config["UPLOAD_FOLDER"] = str(UPLOAD_FOLDER)

    app.register_blueprint(auth_bp)
    app.register_blueprint(exam_bp)
    app.register_blueprint(result_bp)
    app.register_blueprint(history_bp)
    app.register_blueprint(ranking_bp)
    app.register_blueprint(admin_bp)

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/dashboard")
    def dashboard():
        return render_template("dashboard.html")

    return app


if __name__ == "__main__":
    create_app().run(debug=True)
