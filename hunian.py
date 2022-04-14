class Hunian():
    def __init__(self, jenis, jml_penghuni=1, jml_kamar=1, luas_hunian=0, listrik=400):
        self.jenis = jenis
        self.jml_penghuni = jml_penghuni
        self.jml_kamar = jml_kamar
        self.luas_hunian = luas_hunian
        self.listrik = listrik

    def get_jenis(self):
        return self.jenis

    def get_jml_penghuni(self):
        return self.jml_penghuni

    def get_jml_kamar(self):
        return self.jml_kamar

    def get_luas_hunian(self):
        return self.luas_hunian

    def get_listrik(self):
        return self.listrik

    def get_dokumen(self):
        pass

    def get_summary(self):
        return "Hunian " + self.jenis + ", ditempati oleh " + str(self.jml_penghuni) + " orang dengan luas hunian (" + str(self.luas_hunian) + " m^2) dan kapasitas listrik sebesar (" + str(self.listrik) + " VA)."
