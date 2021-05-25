#! python
# -*- coding: utf-8 -*-

"""Скрипт-сканер директории.

Сканируем директорию MY_PATH и вложенные в неё каталоги,
возвращает имена всех файлов если они оканчиваются на .pdf.
Записывает всю информацию (имена файлов) в MS Excel.
"""
import os

# pip install XlsxWriter
import xlsxwriter

MY_PATH = ''

# Создаём дерево (объект-генератор) функции walk()
tree = os.walk(MY_PATH)

# Удаляем старый файл если он существует
if os.path.isfile('dir_scanner_files.xlsx'):
    print('Удаляем старый файл...')
    os.remove('dir_scanner_files.xlsx')

# Создаём новый файл Excel и добавляем лист.
workbook = xlsxwriter.Workbook('dir_scanner_files.xlsx')
worksheet = workbook.add_worksheet()

# Добавляем жирный шрифт для подсветки
bold = workbook.add_format({'bold': True})

# Готовим шапку таблицы
worksheet.set_column('B:B', 50)
worksheet.write('A1', 'Год', bold)
worksheet.write('B1', 'Наименование', bold)

# счётчики для установки позиций
cnt_i = 1

# записываем вывод скрипта в файл
for root, dirs, files in tree:
    for filename in files:
        if filename[-4:] == '.pdf':
            year, name = root[-4:], filename[:-4]
            worksheet.write(cnt_i, 0, year)
            worksheet.write(cnt_i, 1, name)
            cnt_i += 1

workbook.close()
