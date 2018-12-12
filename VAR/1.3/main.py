import csv
from prettytable import PrettyTable 
from contextlib import contextmanager

@contextmanager
def openfile(file):
    try:
        data = open(file, 'r')
        yield data
    except OSError:
        print("Ошибка")
        exit(0)
 
def readfile(f):
    x = PrettyTable()
    read = csv.reader(f)
    x.field_names = next(read)
    for row in read:
        a =[]
        for item in row:
          a.append(item)
        x.add_row(a)
    print(x)
    with open('titanic.txt', 'w') as f:
      f.write(x.get_string())

if __name__ == "__main__":
  with openfile('titanic.csv') as f_obj:
        readfile(f_obj)
