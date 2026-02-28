from kurs import kurs
from konverter import konversi
from tabulate import tabulate

def tampilkan_kurs():
    data = []
    for kode, nilai in kurs.items():
        data.append([kode, f"{nilai:,}".replace(",", ".")])

    print("=== KONVERTER MATA UANG ===")
    print(tabulate(data, headers=["Kode", "Kurs"], tablefmt="grid"))

def main():
    tampilkan_kurs()

    dari = input("\nDari (IDR/USD/EUR/CNY/SHP/KWD): ").upper()
    ke = input("Ke   (IDR/USD/EUR/CNY/SHP/KWD): ").upper()
    jumlah = float(input("Jumlah: "))

    hasil = konversi(dari, ke, jumlah)

    if hasil is not None:
        if dari == "IDR":
            print(f"\nRp {jumlah:,.0f} = {hasil:,.2f} {ke}".replace(",", "."))
        elif ke == "IDR":
            print(f"\n{jumlah:,.2f} {dari} = Rp {hasil:,.0f}".replace(",", "."))
        else:
            print(f"\n{jumlah:,.2f} {dari} = {hasil:,.2f} {ke}".replace(",", "."))
    else:
        print("Kode mata uang tidak valid!")

if __name__ == "__main__":
    main()
