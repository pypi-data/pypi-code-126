def test_wagtailadmin_loads_successfully(admin_client):
    response = admin_client.get("/admin/")
    assert response.status_code == 200
