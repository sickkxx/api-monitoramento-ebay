# 📊 API de Monitoramento de Preços (eBay)

## 📌 Sobre o projeto

Esta aplicação é uma API REST desenvolvida em Python para monitoramento de preços de produtos no eBay.

O sistema realiza scraping automatizado utilizando Selenium, armazena os dados em um banco de dados MySQL e disponibiliza endpoints para consulta via API utilizando FastAPI.

Além disso, o sistema evita duplicação de dados e mantém os preços sempre atualizados utilizando lógica de **upsert** (`ON DUPLICATE KEY UPDATE`).

---

## 🚀 Funcionalidades

* 🔎 Busca de produtos diretamente no eBay
* 🕷️ Coleta automatizada de dados com Selenium
* 💾 Armazenamento em banco de dados MySQL
* 🔄 Atualização automática de preços (sem duplicação)
* 🌐 API REST para consulta dos dados
* 📄 Retorno estruturado em JSON

---

## 🛠️ Tecnologias utilizadas

* Python
* FastAPI
* Selenium
* BeautifulSoup
* MySQL
* SQLAlchemy
* Pandas

---

## 📁 Estrutura do projeto

```bash
.
├── main.py              # API (FastAPI)
├── scraper.py           # Lógica de scraping
├── db/
│   ├── connection.py    # Conexão com banco (SQLAlchemy)
│   └── repository.py    # Operações no banco (insert/select)
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

---

### 2. Crie e ative um ambiente virtual

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

---

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

---

## 🔐 Configuração de variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
DB_USER=root
DB_PASSWORD=sua_senha
DB_HOST=localhost
DB_NAME=ebay_produtos
```

⚠️ O arquivo `.env` não deve ser enviado ao GitHub.

---

## 🗄️ Configuração do banco de dados

```sql
CREATE TABLE produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    produto VARCHAR(255) NOT NULL,
    preco DECIMAL(10,2) NOT NULL,
    vendedor VARCHAR(255) NOT NULL,
    link TEXT,
    data_coleta DATETIME,
    UNIQUE(produto, vendedor)
);
```

---

## ▶️ Executando a API

```bash
uvicorn main:app --reload
```

Documentação automática:

```
http://127.0.0.1:8000/docs
```

---

## 📡 Endpoints

### 🔎 Buscar produtos (scraping + salvar no banco)

```
GET /buscar/{produto}
```

### 📦 Listar produtos salvos

```
GET /produtos
```

---

## 📷 Exemplo de resposta

```json
[
  {
    "id": 1,
    "produto": "iPhone 13",
    "preco": 3500.0,
    "vendedor": "Loja X",
    "link": "https://...",
    "data_coleta": "2026-04-02T16:11:01"
  }
]
```

---

## 🧠 Decisões de projeto

* Uso de **SQLAlchemy** para padronização de acesso ao banco
* Uso de **ON DUPLICATE KEY UPDATE** para evitar duplicatas
* Chave única definida como `(produto, vendedor)`
* Separação em camadas (`connection` e `repository`)

---

## 📈 Possíveis melhorias

* 📊 Histórico de preços (em vez de sobrescrever)
* ⚡ Scraping assíncrono / em background
* 🔎 Filtros avançados na API
* 📄 Paginação dos resultados
* ☁️ Deploy na nuvem (Render, AWS, etc.)

---

## 👨‍💻 Autor

Desenvolvido por **sickk**

GitHub: [https://github.com/sickkxx](https://github.com/sickkxx)
