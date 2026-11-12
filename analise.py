# Script em Python básico para análise de casos de Dengue e Chikungunya
# Município: Santana do Paraíso (MG)

arquivo_dados = 'dados_arboviroses.csv'

total_dengue = 0
total_chikungunya = 0
semanas_lidas = 0

try:
  # Abre o ficheiro CSV gerado a partir da planilha do Excel
  with open(arquivo_dados, mode='r', encoding='utf-8') as ficheiro:
    # Pula a primeira linha (cabeçalho)
    cabecalho = ficheiro.readline()

    for linha in ficheiro:
      # Divide cada linha pelas vírgulas
      colunas = linha.strip().split(',')

      # Verifica se a linha tem dados suficientes
      if len(colunas) >= 4:
        # Converte os valores de texto para números inteiros e soma
        dengue = int(colunas[2])
        chikungunya = int(colunas[3])

        total_dengue += dengue
        total_chikungunya += chikungunya
        semanas_lidas += 1

  print('--- Resumo da Análise (Santana do Paraíso) ---')
  print(f'Semanas epidemiológicas analisadas: {semanas_lidas}')
  print(f'Total de casos de Dengue: {total_dengue}')
  print(f'Total de casos de Chikungunya: {total_chikungunya}')

except FileNotFoundError:
  print(f"Erro: O ficheiro '{arquivo_dados}' não foi encontrado na pasta.")
except ValueError:
  print(
      'Erro: Verifique se as colunas de casos contêm apenas números inteiros.'
  )
