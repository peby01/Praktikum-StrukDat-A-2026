class Person:
  def __init__(self, nama, jenisKelamin, umur):
    self.name = nama
    self.gender = jenisKelamin
    self.age = umur

class Karyawan(Person):
  def __init__(self, nama, jeniskelamin, umur, gaji):
    super().__init__(nama, jeniskelamin, umur, gaji)
    self.name = nama
    self._gaji = 1000000
    
  def get_gaji(self):
    return self._gaji
  
  def set_gaji(self, gaji):
    if 0 <= gaji <= 1000000:
      self._gaji = gaji
    else:
      print("gaji tidak valid")

class Rekening:
    def __init__(self, norek, pin):
        self.no_rekening = norek
        self.__pin = pin  

    def get_pin(self):
        return self.__pin

    def set_pin(self, pin_baru):
        self.__pin = pin_baru    

person1 = Person("minghao", "Laki-laki", 28)
karyawan1 = Karyawan("chaeby", "Perempuan", 20, 5000000)
rekening1 = Rekening("10040797", "20040102")