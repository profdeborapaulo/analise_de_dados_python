# Importando as bibliotecas necessárias
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# --- 1. CARREGAMENTO DOS DADOS (AJUSTE O CAMINHO SE NECESSÁRIO) ---
# Se o arquivo estiver na mesma pasta, use apenas o nome do arquivo.
# Se for no Colab, use o caminho do Google Drive (o que estava no seu notebook)
caminho_arquivo = 'data_turma.csv'
# Para Colab: caminho_arquivo = '/content/drive/MyDrive/Dados/data_turma_expandido.csv'

# O seu notebook usava 'sep=;', garantindo a leitura correta do CSV.
try:
    df = pd.read_csv('data_turma.csv', sep=';')
    print("DataFrame carregado com sucesso!\n")
except FileNotFoundError:
    print(f"ERRO: Arquivo não encontrado em {caminho_arquivo}. Verifique o caminho.")
    exit()

# --- 2. PRÉ-PROCESSAMENTO (Como sugerido no Dicionário) ---
# Renomear coluna de Tolerância para um nome mais claro (opcional, mas bom para clareza)
df.rename(columns={'Tolerancia_Estresse': 'Tolerancia'}, inplace=True)
print("Colunas renomeadas.")

# --- 3. ESTRUTURA E QUALIDADE DOS DADOS ---
print("\n--- Informações Gerais do DataFrame ---")
df.info()
print("\nVerificação de valores nulos:")
print(df.isnull().sum())
print("\nVerificação de valores duplicados:")
print(f"Total de linhas duplicadas: {df.duplicated().sum()}")

# --- 4. ANÁLISE DESCRITIVA DA IDADE ---
print("\n--- Medidas Estatísticas da Idade ---")
print(df['Idade'].describe())
print(f"Idade mais frequente (Moda): {df['Idade'].mode().iloc[0]} anos")
print(f"Intervalo de Idade: De {df.Idade.min()} até {df.Idade.max()} anos")
print(f"Desvio Padrão (std): {df['Idade'].std():.2f}")

# --- 5. ANÁLISE DE FREQUÊNCIA E AGRUPAMENTO ---
# Contagem por Sexo
print("\n--- Contagem por Sexo ---")
print(df['Sexo'].value_counts())

# Tabela Cruzada: Sexo por Turma
print("\n--- Tabulação Cruzada: Sexo por Turma ---")
crosstab_turma_sexo = pd.crosstab(df['Turma'], df['Sexo'])
print(crosstab_turma_sexo)

# --- 6. PLOTAGEM DE GRÁFICOS ---
# Frequência por Sexo (Gráfico de Barras Horizontais)
sexo_freq = df['Sexo'].value_counts()
sexo_freq.plot(kind='barh', title='Frequência por Sexo')
plt.show()

# Gráfico de Barras Stacked: Sexo por Turma
crosstab_turma_sexo.plot(kind='bar', stacked=True, title='Distribuição de Sexo por Turma')
plt.xlabel('Turma')
plt.ylabel('Contagem de Alunos')
plt.xticks(rotation=0)
plt.show()