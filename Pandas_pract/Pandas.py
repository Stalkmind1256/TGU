import pandas as pd
import numpy as np
import json


# data = {
#     'col 1':['Я','Python','Буду'],
#     'col 2':['люблю','мой','стараться'],
#     'col 3':['анализ','лучший','хорошо'],
#     'col 4':['данных','друг','учиться'],
# }
# df = pd.DataFrame(data)


df = pd.read_csv("shop_users.csv")# Показывать все строки
pd.set_option('display.max_rows', None)  # Показывать все строки
pd.set_option('display.max_columns', None)  # Показывать все столбцы
pd.set_option('display.width', None)  # Полная ширина вывода
pd.set_option('display.max_colwidth', None)
# print(df.head())
# print(df.shape)
# print(df.dtypes)

df_copy = df.copy()
#Не нужные колоники Unnamed:0, common_count,home_town, relation, is_closed
# print(df_copy.columns)
columns = ['Unnamed: 0', 'common_count', 'is_closed', 'home_town', 'relation']
# inplace позволяет перезаписать текущий df
df_copy.drop(columns=columns, inplace=True)
print(df_copy.columns)
#Проверка на дубликаты по заголовку таблицы
# (df_copy.duplicated(subset='id').sum())
# print(df_copy.duplicated(subset=['bdate', 'sex'], keep=False).sum())
print(df_copy.shape)
df_copy.drop_duplicates(inplace=True)
print(df_copy.shape)

#Удаление пропусков
# print(df_copy.notna().sum())
df_copy.dropna(subset=['costs', 'games'], inplace=True)
print(df_copy.shape)
# print(df_copy.info())
df_copy.reset_index(drop=True, inplace=True)
print(df_copy.isna().sum())

#JSON
#City
# Приводим в нормальный вид json
# print(df_copy['city'][0])
# print(df_copy['city'][0].replace("'", '"'))
#Достаем по ключу
# print(json.loads(df_copy['city'][0].replace("'", '"'))['title'])

def text_to_json(text):
    if pd.isna(text):
        result = 'Город не указан'
    else:
        result = json.loads(text.replace("'", '"'))['title']
    return  result

#Применяем функцию к столбцу
df_copy['city'] = df_copy['city'].apply(text_to_json)
# print(df_copy.city)

#City
df_copy['country'][0]
df_copy['country'][0].replace("'", '"')
print(json.loads(df_copy['country'][0].replace("'", '"'))['title'])
# for item in df_copy.country:
#     try:
#         eval(item)['title']
#     except:
#         print(item)
# print(df_copy[df_copy.country.str.contains('platform')])
df_copy.drop([3334, 3335, 3336, 3337], inplace=True)
df_copy['country'] = df_copy['country'].apply(text_to_json)
# print(df_copy.country)

#last_seen
# print(df_copy['last_seen'][0])

def text_to_json_2(text):
    if pd.isna(text):
        result = np.nan
    else:
        result = json.loads(text.replace("'", '"'))['time']
    return result

df_copy['last_seen'] = df_copy['last_seen'].apply(text_to_json_2)
# print(df_copy.last_seen.apply("{0:.0f}".format))

#costs
# costs = df_copy['costs'][0]
# print(costs)
# costs_1 = costs.replace("'","").replace("}","").replace("{","").replace(":","")
# costs_2 = costs_1.split(",")
# print(costs_2[0])
# print(costs_2[1])
# print(costs_2[0].split()[1])
# print(costs_2[1].split()[1])
# print(costs_2[1].split()[0].strip())

def costs_func(costs_currency):
    costs = (costs_currency.replace("'", "").replace("{", "").replace("}", "").replace(":", "")
    .split(",")[0]
    .split()[1]
    )
    return costs

def currency_func(costs_currency):
  currency = (costs_currency.replace("'", "").replace("{", "").replace("}", ""). replace(":", "")
                         .split(",")[1]
                         .split()[1]
                         )
  return currency

# print(df_copy.costs[10])
# print(costs_func(df_copy.costs[10]))
# print(currency_func(df_copy.costs[10]))

df_copy['costs_sum'] = df_copy['costs'].apply(costs_func)
df_copy['currency'] = df_copy['costs'].apply(currency_func)

# print(df_copy[['costs_sum', 'currency']])
df_copy.drop(columns='costs', inplace=True)
df_copy.rename(columns={'costs_sum':'costs'}, inplace=True)
# print(df_copy[['costs','currency']])

#Games
games = df_copy['games'][0]
print(games)

# games_1 = eval(games)

def game_func(games):
    res = []
    for game in eval(games):
        game_clean = game['name']
        res.append(game_clean)
    return res

# print(df_copy.games[10])
# print(game_func(df_copy.games[10]))
df_copy['games_clean'] = df_copy['games'].apply(game_func)
# print(df_copy['games_clean'])
df_copy.drop(columns=['games'],inplace=True)
df_copy.rename(columns={'games_clean' : 'games'}, inplace=True)
# print(df_copy.columns)
# print(df_copy.games)

#Data_time
#ddate, last_seen - datetime; followers_count, costs - int
#bdate
df_copy.bdate = pd.to_datetime(df_copy.bdate, format='%d.%m.%Y')
#print(df_copy.bdate)

#last_seen
df_copy.last_seen = pd.to_datetime(df_copy.last_seen, unit='s')
df_copy.last_seen = df_copy.last_seen.dt.strftime('%d.%m.%Y')
# print(df_copy.last_seen)

#followers_count
df_copy.followers_count = df_copy.followers_count.astype('Int64')
# print(df_copy.followers_count)

#costs
df_copy.costs = pd.to_numeric(df_copy.costs, downcast='float')
# print(df_copy.costs)

# Расчеты дополнительных признаков
#Возраст
current_day = pd.Timestamp.today()
current_year = current_day.year
df_copy['age'] = current_year - df_copy.bdate.apply(lambda x: x.year)
df_copy.drop(columns='bdate',inplace=True)

#Валюты
# print(df_copy[['costs', 'currency']])
# print(df_copy['currency'].unique())
rates = dict(RUR = 1, USD = 99.38 , KZT = 0.19, EUR = 105.1)
df_copy['costs_to_rur'] = df_copy['currency'].map(rates) * df_copy['costs']
df_copy.drop(columns=['costs', 'currency'], inplace=True)
# print(df_copy.columns)

#Sex
# print(df_copy.sex.unique())
sex_dict = {1 : "женский", 2 : "мужской", 3 : "не указан"}
df_copy.sex = df_copy.sex.apply(lambda x: sex_dict[x])
# print(df_copy.sex.unique())


#Финал очистки Форматирование данных

#City
# print(len(df_copy.city.unique()))
# print(sorted(df_copy.city.unique()))
df_copy.city = df_copy.city.str.lower()
df_copy.loc[df_copy.city == 'moscow', 'city'] = 'москва'
df_copy.loc[df_copy.city == 'saint-petersburg', 'city'] = 'санкт-петербург'
# print(df_copy.city)
# print(len(df_copy.city.unique()))

#Country
df_copy.country = df_copy.country.str.lower()


#Проверка ДатаСета
print(df_copy.shape)
print(df_copy.info())
print(df_copy.head())

columns = ['id', 'age', 'sex', 'city', 'country', 'followers_count', 'last_seen', 'costs_to_rur', 'games']
df_copy = df_copy[columns]

print(df_copy.head(1))

df_copy.to_excel('shop_users_cleaner.xlsx', index=False)

df_games = df_copy.explode('games', ignore_index=True)
# print(df_games)

print(len(df_games.games.unique()))
print(df_games.games.unique())

df_games.to_csv('df_games.csv')