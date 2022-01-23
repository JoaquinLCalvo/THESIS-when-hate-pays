# Tesis Joaquín López Calvo


## Instrucciones

0. Bajar datos y ponerlos en `data/`

1.

a. Si estás en Conda (?)
b. Si estás usando python a secas, crear virtualenv y activar

Un virtualenv es un entorno distinto de librerías para cada proyecto
```bash
# Crea virtualenv
python -m venv venv
# Lo activa
source venv/bin/activate
```


1. Instalar requerimientos

Instalamos todas las librerías necesarias, incluída la nuestra

```bash
pip install -r requirements.txt
# Esto instala nuestra librería odiogarpa en modo editable
# Así podés cambiar cosas y se actualizan automáticamente
pip install -e .
```


2. Cargar BBDD


```bash
python bin/load_db.py data/comentarios_final.csv
```

3. Analizar comentarios

```bash
python bin/analyze_comments.py --num_comments 10000
```


## Tests

Usamos `pytest` más que nada para ver que funcione todo bien en el preprocesamiento.

```bash
pytest tests/
```