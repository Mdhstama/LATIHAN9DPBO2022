from hunian import Hunian


class Indekos(Hunian):
    def __init__(self, nama_pemilik, nama_penghuni, luas_hunian, listrik):
        super().__init__("Indekos")
        self.nama_pemilik = nama_pemilik
        self.nama_penghuni = nama_penghuni
        self.luas_hunian = luas_hunian
        self.listrik = listrik

    def get_dokumen(self):
        return "Bukti kontrak indekos oleh " + self.nama_penghuni + " dari " + self.nama_pemilik + "."

    def get_nama_pemilik(self):
        return self.nama_pemilik

    def get_nama_penghuni(self):
        return self.nama_penghuni

    def get_summary(self):
        return "Hunian Indekos dengan luas hunian (" + str(self.luas_hunian) + " m^2) dan kapasitas listrik sebesar (" + str(self.listrik) + "VA)."
