import os

route = raw_input("Ingrese la ruta a escanear: ")
##print(route)
##list = open("list.text", "w+")
##for root, dirs, files in os.walk(route):
##  print root
##  for dir in dirs:
##    list.write(dir + "\n")
##list.close()

list = open("test.text", "w+")
c = 0
for root, dirs, files in os.walk(route, topdown=True, onerror=None, followlinks=True):
  for file in files:
    if file.lower().endswith(".mp3"):
      list.write(file + "\n")
print(c)
list.close()
