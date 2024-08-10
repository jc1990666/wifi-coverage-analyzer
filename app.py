import streamlit as st

# Fatores de ajuste
fatores_parede = {
    "drywall": 1.1,
    "concreto": 0.7,
    "tijolo": 0.85,
    "vidro": 1.05
}

fatores_frequencia = {
    "2.4 GHz": 1.2,
    "5 GHz": 0.8
}

fatores_roteador = {
    1: 0.8,
    2: 1.1,
    3: 1.3
}

def calcular_probabilidade(tipo_parede, frequencia_roteador, num_roteadores):
    fator_parede = fatores_parede.get(tipo_parede, 1)
    fator_frequencia = fatores_frequencia.get(frequencia_roteador, 1)
    fator_roteador = fatores_roteador.get(num_roteadores, 1)
    
    cobertura_estimativa = 50
    cobertura_ajustada = cobertura_estimativa * fator_parede * fator_frequencia * fator_roteador
    probabilidade_cobertura_boa = min(cobertura_ajustada / 100, 1)
    
    return probabilidade_cobertura_boa

def main():
    st.title("Analisador de Cobertura Wi-Fi")

    tipo_parede = st.selectbox("Tipo de Parede", ["drywall", "concreto", "tijolo", "vidro"])
    frequencia_roteador = st.selectbox("Frequência do Roteador", ["2.4 GHz", "5 GHz"])
    num_roteadores = st.slider("Número de Roteadores", min_value=1, max_value=3)

    if st.button("Calcular Cobertura"):
        probabilidade = calcular_probabilidade(tipo_parede, frequencia_roteador, num_roteadores)
        st.write(f"Probabilidade de Cobertura Boa: {probabilidade:.2%}")

if __name__ == "__main__":
    main()
