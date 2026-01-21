# 🤖 Roteador Inteligente de Chamados (LangChain + AI)

Este projeto demonstra um sistema de triagem automatizada para empresas, utilizando Inteligência Artificial para classificar intenções de clientes e estruturar dados para sistemas de CRM/ERP.

## 🚀 Tecnologias Utilizadas
* **Python** como linguagem base.
* **LangChain** para orquestração da lógica de IA.
* **Google Gemini AI** (Modelo 1.5 Flash) como motor de processamento.
* **Pydantic/JSON** para estruturação de dados de saída.

## 🧠 Conceitos Aplicados (Os 3 Pilares)
1. **Programação Orientada a Objetos (OOP):** Uso de classes e objetos do LangChain para criar cadeias de processamento reutilizáveis.
2. **Embeddings & Lógica Semântica:** A IA identifica a intenção do cliente por significado (semântica) e não apenas por palavras-chave.
3. **Processamento de JSON:** O sistema não entrega apenas texto, mas um objeto JSON estruturado com `departamento`, `urgencia` e `resumo`, pronto para ser consumido por outros sistemas.

## 🛠️ Como rodar o projeto
1. Clone o repositório.
2. Crie um arquivo `.env` e adicione sua `GOOGLE_API_KEY`.
3. Instale as dependências: `pip install -r requirements.txt`.
4. Execute: `python roteador.py`.
