from Data import *
from Services.write import write

def register():
  id = int(input("Id: "))
  name = input("Name: ")
  lastname = input("Lastname: ")
  email = input("Email: ")
  phone = input("Phone: ")

  data = user.User(id, name, lastname, email, phone)
  print(data)
  aux  = {"id": id, "name": name, "lastname": lastname, "email": email, "phone": phone}
  write(aux)