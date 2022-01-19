class Laptop:
  def __init__(self, nama_merk):
    self.__nama_merk = nama_merk

  def getNama(self):
    return self.__nama_merk

  @staticmethod
  def namaBesar(nama_merk):
    return nama_merk.upper()

class Macbook(Laptop):
  def __init__(self, nama_merk):
    super().__init__(nama_merk)

  def getNama(self):
    return Laptop.namaBesar(super().getNama())

Dell = Laptop('Dell')
print(Dell.getNama())
Macbook_Pro = Macbook('Macbook Pro')
print(Macbook_Pro.getNama())