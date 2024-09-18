from Data import *
from Services.write import write
from Tools.Whastapp import whastapp
import os
import re

def register():
  index_filename = "index.txt"
  if not os.path.exists("index.txt"):
    with open(index_filename, "w") as index_file:
      index_file.write("1")
      new_id = 1
  elif os.path.exists("index.txt"):
    with open(index_filename, "r") as index_file:
      current_index = int(index_file.read())
      new_id = current_index + 1
    with open(index_filename, "w") as index_file:
      index_file.write(str(new_id))

  name = input("Name: ")
  name_re = re.compile(r'^[a-zA-Z]{3,}$')
  while not name_re.match(name):
    print('No ingresaste un nombre valido')
    name = input("Name: ")

  lastname = input("Lastname: ")
  lastname_re = re.compile(r'^[a-zA-Z]{3,}$')
  while not lastname_re.match(lastname):
    lastname = input("Lastname: ")

  email = input("Email: ")
  email_re = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
  while not email_re.match(email):
    email = input("Email: ")
  
  phone = input("Phone: ")
  phone_re = re.compile(r'^\+\d{1,3}\d{9}$')
  while not phone_re.match(phone):
    phone = input("Phone: ")

  data = user.User( name, lastname, email, phone)
  print(data)
  aux  = {"id": new_id, "name": name, "lastname": lastname, "email": email, "phone": phone}
  write(aux)
  whastapp(phone,f"Hello {name} {lastname}, you're welcome in our platform. Your ID: {new_id}") 