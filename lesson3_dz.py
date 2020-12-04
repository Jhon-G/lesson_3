'''
lesson 3 task 1
'''
import csv
from datetime import datetime , timedelta

today = datetime.now() # Узнаем текущую дату
yesturday = timedelta(days=1) # разница в датах в 1 день
day_ago = today - yesturday # Узнаем вчерашний день
mounth = timedelta(days=30) # Разница в датах в 30 дней
mounth_ago = today - mounth # Узнаем дату 30 дней назад
print(day_ago.strftime('%d.%m.%Y'))
print(today.strftime('%d.%m.%Y'))
print(mounth_ago.strftime('%d.%m.%Y'))

date_string = '01/01/25 12:10:03.234567'
date_dt = datetime.strptime(date_string,'%d/%m/%y %H:%M:%S.%f') #Задаем формат вывода
print(date_dt)

'''
task 2 referat.txt
'''
with open('referat.txt', 'r', encoding='utf-8') as referat:
    text = referat.read() 
    # Длинна строки при чтении всего файла
    text_len = len(text.replace('\n', ''))
    print('Длинна строки', text_len)
    words = 0
    for word in text.split(): # считаем количество слов в тексте
        if word in text:
            words += 1
    print(words)
    text = text.replace('.', '!')# Заменяем точку на восклицательный знак

with open('referat2.txt', 'w', encoding='utf-8') as referat2:
    referat2.write(f'Длинна строки: {text_len}''\n')
    referat2.write(f'Количество слов: {words}''\n')
    referat2.write(f'Текст после замены:\n{text}')

    '''
    task 3 CSV fails
    '''


user_list = [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
    ]
#Записываем данные словаря в CSV формат
with open('users.csv', 'w', encoding='utf-8') as f:
    fields = ['name', 'age', 'job',]
    writer = csv.DictWriter(f, fields, delimiter=';')
    writer.writeheader()
    for user in user_list:
        writer.writerow(user)