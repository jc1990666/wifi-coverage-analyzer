import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import Polygon
from shapely import affinity
from io import BytesIO

# Função para importar e desenhar a planta baixa
def importar_planta_baixa():
    # Simulação de uma planta baixa; substitua com código para processar o arquivo real
    return Polygon([(0, 0), (10, 0), (10, 10), (0, 10)])

def desenhar_planta_baixa(planta_baixa):
    fig, ax = plt.subplots()
    x, y = planta_baixa.exterior.xy
    ax.plot(x, y, label="Planta Baixa")
    plt.fill(x, y, alpha=0.5)
    plt.title('Planta Baixa do Edifício')
    st.pyplot(fig)

# Função para simular a cobertura Wi-Fi
def simular_cobertura(planta_baixa, parametros):
    x, y = np.linspace(0, 10, 100), np.linspace(0, 10, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.exp(-((X-5)**2 + (Y-5)**2) / parametros['sigma'])
    return X, Y, Z

def visualizar_cobertura(X, Y, Z):
    fig, ax = plt.subplots()
    c = ax.contourf(X, Y, Z, levels=10, cmap='viridis')
    fig.colorbar(c, ax=ax, label='Intensidade do Sinal')
    plt.title('Cobertura de Sinal Wi-Fi')
    st.pyplot(fig)

# Interface com Streamlit
st.title('Simulador de Cobertura Wi-Fi')

uploaded_file = st.file_uploader("Escolha a planta baixa", type=["pdf", "dwg", "dxf"])

if uploaded_file is not None:
    st.write("Carregando planta baixa...")
    planta_baixa = importar_planta_baixa()
    desenhar_planta_baixa(planta_baixa)
    
    parametros = {'sigma': 1.0}  # Parâmetro de exemplo para a simulação
    X, Y, Z = simular_cobertura(planta_baixa, parametros)
    visualizar_cobertura(X, Y, Z)
else:
    st.write("Nenhum arquivo carregado. Por favor, carregue a planta baixa do edifício.")
