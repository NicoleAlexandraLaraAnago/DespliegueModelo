from flask import Flask, request, jsonify, render_template
import pandas as pd
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

# Cargar el modelo desde el archivo .h5
modelo_cargado = tf.keras.models.load_model('modelo_red_neuronal.h5')

# Definir los valores únicos para cada columna categórica
categorical_columns = {
    'State-gov': ['State-gov', 'Local-gov', 'Federal-gov'],
    'Bachelors': ['Bachelors', 'Masters', 'Doctorate', 'None'],
    'Never-married': ['Never-married', 'Married', 'Divorced'],
    'Adm-clerical': ['Adm-clerical', 'Exec-managerial', 'Handlers-cleaners', 'Prof-specialty'],
    'Not-in-family': ['Not-in-family', 'Husband', 'Wife', 'Own-child'],
    'White': ['White', 'Black', 'Asian-Pac-Islander', 'Amer-Indian-Eskimo'],
    'Male': ['Male', 'Female'],
    'United-States': ['United-States', 'Mexico', 'Germany', 'Canada']
}

# Crear un codificador para cada columna categórica
label_encoders = {col: LabelEncoder().fit(values) for col, values in categorical_columns.items()}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return "Bienvenido a la API de Predicción."

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    
    # Convertir datos a DataFrame
    df = pd.DataFrame([data])
    
    # Convertir columnas categóricas a valores numéricos usando los encoders
    for col in categorical_columns.keys():
        if col in df.columns:
            if df[col].iloc[0] in label_encoders[col].classes_:
                df[col] = label_encoders[col].transform(df[col])
            else:
                return jsonify({"error": f"Valor desconocido en la columna {col}: {df[col].iloc[0]}"})
    
    print("Datos después del preprocesamiento:", df.head())
    
    try:
        # Realizar la predicción utilizando el modelo cargado
        prediction = modelo_cargado.predict(df)
        
        # Convertir la predicción a una etiqueta
        result = 'Predicción: >50K' if prediction[0][1] > 0.5 else 'Predicción: <=50K'
    except Exception as e:
        return jsonify({"error": str(e)})
    
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
