@echo off
:: Verifica se o ambiente virtual existe
if not exist "venv\Scripts\activate" (
    echo Ambiente virtual 'venv' não encontrado.
    echo Certifique-se de que a pasta 'venv' está na mesma pasta que este arquivo.
    pause
    exit
)

call venv\Scripts\activate

streamlit run app.py

pause
