import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import Polygon
from matplotlib.patches import Polygon as mpl_polygon
from tkinter import Tk, filedialog, Button

# Função para importar e desenhar a planta baixa
def importar_planta_baixa(arquivo):
    # Aqui você deve adicionar código para ler o arquivo da planta baixa
    # Para este exemplo, vamos criar uma planta baixa de exemplo
    return Polygon([(0, 0), (10, 0), (10, 10), (0, 10)])

def desenhar_planta_baixa(planta_baixa):
    fig, ax = plt.subplots()
    x, y = planta_baixa.exterior.xy
    ax.plot(x, y, label="Planta Baixa")
    plt.fill(x, y, alpha=0.5)
    plt.legend()
    plt.title('Planta Baixa do Edifício')
    plt.show()

# Função para adicionar obstruções
def adicionar_obstrucoes(planta_baixa, obstrucoes):
    for obstrucao in obstrucoes:
        planta_baixa = planta_baixa.difference(obstrucao)
    return planta_baixa

# Simular cobertura Wi-Fi
def simular_cobertura(planta_baixa, parametros):
    # Este é um exemplo simplificado; uma simulação real deve considerar vários fatores
    x, y = np.linspace(0, 10, 100), np.linspace(0, 10, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.exp(-((X-5)**2 + (Y-5)**2) / parametros['sigma'])
    return X, Y, Z

# Visualizar a cobertura de sinal Wi-Fi
def visualizar_cobertura(X, Y, Z):
    plt.contourf(X, Y, Z, levels=10, cmap='viridis')
    plt.colorbar(label='Intensidade do Sinal')
    plt.title('Cobertura de Sinal Wi-Fi')
    plt.show()

# Função para carregar a planta baixa
def carregar_planta():
    arquivo = filedialog.askopenfilename(filetypes=[("Arquivos de Planta Baixa", "*.pdf;*.dwg;*.dxf")])
    planta_baixa = importar_planta_baixa(arquivo)
    desenhar_planta_baixa(planta_baixa)
    
    parametros = {'sigma': 1.0}  # Parâmetro de exemplo para a simulação
    X, Y, Z = simular_cobertura(planta_baixa, parametros)
    visualizar_cobertura(X, Y, Z)

# Interface gráfica para o aplicativo
def criar_interface():
    root = Tk()
    root.title('Simulador de Cobertura Wi-Fi')

    botao_carregar = Button(root, text="Carregar Planta Baixa", command=carregar_planta)
    botao_carregar.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    criar_interface()
