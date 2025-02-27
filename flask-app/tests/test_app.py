from flask import Flask


def test_app_is_created(test_app):
    assert isinstance(test_app, Flask), "app should be a Flask instance"


def test_blueprints_registered(test_app):
    assert (
        "wishlist" in test_app.blueprints
    ), "wishlist blueprint should be registered"
    assert (
        "reviews" in test_app.blueprints
    ), "reviews blueprint should be registered"
