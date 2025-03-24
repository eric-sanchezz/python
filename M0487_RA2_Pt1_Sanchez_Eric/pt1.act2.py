dividend = int(input("Escriu el dividend: "))
divisor = int(input("Escriu el divisor: "))

quocient = dividend // divisor
residu = dividend % divisor

if residu == 0:
    print("La divisió és exacta")
else:
    print("La divisió no és exacta")

print("Quocient:", quocient)
print("Residu:", residu)
