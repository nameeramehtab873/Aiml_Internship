try:
  file = open("config.txt","r")
  print(file.read())
except FileNotFoundError:
 print("Oops!that file doesn't exist here")

