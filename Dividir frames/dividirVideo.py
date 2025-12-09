import cv2

capture = cv2.VideoCapture('./video/miau.mp4')
path = './frames/'
cont = 0

fps_actuales = capture.get(cv2.CAP_PROP_FPS)
fps_maximos = 3

if fps_actuales > 0:
    intervalo_fps = round(fps_actuales / fps_maximos)
else:
    intervalo_fps = 6

lector_fps = 0


while (capture.isOpened()):
    ret, frame = capture.read()
    if (ret == True):
        if lector_fps % intervalo_fps == 0:
            cv2.imwrite(path + 'IMG_%04d.jpg' % cont, frame)
            cont += 1
        lector_fps += 1
        if (cv2.waitKey(1) == ord ('s')):
            break
    else:
        break
capture.release()
cv2.destroyAllWindows()