# Crear y escribir en el archivo my_notes.txt
with open('my_notes.txt', 'w') as file:
    # Escribiendo notas personales en el archivo
    file.write("Nota 1: Estudiar para el examen de matemáticas.\n")
    file.write("Nota 2: Comprar víveres para la semana.\n")
    file.write("Nota 3: Llamar a la familia el fin de semana.\n")

# Leer el contenido del archivo my_notes.txt
with open('my_notes.txt', 'r') as file:
    # Leer línea por línea
    for line in file:
        # Mostrar cada línea en la consola
        print(line.strip())  # strip() elimina los espacios en blanco y saltos de línea

# El archivo se cierra automáticamente al salir del bloque with