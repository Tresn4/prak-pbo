class dagangan:
  jumlah_barang = 0
  list_barang = []

  def __init__(self, nama, stok, harga):
    self.__nama = nama
    self.__stok = stok
    self.__harga = harga

    dagangan.jumlah_barang += 1
    dagangan.list_barang.append((nama, stok, harga))

  def __del__(self):
    print(f"{self.__nama} dihapus dari toko!")
    print()
    dagangan.jumlah_barang -= 1
    dagangan.list_barang.remove((self.__nama, self.__stok, self.__harga))

  @classmethod
  def lihat_barang(cls):
    print(f"Jumlah barang dagangan pada toko: {cls.jumlah_barang} buah")
    for i, barang in enumerate(cls.list_barang, start=1):
      nama, stok, harga = barang
      print(f"{i}. {nama} seharga Rp {harga} (stok: {stok})")

Dagangan1 = dagangan("Galon Aqua 19L", 32, 17000)
Dagangan2 = dagangan("Gas LPG 5 kg", 22, 88000)
Dagangan3 = dagangan("Beras Ramos 5 kg", 13, 68000)

dagangan.lihat_barang()
print()

del Dagangan1
dagangan.lihat_barang()
print()

del Dagangan2

del Dagangan3