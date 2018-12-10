import json
from prettytable import PrettyTable

Book ='Book.json'

def read_file(Book):
  try:
        file_book = open(Book, 'r') 
        data = json.loads(file_book.read())
  except FileNotFoundError:
        print ("Ошибка! Файл не найден!")

  with open(Book, 'r') as f:
     data = json.loads(f.read())

  name = []
  surname = []
  for i in range(len(data["Partisipants"])):
    name.append(data["Partisipants"][i]["Name"])
    surname.append(data["Partisipants"][i]["Surname"])
  
  x = PrettyTable()
  column_names = ['Name', 'Surname']
  x.add_column(column_names[0], name)
  x.add_column(column_names[1], surname)
  print(x)
  return len(data["Partisipants"]) 

read_file('Book.json')
