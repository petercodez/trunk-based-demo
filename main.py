import os
from fastapi import FastAPI

app = FastAPI()

@app.get("/checkout")
def calcular_checkout(preco: float):
    # Lê a chave do ambiente. Se não existir, fica desligada ("false")
    desconto_ativo = os.getenv("ATIVAR_DESCONTO", "false").lower() == "true"

    if desconto_ativo:
        # Código novo: JÁ ESTÁ NA MAIN, mas só roda quando a chave for ligada
        preco_final = preco * 0.80
        return {"preco_original": preco, "desconto": "20%", "preco_final": preco_final}

    # Código antigo: O que o cliente vê hoje em produção
    return {"preco_original": preco, "desconto": "0%", "preco_final": preco}