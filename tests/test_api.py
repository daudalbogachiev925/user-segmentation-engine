def test_health(client):
    assert client.get("/health").json()["status"] == "ok"

def test_create_user(client):
    r = client.post("/api/users", json={
        "external_id": "u1", "recency_days": 10,
        "frequency": 20, "monetary": 500})
    assert r.status_code == 201
    assert r.json()["rfm_segment"] in ["Champions", "Loyal"]
