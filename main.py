from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from recomendador import buscar_recomendacoes

# ==============================================================================
# 1. CONFIGURAÇÃO DA API
# ==============================================================================
app = FastAPI()

# Modelo de Dados: Define o que o FlutterFlow vai mandar (o JSON Body)
class PedidoUsuario(BaseModel):
    query_montada: str
    filtros: dict  # Recebe o dicionário com orcamento, marcas, ram, sd_card, etc.

# ==============================================================================
# 2. A ROTA (O PORTEIRO)
# ==============================================================================
@app.post("/api/recomendar")
@app.post("/api/recomendar")
def receber_pedido(pedido: PedidoUsuario):
    print(f"\n📩 Recebi: {pedido.query_montada} | Filtros: {pedido.filtros}")
    
    # 1. Busca os resultados
    resultados_brutos = buscar_recomendacoes(
        query_texto=pedido.query_montada,
        filtros_dict=pedido.filtros,
        top_k=3
    )
    
    # 2. LISTA DE OBJETOS (O jeito que o FlutterFlow gosta)
    lista_final = []
    
    if not resultados_brutos:
            # Item de erro amigável
            lista_final.append({
                "nome": "Nenhum encontrado",
                "preco": "R$ 0,00",
                # AQUI ESTAVA O ERRO! Troque pela linha abaixo:
                "imagem": "https://dummyimage.com/600x400/000/fff.jpg",
                "motivo": "Tente ajustar seus filtros."
            })
    else:
        for cel in resultados_brutos:
            score_percent = int(cel['match_score'] * 100)
            
            # --- CÓDIGO ATUALIZADO ---
            # Tenta pegar a imagem real. Se for um arquivo estranho (SVG), usa a genérica.
            link_imagem = cel['imagem']
            if not link_imagem.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
                link_imagem = "https://dummyimage.com/600x400/000/fff.jpg&text=Sem+Imagem"

            celular_obj = {
                "nome": cel['nome'],
                "preco": f"R$ {cel['preco']:.2f}",
                "imagem": link_imagem,  # <--- AGORA USA A IMAGEM REAL
                "motivo": f"{score_percent}% de match! Ideal para seu perfil."
            }
            lista_final.append(celular_obj)

    print(f"✅ Enviando lista pronta para o App.\n")
    # Retorna direto a lista []
    return lista_final
# ==============================================================================
# 3. INICIALIZAÇÃO DO SERVIDOR
# ==============================================================================
if __name__ == "__main__":
    # Roda o servidor na porta 8000
    print("🚀 Servidor TechMatch rodando! Aguardando conexões...")
    uvicorn.run(app, host="0.0.0.0", port=8000)