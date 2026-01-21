import os
from dotenv import load_dotenv

# Carrega a chave do arquivo .env
load_dotenv()

# Nosso mapa de departamentos que definimos
info_departamentos = [
    {
        "name": "vendas",
        "description": "Ideal para clientes que querem comprar, pedir orçamentos ou saber preços."
    },
    {
        "name": "suporte",
        "description": "Ideal para clientes relatando erros, bugs ou dificuldades técnicas no sistema."
    },
    {
        "name": "financeiro",
        "description": "Ideal para questões de boletos, notas fiscais, faturamento e reembolsos."
    }
]