# 📊 API de Monitoramento de Preços (eBay)

## 📌 Sobre o projeto

Esta aplicação é uma API REST desenvolvida em Python para monitoramento de preços de produtos no eBay.

O sistema realiza scraping automatizado utilizando Selenium, armazena os dados em um banco de dados MySQL e disponibiliza endpoints para consulta via API utilizando FastAPI.

---

## 🚀 Funcionalidades

* 🔎 Busca de produtos diretamente no eBay
* 🕷️ Coleta automatizada de dados com Selenium
* 💾 Armazenamento em banco de dados MySQL
* 🌐 API REST para consulta dos dados
* 📄 Retorno estruturado em JSON

---

## 🛠️ Tecnologias utilizadas

* Python
* FastAPI
* Selenium
* BeautifulSoup
* MySQL

---

## 📁 Estrutura do projeto

```bash
.
├── main.py        # API (FastAPI)
├── scraper.py     # Lógica de scraping (Selenium + BeautifulSoup)
├── database.py    # Conexão e operações com MySQL
├── requirements.txt
└── README.md
```

---

## ⚙️ Como rodar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo
```

### 2. Crie um ambiente virtual

```bash
python -m venv venv
```

### 3. Ative o ambiente virtual

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

---

## 🗄️ Configuração do banco de dados

Edite o arquivo `database.py` com suas credenciais:

```python
host="localhost"
user="root"
password="SUA_SENHA"
database="ebay_produtos"
```

Certifique-se de que a tabela já foi criada:

```sql
CREATE TABLE produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    produto VARCHAR(255),
    preco DECIMAL(10,2),
    vendedor VARCHAR(255),
    link TEXT,
    data_coleta DATETIME
);
```

---

## ▶️ Executando a API

```bash
uvicorn main:app --reload
```

Acesse a documentação automática:

```
http://127.0.0.1:8000/docs
```

---

## 📡 Endpoints

### 🔎 Buscar produtos (scraping + salvar no banco)

```
GET /buscar/{produto}
```

Exemplo:

```
/buscar/iphone
```

---

### 📦 Listar produtos salvos

```
GET /produtos
```

---

## 📷 Exemplo de resposta

```json
{
  "busca": "iphone",
  "quantidade": 5,
  "produtos": [
    {
      "produto": "iPhone 13",
      "preco": 3500.0,
      "vendedor": "Loja X",
      "link": "https://...",
      "data_coleta": "2026-03-30T14:32:10"
    }
  ]
}
```

---

## 📈 Possíveis melhorias

* Evitar duplicação de dados no banco
* Implementar paginação
* Adicionar filtros de busca
* Executar scraping em background
* Deploy da API na nuvem

---

## 👨‍💻 Autor

Desenvolvido por sickk

GitHub: https://github.com/sickkxx
