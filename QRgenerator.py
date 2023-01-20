import qrcode, os
from colorama import init, Fore, Back
init(autoreset=True)

os.system("clear")

def _Opcion1():
    os.system("clear")
    _Texto = input(Fore.GREEN + "[#] Ingrese el texto: ")
    _Img = qrcode.make(f"{_Texto}")
    _Crear = open("QrQrQr.png", "wb")
    _Img.save( _Crear )
    _Crear.close()
    print("[!] Codigo QR generdo correctamente!!")
    print(Back.WHITE + Fore.BLACK + "[!] escanee la imagen que se creo con el codigo QR, en la carpeta actual.")
    input(Fore.RED + "[#] Presione enter para volver al menu principal: ")

def _Opcion2():
    print("   ")
    print(Back.GREEN + Fore.BLACK + """[!] El codigo qr se generara y se guardara
en la carpeta del script, trata de no exederte en las frases
con las que quieres generar el codigo, para no crear multiples
archivos .png de los codigos generados, cada vez que se cree
un nuevo codigo QR el script sobreescribira la imagen actual
[QrQrQr.png]""")
    print("  ")
    input(Fore.RED + "[!] Presiona enter para volver al menu principal ")

_Entrar = True

while _Entrar:
    os.system("clear")
    print(Fore.RED + "      ########################")
    print(Fore.RED + "      #──▄────▄▄▄▄▄▄▄────▄───#")
    print(Fore.RED + "      #─▀▀▄─▄█████████▄─▄▀▀──#")
    print(Fore.RED + "      #─────██─▀███▀─██──────#")
    print(Fore.RED + "      #───▄─▀████▀████▀─▄────#")
    print(Fore.RED + "      #─▀█────██▀█▀██────█▀──#")
    print(Fore.RED + "      ########################")

    print(Fore.GREEN + "     .:GeneradorDeCodigos(QR):.")
    print(Fore.GREEN + "")
    print(Fore.GREEN + "        creador: migueJous")
    print(Fore.GREEN + "  github: https://github.com/migueJous")
    print(Fore.GREEN + "")
    print(Fore.GREEN + "[1]", Fore.WHITE + "> Generar QR")
    print(Fore.GREEN + "[2]", Fore.WHITE + "> Mostrar ayuda/descripcion")
    print(Fore.GREEN + "[99]", Fore.WHITE + "> Salir")
    _Seleccion = int(input(Fore.GREEN + "[#] Seleccione una opcion: "))
    if _Seleccion == 1:
        _Opcion1()
    elif _Seleccion == 2:
        _Opcion2()
    elif _Seleccion == 99:
        print(Fore.RED + "[!] Porgrama finalizado...")
        break
    else:
        input(Fore.RED + "[!] Opcion invalida!!, presione enter para volver al menu")
