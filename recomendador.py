import pandas as pd
import torch
from sentence_transformers import SentenceTransformer, util

# ==============================================================================
# 1. CONFIGURAÇÃO E CARREGAMENTO (Roda uma vez no import)
# ==============================================================================
print("--- [MOTOR] Iniciando sistema de recomendação... ---")

# CAMINHO DO ARQUIVO (Ajuste se necessário)
CAMINHO_CSV = "dataset_celulares_final.csv"

# Carregar Modelo de IA (Pesado - Fica na memória RAM)
print("--- [MOTOR] Carregando modelo SentenceTransformer... ---")
model = SentenceTransformer('all-MiniLM-L6-v2')

# Carregar e Limpar Dados
print("--- [MOTOR] Carregando e limpando banco de dados... ---")
df_completo = pd.read_csv(CAMINHO_CSV)

# --- LIMPEZA DE DADOS (CRUCIAL) ---
# 1. Remover preços zerados ou inválidos
df_completo = df_completo[df_completo['Preco_Num'] > 0].copy()

# Passo B: REMOVE DUPLICATAS (A Mágica acontece aqui) 
# subset=['Nome']: Olha apenas a coluna 'Nome' para achar repetidos
# keep='first': Mantém o primeiro que achar e apaga as cópias seguintes
df_completo = df_completo.drop_duplicates(subset=['Nome'], keep='first')

# 2. Corrigir TB para GB (Ex: 1.0 virar 1024)
def corrigir_armazenamento(valor):
    # Se for menor que 10 (ex: 1TB), multiplica por 1024
    if valor < 10: 
        return valor * 1024
    return valor

df_completo['Armazenamento_Num'] = df_completo['Armazenamento_Num'].apply(corrigir_armazenamento)

print(f"--- [MOTOR] Sistema pronto! {len(df_completo)} celulares carregados. ---")


# ==============================================================================
# 2. FUNÇÃO DE BUSCA (Chamada pelo Main)
# ==============================================================================
def buscar_recomendacoes(query_texto, filtros_dict, top_k=3):
    """
    Realiza a filtragem e a busca vetorial.
    """
    
    # --- PASSO A: HARD FILTERS (Funil SQL) ---
    banco_filtrado = df_completo.copy()
    
    # 1. Filtro de Preço
    if filtros_dict.get("orcamento_max", 0) > 0:
        banco_filtrado = banco_filtrado[banco_filtrado['Preco_Num'] <= filtros_dict['orcamento_max']]

    # 2. Filtro de Marca
    if filtros_dict.get("marcas_preferidas"):
        banco_filtrado = banco_filtrado[banco_filtrado['Marca'].isin(filtros_dict['marcas_preferidas'])]

    # 3. Filtros Técnicos (RAM, Storage, Bateria)
    if filtros_dict.get("target_ram", 0) > 0:
        banco_filtrado = banco_filtrado[banco_filtrado['RAM_Num'] >= filtros_dict['target_ram']]
        
    if filtros_dict.get("target_armazenamento", 0) > 0:
        banco_filtrado = banco_filtrado[banco_filtrado['Armazenamento_Num'] >= filtros_dict['target_armazenamento']]
        
    if filtros_dict.get("target_bateria", 0) > 0:
        banco_filtrado = banco_filtrado[banco_filtrado['Bateria_Num'] >= filtros_dict['target_bateria']]

    # Reset Index (Obrigatório para bater com o vetor)
    banco_filtrado = banco_filtrado.reset_index(drop=True)

    # Se o filtro foi muito rígido e não sobrou nada
    if len(banco_filtrado) == 0:
        return []

    # --- PASSO B: SOFT FILTERS (IA / Embedding) ---
    # Vetoriza apenas os celulares que sobraram (Performance otimizada)
    vetor_banco = model.encode(banco_filtrado['Specs_Completa'].tolist())
    vetor_usuario = model.encode(query_texto)

    # --- PASSO C: SIMILARIDADE ---
    scores = util.cos_sim(vetor_usuario, vetor_banco)
    
    # Pega os Top K (garantindo que não pedimos mais do que existe)
    k_real = min(top_k, len(banco_filtrado))
    vals, indices = torch.topk(scores, k=k_real)

    indices_lista = indices[0].tolist()
    scores_lista = vals[0].tolist()

    # --- PASSO D: FORMATAR RETORNO ---
    resultado_final = []
    
    for i in range(len(indices_lista)):
        idx_real = indices_lista[i]
        score = scores_lista[i]
        
        celular = banco_filtrado.iloc[idx_real]
        
        resultado_final.append({
            "nome": celular['Nome'],
            "marca": celular['Marca'],
            "preco": celular['Preco_Num'],
            "specs": celular['Specs_Completa'][:100] + "...", # Resumo
            "ram": celular['RAM_Num'],
            "armazenamento": celular['Armazenamento_Num'],
            "match_score": round(score, 4) # Arredonda para ficar bonito
        })
        
    return resultado_final