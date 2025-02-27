import argparse
import logging

from flask import Flask, current_app, redirect, request, url_for

from config import PORT
from logs import setup_logging
from routes import docs_bp
from routes.reviews import reviews_bp
from routes.wishlist import wishlist_bp

setup_logging()


def create_app():
    app = Flask(__name__)
    app.register_blueprint(docs_bp)
    app.register_blueprint(wishlist_bp)
    app.register_blueprint(reviews_bp)

    @app.errorhandler(404)
    def handle_404(e):
        current_app.logger.warning(
            f"HTTP/{request.method}: Route not found, redirecting to home"
        )
        return redirect(url_for("docs.home")), 302

    if __name__ != "__main__":
        gunicorn_logger = logging.getLogger("gunicorn.error")
        app.logger.setLevel(gunicorn_logger.level)
    app.logger.info("App started")
    return app


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the Flask app.")
    parser.add_argument(
        "--debug", action="store_true", help="Run the app in debug mode."
    )
    args = parser.parse_args()

    app = create_app()
    app.run(host="0.0.0.0", port=PORT, debug=args.debug)
