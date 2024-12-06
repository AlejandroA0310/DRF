# API REST en Django

Este proyecto es una API REST desarrollada con Django, diseñada para gestionar [inserta una breve descripción del propósito de la API]. El sistema está desplegado en la plataforma Render para facilitar su acceso público.

---

## Descripción de la Aplicación

- **Framework usado:** Django
- **Base de datos:** [indica el tipo de base de datos, por ejemplo, SQLite, MySQL, PostgreSQL, etc.]
- **Propósito:** [describe brevemente lo que hace la API, por ejemplo, "Permite realizar operaciones CRUD sobre un modelo de tareas".]
- **Endpoints principales:** 
  - `GET /api/items` - Obtiene todos los ítems.
  - `POST /api/items` - Crea un nuevo ítem.
  - `PUT /api/items/<id>` - Actualiza un ítem existente.
  - `DELETE /api/items/<id>` - Elimina un ítem.

---

## Instrucciones para Ejecutar el Proyecto Localmente

### 1. Clonar el repositorio
```bash
git clone <URL_DEL_REPOSITORIO>
cd <nombre_del_proyecto>


## 2. Crear y activar un entorn virtual 

python -m venv env

source env/bin/activate

## 3. Instalar las dependencias 

pip install -r requirements.txt


## 4. Configurar las variables de entorno

SECRET_KEY='tu_clave_secreta'
DEBUG=True
DATABASE_URL='URL_de_tu_base_de_datos'


## 5.Aplicar las migraciones de la base de datos

pyhton manage.py makemigrations

python manage.py migrate


## 6.Ejecutar el servidor de desarrollo

python manage.py runserver
