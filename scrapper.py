from time import sleep
from datetime import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class EbayScraper:
    def __init__(self):
        options = Options()
        options.add_argument("--headless")
        self.driver = webdriver.Firefox(options=options)

    def buscar(self, produto: str) -> list:
        resultado = []

        self.driver.get("https://www.ebay.com/")

        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, "gh-ac"))
        )

        barra_pesquisa: WebElement = self.driver.find_element(By.ID, "gh-ac")
        barra_pesquisa.send_keys(produto)
        barra_pesquisa.send_keys(Keys.ENTER)

        WebDriverWait(self.driver, 5).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "s-card__link"))
        )

        for _ in range(5):
            self.driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
            sleep(1)

        links_produto: list[WebElement] = self.driver.find_elements(By.CLASS_NAME, "s-card__link")

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
            # Remove formatos brasileiros para converter em float
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
