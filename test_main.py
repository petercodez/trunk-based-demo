import os
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_deve_retornar_fluxo_estavel_com_flag_desligada():
    os.environ["FEATURE_NOVO_ALGORITMO"] = "False"
    
    response = client.get("/produtos")
    assert response.status_code == 200
    assert response.json()["versao_fluxo"] == "Fluxo Estável v1 (Padrão)"

def test_deve_retornar_novo_fluxo_com_flag_ligada():
    os.environ["FEATURE_NOVO_ALGORITMO"] = "True"
    
    response = client.get("/produtos")
    assert response.status_code == 200
    assert response.json()["versao_fluxo"] == "Novo Fluxo v2 (Ativado via Flag)"