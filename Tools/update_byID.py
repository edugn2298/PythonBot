from Data import *
from Services.update import update

def updatedID():
    
  id = int(input("Id: "))
  name = input("Name: ")
  lastname = input("Lastname: ")
  email = input("Email: ")
  phone = input("Phone: ")

  data = user.User(id, name, lastname, email, phone)
  print(data)
  aux  = {"id": id, "name": name, "lastname": lastname, "email": email, "phone": phone}
  update(aux)