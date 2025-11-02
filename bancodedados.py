from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from time import sleep
import csv

# Configuração inicial do driver
driver = webdriver.Chrome()
driver.get('https://www.qconcursos.com/questoes-de-concursos/disciplinas/matematica-matematica/questoes')
print("Aguardando a página carregar...")
sleep(5) # Espera 5 segundos para a página carregar completamente

try:
    # 1. Encontrar todos os "containers" de questões
    # Este é o elemento que agrupa UM enunciado e SUAS alternativas
    # Usamos 'contains' para ser mais flexível com o nome da classe
    questoes_containers = driver.find_elements(By.XPATH, "//div[contains(@class, 'q-question-item')]")
    
    print(f"Encontrados {len(questoes_containers)} containers de questões.")
    
    # Lista para guardar os dados antes de salvar
    dados_questoes = []

    # 2. Iterar por cada container de questão
    for questao_container in questoes_containers:
        try:
            # 3. Dentro do container, encontrar o enunciado
            # O '.' no início do XPath é crucial, significa "procure APENAS DENTRO deste container"
            enunciado_element = questao_container.find_element(By.XPATH, ".//div[@class='q-question-enunciation']")
            enunciado_texto = enunciado_element.text
            
            # 4. Dentro do container, encontrar TODAS as alternativas
            alternativas_elements = questao_container.find_elements(By.XPATH, ".//div[@class='q-item-enum js-alternative-content']")
            
            # Criar uma lista com o texto de cada alternativa
            alternativas_lista = [alt.text for alt in alternativas_elements]
            
            # Juntar todas as alternativas em um único bloco de texto, separadas por nova linha
            alternativas_bloco = "\n".join(alternativas_lista)
            
            # Adicionar os dados encontrados à nossa lista
            if enunciado_texto and alternativas_bloco:
                dados_questoes.append([enunciado_texto, alternativas_bloco])
                print(f"Questão processada: {enunciado_texto[:50]}...") # Mostra os primeiros 50 chars

        except Exception as e:
            print(f"Erro ao processar um item de questão: {e}")

    # 5. Salvar tudo no arquivo CSV (fora do loop)
    # Abrimos o arquivo em modo 'w' (write) para criar um novo arquivo limpo
    # 'newline=""' é recomendado pela documentação do módulo csv
    with open('questoes.csv', 'w', encoding='utf-8', newline='') as arquivo:
        # Cria um "escritor" CSV
        writer = csv.writer(arquivo, delimiter=';')
        
        # Escreve o cabeçalho
        writer.writerow(['Enunciado', 'Alternativas'])
        
        # Escreve todos os dados que coletamos
        writer.writerows(dados_questoes)

    print("\nArquivo 'questoes.csv' salvo com sucesso!")

    # 6. Ler e imprimir o arquivo para verificação
    print("\n--- Conteúdo do CSV (verificação) ---")
    with open('questoes.csv', 'r', encoding='utf-8') as arquivo:
        arquivo_csv = csv.reader(arquivo, delimiter=';')
        # Pula o cabeçalho
        next(arquivo_csv, None)
        for i, linha in enumerate(arquivo_csv):
            print(f"--- Questão {i+1} ---")
            print(f"Enunciado: {linha[0]}")
            print(f"Alternativas:\n{linha[1]}")
            print("-" * 20)


finally:
    # Garante que o navegador feche mesmo se der erro
    driver.quit()
    print("Driver fechado.")
