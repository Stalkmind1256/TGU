import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv("housing_market_dataset.csv", low_memory=False)

df_copy = df.copy()

print(df.shape)
# Оценка размеров и наличие пропусков

print(df.info())

df_copy['Очищенная цена'] = df_copy['Цена'].str.replace(" ", '').str.replace("₽", "").astype(int)
df_copy = df_copy.sort_values(['Очищенная цена'] )

year_of_construction = df_copy['Год постройки']
max_value = year_of_construction.max()
min_value = year_of_construction.min()
print(f"Максимальный год постройки: {max_value}, Минимальный год постройки: {min_value}")
mean_value = year_of_construction.mean()
print(f"Средний год построки: {mean_value:.2f}")
print(df_copy.describe())

# df_copy['Цена за м²'] = df_copy['Очищенная цена'] / df_copy['Площадь, м²']

# print(df_copy['Класс жилья'])

# class_home = df_copy['Номер этажа'].value_counts()
# sorted_class_home = class_home.sort_values(ascending=False)
#
# plt.figure(figsize=(10, 6))
# sorted_class_home.plot(kind='bar', color='skyblue', edgecolor='black')
# plt.title("Количество записей по классу жилья")
# plt.xlabel("Класс жилья")
# plt.ylabel("Количество")
# plt.xticks(rotation=45)
# plt.show()

# class_order = sorted_class_home.index.tolist()
# print("Порядок классов:", class_order)

unique_categories = df_copy['Площадь кухни'].nunique(dropna=False)
print(f"Количество уникальных категорий в колонке 'Площадь кухни': {unique_categories}")

type_counts = df_copy['Тип объекта'].value_counts()
print(type_counts)

order = type_counts.index.tolist()
print(f"Порядок категорий: {order}")

# plt.figure(figsize=(10, 6))
# type_counts.plot(kind='bar', color='skyblue', edgecolor='black')
# plt.title("Количество записей по типу объекта", fontsize=14)
# plt.xlabel("Тип объекта", fontsize=12)
# plt.ylabel("Количество", fontsize=12)
# plt.xticks(ticks=range(len(type_counts.index)), labels=type_counts.index, rotation=45, fontsize=10)
# plt.tight_layout()
# plt.show()

# print(df_copy['Площадь кухни'])
non_empty_kitchen_area = df['Площадь кухни'].dropna()  # Убираем NaN
non_empty_kitchen_area = non_empty_kitchen_area[non_empty_kitchen_area.str.strip() != ""]  # Убираем пустые строки
non_empty_kitchen_area = non_empty_kitchen_area[non_empty_kitchen_area.str.contains(r'\d')]  # Проверяем наличие цифр

# Количество ненулевых значений
non_null_count = len(non_empty_kitchen_area)
print(f"Количество ненулевых значений в колонке 'Площадь кухни': {non_null_count}")

# type_room = df_copy['Количество комнат'].value_counts()
# print(type_room)
#
# plt.figure(figsize=(10, 6))
# plt.boxplot(type_room, vert=False, patch_artist=True,
#             boxprops=dict(facecolor='skyblue', color='black'),
#             whiskerprops=dict(color='black', linewidth=1.5),
#             flierprops=dict(markerfacecolor='red', marker='o', markersize=7),
#             medianprops=dict(color='orange', linewidth=2))
#
# plt.title("Распределение количества комнат с усиками", fontsize=14)
# plt.xlabel("Количество комнат", fontsize=12)
# plt.tight_layout()
# plt.show()

non_null_stage = df_copy['Этап строительства'].dropna()

# Определение наиболее распространенного этапа
most_common_stage = non_null_stage.mode()[0]  # mode() возвращает серию, берем первый элемент

# Вывод результата
print(f"Наиболее распространенный ненулевой этап строительства: {most_common_stage}")

percentile_70 = df_copy['Год постройки'].quantile(0.70)
print(f"70-й процентиль года постройки: {percentile_70}")

# class_counts = df_copy['Класс жилья'].value_counts()
# class_counts_sorted = class_counts.sort_values(ascending=False)
#
# plt.figure(figsize=(10, 6))
# class_counts_sorted.plot(kind='bar', color='skyblue', edgecolor='black')
# plt.title("Распределение классов жилья", fontsize=14)
# plt.xlabel("Класс жилья", fontsize=12)
# plt.ylabel("Количество", fontsize=12)
# plt.xticks(rotation=45, fontsize=10)
# plt.tight_layout()
# plt.show()
#
# # Выводим порядок классов
# print(class_counts_sorted)

# business_class_data = df_copy[df_copy['Класс жилья'] == 'Бизнес класс']
# most_common_building_type = business_class_data['Тип здания'].mode()[0]
# print("Наиболее распространенный тип здания в бизнес классе:", most_common_building_type)

# elit_class_data = df_copy[df_copy['Класс жилья'] == 'Элит класс']
# comfort_class_data = df_copy[df_copy['Класс жилья'] == 'Комфорт класс']
#
# # Получаем количество объектов для каждого класса
# elit_class_count = elit_class_data.shape[0]
# comfort_class_count = comfort_class_data.shape[0]
#
# # Рассчитываем соотношение элит-класса к комфорт-классу
# if comfort_class_count > 0:
#     ratio = elit_class_count / comfort_class_count
# else:
#     ratio = 0  # Если комфорт-класса нет, соотношение равно 0
#
# print(f"Количество квартир элит-класса: {elit_class_count}")
# print(f"Количество квартир комфорт-класса: {comfort_class_count}")
# print(f"Соотношение элит-класса к комфорт-классу: {ratio:.2f}")

class_counts = df['Класс жилья'].value_counts()

# # Выводим наиболее распространенную категорию
# most_common_class = class_counts.idxmax()
# print("Наиболее распространенная категория:", most_common_class)
#
# sns.scatterplot(data=df, x='Год постройки', y='Очищенная цена за м²')
#
# # Добавляем заголовки и отображаем график
# plt.title("Зависимость цены за кв.м от года постройки")
# plt.xlabel("Год постройки")
# plt.ylabel("Цена за кв.м")
# plt.show()
#
# # Рассчитываем коэффициент корреляции между годом постройки и ценой за квадратный метр
# correlation = df['Год постройки'].corr(df['Очищенная цена за м²'])
# print("Коэффициент корреляции:", correlation)

plt.figure(figsize=(10, 6))
sns.boxplot(x='Тип объекта', y='Очищенная цена за м²', data=df)
plt.title('Зависимость цены за м² от типа объекта', fontsize=16)
plt.xlabel('Тип объекта', fontsize=14)
plt.ylabel('Очищенная цена за м²', fontsize=14)
plt.xticks(rotation=45)  # Поворот подписей на оси X для улучшения читаемости
plt.tight_layout()
plt.show()
