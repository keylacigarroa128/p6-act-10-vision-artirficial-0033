import numpy as np
import cv2
# Vision Artificial Act 10  NC = 0033
# Lee la imagen en escala de grises
img = cv2.imread("bob esponja.jpg", cv2.IMREAD_GRAYSCALE)

# Abre la ventana con la imagen
cv2.imshow("bob esponja 0033", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Linea
print("La Linea 0033")
# Crea una imagen negra
img = np.zeros((512,512,3), np.uint8)

# Dibuja una diagonal blanca de 3px desde una esquina a la otra
img = cv2.line(img,(0,0),(511,511),(255,255,255),3)

# Abre la ventana con la imagen
cv2.imshow("Line 0033", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# circulos
print("Circulos 0033")
# Dibuja un circulo azul de radio 10px al centro de la imagen
img = cv2.circle(img, (260,260), 10, (255,0,0),-1)
# Abre la ventana con la imagen
cv2.imshow("Circulos 0033", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Texto
print("Texto 0033")
# Añade a la imagen el texto "Example Text" en color blanco
img = cv2.putText(img, "Example Text", (200, 30),cv2.FONT_HERSHEY_SIMPLEX, \
                  0.5, (255, 255, 255), 2)
cv2.imshow("Texto 0033", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Trackbars
print("Trackbars 0033")

# Trackbars
print("Trackbars 0033")
print("Trackbars 0033")

# Cargar imagen
img = cv2.imread("bob esponja.jpg")

if img is None:
    print("No se encontró bob esponja.jpg")
    exit()

# Crear ventana
cv2.namedWindow("Bob Esponja - Trackbars")

def nada(x):
    pass

# Crear Trackbars
cv2.createTrackbar("R", "Bob Esponja - Trackbars", 0, 255, nada)
cv2.createTrackbar("G", "Bob Esponja - Trackbars", 0, 255, nada)
cv2.createTrackbar("B", "Bob Esponja - Trackbars", 0, 255, nada)

while True:

    # Obtener valores
    r = cv2.getTrackbarPos("R", "Bob Esponja - Trackbars")
    g = cv2.getTrackbarPos("G", "Bob Esponja - Trackbars")
    b = cv2.getTrackbarPos("B", "Bob Esponja - Trackbars")

    # Crear una copia de la imagen
    resultado = img.copy()

    # Aplicar color
    resultado[:, :, 0] = np.clip(resultado[:, :, 0] + b, 0, 255)
    resultado[:, :, 1] = np.clip(resultado[:, :, 1] + g, 0, 255)
    resultado[:, :, 2] = np.clip(resultado[:, :, 2] + r, 0, 255)

    cv2.imshow("Bob Esponja - Trackbars", resultado)

    # ESC para salir
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Thresholding
img = cv2.imread('bob esponja.jpg',0)

ret,thr1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thr2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thr3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thr4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thr5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

cv2.imshow('BINARY',thr1)
cv2.imshow('BINARY_INV',thr2)
cv2.imshow('TRUNC',thr3)
cv2.imshow('TOZERO',thr4)
cv2.imshow('TOZERO_INV',thr5)


cv2.waitKey(0)
cv2.destroyAllWindows()

print(" Keyla Paola 0033")