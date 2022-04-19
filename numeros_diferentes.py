"""PROGRAMA 7 VERIFICAR SI DOS NUMEROS SON DIFERENTES"""

print("--------------------------")
print("----Numeros diferentes----")
print("--------------------------")

# input
X = int(input("Digite el valor de X: "))
Y = int(input("Digite el valor de Y: "))

# procesing
if X != Y:
    msj = "Son diferentes"
else: 
    msj = "Son iguales"

# output
print("Los numeros " +msj) 