import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_upload(client):
    # Open a test image file
    with open("tests/test.png", "rb") as file:
        image_data = file.read()

    # Send a POST request with the test image file
    response = client.post("/upload", data={"file": (image_data, "test.png")}, content_type="multipart/form-data")

    # Assert that the response is successful
    assert response.status_code == 200

    # Assert that the response contains the expected text
    assert b"Processing image..." in response.data
