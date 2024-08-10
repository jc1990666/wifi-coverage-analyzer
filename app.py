import streamlit as st
import pandas as pd

# Função para calcular a cobertura com base na metragem
def calcular_cobertura(metragens, dados_telecom):
    cobertura = {}
    for cidade, dados in dados_telecom.items():
        if cidade in metragens:
            probabilidade = min(100, (metragens[cidade] / dados['max_metragem']) * 100)
            cobertura[cidade] = probabilidade
        else:
            cobertura[cidade] = 0  # Se não houver metragem para a cidade
    return cobertura

# Dados de exemplo
metragens = {
    'Cidade1': 1500,
    'Cidade2': 2500,
    'Cidade3': 1000
}

dados_telecom = {
    'Cidade1': {'max_metragem': 2000},
    'Cidade2': {'max_metragem': 3000},
    'Cidade3': {'max_metragem': 1500}
}

# Calculando a cobertura
cobertura = calcular_cobertura(metragens, dados_telecom)

# Exibindo os resultados com Streamlit
st.title('Analisador de Cobertura de Wi-Fi')

for cidade, probabilidade in cobertura.items():
    st.write(f'Cobertura de internet em {cidade}: {probabilidade:.2f}%')
