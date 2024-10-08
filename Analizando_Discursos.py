import subprocess
import tkinter as tk
import time
import sys

# estamos haciendo el subproceso para analizar discursos, para el caso practico analizaremos
# el discurso de un RAPEROS, politico


#Estructura de actividades: (nombre, [scripts])

#transformar desde el VIDEO
Transfo_Video_Audio = "C:\\Users\\alber\\Documents\\Personal\\Proyecto_Rap_Palabras\\Scripts\\Video_Audio.py"

#Antes de avanzar a la transf a texto hay que dividir el audio
Transfo_Divide_Audio = "C:\\Users\\alber\\Documents\\Personal\\Proyecto_Rap_Palabras\\Scripts\\Divide_Audio.py" 

#transformar desde el TEXTO todo el que encuentre en la carpeta mencionada en la ruta abajo
Transfo_Audio_Texto = "C:\\Users\\alber\\Documents\\Personal\\Proyecto_Rap_Palabras\\Scripts\\Audio_Texto.py"


#Union_Gramatical
union_gramatical = "C:\\Users\\alber\\Documents\\Personal\\Proyecto_Rap_Palabras\\Scripts\\Union_Gramatical.py"

#grafica de barras de toda una conversacion
Graficar_Dialogo = "C:\\Users\\alber\\Documents\\Personal\\Proyecto_Rap_Palabras\\Scripts\\Graficar_Dialogo.py"


#Seguimiento de palabras, Bi_Grama, palabra1 y palabra2
seguimiento_palabras = "C:\\Users\\alber\\Documents\\Personal\\Proyecto_Rap_Palabras\\Scripts\\Seguim_Palabras.py"


#Actividades 
actividades = {

    #TRANSFORMACIONES

    "0-Transfo_Video_Audio": Transfo_Video_Audio,
    "1-Transfo_Divide_Audio": Transfo_Divide_Audio,
    "2-Transfo_Audio_Texto": Transfo_Audio_Texto,
  
    "3-Union_Gramatical": union_gramatical,

    "4-Graficar_Dialogo": Graficar_Dialogo,
    "5-Seguimiento_Palabras": seguimiento_palabras,


    

}




# Índice de la actividad actual
indice_actividad_actual = 0

def avanzar_actividad():
    global indice_actividad_actual
    if indice_actividad_actual < len(actividades) - 1:
        indice_actividad_actual += 1
        actualizar_actividad()

def retroceder_actividad():
    global indice_actividad_actual
    if indice_actividad_actual > 0:
        indice_actividad_actual -= 1
        actualizar_actividad()

def actualizar_actividad():
    nombre_actividad.config(text=list(actividades.keys())[indice_actividad_actual])

def ejecutar_script():
    script = actividades[list(actividades.keys())[indice_actividad_actual]]
    
    subprocess.run(["python", script])  # Pasar el valor como argumento al script

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Analizador de Discursos")
ventana.configure(bg="navy")  # Establecer color de fondo de la ventana
ventana.geometry("600x300")
# Etiqueta para mostrar el nombre de la actividad actual
nombre_actividad = tk.Label(ventana, text=list(actividades.keys())[indice_actividad_actual], font=("Arial", 14), bg="lightgray")
nombre_actividad.pack(pady=20)



# Botón para avanzar entre las actividades
btn_avanzar = tk.Button(ventana, text="Avanzar", command=avanzar_actividad, bg="#006600", fg="white", font=("Arial", 18))
btn_avanzar.config(width=10, height=2)  # Ajustar el tamaño del botón
btn_avanzar.pack(side=tk.RIGHT, padx=10)  # Alineado a la derecha

# Botón para retroceder entre las actividades
btn_retroceder = tk.Button(ventana, text="Retroceder", command=retroceder_actividad, bg="#006600", fg="white", font=("Arial", 18))
btn_retroceder.config(width=10, height=2)  # Ajustar el tamaño del botón
btn_retroceder.pack(side=tk.LEFT, padx=30)  # Alineado a la izquierda


# Botón para ejecutar el script de la actividad actual
btn_ejecutar = tk.Button(ventana, text="Ejecutar Script", command=ejecutar_script, bg="red", fg="white", font=("Arial", 14, "bold"), width=20, height=2)
btn_ejecutar.place(relx=0.5, rely=1.0, anchor=tk.S, y=-20)



# Ejecutar la aplicación
ventana.mainloop()