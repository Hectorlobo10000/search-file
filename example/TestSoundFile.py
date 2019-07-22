# coding=utf-8
import audioread
import os
import shutil

""" files = ["/media/lobo/RadioMickyandonie/Hector-18-06-2019-Radio/50's rockabilly - album country, bluegrass and mountain music/Bluegrass/50's rockabilly - album country, bluegrass and mountain music/A Gay Ranchero.mp3"] """
""" files = ["01 Pearl Jam - Once.mp4", "01 Chris Isaack - Wicked Game.wma", "Alvaro Carrillo - Radio Robledo.mp3"] """
files = [
"/media/lobo/RadioMickyandonie/Hector-8-6-2019 mas musica/MUSICA EN ESPAÑOL/Hector-5-7-2019-radio/BOLEROS/Alvaro Carrillo/Alvaro Carrillo - Radio Robledo.mp3", 
"/media/lobo/RadioMickyandonie/Hector-8-6-2019 mas musica/MUSICA EN ESPAÑOL/Hector-5-7-2019-radio/Cumbias/Otras Cumbias/01 Dj Tincho - Tema de la muerte.MP3", 
"/media/lobo/RadioMickyandonie/Hector-8-6-2019 mas musica/MUSICA EN ESPAÑOL/Hector-5-7-2019-radio/Jarabe De Palo Orquesta Reciclando 2009/01 - Dueño De Mi Silencio.mp3",
"/media/lobo/RadioMickyandonie/Hector-8-6-2019 mas musica/MUSICA EN ESPAÑOL/Hector-5-7-2019-radio/BOLEROS/Alvaro Carrillo/Alvaro Carrillo - La Llorona Capinguera.mp3"]

for file in files:
  with audioread.audio_open(file) as f:
    """ print(f.channels, f.samplerate, f.duration) """
    print("duration", f.duration / 60)
    fileSizeKB = round((os.stat(file).st_size / 1024), 2)
    fileSizeMB = round((fileSizeKB / 1024), 2)
    fileSizeGB = round((fileSizeMB / 1024), 10)
    duration = f.duration / 60
    """ if duration > 10:
      destination = "musica-larga/" + file
      shutil.move(file, destination) """
  print(fileSizeGB)