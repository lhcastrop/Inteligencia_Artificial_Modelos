<h1 align="center"> Proyecto_Sustituto_Inteligencia_Artificial </h1>

![Texto alternativo](images/Recurso_Kaggle.jpg)
## Contexto

En el siguiente proyecto se utilizó una solución disponible para la Competición de Kaggle llamada "NeurIPS 2024 - Predict New Medicines with BELKA". La competición buscaba el uso de Modelos de Machine Learning para predecir la afinidad entre moleculas pequeñas y determinadas proteinas objetivo usando la Gran Biblioteca Codificada para la Evaluación Quimica (BELKA).

La predicción de afinidad de las moleculas pequeñas a ciertos objetivos proteícos es fundamental para el desarrollo en la industria farmaceutica, y para el caso de la competición se usará una parte de los datos de pruebas realizadas por Leash Bioscience, los cuales se encuentran en la BELKA.

BELKA es una Gran Biblioteca Codificada para la Evaluación Química que contiene aproximadamente 3.6 mil millones de mediciones de unión física entre 3.6 mil millones de moléculas pequeñas y 3 proteinas objetivo utilizando la tecnologia de biblioteca química codificada por ADN. 

El desarrollo de un modelo de Machine Learning adecuado sería util para el descubrimiento de nuevos farmacos ya que permite realizar una preselección de medicamentos candidatos con determinadas proteinas objetivo, disminuyendo de manera drastica la cantidad de pruebas de laboratorio que se deben realizar, optimizando tiempo y reduciendo costos en experimentación.

Para la competición en específico se modelará la afinidad de diferentes moléculas en 3 proteínas: EPHX2 (sEH), BRD4 y ALB (HSA). Estas proteínas estan relacionadas con presión arterial alta, progresión de diabetes y cancer. La base de datos suministrada se encuentra en un archivo .paquet, y contiene la información de las moleculas en notación SMILES (Simplified Molecular Input Line Entry System), la cual es usada para uso computacional.

## Codigo

De las soluciones encontradas para el desafio se escogió la mejor calificada. Dicha solución tal como se ve en la siguiente imagen se puede consultar en el siguiente enlace https://www.kaggle.com/code/andrewdblevins/leash-tutorial-ecfps-and-random-forest: 

![Texto alternativo](images/Code_Kaggle.jpg)

El codigo disponible se ejecutó en la herramienta Google Colab, y se puede acceder a través del siguiente enlace: https://colab.research.google.com/drive/1TFxXRKhgDSLkFGkjLCTNdW86vjXow0LB?usp=sharing

![Texto alternativo](images/Recorte_Colab.jpg)

Para el procesamiento de la informacion de la base de datos se usarán los ECFPs de cada molécula (Extended-connectivity fingerprints), los cuales se procesarán para generar el modelo usando Random Forest. Para la manipulación de la base de datos y la información de las moleculas en SMILES que está en esta base de datos, se usarán las librearías duckdb y rdkit respectivamente.



Para una correcta ejecución es necesario importar la base de datos desde Kaggle por lo que debe descargarse el archivo que llamado "kaggle.json" que se encuentra dentro de la carpeta fase-1. Tal como se puede ver en la siguiente imagen: 
![Texto alternativo](images/Recorte_Token.jpg)
Una vez se descarga el archivo se procede a la ejecución en Kaggle y este se carga posterior a la ejecución de la linea de comando files.upload() tal como se puede ver en las imagenes:

![Texto alternativo](images/Cargar_Archivo.jpg)

![Texto alternativo](images/Carga_Kaggle.jpg)

Posterior a la carga y lectura del archivo se puede acceder a la base de datos para su utilización en el proyecto.

![Texto alternativo](images/Archivo_Cargado.jpg)


