# importation du package
from manita import *

# Fonction menu
def menu() :
    print("MENU – Modules & Packages")
    print("=" * 40)
    print("1. Scanner WiFi (Windows)")
    print("2. OCR (image -> texte)")
    print("3. Générateur de QR Code")
    print("4. Raccourcisseur de lien")
    print("5. Compresseur d’image")
    print("0. Quitter")

    choix = input("Votre choix :")
    return choix

# Principal
while True:
    choice = menu()

    if choice == "1" :
        pass
    elif choice == "2" :
        ocr()
    elif choice == "3" :
        pass
    elif choice == "4" :
        raccoucisseur_url()
    elif choice == "5" :
        img_compressor()
    else :
        break