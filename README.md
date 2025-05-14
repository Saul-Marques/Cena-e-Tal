# Cena&Tal 🛒


O Cena&Tal vai ser um website de compra, vendas e de leilões.
Este projeto é a continuação do projeto da cadeira de DPWEB do primeiro semestre do 3º ano de LIG.

---

## ✅ Funcionalidades a Implementar

- [x] Home Page com alguns dos anúncios mais populares e com acesso a outras páginas do website como categorias, login, signup, etc...
- [x] Categorização de produtos
- [x] Inserção de produtos pelos utilizadores
- [x] Formulário de contacto
- [ ] FAQ
- [ ] Tratamento de erros
- [X] Login
- [X] Signup
---

## 🛠️ Tecnologias Utilizadas

- **HTML5**: Estrutura do site.
- **DJANGO**: Framework principal, de programação ORM (Object Relational Mapping)
- **SQL (MariaDB)**: Manipulação e gestão da base de dados.
- **CSS**: Estilização e layout.
- **JavaScript**: Funcionalidades interativas.
- **Bootstrap**: Framework para os elementos do design.

---
# Setup
(Passos em Linux)

Criar um _Virtual Environment _ python e instalar as packages necessárias 
```plaintext
python -m venv <venv>
git clone https://github.com/Saul-Marques/projetoPDI/
pip install requirements.txt
```
Instalar e iniciar uma engine de base de dados, neste projeto foi usada a mariaDB
Archlinux:
```plaintext
sudo pacman -S mariadb
sudo systemctl start mariadb
```
Alterar a ligação à base de dados, se necessário ("projetoPDI/settings.py")
```plaintext
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'projetoPDI',
        'USER': 'saul',
        'PASSWORD': 'projetopdi',
        'HOST': 'localhost',
        'PORT': '3306',  # Default MariaDB port
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}
```

Clonar o repositório e iniciar o servidor
```plaintext
git clone https://github.com/Saul-Marques/projetoPDI
cd projetoPDI
python manage.py runserver
```
O projeto dispõe de dados "Boilerplate" ou iniciais.
Para os utilizar basta correr o comando:
```plaintext
python manage.py loaddata fixtures/initial_data.json
```
Isto vai importar o user de admin, dois produtos iniciais e algumas categorias.

Utilizador inicial/admin:
```plaintext
Email: projetopdi@mail.com
Password: projetopdi
```




## 📂 Estrutura do Repositório

```plaintext
/projetoPDI/
│
├── manage.py
│
├── /uploads/  # Diretório utilizado para os uploadss de utilizadores
│   ├── /products/ 
│   │   ├── /1/  # Imagens do produto 1
│   │   │   ├── image1.jpg
│   │   │   ├── image2.jpg
│   │   ├── /2/  # Imagens do produto 2
│   │   │   ├── image1.jpg
│   │   │   ├── image2.jpg
│   ├── /categorias/
│
├── /loja/  # Applicação django principal (django app)
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py  # Um único ficheiro para todos os models
│   ├── views.py  # Mapeamento das views de várias paginas
│   ├── urls.py  # Url's específicas da app
│   ├── forms.py  # Django forms
│   ├── tests.py
│   ├── /views/
│   │   ├── __init__.py
│   │   ├── home.py  # Index view
│   │   ├── login.py
│   │   ├── signup.py
│   │   ├── upload_product.py  # Handle ao upload dos produtos
│   │   ├── categoria.py
│   │   ├── user.py
│   │   ├── contactos.py
│   │
│   ├── /templates/  # Django HTML templates
│   │   ├── index.html
│   │   ├── login.html
│   │   ├── signup.html
│   │   ├── upload_product.html
│   │   ├── navbar.html
│   │   ├── footer.html  
│   │   ├── contactos.html
│   │
│   ├── /static/  # Todos os ficheiros estáticos (CSS, JS, Imagens)
│   │   ├── /css/
│   │   │   ├── bootstrap.min.css
│   │   │   ├── bootstrap-icons.min.css
│   │   │   ├── styles.css
│   │   │   ├── customfonts.css
│   │   │
│   │   ├── /js/
│   │   │   ├── bootstrap.bundle.min.js
│   │   │   ├── bootstrap.bundle.min.js.map
│   │   │
│   │   ├── /fonts/
│   │   │   ├── Jomhuria-Regular.ttf
│   │   │
│   │   ├── /imgs/  # Imagens e icons
│   │   │   ├── logo.svg
│   │   │   ├── favicon.svg
│   │   │   ├── imgswebsite/
│   │
│   ├── /migrations/
│   │   ├── __init__.py
│   │   ├── 0001_initial.py
│   │   ├── ...
│
├── /projetoPDI/  # Definiçoes principais do projeto
│   ├── __init__.py
│   ├── settings.py  # Configuração da base de dados, apps, static files, etc...
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
