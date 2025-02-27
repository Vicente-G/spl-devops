from flask import Blueprint, current_app, jsonify, request

reviews_bp = Blueprint("reviews", __name__, url_prefix="/reviews")

reviews = [
    {"id": 1, "game": "Celeste", "review": "Great game!", "rating": 5},
    {"id": 2, "game": "Elden Ring", "review": "TL;DR...", "rating": 4},
    {"id": 3, "game": "Fortnite", "review": "Shitty game", "rating": 1},
]


@reviews_bp.route("", methods=["GET"])
def get_reviews():
    current_app.logger.info("HTTP/GET: Reviews retrieved")
    return jsonify(data=reviews), 200


@reviews_bp.route("/<int:review_id>", methods=["GET"])
def get_review(review_id):
    current_app.logger.info(f"HTTP/GET: Sending review #{review_id}")
    review = next((r for r in reviews if r["id"] == review_id), None)
    if review:
        current_app.logger.info(f"HTTP/GET: Review #{review_id} sent")
        return jsonify(data=review), 200
    current_app.logger.error(f"HTTP/GET: Review #{review_id} not found")
    return jsonify(data="Review not found"), 404


@reviews_bp.route("", methods=["POST"])
def add_review():
    new_id_generated = max(r["id"] for r in reviews) + 1
    current_app.logger.info(f"HTTP/POST: Adding review #{new_id_generated}")
    new_review = request.get_json()
    new_review["id"] = new_id_generated
    reviews.append(new_review)
    current_app.logger.info(f"HTTP/POST: Review #{new_id_generated} added")
    return jsonify(data=new_review), 201


@reviews_bp.route("/<int:review_id>", methods=["PUT"])
def update_review(review_id):
    current_app.logger.info(f"HTTP/PUT: Updating review #{review_id}")
    review = next((r for r in reviews if r["id"] == review_id), None)
    if review:
        updated_data = request.get_json()
        review.update(updated_data)
        current_app.logger.info(f"HTTP/PUT: Review #{review_id} updated")
        return jsonify(review), 200
    current_app.logger.error(f"HTTP/PUT: Review #{review_id} not found")
    return jsonify({"error": "Review not found"}), 404


@reviews_bp.route("/<int:review_id>", methods=["DELETE"])
def delete_review(review_id):
    global reviews
    current_app.logger.info(f"HTTP/DELETE: Deleting review #{review_id}")
    new_reviews = [r for r in reviews if r["id"] != review_id]
    if len(new_reviews) == len(reviews):
        current_app.logger.error(f"HTTP/DELETE: Review #{review_id} not found")
        return jsonify({"error": "Review not found"}), 404
    reviews = new_reviews
    current_app.logger.info(f"HTTP/DELETE: Review #{review_id} deleted")
    return jsonify({"message": "Review deleted"}), 200
