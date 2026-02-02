import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import re
from tqdm import tqdm

# --- CONFIGURAÇÕES ---
MARCAS = ['samsung', 'xiaomi', 'apple', 'motorola', 'realme', 'infinix', 'oppo', 'honor', 'asus']
ANOS_ALVO = ['2024', '2025', '2026'] 
PAGINAS = 3

# --- CONEXÃO ---
session = requests.Session()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Referer': 'https://www.google.com/',
}
session.headers.update(headers)

# --- FUNÇÕES ---
def limpar_numero(texto):
    if not texto: return 0.0
    nums = re.findall(r'(\d+)', str(texto))
    return float(nums[-1]) if nums else 0.0

def limpar_preco(texto):
    if not texto: return 0.0
    nums = re.sub(r'[^\d,]', '', str(texto))
    try: return float(nums.replace(',', '.'))
    except: return 0.0

dados_finais = []

# --- VARREDURA SILENCIOSA ---
pbar = tqdm(MARCAS, desc="Iniciando...", unit="marca")

for marca in pbar:
    pbar.set_description(f"Lendo {marca.upper()} (Capturados: {len(dados_finais)})")
    
    for page in range(1, PAGINAS + 1):
        try:
            url_busca = f"https://www.oficinadanet.com.br/smartphones/buscar?palavra=&marca={marca}&pagina={page}"
            r = session.get(url_busca, timeout=20)
            soup = BeautifulSoup(r.content, 'html.parser')
            
            cards = soup.select('.list-item, .col-xl-3') 
            if not cards: cards = soup.select('a[href*="/smartphones/"]')
            if len(cards) == 0: break

            for card in cards:
                link_tag = card if card.name == 'a' else card.find('a', href=True)
                if not link_tag: continue
                
                url_produto = link_tag['href']
                if "/smartphones/" not in url_produto or "buscar" in url_produto: continue
                
                texto_card = card.get_text(" ", strip=True)
                match_data = re.search(r'(\d{2}/\d{2}/(20\d{2}))', texto_card)
                
                ano_detectado = match_data.group(2) if match_data else None
                data_completa = match_data.group(1) if match_data else None
                
                if ano_detectado and ano_detectado not in ANOS_ALVO: continue 
                
                try:
                    r_prod = session.get(url_produto, timeout=15)
                    soup_prod = BeautifulSoup(r_prod.content, 'html.parser')
                    
                    h1 = soup_prod.find('h1')
                    nome = h1.get_text(strip=True).replace(': Ficha Técnica', '') if h1 else 'Desconhecido'
                    
                    # --- MUDANÇA: Busca pela estrutura exata que você mandou (width/height) ---
                    img_tag = soup_prod.find('img', {'width': '381', 'height': '249'})
                    link_img = img_tag.get('src') if img_tag else ""
                    
                    if not data_completa:
                        infos = soup_prod.select('.obj-info-item')
                        for info in infos:
                            txt = info.get_text(" ", strip=True)
                            if "Lançamento" in txt:
                                match_interna = re.search(r'(\d{2}/\d{2}/(20\d{2}))', txt)
                                if match_interna:
                                    data_completa = match_interna.group(1)
                                    ano_detectado = match_interna.group(2)
                                    break
                    
                    if not ano_detectado or ano_detectado not in ANOS_ALVO: continue 
                    
                    specs = {}
                    for el in soup_prod.select('.title-item, .title-cat'):
                        chave = el.get_text(strip=True).replace(":", "").strip()
                        val_div = el.find_next_sibling('div')
                        if val_div: 
                            valor = val_div.get_text(strip=True)
                            if valor and valor != "Não especificado": 
                                specs[chave] = valor
                    
                    texto_ia_lista = [f"Smartphone: {nome}", f"Marca: {marca.capitalize()}", f"Lançamento: {data_completa}"]
                    for k, v in specs.items(): texto_ia_lista.append(f"{k}: {v}")
                    texto_ia_final = ". ".join(texto_ia_lista) + "."

                    dados_finais.append({
                        'Nome': nome,
                        'Marca': marca.capitalize(),
                        'Ano': data_completa,
                        'Preco_Num': limpar_preco(specs.get('Preço atual')),
                        'images': link_img,
                        'RAM_Num': limpar_numero(specs.get('Memória RAM')),
                        'Armazenamento_Num': limpar_numero(specs.get('Armazenamento')),
                        'Bateria_Num': limpar_numero(specs.get('Bateria')),
                        'Specs_Completa': texto_ia_final,
                        'Url': url_produto
                    })
                    
                    pbar.set_description(f"Lendo {marca.upper()} (Capturados: {len(dados_finais)})")
                    time.sleep(0.05)
                    
                except Exception: pass
        except Exception: pass

if dados_finais:
    df = pd.DataFrame(dados_finais)
    
    cols_order = ['Nome', 'Marca', 'Ano', 'Preco_Num', 'images', 'RAM_Num', 'Specs_Completa']
    cols = [c for c in cols_order if c in df.columns] + [c for c in df.columns if c not in cols_order]
    df = df[cols]
    
    df.to_csv("dataset_celulares_final.csv", index=False)
    print(f"\n✅ Concluído! {len(df)} celulares salvos.")
else:
    print("\n❌ Nada encontrado.")