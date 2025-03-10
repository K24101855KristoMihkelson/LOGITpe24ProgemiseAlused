from random import randint

kasutaja = int(input("Kui pikk ja lai on põrand"))
kasutajaPikkus = int(input(" kui pikk on põrand"))
kasutajaLaius =int(input("kui lai on põrand"))
põrandaPindala = kasutajaPikkus * kasutajaLaius
print("\n siin on põrandaPindala, see teeb: "+str(kasutajaPikkus)+" cm.")

kasutajaPõrand = int(input("Missuguseid põrandaplaate tahate"))
print("▀▄░░\n░░▀▄")
muster1 = 100
print("║┌─┐\n║└─┘")
muster2 = 200
print("▀▄░░\n░░▀▄")
muster3 = 400
print("░░▀▄\n██░░")
muster4 = 600
print("║┌─┐\n██░░")
muster5 = 900
print("░░▀▄\n░░██")
muster6 = 1100
# ██░░ ║┌─┐ ▀▄░░
# ░░██ ║└─┘ ░░▀▄
kasutajaPõrand = int(input("Millist põrandat soovite 1-6"))
põrandahind = 0

if(kasutajaPõrand == 1):
    põrandahind = muster1
if(kasutajaPõrand == 2):
    põrandahind = muster2
if(kasutajaPõrand == 3):
    põrandahind = muster3
if(kasutajaPõrand == 4):
    põrandahind = muster4
if(kasutajaPõrand == 5):
    põrandahind = muster5
if(kasutajaPõrand == 6):
    põrandahind = muster6
    
mustripindala = põrandaPindala * põrandahind

print("Kas kasutaja maksab või mitte")
    if("jah")
print("Maksan")
else
    print("ei maksa alandan 10 %")
    
print("Kui ei sobi siis alandan 10%")

print("Lõpplik hind")

