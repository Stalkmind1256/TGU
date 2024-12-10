# "В переменной library содержится список словарей, каждый словарь - данные о книге.",
#     "`title` - название  ",
#     "`author` - автор  ",
#     "`year` - год издания  ",
#     "`genre` - жанр n",
#     "`ratings` - оценка читателя в виде кортежа  "
from homeWork import total_salary

library = [
    {
        "title": "1984",
        "author": "Джордж Оруэлл",
        "year": 1949,
        "genre": "Дистопия",
        "ratings": (10, 9, 10, 10, 8)
    },
    {
        "title": "Убить пересмешника",
        "author": "Харпер Ли",
        "year": 1960,
        "genre": "Драма",
        "ratings": (8, 9, 8, 7, 9)
    },
    {
        "title": "Гарри Поттер и философский камень",
        "author": "Дж.К. Роулинг",
        "year": 1997,
        "genre": "Фэнтези",
        "ratings": (10, 10, 9, 8, 10)
    },
    {
        "title": "Мастер и Маргарита",
        "author": "Михаил Булгаков",
        "year": 1967,
        "genre": "Роман",
        "ratings": (10, 10, 10, 10, 10)
    },
    {
        "title": "Скотный двор",
        "author": "Джордж Оруэлл",
        "year": 1945,
        "genre": "Аллегория",
        "ratings": (9, 8, 9, 9, 10)
    },
    {
        "title": "Пойди, поставь сторожа",
        "author": "Харпер Ли",
        "year": 2015,
        "genre": "Драма",
        "ratings": (7, 8, 7, 6, 8)
    },
    {
        "title": "Гарри Поттер и тайная комната",
        "author": "Дж.К. Роулинг",
        "year": 1998,
        "genre": "Фэнтези",
        "ratings": (9, 9, 8, 9, 10)
    },
    {
        "title": "Гарри Поттер и узник Азкабана",
        "author": "Дж.К. Роулинг",
        "year": 1999,
        "genre": "Фэнтези",
        "ratings": (10, 10, 9, 10, 10)
    },
    {
        "title": "Собачье сердце",
        "author": "Михаил Булгаков",
        "year": 1925,
        "genre": "Сатира",
        "ratings": (9, 8, 9, 9, 9)
    },
    {
        "title": "Роман о девяти днях",
        "author": "Михаил Булгаков",
        "year": 1926,
        "genre": "Роман",
        "ratings": (8, 7, 8, 8, 9)
    }
]
# 1 "Для каждой книги вычислите среднюю оценку и запишите ее в каждый словарь в виде новой пары ключ-значение (ключ - `avg_rat`)."
for book in library:
    ratings = book["ratings"]
    avg_rating = sum(ratings)/len(ratings)
    book["avg_rat"] = avg_rating

for book in library:
    print(book)
print("-"*40)
#2 "Сформируйте список уникальных авторов `unique_authors`, представленных в library. "
unique_authors = set()
for book in library:
    unique_authors.add(book["author"])
    unique_authors_list = list(unique_authors)

print("Уникальные авторы: ")
for author in unique_authors_list:
    print(author)
print("-"*40)
#3 "Определите наиболее популярную книгу и запишите ее название в переменную popular_book.  "
popular_book = 0
popular_book_title = ""
for book in library:
    rating = book["avg_rat"]
    if rating > popular_book:
        popular_book = rating
        popular_book_title = book["title"]
print(f"Книга с максимальным рейтингом: {popular_book_title}, рейтинг : {popular_book}")
print("-"*40)

#4"В CSV-файле platform.csv находятся данные о продаже компьютерных игр в разрезе платформ за 2013-2016 гг.  "
#"Используя стандартную библиотеку Python, прочитайте файл и запишите его в переменную platforms. В platforms должен быть список словарей. Выведите данные на просмотр.\n",
#"Обратите внимание на параметр delimeter."

#5 "Преобразуйте данные о продажах по годам к числовому типу и выведите platforms."

#6 "Рассчитайте суммарный объем продаж за 2013-2016 гг. для каждой платформы и запишите значение в словарь по ключу total. Выведите данные на просмотр."

#7  "Рассчитайте совокупный объем продаж по всем платформам и запишите его в переменную total_sale."

#8 "Используя стандартную библиотеку Python, запишите обновленные данные platforms в новый файл platform_new.csv"
import csv

path = "platform.csv"

platforms = []

with open(path,mode="r", encoding="utf-8") as csv_file:
    file_reader = csv.reader(csv_file, delimiter="\t")
    headers = next(file_reader)
    for row in file_reader:
        platform_data = {headers[i]: (float(row[i]) if i > 0 else row[i]) for i in range(len(headers))}
        platforms.append(platform_data)
        # print(" ".join(row))
for platform in platforms:
    print(platform)

print("-"*40)

total_sale = 0
for platform in platforms:
    total = sum(platform[year] for year in headers[1:])
    platform['total'] = total
    total_sale += total
    ratio = total_sale/total
    platform['ratio'] = ratio


for platform in platforms:
    print(platform)

print(f"Совокупный объем продаж: {total_sale}")

new_path = "platform_new.csv"

with open(new_path,mode="w", newline='',encoding='utf-8') as csv_file:
    writer = csv.DictWriter(csv_file , fieldnames=platforms[0].keys())
    writer.writeheader()
    writer.writerows(platforms)
print(f"Данные успешно записаны в файл {new_path}")