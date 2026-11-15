import os
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_deve_retornar_produtos_legados_com_flag_desligada():
    os.environ["FEATURE_NOVO_ALGORITMO"] = "False"
    
    response = client.get("/produtos")
    assert response.status_code == 200
    assert response.json()["motor_recomendacao"] == "Motor Legado v1"

def test_deve_retornar_produtos_premium_com_flag_ligada():
    os.environ["FEATURE_NOVO_ALGORITMO"] = "True"
    
    response = client.get("/produtos")
    assert response.status_code == 200
    assert response.json()["motor_recomendacao"] == "Motor IA v2 (Em Testes)"