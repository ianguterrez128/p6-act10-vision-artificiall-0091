import numpy as np
import cv2

# Vision Artificial Act10 NC 0091

# Lee la imagen en escala de grises
img = cv2.imread("chevy pop.jpg", cv2.IMREAD_GRAYSCALE)

# Abre la ventana con la imagen
cv2.imshow("chevy pop 0091", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Linea
print("La Linea")

# Crea una imagen negra
img = np.zeros((512, 512, 3), np.uint8)

# Dibuja una diagonal blanca de 3px
img = cv2.line(img, (0, 0), (511, 511), (255, 255, 255), 3)

# Abre la ventana con la imagen
cv2.imshow("Line 0091", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Circulo
print("El Circulo")

# Dibuja un circulo azul de radio 10px
img = cv2.circle(img, (260, 260), 10, (255, 0, 0), -1)

# Abre la ventana con la imagen
cv2.imshow("Circulo 0091", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Texto
print("El texto")

# Añade texto a la imagen
img = cv2.putText(
    img,
    "Example Text",
    (200, 30),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.5,
    (255, 255, 255),
    2
)

# Abre la ventana con la imagen
cv2.imshow("Texto 0091", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Trackbars
print("Trackbars")

def on_trackbar(val):
    print(val)

# Crea una imagen negra
img = np.zeros((300, 512, 3), np.uint8)

# Crea una ventana llamada frame
cv2.namedWindow("frame")

# Crea los Trackbars
cv2.createTrackbar("R", "frame", 0, 255, on_trackbar)
cv2.createTrackbar("G", "frame", 0, 255, on_trackbar)
cv2.createTrackbar("B", "frame", 0, 255, on_trackbar)

while True:

    cv2.imshow("frame", img)

    k = cv2.waitKey(1) & 0xFF

    if k == 27:
        break

    # Obtiene las posiciones de los Trackbars
    r = cv2.getTrackbarPos("R", "frame")
    g = cv2.getTrackbarPos("G", "frame")
    b = cv2.getTrackbarPos("B", "frame")

    img[:] = [b, g, r]

cv2.destroyAllWindows()


# Abre la ventana con la imagen
cv2.imshow("Trackbars 0091", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Thresholding
print("Thresholding")

# Lee la imagen
img = cv2.imread("chevy pop.jpg", 0)

# Thresholding simple
ret, thr1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
ret, thr2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
ret, thr3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
ret, thr4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
ret, thr5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

# Mostrar resultados
cv2.imshow("BINARY 0091", thr1)
cv2.imshow("BINARY_INV 0091", thr2)
cv2.imshow("TRUNC 0091", thr3)
cv2.imshow("TOZERO 0091", thr4)
cv2.imshow("TOZERO_INV 0091", thr5)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("programa realizado por ian gutierrez NC = 0091")