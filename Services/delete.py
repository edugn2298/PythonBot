def delete(id):
  
  with open("archivo.txt", "r+") as archivo:
    lines = archivo.readlines()
    for index , line in enumerate(lines):
      if f'id: {id}' in line:
        lines[index] = ''
    archivo.seek(0)
    archivo.writelines(lines)