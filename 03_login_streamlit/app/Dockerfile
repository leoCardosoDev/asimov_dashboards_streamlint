# Usa a imagem oficial do Python
FROM python:3.11-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos do projeto para dentro do container
COPY requirements.txt ./
COPY main.py ./

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta 8501 (padrão do Streamlit)
EXPOSE 8501

# Comando para rodar o aplicativo Streamlit
CMD ["streamlit", "run", "main.py"]