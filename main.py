import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

colunas_obrigatorias = ['id_cliente', 'data_transacao', 'valor', 'origem', 'estado_cliente']
df = pd.read_csv('transacoes.csv', encoding='latin1', usecols=colunas_obrigatorias)


df['valor'] = df.groupby('estado_cliente')['valor'].transform(lambda x: x.fillna(x.median()))


df['plataforma'] = 'Mobile'
df['data_transacao'] = pd.to_datetime(df['data_transacao'])
df['data_transacao'] = df['data_transacao'].dt.tz_localize('America/Sao_Paulo')

df['dia_semana'] = df['data_transacao'].dt.day_name()
df['mes'] = df['data_transacao'].dt.month_name()

df = df.drop_duplicates(keep='first')


condicao_mes = (df['data_transacao'].dt.month == 9)
condicao_estado = (df['estado_cliente'] == 'SP') | (df['estado_cliente'] == 'RJ')
condicao_valor = (df['valor'] > 5000.00)

df_filtrado = df[condicao_mes & condicao_estado & condicao_valor]


risco_dict = {'C100': 'Baixo', 'C101': 'Alto'}

df['nivel_risco'] = df['id_cliente'].map(risco_dict)

tabela_dinamica = df.pivot_table(
    index='mes',
    columns='nivel_risco',
    values='valor',
    aggfunc='sum',
    margins=True
)

def calcular_zscore_por_estado(dataframe):
    meios = dataframe.groupby('estado_cliente')['valor'].transform('mean')
    desvios = dataframe.groupby('estado_cliente')['valor'].transform('std')
    return (dataframe['valor'] - meios) / desvios

df['z_score'] = calcular_zscore_por_estado(df)
df_anomalias = df[df['z_score'] > 2.5]


df['data_dia'] = df['data_transacao'].dt.date
dados_grafico = df.groupby('data_dia')['valor'].sum().reset_index()

dados_grafico['media_movel_7d'] = dados_grafico['valor'].rolling(window=7).mean()

fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(dados_grafico['data_dia'], dados_grafico['valor'], label='Valor Total Diário', color='lightblue', alpha=0.7)

ax.plot(dados_grafico['data_dia'], dados_grafico['media_movel_7d'], label='Média Móvel (7 Dias)', color='darkblue', linewidth=2)

ax.set_ylim(bottom=0)
ax.set_title('Desempenho de Transações Financeiras e Tendência Média', fontsize=14, fontweight='bold')
ax.set_xlabel('Data da Transação', fontsize=12)
ax.set_ylabel('Valor Total (R$)', fontsize=12)
ax.legend(loc='upper right')
ax.grid(True, linestyle='--', alpha=0.5)


plt.tight_layout()
plt.savefig('relatorio_performance.png')
print("Pipeline executado com sucesso! Gráfico salvo como 'relatorio_performance.png'.")
plt.show()
