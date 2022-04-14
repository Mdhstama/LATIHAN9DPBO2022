from apartemen import Apartemen
from rumah import Rumah
from indekos import Indekos
from tkinter import *

hunians = []
hunians.append(Apartemen("Adit", 3, 3, 40, 500))
hunians.append(Rumah("Fahreza", 5, 2, 250, 2200))
hunians.append(Indekos("Nabhan", "Reydi", 35, 400))
hunians.append(Rumah("Fadhil", 1, 4, 175, 1300))

root = Tk()
root.title("2000360 - Muhammad Aditya C1 2020 | Praktikum LP9 DPBO Python")

# ---------- Frame Detail ----------


def details(index):

    # frame detail
    top = Toplevel()
    top.title("Detail Residen" + hunians[index].get_jenis())

    # frame data residem
    d_frame = LabelFrame(top, text="Data Residen", padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)

    # ---------- Data ----------

    # summary
    d_summary = Label(d_frame, text="Summary : " +
                      hunians[index].get_summary(), anchor="w").grid(row=0, column=0, sticky="w")

    # pemilik hunian
    d_pemilik = Label(d_frame, text="Pemilik Hunian : " +
                      hunians[index].get_nama_pemilik(), anchor="w").grid(row=1, column=0, sticky="w")

    # (hunian == indekos, tampilkan penghuni) dan (hunian != indekos, tampilkan jumlah kamar)
    if hunians[index].get_jenis() == "Indekos":
        d_penghuni = Label(d_frame, text="Penghuni : " + hunians[index].get_nama_penghuni(
        ), anchor="w").grid(row=2, column=0, sticky="w")
    else:
        d_jml_kamar = Label(d_frame, text="Jumlah Kamar : " + str(
            hunians[index].get_jml_kamar()), anchor="w").grid(row=2, column=0, sticky="w")

    # luas hunian
    d_luasTanah = Label(d_frame, text="Luas Hunian : " + str(
        hunians[index].get_luas_hunian()) + " m^2", anchor="w").grid(row=3, column=0, sticky="w")

    # luas hunian
    d_listrik = Label(d_frame, text="Kapasitas Listrik : " + str(
        hunians[index].get_listrik()) + "VA", anchor="w").grid(row=4, column=0, sticky="w")

    # dokumen
    d_document = Label(d_frame, text="Dokumen : " +
                       hunians[index].get_dokumen(), anchor="w").grid(row=5, column=0, sticky="w")

    # ---------- Button ----------
    opts = LabelFrame(top, padx=10, pady=10)
    opts.pack(padx=10, pady=10)

    # add data button
    d_exit = Button(opts, text="Add Data", state="disabled")
    d_exit.grid(row=0, column=0)

    # exit button
    d_exit = Button(opts, text="Exit", command=root.quit)
    d_exit.grid(row=0, column=1)


# ---------- Frame Utama ----------
frame = LabelFrame(root, text="Data Seluruh Residen", padx=10, pady=10)
frame.pack(padx=10, pady=10)

# ---------- Button ----------
opts = LabelFrame(root, padx=10, pady=10)
opts.pack(padx=10, pady=10)

# button add
b_add = Button(opts, text="Add Data", state="disabled")
b_add.grid(row=0, column=0)

# button exit
b_exit = Button(opts, text="Exit", command=root.quit)
b_exit.grid(row=0, column=1)

# ---------- Data ----------
for index, h in enumerate(hunians):

    # iterasi nomor
    idx = Label(frame, text=str(index+1), width=5,
                borderwidth=1, relief="solid")
    idx.grid(row=index, column=0)

    # jenis hunian
    type = Label(frame, text=h.get_jenis(), width=15,
                 borderwidth=1, relief="solid")
    type.grid(row=index, column=1)

    # hunian nama pemilik
    if h.get_jenis() != "Indekos":
        name = Label(frame, text=" " + h.get_nama_pemilik(),
                     width=40, borderwidth=1, relief="solid", anchor="w")
        name.grid(row=index, column=2)
    else:
        name = Label(frame, text=" " + h.get_nama_penghuni(),
                     width=40, borderwidth=1, relief="solid", anchor="w")
        name.grid(row=index, column=2)

    # button detail
    b_detail = Button(frame, text="Details ",
                      command=lambda index=index: details(index))
    b_detail.grid(row=index, column=3)

root.mainloop()
