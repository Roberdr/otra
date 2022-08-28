import pickle

class Vehiculo():
    ruedas = 0
    combustible = None

    def __init__(self, ruedas, combustible) -> None:
        self.ruedas = ruedas
        self.combustible = combustible

    
v1 = Vehiculo(4, 'Gasolina')



f=open('fichero.bin', 'wb')
pickle.dump(v1, f)
f.close()

f=open('fichero.bin', 'rb')
v2=pickle.load(f)
f.close()

print(v2.ruedas)
print(v2.combustible)
