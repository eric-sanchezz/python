def esTraspas(any):
    return (any % 4 == 0 and any % 100 != 0) or (any % 400 == 0)

anys = [1900, 2000, 2016, 1987]
for any in anys:
    print(f"{any}: {'Traspàs' if esTraspas(any) else 'Comú'}")
