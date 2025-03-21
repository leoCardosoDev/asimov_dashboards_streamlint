# Usa a imagem base do Anaconda com Python 3.9
FROM continuumio/anaconda3:latest

# Define o diretório de trabalho dentro do container
WORKDIR /workspace

# Copia os arquivos locais para o container (opcional)
COPY . /workspace

# Instala dependências adicionais: Jupyter, Pandas, NumPy, Matplotlib, Seaborn, Plotly e Dash
RUN conda install -y \
    jupyter \
    notebook \
    pandas \
    numpy \
    matplotlib \
    seaborn && \
    pip install plotly dash && \
    conda clean --all

# Expõe as portas para Jupyter Notebook e Dash
EXPOSE 8888 8050

# Comando para iniciar o Jupyter Notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=''"]
