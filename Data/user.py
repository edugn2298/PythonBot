class User:
  def __init__(self, name, lastname, email, phone):
    self.name = name
    self.lastname = lastname
    self.email = email
    self.phone = phone

  def __str__(self):
    return f"name: {self.name}, lastname: {self.lastname}, email: {self.email}, phone: {self.phone}"