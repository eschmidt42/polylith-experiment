# -*- coding: utf-8 -*-
from experiment.fastapi_app import core
from fastapi.testclient import TestClient
from experiment.fastapi_app.core import app


def test_sample():
    assert core is not None


client = TestClient(app)


def test_get_quote():
    response = client.get("/quote")
    assert response.status_code == 200
    data = response.json()
    assert "quote" in data
    assert isinstance(data["quote"], str)
