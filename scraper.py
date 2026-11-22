import json
from datetime import datetime
from playwright.sync_api import sync_playwright

ARQUIVO_JSON = "dados_precos.json"

def carregar_dados():
    try:
        with open(ARQUIVO_JSON, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def coletar():
    print("Iniciando busca de preços...")
    dados = carregar_dados()
    hoje = datetime.now().strftime("%Y-%m-%d")
    
    urls = {
        "Mercado Livre": "https://www.mercadolivre.com.br/cafeteira-nescafe-dolce-gusto-arno-genio-s-plus-preta-110v/p/MLB17003267",
        "Amazon": "https://a.co/d/08MUsjUM"
    }

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
        
        for loja, url in urls.items():
            try:
                print(f"Acessando {loja}...")
                page.goto(url, timeout=30000)
                page.wait_for_timeout(3000)
                preco = None
                
                if loja == "Mercado Livre":
                    el = page.locator(".ui-pdp-price__second-line .andes-money-amount__fraction").first
                    if el.is_visible():
                        preco = float(el.inner_text().replace(".", "").replace(",", "."))
                elif loja == "Amazon":
                    inteiro = page.locator(".a-price-whole").first
                    centavos = page.locator(".a-price-fraction").first
                    if inteiro.is_visible():
                        v_int = inteiro.inner_text().replace(".", "").replace("\n", "")
                        v_cent = centavos.inner_text() if centavos.is_visible() else "00"
                        preco = float(f"{v_int}.{v_cent}")

                if preco:
                    dados.append({"data": hoje, "plataforma": loja, "preco": preco, "url": url})
                    print(f"Sucesso! {loja}: R$ {preco:.2f}")
                else:
                    print(f"Aviso: Não achei o preço na {loja}.")
            except Exception as e:
                print(f"Erro em {loja}: {e}")
                
        browser.close()

    with open(ARQUIVO_JSON, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=2, ensure_ascii=False)
    print("Arquivo dados_precos.json atualizado!")

if __name__ == "__main__":
    coletar()