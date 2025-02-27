from src.routes.reviews import reviews


def test_get_reviews(client):
    response = client.get("/reviews")
    assert response.status_code == 200
    assert response.get_json()["data"] == reviews


def test_get_review(client):
    response = client.get("/reviews/1")
    assert response.status_code == 200
    assert response.get_json()["data"]["id"] == 1


def test_get_review_not_found(client):
    response = client.get("/reviews/999")
    assert response.status_code == 404
    assert response.get_json()["data"] == "Review not found"


def test_add_review(client):
    new_review = {"game": "GTA VI", "review": "Trash game", "rating": 2}
    response = client.post("/reviews", json=new_review)
    assert response.status_code == 201
    assert response.get_json()["data"]["id"] == 4


def test_update_review(client):
    updated_review = {"game": "Celeste", "review": "Still great!", "rating": 5}
    response = client.put("/reviews/1", json=updated_review)
    assert response.status_code == 200
    assert response.get_json()["review"] == "Still great!"


def test_update_review_not_found(client):
    updated_review = {"game": "Unknown", "review": "Not found", "rating": 3}
    response = client.put("/reviews/999", json=updated_review)
    assert response.status_code == 404
    assert response.get_json()["error"] == "Review not found"


def test_delete_review(client):
    response = client.delete("/reviews/1")
    assert response.status_code == 200
    assert response.get_json()["message"] == "Review deleted"


def test_delete_review_not_found(client):
    response = client.delete("/reviews/999")
    assert response.status_code == 404
    assert response.get_json()["error"] == "Review not found"
