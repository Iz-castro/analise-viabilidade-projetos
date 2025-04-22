import streamlit as st
import pandas as pd
import joblib
import cloudpickle
import os

# Título da aplicação
st.title("🔍 Análise de Viabilidade de Projetos")
st.subheader("Insira os parâmetros ou envie dados para treinar um novo modelo.")

# Carrega o modelo pré-treinado

with open("logistic_model.pkl", "rb") as f:
    modelo = cloudpickle.load(f)
    
# === SEÇÃO 1: PREVISÃO DE UM PROJETO ===
st.header("🎯 Prever viabilidade de um projeto")

# Inputs do usuário
tempo = st.slider("Tempo de execução (meses)", 3, 24, 12)
custo = st.slider("Custo total (mil R$)", 50, 1000, 300)
recursos = st.slider("Recursos humanos", 1, 30, 10)
complexidade = st.selectbox("Complexidade técnica", ["Baixa", "Média", "Alta"])
inovacao = st.selectbox("Grau de inovação", ["Baixo", "Médio", "Alto"])
setor = st.selectbox("Setor de atuação", ["Educação", "Saúde", "Financeiro", "Tecnologia", "Industrial"])
risco = st.selectbox("Risco", ["Baixo", "Médio", "Alto"])

# Montar DataFrame com os dados de entrada
entrada = pd.DataFrame([{
    "tempo_execucao_meses": tempo,
    "custo_total_mil_reais": custo,
    "recursos_humanos": recursos,
    "complexidade_tecnica": complexidade,
    "grau_inovacao": inovacao,
    "setor_atuacao": setor,
    "risco": risco
}])

# Previsão
if st.button("Verificar Viabilidade"):
    previsao = modelo.predict(entrada)[0]
    probabilidade = modelo.predict_proba(entrada)[0][1]

    if previsao == 1:
        st.success(f"✅ Projeto viável com {probabilidade:.1%} de confiança.")
    else:
        st.error(f"❌ Projeto inviável com apenas {probabilidade:.1%} de chance de sucesso.")

# === SEÇÃO 2: TREINAMENTO COM NOVOS DADOS ===
st.header("📤 Treinar o modelo com novos dados")

uploaded_file = st.file_uploader("Envie um arquivo CSV com novos projetos (com coluna 'viavel')", type=["csv"])

if uploaded_file:
    novos_dados = pd.read_csv(uploaded_file)
    st.write("Prévia dos dados enviados:")
    st.dataframe(novos_dados.head())

    if st.button("Treinar com novos dados"):
        try:
            # Carrega os dados antigos usados no primeiro treino
            dados_antigos = pd.read_csv("projetos_1000.csv")

            # Junta os dados
            df_completo = pd.concat([dados_antigos, novos_dados], ignore_index=True)

            # Separar X e y
            X = df_completo.drop(columns=["nome_projeto", "viavel"])
            y = df_completo["viavel"]

            # Treinar novo modelo com pipeline existente
            modelo.fit(X, y)

            # Salvar novo modelo atualizado com cloudpickle
            import cloudpickle
            with open("logistic_model_atualizado.pkl", "wb") as f:
                cloudpickle.dump(modelo, f)

            st.success("✅ Modelo atualizado com sucesso e salvo como 'logistic_model_atualizado.pkl'.")

        except Exception as e:
            st.error(f"Erro ao treinar com novos dados: {e}")
