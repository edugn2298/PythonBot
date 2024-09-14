class User:
  def __init__(self, id, name, lastname, email, phone):
    self.id = id
    self.name = name
    self.lastname = lastname
    self.email = email
    self.phone = phone

  def __str__(self):
    return f"id: {self.id}, name: {self.name}, lastname: {self.lastname}, email: {self.email}, phone: {self.phone}"