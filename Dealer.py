def chatbot():
    print("Selamat datang di Dealer Sepeda Motor!")
    print("Apakah Anda mencari motor dari merek Yamaha, Honda, atau Kawasaki?")

    while True:
        # Pilih merek
        brand = input("Masukkan merek pilihan Anda (Yamaha/Honda/Kawasaki) atau ketik 'exit' untuk keluar: ").lower()
        
        if brand == "exit":
            print("Terima kasih telah menggunakan chatbot kami. Sampai jumpa! semoga segera mendapatkan motor impian anda!")
            break

        if brand not in ["yamaha", "honda", "kawasaki"]:
            print("Merek tidak valid. Silakan coba lagi sesuai pilihan yang ada.")
            continue

        # Pilih segmen
        print(f"\nApakah Anda tertarik dengan segmen Scooter, Manual, atau Sport untuk {brand.capitalize()}?")
        segment = input("Masukkan segmen pilihan Anda (Scooter/Manual/Sport): ").lower()

        if segment not in ["scooter", "manual", "sport"]:
            print("Segmen tidak valid. Silakan coba lagi.")
            continue

        # Pilihan motor
        if brand == "honda":
            if segment == "scooter":
                print("\nApakah Anda tertarik dengan motor scooter di kelas 150cc atau 115cc?")
                cc = input("Masukkan kelas cc pilihan Anda (150/115): ")
                if cc == "150":
                    print("Pilihan: PCX 150cc, Vario 150cc, ADV 150cc")
                elif cc == "115":
                    print("Pilihan: Genio, Beat, Scoopy, Stylo")
                else:
                    print("Kelas cc tidak valid.")
            elif segment == "manual":
                print("Pilihan: Vega Force, Jupiter Z1")
            elif segment == "sport":
                print("\nApakah Anda tertarik dengan motor sport di kelas 150cc atau 250cc?")
                cc = input("Masukkan kelas cc pilihan Anda (150/250): ")
                if cc == "150":
                    print("Pilihan: CBR150R, CRF150L")
                elif cc == "250":
                    print("Pilihan: CBR250RR, CRF250R")
                else:
                    print("Kelas untuk cc tersebut tidak valid.")
        
        elif brand == "yamaha":
            if segment == "scooter":
                print("Pilihan: Fazzio, Mio M3, Lexi, Nmax, Aerox")
            elif segment == "manual":
                print("Pilihan: Vega Force, Jupiter Z1")
            elif segment == "sport":
                print("\nApakah Anda tertarik dengan motor sport di kelas 150cc atau 250cc?")
                cc = input("Masukkan kelas untuk cc motor pilihan Anda (150/250): ")
                if cc == "150":
                    print("Pilihan: R15 V4, MT 15")
                elif cc == "250":
                    print("Pilihan: R25")
                else:
                    print("Kelas untuk cc tersebut tidak valid.")
        
        elif brand == "kawasaki":
            if segment == "scooter":
                print("Kawasaki tidak memiliki pilihan scooter.")
            elif segment == "manual":
                print("Pilihan: Kawasaki Kaze ZX 125")
            elif segment == "sport":
                print("\nApakah Anda tertarik dengan motor sport di kelas 150cc atau 250cc?")
                cc = input("Masukkan kelas cc pilihan Anda (150/250): ")
                if cc == "150":
                    print("Pilihan: Kawasaki Ninja 150")
                elif cc == "250":
                    print("Pilihan: Ninja 250, Z250, ZX250RR")
                else:
                    print("Kelas cc tidak valid.")
        
        print("\nKembali ke menu utama...\n")
        
        


# Jalankan chatbot
chatbot()