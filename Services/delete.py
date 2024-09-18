def delete(id):
  with open("archivo.txt", "r+") as archivo:
    lines = archivo.readlines()
    archivo.seek(0)  
    for line in lines:
      if f'id: {id}' not in line:
        archivo.write(line)  
    archivo.truncate()  