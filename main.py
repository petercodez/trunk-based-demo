import os
from fastapi import FastAPI

app = FastAPI(title="Demo Trunk-Based e Feature Flags")

def is_feature_enabled(flag_name: str) -> bool:
    return os.getenv(flag_name, "False") == "True"

@app.get("/produtos")
def listar_produtos():
    # Avalia a flag em tempo de execução, sem precisar reiniciar o processo
    if is_feature_enabled("FEATURE_NOVO_ALGORITMO"):
        return {
            "status": "sucesso",
            "versao_fluxo": "Novo Fluxo v2 (Ativado via Flag)",
            "produtos": ["Notebook Gamer", "Monitor Ultrawide", "Cadeira Ergonômica"]
        }
    
    return {
        "status": "sucesso",
        "versao_fluxo": "Fluxo Estável v1 (Padrão)",
        "produtos": ["Teclado Padrão", "Mouse Óptico", "Monitor 15 polegadas"]
    }