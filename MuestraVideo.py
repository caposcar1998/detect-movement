import cv2
import time

# Nombre del video y caracteristicas
archivo = "walking.mp4"
ancho = 722
largo = 406

f = 0

video = cv2.VideoCapture(archivo)

fps= int(video.get(cv2.CAP_PROP_FPS))

while video.isOpened():
    ret,imagen = video.read()  # lee cada imagen del video
    #regresa una bandera de status y la imagen del video 
    if ret: #mientras la bandera sea valida se devuelve el cuadro
        cv2.putText(imagen,str(f),(ancho-100,largo-50),cv2.FONT_HERSHEY_PLAIN,2,(255,255,255))
        cv2.imshow('Video', imagen)  #Muestra el fotograma
        time.sleep(1/fps)
        if cv2.waitKey(1) == ord('q'): # Termina cuando se apriete q
            break
        f += 1
    else:
        video.release()
        break

cv2.destroyAllWindows()