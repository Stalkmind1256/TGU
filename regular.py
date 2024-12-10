import re
# compile
# search
# split
# sub
# findall
pattern = re.compile(r'\d+')
text = "На корабле Восток 12 апреля 1961 года летчик-космонавт СССР майор ВСС Юрий Алексеевич Гагарин"
re.search(pattern,text)
print(re.findall(pattern,text))
# pattern = '^[A-ZА-ЯЁ a-zа-яё]+'
# pattern