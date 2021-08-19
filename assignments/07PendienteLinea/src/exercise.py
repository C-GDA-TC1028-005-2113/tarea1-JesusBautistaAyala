def main():
    #escribe tu código abajo de esta línea

    coordenadax1 = float(input("Dame x1: "))
    coordenaday1 = float(input("Dame y1: "))
    coordenadax2 = float(input("Dame x2: "))
    coordenaday2 = float(input("Dame y2: "))
    pendiente = (coordenaday2 - coordenaday1) / (coordenadax2 - coordenadax1)
    print("Pendiente: " + str(pendiente))


if __name__ == '__main__':
    main()
