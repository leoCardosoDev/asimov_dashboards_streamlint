## Instruções gerais sobre docker

Para adicionar o **pgAdmin 4** ao seu `docker-compose.yml`, siga os passos abaixo:

---

### **1️⃣ Atualize o `docker-compose.yml`**
Adicione o serviço do **pgAdmin** ao seu `docker-compose.yml`:

```yaml
version: "3.9"

services:
  app:
    build: ./app
    container_name: streamlit_app
    ports:
      - "8501:8501"
    depends_on:
      - db
    env_file:
      - ./app/.env

  db:
    image: postgres:15
    container_name: postgres_db
    restart: always
    environment:
      POSTGRES_DB: mydatabase
      POSTGRES_USER: myuser
      POSTGRES_PASSWORD: mypassword
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

  pgadmin:
    image: dpage/pgadmin4
    container_name: pgadmin4
    restart: always
    environment:
      PGADMIN_DEFAULT_EMAIL: admin@example.com
      PGADMIN_DEFAULT_PASSWORD: admin
    ports:
      - "5050:80"
    depends_on:
      - db

volumes:
  postgres_data:
```

---

### **2️⃣ Execute os containers**
No terminal, rode:

```sh
docker-compose up -d
```

Isso iniciará os serviços **app**, **PostgreSQL** e **pgAdmin 4**.

---

### **3️⃣ Acesse o pgAdmin 4**
1. Abra o navegador e vá para:  
   **`http://localhost:5050`**
2. Faça login com:  
   - **E-mail:** `admin@example.com`
   - **Senha:** `admin`
3. No **pgAdmin**, clique em **Add New Server** e configure:
   - **Name:** PostgreSQL (ou qualquer nome)
   - **Connection:**
     - **Host:** `db` *(Nome do serviço no `docker-compose.yml`)*
     - **Port:** `5432`
     - **Username:** `myuser`
     - **Password:** `mypassword`
     - **Database:** `mydatabase`

4. Clique em **Save** e pronto! 🎉 Agora você pode gerenciar o banco PostgreSQL no pgAdmin. 🚀