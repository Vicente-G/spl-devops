from flask import Blueprint, current_app, request

docs_bp = Blueprint("docs", __name__)


@docs_bp.route("/docs")
def home():
    current_app.logger.info(
        f"HTTP/GET: {request.remote_addr} Redirected successfully"
    )
    return (
        r"""
        <html>
            <h1>404</h1>
            <h3>Route not found, try on /reviews like this:</h3>
            <p>(Consider the review model {id: int, game: str, review: str, rating: int})</p>
            <h5>GET /reviews - To get all listed reviews available on the server</h5>
            <h5>GET /reviews/\<ID\> - To get a specific review by its ID</h5>
            <h5>POST /reviews - To add a new review</h5>
            <h5>PUT /reviews/\<ID\> - To update a review by its ID</h5>
            <h5>DELETE /reviews/\<ID\> - To delete a review by its ID</h5>
            <br/>
            <h3>Or maybe try /wishlist routes like this:</h3>
            <p>(Consider that wishlist games are all just strings)</p>
            <h5>GET /wishlist - To get all games in the wishlist</h5>
            <h5>POST /wishlist - To add a game to the wishlist</h5>
            <h5>DELETE /wishlist/\<GAME\> - To remove a game from the wishlist</h5>
        </html>""",
        404,
    )
