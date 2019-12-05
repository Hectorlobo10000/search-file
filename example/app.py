import os

route = raw_input("Directory: ")
file = raw_input("File name: ")
fileName = file + ".txt"
list = open(fileName, "w+")
for root, dirs, files in os.walk(route):
  for roots, dirss, filess in os.walk(root):
    for file in filess:
      if file.endswith(".mp3") or file.endswith(".mp4") or file.endswith(".wav") or file.endswith(".wma") or file.endswith(".acc"):
        """ list.write(file + "\n") """
        list.write(roots + "/" + file + "\n")
list.close()