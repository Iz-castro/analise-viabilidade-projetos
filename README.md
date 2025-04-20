# 🔍 Análise de Viabilidade de Projetos

Este é um aplicativo interativo desenvolvido com **Python** e **Streamlit**, que utiliza um modelo simples de Machine Learning para prever a viabilidade de projetos com base em parâmetros como custo, tempo, complexidade, inovação e risco.

> 🧠 **Nota de responsabilidade e propósito profissional**  
> Este projeto é parte do meu **portfólio pessoal** e tem como objetivo **demonstrar minha capacidade de estruturar soluções em ciência de dados, machine learning e desenvolvimento de interfaces com Streamlit**.  
> Todos os dados utilizados são **fictícios**, gerados com o auxílio da inteligência artificial ChatGPT para fins educativos e demonstrativos.  
>  
> O modelo incluído é **propositalmente simples (regressão logística)**, ideal para ilustrar conceitos de pré-processamento, previsão e re-treinamento interativo.  
>  
> **Se você é recrutador(a), gerente de produto ou desenvolvedor interessado em colaboração**, este projeto mostra como posso desenvolver e entregar modelos reais em produção.  
> Entre em contato comigo via GitHub!

---

## 📌 Funcionalidades

- **📊 Previsão de Viabilidade**: O usuário pode informar parâmetros do projeto (como tempo, custo e risco), e o modelo prevê se o projeto é viável ou não.
- **📤 Re-Treinamento com Novos Dados**: Você pode carregar arquivos `.csv` com novos projetos para treinar novamente o modelo.
- **🖥️ Interface Web via Navegador**: O app funciona com interface amigável em qualquer navegador moderno.
- **📦 Empacotável para uso offline**: Possui suporte a `.bat` e `.exe` para uso por não-programadores.

---

## 🧭 Como usar o projeto

### ✅ Opção 1 — Usar com `Streamlit` (para desenvolvedores)

> Recomendado se você estiver familiarizado com Python

1. Clone o repositório:

git clone https://github.com/iz-castro/analise-viabilidade-projetos.git
cd analise-viabilidade-projetos

2. (Opcional) Crie e ative um ambiente virtual:
python -m venv venv
venv\Scripts\activate   # No Windows

3. Instale as dependências:
pip install -r requirements.txt

4. Rode o app:
streamlit run app.py



### 🧰 Opção 2 — Usar com `.bat` (modo simples para usuários finais)

Se você recebeu este projeto em formato .zip com o ambiente virtual e o script iniciar_app.bat:

1. Extraia a pasta para qualquer lugar no seu computador
2. Dê dois cliques no arquivo iniciar_app.bat
3. O navegador abrirá automaticamente com o app

> ⚠️ Certifique-se de que a pasta venv/ esteja presente!

├── app.py                           # Código principal do Streamlit
├── iniciar_app.bat                  # Script para iniciar o app facilmente
├── projetos_1000.csv                # Base de dados artificial usada para treino
├── novos_projetos_teste.csv         # Exemplo de novos dados para re-treinamento
├── logistic_model.joblib            # Modelo pré-treinado inicial
├── logistic_model_atualizado.joblib # Modelo gerado após novo treino
├── requirements.txt                 # Dependências do projeto
├── venv/                            # Ambiente virtual (não versionado no GitHub)


### 📊 Formato dos dados esperados

Seu .csv para re-treinamento deve conter estas colunas:

nome_projeto | tempo_execucao_meses | custo_total_mil_reais | recursos_humanos | complexidade_tecnica | grau_inovacao | setor_atuacao | risco | viavel

. A coluna viavel deve conter: 1 para viável, 0 para inviável

. Os dados são categóricos e numéricos mistos


### 👨‍💻 Desenvolvido por Izael Castro
🔗 github.com/Iz-castro

### 📜 Licença
Este projeto está licenciado sob a MIT License.


