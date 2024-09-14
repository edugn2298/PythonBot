def update(value):
  
  with open("archivo.txt", "r+") as archivo:
    lines = archivo.readlines()
    for index , line in enumerate(lines):
      if f'id: {value["id"]}' in line:
        lines[index] = f"id: {value["id"]}, name: {value['name']}, lastname: {value['lastname']}, email: {value['email']}, phone: {value['phone']}\n"

    archivo.seek(0)
    archivo.writelines(lines)