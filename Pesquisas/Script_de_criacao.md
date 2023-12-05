#!/bin/bash

# Criação dos diretórios
mkdir app tests config static templates

# Criação dos arquivos dentro do diretório "app"
touch app/__init__.py
touch app/models.py
touch app/views.py
touch app/controllers.py

# Criação dos arquivos dentro do diretório "tests"
touch tests/__init__.py
touch tests/test_models.py
touch tests/test_views.py
touch tests/test_controllers.py

# Criação dos arquivos dentro do diretório "config"
touch config/__init__.py
touch config/settings.py
touch config/database.py

# Criação dos subdiretórios dentro do diretório "static"
mkdir static/css static/js static/images

# Criação dos arquivos dentro do subdiretório "css"
touch static/css/style.css

# Criação dos arquivos dentro do subdiretório "js"
touch static/js/script.js

# Criação dos arquivos dentro do subdiretório "images"
touch static/images/logo.png

# Criação dos arquivos dentro do diretório "templates"
touch templates/base.html
touch templates/home.html
touch templates/about.html

# Criação dos arquivos na raiz do projeto
touch requirements.txt
touch README.md
touch main.py

echo "Estrutura de diretórios criada com sucesso!"