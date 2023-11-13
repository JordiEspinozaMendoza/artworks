# Artworks Proyecto 3

## Integrantes

- Luis Alejandro Fierro Jacobo 19211637
- Jordi Espinoza Mendoza 19211633

[Video del proyecto](https://www.loom.com/share/21bdaa33358748f39943d110db09fdeb?sid=5ff186d1-a9ea-4b2d-9187-a6ffeaff59b5)

## Descripción

Este es el repositorio para el proyecto 3 de la materia de desarrollo web, proyecto realizado con el framework de Django.

## Instrucciones

1. Clonar el repositorio

```bash
git clone https://github.com/JordiEspinozaMendoza/artworks
```

2. Crear un entorno virtual

```bash
python -m venv venv
```

3. Activar el entorno virtual

```bash
source venv/bin/activate
```

4. Instalar las dependencias

```bash
pip install -r requirements.txt
```

5. Crea una carpeta llamada `artworks_data` en la raíz del proyecto para agregar los archivos CSV con los datos de las obras de arte.

6. Ejecuta las migraciones

```bash
python manage.py migrate
```

7. Carga los datos de las obras de arte

```bash
python manage.py load_artists

python manage.py load_artworks
```

8. Ejecuta el servidor

```bash
python manage.py runserver
```
