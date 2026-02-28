from kurs import kurs

def konversi(dari, ke, jumlah):
    dari = dari.upper()
    ke = ke.upper()

    if dari == "IDR" and ke in kurs:
        hasil = jumlah / kurs[ke]
        return hasil

    elif dari in kurs and ke == "IDR":
        hasil = jumlah * kurs[dari]
        return hasil

    elif dari in kurs and ke in kurs:
        
        ke_idr = jumlah * kurs[dari]
        hasil = ke_idr / kurs[ke]
        return hasil

    else:
        return None