import os
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_checkout_normal():
    os.environ["ATIVAR_DESCONTO"] = "false"
    resposta = client.get("/checkout?preco=100")
    assert resposta.status_code == 200
    assert resposta.json()["preco_final"] == 100.0

def test_checkout_com_desconto():
    os.environ["ATIVAR_DESCONTO"] = "true"
    resposta = client.get("/checkout?preco=100")
    assert resposta.status_code == 200
    assert resposta.json()["preco_final"] == 80.0