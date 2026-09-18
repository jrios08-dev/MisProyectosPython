# procesador_ventas.py
# Actividad 1.2 - Programacion Estructurada (version de clase)
# Lee ventas de un archivo y las procesa con funciones.
# Cada linea de ventas.txt tiene:  ProductoID, Categoria, Valor
# Para ejecutar:  python procesador_ventas.py

# 1) Leer el archivo y guardar las transacciones en una lista de diccionarios
def cargar_transacciones(nombre_archivo):
    lista_transacciones = []

    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            partes = linea.strip().split(",")

            transaccion = {
                "ID": partes[0],
                "Tipo": partes[1],
                "Monto": int(partes[2])
            }

            lista_transacciones.append(transaccion)

    return lista_transacciones


# 2) Sumar el valor de todas las transacciones
def calcular_valor_total(lista_transacciones):
    total = 0

    for transaccion in lista_transacciones:
        total = total + transaccion["Monto"]

    return total


# 3) Dejar solo las transacciones de una categoria
def filtrar_por_categoria(lista_transacciones, categoria):
    lista_filtrada = []

    for transaccion in lista_transacciones:
        if transaccion["Tipo"] == categoria:
            lista_filtrada.append(transaccion)

    return lista_filtrada

# 4) Funcion principal que usa todas las demas
def ejecutar_sistema():
    # CORRECCIÓN: Se especificó la carpeta 'Semana 1/' en la ruta
    transacciones = cargar_transacciones("Semana 1/transacciones.txt")

    total = calcular_valor_total(transacciones)
    print("Valor total de las transacciones:", total)

    copagos = filtrar_por_categoria(transacciones, "COPAGO")
    print("Transacciones de COPAGO:")

    for transaccion in copagos:
        print(transaccion)

# Iniciar el programa
ejecutar_sistema()