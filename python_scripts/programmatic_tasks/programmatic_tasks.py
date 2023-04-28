import time

import schedule


# Definir una función para la tarea programada
def my_task():
    print("¡Hola, esta es una tarea programada!")


# Programar las tareas usando un bucle for y una lista de tuplas
tasks = [
    (schedule.every(5).minutes, my_task),
    (schedule.every().hour, my_task),
    (schedule.every().day.at("09:00"), my_task)
]

# Ejecutar las tareas programadas indefinidamente en un bucle while
while True:
    for task in tasks:
        task[0].do(task[1])
    schedule.run_pending()
    time.sleep(1)
