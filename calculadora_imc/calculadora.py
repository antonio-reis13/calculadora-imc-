altura=float(input("digite sua altura"))
print(altura)
peso=float(input("digite seu peso"))
print(peso)
IMC=peso/(altura**2)
print(IMC)

if(IMC<18):
    print("abaixo da media")
if(IMC>18 and IMC<24):
    print("normal")
if(IMC>25 and IMC<29):
    print("sobre")
if(IMC>30 and IMC<34):
    print("obeso")
if(IMC>35 and IMC<39):
    print("obeso t2")
if(IMC>40):
    print("obeso t3")