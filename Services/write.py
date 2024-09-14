import os
def write(value):

  archivo = open("archivo.txt", "a")
  archivo.write(f"id: {value["id"]}, name: {value["name"]}, lastname: {value["lastname"]}, email: {value["email"]}, phone: {value["phone"]}\n")
  archivo.close()
