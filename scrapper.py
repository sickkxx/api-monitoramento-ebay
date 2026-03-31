from time import sleep
from datetime import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def ebay_scraper(pergunta: str) -> list[dict[str, str | float | datetime]]:
    resultado: list[dict[str, str | float | datetime]] = []

    options: Options = Options()
    options.add_argument("--headless")

    # Pegando o site do mercado livre
    driver: "webdriver.Firefox" = webdriver.Firefox(options=options)
    driver.get("https://www.ebay.com/")

    # Esperando o elemento aparecer
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "gh-ac"))
    )

    # Pegando a barra de pesquisa e fazendo a busca
    barra_pesquisa: "WebElement" = driver.find_element(By.ID, "gh-ac")
    barra_pesquisa.send_keys(pergunta)
    barra_pesquisa.send_keys(Keys.ENTER)

    # Esperando o elemento aparecer
    WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "s-card__link"))
    )

    # Rola a página até o final para carregar tudo
    for _ in range(5):
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        sleep(1)

    # Pegando todos links dos produtos
    links_produto: list["WebElement"] = driver.find_elements(By.CLASS_NAME, "s-card__link")

    # Usa set para evitar links duplicados
    links: set[str] = set()

    # Adicionando os link em uma lista
    for link in links_produto:
        url: str | None = link.get_attribute("href")

        # Ignora links inválidos ou com parâmetros desnecessários
        if not url or "?itmmeta=" in url:
            continue

        links.add(url)

    for link in links:
        driver.get(link)

        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "ux-textspans"))
        )

        html: str = driver.page_source
        soup: BeautifulSoup = BeautifulSoup(html, "html.parser")

        produto = soup.select_one(".x-item-title .x-item-title__mainTitle .ux-textspans--BOLD")
        preco_tag = soup.select_one(".x-price-approx__price")
        vendedor = soup.select_one(".x-sellercard-atf__info__about-seller .ux-action .ux-textspans--BOLD")

        if not produto or not preco_tag or not vendedor:
            continue

        preco_texto: str = preco_tag.text

        # Remove formatos brasileiros para converter em float
        preco_texto = preco_texto.replace("R$", "").replace(".", "").replace(",", ".").strip()
        preco: float = float(preco_texto)

        data_coleta: datetime = datetime.now()

        resultado.append({
            "produto": produto.get_text(strip=True),
            "preco": preco,
            "vendedor": vendedor.get_text(strip=True),
            "link": link,
            "data_coleta": data_coleta
        })

    driver.quit()

    return resultado
