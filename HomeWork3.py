# "В переменной записаны итоги торгов за день на Московской бирже.  \n",
#     "company - управляющая компания фонда  \n",
#     "`ticker` - тикер (код) фонда  \n",
#     "`etf_name` - название фонда  \n",
#     "`trade_cnt` - количество сделок за день  \n",
#     "`result` - объем сделок за день в руб.  \n",
#     "`price`- средняя цена лота"

moex_lst = [
    {
        "company": "УК Альфа-Капитал",
        "ticker": "AKGD",
        "etf_name": "БПИФ Альфа Капитал Золото",
        "trade_cnt": 1025,
        "result": 7904539.64,
        "price": 154.32,
    },
    {
        "company": "УК Тинькофф",
        "ticker": "TGLD",
        "etf_name": "БПИФ ТИНЬКОФФ ЗОЛОТО",
        "trade_cnt": 0,
        "result": 0,
        "price": 0.0,
    },
    {
        "company": "УК Первая",
        "ticker": "SBGD",
        "etf_name": "БПИФ Первая – Фонд Доступное Золото",
        "trade_cnt": 2106,
        "result": 12178781.79,
        "price": 20.35,
    },
    {
        "company": "УК Райфайзен Капитал",
        "ticker": "RCGL",
        "etf_name": "БПИФ Райффайзен - Золото",
        "trade_cnt": 50,
        "result": 981580,
        "price": 1995,
    },
    {
        "company": "УК ВИМ Инвестиции",
        "ticker": "GOLD",
        "etf_name": "БПИФ Золото.Биржевой УК ВИМ",
        "trade_cnt": 84995,
        "result": 42672979.45,
        "price": 1.7,
    },
]
#1 "Отфильтруйте данные и запишите в новый список `moex_filtered` только те элементы, где количество сделок (trade_cnt) больше 1000."
moex_filtered = []
for trade_cnt in moex_lst:
    if trade_cnt["trade_cnt"] > 1000:
        moex_filtered.append(trade_cnt["trade_cnt"])
print(moex_filtered)

#2 "Отсортируйте список `moex_lst` по полю `result` в порядке убывания и запишите отсортированный список в переменную `moex_sorted`."
moex_sorted = sorted(moex_lst, key=lambda x: x["result"],reverse=True)
for result in moex_sorted:
    print(result)
#3 "Определите среднюю цену ETF для всех компаний, у которых количество сделок (trade_cnt) не равно нулю и запишите ее в переменную
# `avg_price`. Результат округлите до копеек."
price = []
for item in moex_lst:
    if item["trade_cnt"]!= 0:
        price.append(item["price"])
if price:
    avg_price = round(sum(price)/len(price), 2)
else:
    avg_price = 0.0
print(f"Средняя цена ETF: {avg_price}")
#4 "Найдите компанию с максимальным значением result и запишите ее название в переменную `best_company`."
best_company = max(moex_lst, key=lambda x :x['result'])
print(f"Компания с наилучшим результатом: {best_company['company']}")
print(f"Результат: {best_company['result']}")
# 5 "Напишите функцию, которая принимает список словарей moex_lst и возвращает новый список,
# содержащий только те элементы, где количество сделок (trade_cnt) больше 1000."

def filter_trade_counts(moex_lst):
    return [item for item in moex_lst if item["trade_cnt"] > 1000]

filter_list = filter_trade_counts(moex_lst)
for item in filter_list:
    print(item)
print(40*"--")
# 6  "Создайте функцию, которая сортирует список moex_lst по полю result в порядке убывания и возвращает отсортированный список."
def sorted_list(moex_lst):
    return sorted(moex_lst, key=lambda x: x["result"],reverse=True)

sorted_list_new = sorted_list(moex_lst)
for item in sorted_list_new:
    print(item)
print(40*"--")
#7"Напишите функцию, которая вычисляет среднюю цену ETF (price) для всех компаний, у которых количество сделок (trade_cnt) не равно нулю."
