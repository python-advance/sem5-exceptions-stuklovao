import json
from prettytable import PrettyTable

Book ='Book.json'

def read(Book):
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

def assert_func_file(read):
  try:
       name = open(read, 'r') 
       data = json.loads(name.read())
       return True
  except FileNotFoundError:
       return False  

def call_func():
    read_file = 'Book.json'
    print(read(read_file))
    print(assert_func_file(read_file))
    assert assert_func_file('Book.json')== True 
    assert assert_func_file('Book2.json')== False

if __name__ == "__main__":
   call_func()
