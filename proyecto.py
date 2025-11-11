import cv2
import pytesseract
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Leer imagen
image_path = r"C:/Users/alumnomizv/Desktop/auto001.jpg"
image = cv2.imread(image_path)
if image is None:
    print("⚠️ No se pudo cargar la imagen.")
    exit()

# Escala de grises y suavizado
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5,5), 0)

# Detección de bordes
edges = cv2.Canny(gray, 100, 200)
edges = cv2.dilate(edges, None, iterations=1)

# Contornos
cnts, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

texto_final = "NO SE DETECTO"

for c in cnts:
    area = cv2.contourArea(c)
    if area < 2000:  # Ignorar contornos muy pequeños
        continue

    epsilon = 0.02 * cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, epsilon, True)

    x, y, w, h = cv2.boundingRect(approx)
    aspect_ratio = w / h

    # Filtrar posibles placas
    if 2 <= aspect_ratio <= 6 and 0.2*image.shape[1] < w < 0.9*image.shape[1]:
        placa = image[y:y+h, x:x+w]

        # Preprocesamiento OCR
        placa_gray = cv2.cvtColor(placa, cv2.COLOR_BGR2GRAY)
        placa_blur = cv2.bilateralFilter(placa_gray, 11, 17, 17)
        _, placa_thresh = cv2.threshold(placa_blur, 150, 255, cv2.THRESH_BINARY)

        # OCR
        texto = pytesseract.image_to_string(
            placa_thresh,
            config='--psm 8 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        ).strip()

        if texto:
            texto_final = texto
            print("PLACA DETECTADA:", texto_final)

        cv2.rectangle(image, (x, y), (x+w, y+h), (0,255,0), 3)
        cv2.putText(image, texto_final, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0,255,0), 3)
        cv2.imshow("PLACA", placa_thresh)
        break  # solo la primera placa

# Guardar en txt
with open("matricula.txt", "w") as f:
    f.write(texto_final)

print("✅ Matrícula guardada en matricula.txt")

cv2.imshow("Imagen con placa", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
