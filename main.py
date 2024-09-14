import sys
from Services.show import show
from Tools import *


las_id = 0

if __name__=="__main__":
  start = True
  while(start):
    swich = int(input("1. Registrar usuario\n2. Eliminar usuario por id\n3. Actualizar usuario por id\n4. Ver usuarios\n5. Salir\n"))
    if swich == 1:
      print("Registrar usuario")
      register.register()
    elif swich == 2:
      print("Eliminar usuario por id")
      delete_byID.deletedID()
    elif swich == 3:
      print("Actualizar usuario por id")
      update_byID.updatedID()
    elif swich == 4:
      print("Ver usuarios")
      show.show()
    elif swich == 5:
      start = False