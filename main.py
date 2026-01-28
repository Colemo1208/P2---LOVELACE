# main.py
from recomendador import buscar_recomendacoes

# 1. Simulação do Usuário (Isso viria do React Native/Frontend)
perfil_usuario = {
    "query_montada": "Smartphone gamer, processador Snapdragon Elite ou superior, GPU potente Adreno, tela com alta taxa de atualização 120Hz. alto armazenamento interno.",
    "filtros": {
        "orcamento_max": 4000.00,
        "marcas_preferidas": ["Samsung", "Motorola", "Xiaomi"],
        "target_ram": 8,           # Requisito mínimo
        "target_armazenamento": 256, # O Acumulador (Agora corrigido de TB para GB no motor)
        "target_bateria": 0
    }
}

print("\n" + "="*50)
print("  BUSCANDO RECOMENDAÇÕES NO MAIN  ")
print("="*50 + "\n")

# 2. Chama a função importada
resultados = buscar_recomendacoes(
    query_texto=perfil_usuario['query_montada'],
    filtros_dict=perfil_usuario['filtros'],
    top_k=3
)

# 3. Exibe o resultado
if not resultados:
    print("Nenhum celular encontrado com esses filtros.")
else:
    print(f"Encontramos {len(resultados)} opções ideais:\n")
    for i, cel in enumerate(resultados):
        print(f"🥇 TOP {i+1}: {cel['nome']}")
        print(f"   💰 Preço: R$ {cel['preco']}")
        print(f"   🧠 RAM: {cel['ram']}GB | 💾 Armaz: {cel['armazenamento']}GB")
        print(f"   🎯 Similaridade (IA): {cel['match_score']}")
        print("-" * 40)