import cv2
import os

path_servidor = 'Z:/capturas/'


dir_actual = os.path.dirname(os.path.abspath(__file__))
video_name = 'miau.mp4' 
video_path = os.path.join(dir_actual, video_name)

print(f"Intentando abrir video en: {video_path}")

if not os.path.exists(path_servidor):
    print(f"ERROR: La unidad Z: no está accesible.")
    exit()
if not os.path.exists(video_path):
    print(f"ERROR: El archivo de video '{video_name}' no está en {dir_actual}")
    exit()

capture = cv2.VideoCapture(video_path)
cont = 0

if not capture.isOpened():
    print("ERROR: OpenCV no puede procesar el video. Verifica que no esté abierto en otro programa.")
    exit()

fps_actuales = capture.get(cv2.CAP_PROP_FPS)
fps_maximos = 3
intervalo_fps = round(fps_actuales / fps_maximos) if fps_actuales > 0 else 6
lector_fps = 0

print("Procesando... Pulsa 's' para salir.")

while (capture.isOpened()):
    ret, frame = capture.read()
    if (ret == True):
        if lector_fps % intervalo_fps == 0:
            nombre_archivo = f'IMG_{cont:04d}.jpg'
            ruta_final = os.path.join(path_servidor, nombre_archivo)
            
            exito = cv2.imwrite(ruta_final, frame)
            if exito:
                print(f"Guardado frame {cont} en servidor.")
                cont += 1
            else:
                print(f"Error de escritura en Z:. Revisa permisos.")
        
        lector_fps += 1
        if (cv2.waitKey(1) == ord('s')):
            break
    else:
        break

capture.release()
cv2.destroyAllWindows()
print("Tarea finalizada.")