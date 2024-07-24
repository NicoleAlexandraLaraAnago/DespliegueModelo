# Evaluación y Comparación de Algoritmos de Aprendizaje Supervisado

## Objetivo

El objetivo de este proyecto es evaluar y comparar diversos algoritmos de aprendizaje supervisado utilizando un dataset específico. El enfoque está en determinar el mejor modelo en términos de precisión y capacidad para manejar el problema en cuestión. El trabajo incluye:

- **Análisis y limpieza de datos**: Evaluación inicial del dataset, manejo de valores nulos, codificación y normalización de características.
- **Aplicación de algoritmos de aprendizaje supervisado**: Implementación y evaluación de modelos como Regresión, SVM con varios kernels, k-NN, Árboles de Decisión, Bayes y Redes Neuronales Artificiales (RNA).
- **Evaluación y Comparación**: Uso de métricas de rendimiento como precisión, recall, f1-score y matrices de confusión para comparar la eficacia de los modelos.
- **Despliegue Local**: Despliegue del modelo con mejor rendimiento en un entorno local para demostrar su aplicabilidad práctica.

## Requisitos

Para ejecutar el proyecto, asegúrate de tener instalados los siguientes paquetes:

- Python 3.x
- `pandas`
- `numpy`
- `scikit-learn`
- `matplotlib`
- `seaborn`
- `jupyter` (opcional, para ejecutar notebooks)

Puedes instalar estos paquetes usando `pip`. Asegúrate de estar en el entorno adecuado y ejecuta:

`pip install pandas numpy scikit-learn matplotlib seaborn jupyter`

## Requisitos
1. **Clona el repositorio**:

   Abre tu terminal y ejecuta el siguiente comando para clonar el repositorio:

   `git clone https://github.com/NicoleAlexandraLaraAnago/DespliegueModelo.git `

2. **Navega al directorio del proyecto**:

  Cambia al directorio del proyecto con:

   `cd DespliegueModelo`
  
3. **Instala las dependencias:**:

  Asegúrate de tener pip instalado y luego instala las dependencias necesarias con:

   ``` pip install -r requirements.txt```



4. **Prepara los datos:**:

Coloca el archivo data_evaluacion.csv en el directorio data/.

Ejecuta el script para preparar y limpiar los datos:

   ``` python scripts/app.py```
 


5. **Ejecuta los modelos:**:

  Para entrenar y evaluar los modelos, usa el siguiente comando:

   ```python scripts/RNA.ipynb```
 

6. **Revisa los resultados:**:

Los resultados y métricas se guardarán en el directorio results/. Revisa estos archivos para comparar el desempeño de los modelos.


7. **Despliega el modelo:**:

Para desplegar el modelo con mejor rendimiento, ejecuta el script de despliegue:

   ``` python scripts/RNA.ipynb```
 
























