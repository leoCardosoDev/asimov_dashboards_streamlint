Versão do **Dockerfile** e **docker-compose.yml**, agora incluindo **Plotly** e **Dash**, além do **Jupyter Notebook** com persistência de volumes. Também tem o tutorial para cobrir o uso do **Dash**.  

---

## 🐳 **Dockerfile**
```dockerfile
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
```

---

## 📄 **docker-compose.yml**
```yaml
version: '3.8'

services:
  jupyter:
    build: .
    container_name: jupyter-anaconda-dash
    ports:
      - "8888:8888"  # Porta do Jupyter Notebook
      - "8050:8050"  # Porta do Dash
    volumes:
      - ./workspace:/workspace
    restart: always
```

---

## 📖 **Tutorial Completo**

### ✅ **1. Instalar Docker e Docker Compose**
Se ainda não tem o Docker e o Docker Compose instalados, siga os passos:

#### **Linux**
```sh
sudo apt update && sudo apt install -y docker.io docker-compose
sudo systemctl enable --now docker
```

#### **MacOS (com Homebrew)**
```sh
brew install --cask docker
brew install docker-compose
```

#### **Windows (com WSL)**
- Instale o [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- Ative o suporte ao WSL 2

---

### ✅ **2. Criar e Configurar o Projeto**
1. **Crie a pasta do projeto**  
   ```sh
   mkdir jupyter-docker && cd jupyter-docker
   ```

2. **Crie os arquivos**  
   ```sh
   touch Dockerfile docker-compose.yml
   mkdir workspace  # Pasta para armazenar os notebooks
   ```

3. **Copie o código do Dockerfile e docker-compose.yml** para os arquivos criados.

---

### ✅ **3. Construir e Rodar o Container**
1. **Construa a imagem Docker**  
   ```sh
   docker-compose build
   ```

2. **Inicie o container**  
   ```sh
   docker-compose up -d
   ```

3. **Verifique se o container está rodando**  
   ```sh
   docker ps
   ```

---

### ✅ **4. Acessar o Jupyter Notebook**
1. Abra o navegador e acesse:  
   ```
   http://localhost:8888
   ```

2. Como removemos o token (`--NotebookApp.token=''`), você não precisará inserir senha.

---

### ✅ **5. Rodar um Aplicativo Dash**
1. **Crie um arquivo dentro da pasta `workspace` chamado `app.py`**
   ```python
   import dash
   from dash import dcc, html
   import plotly.express as px
   import pandas as pd

   # Criar um DataFrame de exemplo
   df = pd.DataFrame({
       "Categoria": ["A", "B", "C", "D"],
       "Valores": [10, 20, 15, 25]
   })

   # Criar um gráfico de barras com Plotly
   fig = px.bar(df, x="Categoria", y="Valores", title="Exemplo de Gráfico com Plotly e Dash")

   # Criar a aplicação Dash
   app = dash.Dash(__name__)

   app.layout = html.Div([
       html.H1("Dashboard com Dash e Plotly"),
       dcc.Graph(figure=fig)
   ])

   if __name__ == '__main__':
       app.run_server(debug=True, host='0.0.0.0', port=8050)
   ```

2. **Acesse o container e rode o app**  
   ```sh
   docker exec -it jupyter-anaconda-dash bash
   ```

3. **No terminal do container, execute:**
   ```sh
   python /workspace/app.py
   ```

4. **Acesse no navegador:**  
   ```
   http://localhost:8050
   ```

---

### ✅ **6. Parar e Remover o Container**
- Para **parar** o container:  
  ```sh
  docker-compose down
  ```

- Para **remover completamente** a imagem e os volumes:  
  ```sh
  docker system prune -a
  ```

---

### 🎯 **Benefícios**
✅ **Persistência de dados**: Os notebooks e códigos do Dash ficam salvos localmente na pasta `workspace`.  
✅ **Ambiente isolado**: Não bagunça sua instalação local do Python.  
✅ **Dash + Plotly**: Criar dashboards interativos sem precisar de configurações extras.  
✅ **Customizável**: Pode adicionar mais bibliotecas conforme necessário.  

Agora você tem um ambiente completo com **Jupyter Notebook, Dash e Plotly** rodando no Docker! 🚀