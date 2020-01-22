from lokobolder import create_app

def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing

def test_world(client):
    response = client.get('/api/v1/world/0/0')

    assert response.status_code == 200
    assert len(response.text) > 0
