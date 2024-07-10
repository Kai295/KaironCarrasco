import random

trabajadores = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", 
                "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez", 
                "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]

sueldos = [0] * len(trabajadores)

def asignar_sueldos_aleatorios():
    global sueldos
    sueldos = [random.randint(300000, 2500000) for _ in range(len(trabajadores))]

def clasificar_sueldos():
    sueldos_ordenados = sorted(sueldos)
    for i, sueldo in enumerate(sueldos_ordenados):
        print(f"{i+1}. {trabajadores[sueldos.index(sueldo)]}: ${sueldo}")

def ver_estadisticas():
    total = sum(sueldos)
    promedio = total / len(trabajadores)
    menor = min(sueldos)
    mayor = max(sueldos)
    
    print(f"Total de sueldos: ${total}")
    print(f"Promedio de sueldos: ${promedio:.2f}")
    print(f"Sueldo mas bajo: ${menor}")
    print(f"Sueldo mas alto: ${mayor}")

def generar_reporte():
    print("Reporte de sueldos:")
    for i in range(len(trabajadores)):
        print(f"{trabajadores[i]}: ${sueldos[i]}")

def main():
    while True:
        print("...............Menu................")
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas")
        print("4. Reporte de sueldos")
        print("5. Salir del programa")
        print("..................................")
        opcion = input("Seleccione una de las siguientes opciones")
        print("..................................")
        if opcion == "1":
            asignar_sueldos_aleatorios()
            print("Sueldos asignados aleatoriamente.")
        elif opcion == "2":
            clasificar_sueldos()
        elif opcion == "3":
            ver_estadisticas()
        elif opcion == "4":
            generar_reporte()
        elif opcion == "5":
            print("Programa Finalizado...")
            print("Desarrollado por Kairon Carrasco")   
            print("RUT:21.897.757-K")   
            break
        else:
            print("Intentelo Denuevo.")

main()

