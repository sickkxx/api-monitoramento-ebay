from time import sleep
from datetime import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class EbayScraper:
    def __init__(self):
        options = Options()
        options.add_argument("--headless")
        self.driver = webdriver.Edge(options=options)
        self.wait = WebDriverWait(self.driver, 10)

    def iniciar(self):
        self.driver.get("https://www.ebay.com/")

    def pesquisar_produtos(self, produto):
        try:
            barra_pesquisa = self.wait.until(
                EC.element_to_be_clickable((By.ID, "gh-ac"))
            )
            barra_pesquisa.send_keys(produto)
            barra_pesquisa.send_keys(Keys.ENTER)

        except TimeoutException:
            pass

    def produtos(self) -> list:
        resultado = []

        for _ in range(5):
            self.driver.execute_script("window.scrollBy(0, 1000);")
            sleep(0.8)

        links_produto = self.wait.until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "s-card__link"))
        )

        links = set()

        for link in links_produto:
            url = link.get_attribute("href")

            if not url or "?itmmeta=" in url:
                continue

            links.add(url)

        for link in links:
            self.driver.get(link)

            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "ux-textspans"))
            )

            html = self.driver.page_source
            soup = BeautifulSoup(html, "html.parser")

            produto_tag = soup.select_one(".x-item-title .x-item-title__mainTitle .ux-textspans--BOLD")

            preco_tag = soup.select_one(".x-price-approx__price")

            preco = preco_tag.text
            preco = preco.replace("R$", "").replace(".", "").replace(",", ".").strip()
            preco = float(preco)

            vendedor = soup.select_one(".x-sellercard-atf__info__about-seller .ux-action .ux-textspans--BOLD")

            data_coleta = datetime.now()

            resultado.append({
                "produto": produto_tag.get_text(strip=True),
                "preco": preco,
                "vendedor": vendedor.get_text(strip=True),
                "link": link,
                "data_coleta": data_coleta
            })

        return resultado

    def fechar(self):
        self.driver.quit()
