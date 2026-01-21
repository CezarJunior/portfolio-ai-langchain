import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser 
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

# 1. Nossa lista de departamentos (O Mapa)
info_departamentos = [
    {"name": "vendas", "description": "Clientes querendo comprar, orçamentos ou preços."},
    {"name": "suporte", "description": "Clientes com erros, bugs ou problemas técnicos."},
    {"name": "financeiro", "description": "Boletos, notas fiscais e pagamentos."}
]

# Transformando a lista em texto para o Prompt (Pilar 3 - Estrutura)
opcoes_formatadas = "\n".join([f"{d['name']}: {d['description']}" for d in info_departamentos])

# 2. Configurando a IA (Pilar 1 - OOP)
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

# 3. Criando o "Cérebro" do Roteador
template = """
Você é um classificador de e-mails. Sua única função é escolher o departamento correto.

DEPARTAMENTOS DISPONÍVEIS:
{opcoes}

MENSAGEM DO CLIENTE:
{mensagem}

Responda apenas o NOME do departamento.
"""

prompt = PromptTemplate.from_template(template)

# 1. Definindo o Parser de JSON (Pilar 3)
parser = JsonOutputParser()

# 2. Atualizando o Prompt para exigir JSON
# Adicionamos instruções de formato que o parser gera sozinho
template_json = """
Você é um sistema de triagem inteligente. 
Analise a mensagem e extraia os dados no formato JSON.

DEPARTAMENTOS:
{opcoes}

MENSAGEM DO CLIENTE:
{mensagem}

Responda seguindo exatamente este formato JSON:
{{
    "departamento": "nome do departamento",
    "urgencia": "alta, media ou baixa",
    "resumo_curto": "resumo de até 5 palavras"
}}
"""

prompt_json = PromptTemplate(
    template=template_json,
    input_variables=["mensagem", "opcoes"]
)

# 3. A Nova Cadeia (A esteira agora entrega uma caixa lacrada)
cadeia_final = prompt_json | llm | parser

# TESTANDO O NOVO FORMATO
mensagem_urgente = "SOCORRO! Meu site caiu e não consigo vender nada, resolvam logo!"

resposta_final = cadeia_final.invoke({
    "opcoes": opcoes_formatadas,
    "mensagem": mensagem_urgente
})

print("SAÍDA EM JSON (DICIONÁRIO):")
print(resposta_final)
# Agora você pode acessar dados específicos:
print(f"O setor de {resposta_final['departamento']} recebeu um chamado de urgência {resposta_final['urgencia']}.")