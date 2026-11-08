import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine


# 1. Seus dados em formato de Lista de Dicionários
dados_brutos = [
    {"id_venda": 1, "cliente": "Empresa Alfa", "valor": 5000.00, "data": "2026-11-01", "status": "Fechado"},
    {"id_venda": 2, "cliente": "Empresa Beta", "valor": 12000.00, "data": "2026-11-03", "status": "Em Negociação"},
    {"id_venda": 3, "cliente": "Tech Soluções", "valor": 3500.00, "data": "2026-11-04", "status": "Fechado"},
    {"id_venda": 4, "cliente": "Global Trade", "valor": 8500.00, "data": None, "status": "Perdido"}
]

df = pd.DataFrame(dados_brutos)

# Tratamento de Engenharia: se a data estiver vazia, preenche com a data atual
df["data"] = df["data"].fillna(datetime.today().strftime('%Y-%m-%d'))

# 2. Criando e conectando ao banco SQLite na pasta do projeto
engine = create_engine('sqlite:///inteligencia.db')

# Salva no banco de dados SQLite do celular
df.to_sql('tb_vendas', engine, if_exists='replace', index=False)
print("--- SUCESSO: Dados salvos no SQLite do celular! ---")

# 3. Lendo do banco de dados para exportar o relatório
df_do_banco = pd.read_sql('tb_vendas', engine)

# Exportando para CSV para usar no Looker Studio
df_do_banco.to_csv('dados_para_dashboard.csv', index=False)
print("--- SUCESSO: Arquivo 'dados_para_dashboard.csv' gerado! ---")
