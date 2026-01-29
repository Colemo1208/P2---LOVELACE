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
def receber_pedido(pedido: PedidoUsuario):
    """
    Recebe o JSON do FlutterFlow, chama a IA e devolve no formato Struct.
    """
    print(f"\n📩 Recebi um novo pedido do App!")
    print(f"   Query: {pedido.query_montada[:50]}...")
    print(f"   Filtros: {pedido.filtros}")
    
    # 1. Busca os resultados no Motor (Retorna Lista de Dicionários)
    resultados_brutos = buscar_recomendacoes(
        query_texto=pedido.query_montada,
        filtros_dict=pedido.filtros,
        top_k=3
    )
    
    # 2. Transforma para o formato do FlutterFlow (Listas Paralelas/Struct)
    lista_nomes = []
    lista_precos = []
    lista_motivos = []
    lista_imagens = [] 
    
    if not resultados_brutos:
        # Se não achou nada, manda listas com um aviso
        lista_nomes = ["Nenhum encontrado"]
        lista_precos = ["R$ 0,00"]
        lista_motivos = ["Tente ajustar seus filtros."]
        lista_imagens = ["https://placehold.co/600x400?text=404"]
    else:
        for cel in resultados_brutos:
            # Preenche as listas separadas
            lista_nomes.append(cel['nome'])
            
            # Formata preço como texto (FlutterFlow espera String)
            lista_precos.append(f"R$ {cel['preco']:.2f}") 
            
            # Cria um motivo baseado no Score da IA
            score_percent = int(cel['match_score'] * 100)
            lista_motivos.append(f"{score_percent}% de match! Ideal para seu perfil.")
            
            # Placeholder de imagem (já que o scraper não pegou URLs de imagem reais)
            lista_imagens.append("https://placehold.co/600x400/png")

    print(f"✅ Enviando resposta formatada para o App.\n")

    # 3. Retorna o JSON no formato exato da Struct "CelularrecomendadoStruct"
    return {
        "nome": lista_nomes,
        "preco": lista_precos,
        "imagem": lista_imagens,
        "motivo": lista_motivos
    }

# ==============================================================================
# 3. INICIALIZAÇÃO DO SERVIDOR
# ==============================================================================
if __name__ == "__main__":
    # Roda o servidor na porta 8000
    print("🚀 Servidor TechMatch rodando! Aguardando conexões...")
    uvicorn.run(app, host="0.0.0.0", port=8000)