# Actividad Semana 2 - Programación Orientada a Objetos
# Refactorización de transacciones de PE a POO


# 1) Definición de la clase Transaccion
class Transaccion:

    # Constructor
    def __init__(self, id, tipo, monto):
        self.id = id
        self.tipo = tipo
        self.monto = monto

    # Método para obtener la información de la transacción
    def obtener_informacion(self):
        return f"ID: {self.id}, Tipo: {self.tipo}, Monto: {self.monto}"


# 2) Leer el archivo y almacenar objetos Transaccion
def leer_y_almacenar_datos(nombre_archivo):
    lista_transacciones = []

    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            partes = linea.strip().split(",")

            transaccion = Transaccion(
                partes[0],
                partes[1],
                int(partes[2])
            )

            lista_transacciones.append(transaccion)

    return lista_transacciones


# 3) Calcular el valor total de las transacciones
def calcular_valor_total(lista_transacciones):
    total = 0

    for transaccion in lista_transacciones:
        total = total + transaccion.monto

    return total


# 4) Filtrar las transacciones por tipo
def filtrar_por_categoria(lista_transacciones, categoria):
    lista_filtrada = []

    for transaccion in lista_transacciones:
        if transaccion.tipo == categoria:
            lista_filtrada.append(transaccion)

    return lista_filtrada


# 5) Función principal
def ejecutar_sistema():

    # Crear una lista de objetos Transaccion
    transacciones = leer_y_almacenar_datos("transacciones.txt")

    # Calcular el total
    total = calcular_valor_total(transacciones)

    print("Valor total de las transacciones:", total)

    # Filtrar transacciones de tipo COPAGO
    copagos = filtrar_por_categoria(transacciones, "COPAGO")

    print("\nTransacciones de COPAGO:")

    for transaccion in copagos:
        print(transaccion.obtener_informacion())


# Ejecutar el programa
ejecutar_sistema()

