import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout

# Настройка отображения данных
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# Загрузка данных
df = pd.read_csv("patient_ml_dataset.csv", low_memory=False)

# Копия данных для работы
df_copy = df.copy()

# Удаление пропущенных значений
df_copy.dropna(inplace=True)

# Кодирование категориальных переменных
label_encoder = LabelEncoder()
df_copy["Gender"] = label_encoder.fit_transform(df_copy["Gender"])
df_copy["Diagnosis"] = label_encoder.fit_transform(df_copy["Diagnosis"])

# Разделение данных на признаки и целевую переменную
X = df_copy.drop(columns=["Patient_ID", "Diagnosis"])
y = df_copy["Diagnosis"]

# Масштабирование признаков
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Разделение данных на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42, stratify=y)

# Создание модели
model = Sequential([
    Dense(16, activation='relu', input_shape=(X_train.shape[1],)),
    Dropout(0.2),
    Dense(8, activation='relu'),
    Dense(3, activation='softmax')  # 3 класса (Healthy, At Risk, Ill)
])

# Компиляция модели
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Обучение модели
model.fit(X_train, y_train, epochs=1000, batch_size=16, validation_data=(X_test, y_test))

# Оценка модели на тестовых данных
loss, accuracy = model.evaluate(X_test, y_test)
print(f'Accuracy: {accuracy:.4f}')

# Предсказание на тестовых данных
y_pred = np.argmax(model.predict(X_test), axis=1)
comparison = pd.DataFrame({"Real": y_test.values, "Predicted": y_pred})
print(comparison.sample(20))  # Выведем 20 случайных примеров

# Пример новых данных
new_data = pd.DataFrame({
    'Patient_ID': [501, 502, 503, 504],
    'Age': [45, 60, 50, 70],
    'Gender': ['Male', 'Female', 'Male', 'Female'],
    'Systolic_BP': [120, 140, 160, 110],  # Нормальное и повышенное давление
    'Diastolic_BP': [80, 90, 100, 70],    # Нормальное и повышенное давление
    'Heart_Rate': [70, 80, 110, 50],       # Нормальный и повышенный/пониженный пульс
    'Body_Temperature': [36.5, 37.0, 38.0, 35.5],  # Нормальная и повышенная/пониженная температура
    'Glucose_Level': [5.5, 6.0, 8.5, 4.0]  # Нормальный и повышенный уровень глюкозы
})

# Ручное кодирование пола
gender_mapping = {'Female': 0, 'Male': 1}
new_data["Gender"] = new_data["Gender"].map(gender_mapping)

# Удаление ненужных колонок
X_new = new_data.drop(columns=["Patient_ID"])

# Масштабирование признаков
X_new_scaled = scaler.transform(X_new)

# Получение предсказаний
new_predictions = np.argmax(model.predict(X_new_scaled), axis=1)

# Расшифровка предсказаний
decoded_predictions = label_encoder.inverse_transform(new_predictions)

# Добавление предсказаний в DataFrame
new_data["Predicted Diagnosis"] = decoded_predictions
print(new_data)