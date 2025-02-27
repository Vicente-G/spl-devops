from src.routes.wishlist import wishlist


def test_get_wishlist(client):
    response = client.get("/wishlist")
    assert response.status_code == 200
    assert response.json["data"] == wishlist


def test_add_to_wishlist(client):
    response = client.post("/wishlist", json={"game": "GTA VI"})
    assert response.status_code == 201
    assert response.json == {"data": "Game added to wishlist"}
    response = client.get("/wishlist")
    assert "GTA VI" in response.json["data"]


def test_add_to_wishlist_duplicate_game(client):
    response = client.post("/wishlist", json={"game": "Hades"})
    assert response.status_code == 400
    assert response.json == {"data": "Invalid input"}


def test_remove_from_wishlist(client):
    response = client.delete("/wishlist/Hades")
    assert response.status_code == 200
    assert response.json == {"data": "Game removed from wishlist"}
    response = client.get("/wishlist")
    assert "Hades" not in response.json["data"]


def test_remove_from_wishlist_not_found(client):
    response = client.delete("/wishlist/NonExistentGame")
    assert response.status_code == 404
    assert response.json == {"data": "Game not found in wishlist"}
