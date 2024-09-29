import os
import speech_recognition as sr
from tkinter import filedialog

def select_folder():
    folder = filedialog.askdirectory()
    if not folder:
        print("No se seleccionó ninguna carpeta.")
        exit()
    return folder

def get_output_filename():
    output_filename = input("Ingrese el nombre del archivo de salida (sin extensión): ")
    output_path = os.path.join(
        'C:\\Users\\alber\\Documents\\Personal\\Proyecto_Rap_Palabras\\TXT\\transcripciones\\',
        output_filename + '.txt'
    )
    if os.path.exists(output_path):
        print(f"El archivo {output_path} ya existe. Por favor, elige otro nombre.")
        exit()
    return output_path

def transcribe_audio(recognizer, audio_path):
    try:
        with sr.AudioFile(audio_path) as source:
            audio = recognizer.record(source)
        transcription = recognizer.recognize_google(audio, language="es-ES")
        return transcription
    except sr.UnknownValueError:
        print(f"No se pudo entender el audio en {audio_path}")
    except sr.RequestError as e:
        print(f"Error en la solicitud para {audio_path}: {e}")
    return None

def main():
    selected_folder = select_folder()
    output_path = get_output_filename()
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 4000

    for filename in os.listdir(selected_folder):
        if filename.endswith(('.wav', '.mp3', '.ogg', '.flac')):
            audio_path = os.path.join(selected_folder, filename)
            transcription = transcribe_audio(recognizer, audio_path)
            if transcription:
                with open(output_path, 'a', encoding='utf-8') as f:
                    f.write(f'{transcription}\n')

    print("Proceso completado.")

if __name__ == "__main__":
    main()
