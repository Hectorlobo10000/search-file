# coding=utf-8
import os
import audioread
import shutil

def Main():
  data = getData()
  getDataFiles(data["directory"], data["filename"], data["destination"])

def getData():
  directory = raw_input("Directory: ")
  filename =  raw_input("Filename: ")
  destination = raw_input("destination (Esta carpeta debe estar previamente creada en la misma direccion): ")
  dest = "/" + destination + "/"
  return {
    "directory": directory,
    "filename": filename,
    "destination": dest
  }

def getFileSize(pathFile):
  fileSizeKB = round((os.stat(pathFile).st_size / 1024), 2)
  fileSizeMB = round((fileSizeKB / 1024), 2)
  fileSizeGB = round((fileSizeMB / 1024), 10)
  return fileSizeGB

def moveLargeFile(pathFile, duration, destination):
  if duration > 10:
    shutil.move(pathFile, destination)
    print("File moved")
    return True
  else:
    return False

def getDuration(duration):
  minutes = round((duration / 60), 2)
  hours = round((minutes / 60), 2)
  days = round((hours / 24), 2)
  return days

def getDataFiles(directory, filename, destination):
  totalSeconds = 0
  totalSizeGB = 0
  totalDurationDays = 0
  fileSize = 0
  fileDuration = 0
  totalFiles = 0
  list = open(filename + ".txt", "w+")
  for root, dirs, files in os.walk(directory):
    """ for roots, dirss, filess in os.walk(root): """
    for file in files:
      if file.lower().endswith(".mp3") or file.endswith(".mp4") or file.endswith(".wav") or file.endswith(".wma") or file.endswith(".acc"):
        """ or file.endswith(".mp4") or file.endswith(".wav") or file.endswith(".wma") or file.endswith(".acc") """
        pathFile = root + "/" + file
        if not "Musica-Larga" in pathFile:
          try:
            with audioread.audio_open(pathFile) as f:
              totalFiles = totalFiles + 1
              print(totalFiles)
              """ tamano en total en gb """
              fileSize = getFileSize(pathFile)
              totalSizeGB += fileSize

              """ duracion del archivo """
              fileDuration = f.duration

              """ mover archivos grandes """
              dest = directory + destination + file
              if moveLargeFile(pathFile, round((fileDuration / 60), 2), dest):
                text = file + " --- " + str(round((fileDuration / 60), 2)) + " --- " + str(fileSize) + " --- FILE MOVED" + "\n"
              else:
                text = file + " --- " + str(round((fileDuration / 60), 2)) + " --- " + str(fileSize) + "\n"
              """ impresion """
              list.write(root + " --- " + text)
              totalSeconds += f.duration
          except Exception as e:
            print(e)
            list.write(root + " --- " + file + " --- ERROR DE ARCHIVO" + "\n")
  totalDurationDays = getDuration(totalSeconds)
  list.write("\n")
  list.write("Total seconds: " + str(totalSeconds) + "\n")
  list.write("Total days: " + str(totalDurationDays) + "\n")
  list.write("Total GB: " + str(totalSizeGB) + "\n")
  list.write("Total files: " + str(totalFiles) + "\n")
  list.close()
  print("Total seconds: ", totalSeconds)
  print("Total days: ", totalDurationDays)
  print("Total GB: ", totalSizeGB)
  print("Finished")

Main()