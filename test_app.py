import json
from app import app

def test_home():
    response = app.test_client().get('/')
    assert response.status_code == 200
    
    # Parse the JSON response
    data = json.loads(response.data)
    assert data == {"message": "Hello, World!"}