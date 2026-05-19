print("Bienvenido a la tienda de sushi.")

total_productos = 0
pikachu = 0
otaku = 0
pulpo = 0
anguila = 0
subtotal = 0
descuento_total = 0
descuento = 0

while True: 

    print("----- MENÚ DISPONIBLE -----")
    print("1. Pikachu Roll: $4500")
    print("2. Otaku Roll: $5000")
    print("3. Pulpo Venenoso Roll: $5500")
    print("4. Anguila Eléctrica Roll: $4800")
    print("5. Terminar pedido")

    while True:
        try:
            pedido = int(input("Seleccione una opción para agregarlo al pedido: "))
            break
        except ValueError:
            print("Error. Ingrese sólo números enteros positivos del 1 al 5.")

    match pedido:

        case 1:
            print("Has agregado un Pikachu Roll a tu pedido.")
            total_productos = total_productos + 1
            pikachu = pikachu + 1
            subtotal = subtotal + 4500

        case 2:
            print("Has agregado un Otaku Roll a tu pedido.")
            total_productos = total_productos + 1
            otaku = otaku + 1
            subtotal = subtotal + 5000

        case 3:
            print("Has ahregado un Pulpo Venenoso Roll a tu pedido.")
            total_productos = total_productos + 1
            pulpo = pulpo + 1
            subtotal = subtotal + 5500

        case 4:
            print("Has agregado una Anguila Eléctrica Roll a tu pedido.")
            total_productos = total_productos + 1
            anguila = anguila + 1
            subtotal = subtotal + 4800

        case 5:

            descuento_pregunta = input("¿Posee un código de descuento? Si es así, escríbalo a continuación: ").lower()

            while True:
                if descuento_pregunta == "soyotaku":
                    descuento = 0.10
                    break
                elif descuento_pregunta == "x":
                    break
                else:
                    print("Descuento no válido.")
                    descuento_pregunta = input("Intente ingresar nuevamente el código o presione X para volver al menú: ")


            descuento_total = descuento * subtotal
            total = subtotal - descuento_total

            print("******************************")
            print(f"TOTAL PRODUCTOS: {total_productos}")
            print("******************************")
            print(f"Pikachu Roll: {pikachu}.")
            print(f"Otaku Roll: {otaku}.")
            print(f"Pulpo Venenoso Roll: {pulpo}.")
            print(f"Anguila Eléctrica Roll: {anguila}.")
            print("******************************")
            print(f"Subtotal por pagar: ${subtotal}.")
            print(f"Descuento por código: ${descuento_total}.")
            print(f"TOTAL: ${total}.")
            break

        case _:
            print("Error. Debe ingresar una opción del 1 al 5.")
        