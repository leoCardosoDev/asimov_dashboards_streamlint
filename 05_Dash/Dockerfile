# Usa a imagem base do Anaconda com Python 3.9
FROM continuumio/anaconda3:latest

# Define o diretório de trabalho dentro do container
WORKDIR /workspace

# Copia os arquivos locais para o container (opcional)
COPY . /workspace

# Instala dependências adicionais, caso necessário
RUN conda install -y jupyter notebook pandas numpy matplotlib seaborn && \
    conda clean --all

# Expõe a porta 8888 para o Jupyter Notebook
EXPOSE 8888

# Comando para iniciar o Jupyter Notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=''"]
