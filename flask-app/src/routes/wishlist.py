from flask import Blueprint, current_app, jsonify, request

wishlist_bp = Blueprint("wishlist", __name__, url_prefix="/wishlist")
wishlist = [
    "Hollow Knight",
    "Hades",
    "Dead Cells",
    "Silk Song",
]


@wishlist_bp.route("", methods=["GET"])
def get_wishlist():
    current_app.logger.info("HTTP/GET: Wishlist retrieved")
    return jsonify(data=wishlist)


@wishlist_bp.route("", methods=["POST"])
def add_to_wishlist():
    current_app.logger.info("HTTP/POST: Adding game to wishlist")
    game = request.json.get("game")
    if game and game not in wishlist:
        wishlist.append(game)
        current_app.logger.info(f"HTTP/POST: Game {game} added to wishlist")
        return jsonify(data="Game added to wishlist"), 201
    current_app.logger.error(
        f"HTTP/POST: Failed to add game {game} to wishlist"
    )
    return jsonify(data="Invalid input"), 400


@wishlist_bp.route("/<string:game>", methods=["DELETE"])
def remove_from_wishlist(game):
    current_app.logger.info("HTTP/DELETE: Removing game from wishlist")
    if game in wishlist:
        wishlist.remove(game)
        current_app.logger.info(
            f"HTTP/DELETE: Game {game} removed from wishlist"
        )
        return jsonify(data="Game removed from wishlist"), 200
    current_app.logger.error(f"HTTP/DELETE: Game {game} not found in wishlist")
    return jsonify(data="Game not found in wishlist"), 404
