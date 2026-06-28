# Laboratorio02_Progra_Cientifica

Proyecto de análisis computacional sobre el corpus bíblico utilizando técnicas de PLN, representación vectorial TF-IDF manual y modelos estadísticos.

## Integrantes
* Marianela Díaz Rodríguez
* Inti Santibañez

## Requisitos de Datos
Para que el sistema funcione correctamente, debes colocar los siguientes archivos CSV en la carpeta raíz del proyecto:
1. `t_kjv.csv`: Contiene los versículos de la Biblia (versión King James).
2. `key_english.csv`: Contiene el mapeo de los IDs de los libros a sus nombres reales.

*Nota: Estos archivos no se encuentran en el repositorio por temas de tamaño, asegúrate de descargarlos del dataset original en Kaggle.*

## Instrucciones de Ejecución
1. Asegúrate de tener instalado Python 3.x.
2. Crea un entorno virtual e instala las dependencias necesarias:
   ```bash
   pip install pandas matplotlib seaborn scikit-learn textblob
