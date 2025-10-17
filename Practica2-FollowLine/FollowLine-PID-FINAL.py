import WebGUI
import HAL
import Frequency

import cv2
import numpy as np

# PID volante (más agresivo, sin perder estabilidad)
kp = 3.5
ki = 0.03
kd = 1.7

prev_err = 0.0
integral = 0.0

# PID acelerador sin integral, ultra agresivo
kp_v = 3.5
kd_v = 0.8  # menos freno por derivada

Vmin = 4
Vmax = 8

v_prev_err = 0.0

while True:
    image = HAL.getImage()
    Height, Width, _ = image.shape

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower_red1 = np.array([0, 100, 100])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([160, 100, 100])
    upper_red2 = np.array([179, 255, 255])

    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = cv2.bitwise_or(mask1, mask2)

    M = cv2.moments(mask)
    WebGUI.showImage(image)

    if M["m00"] > 0:
        cx = M["m10"] / M["m00"]
        cy = M["m01"] / M["m00"]

        cv2.circle(image, (int(cx), int(cy)), 5, (0,255,0), -1)

        # PID volante
        err = (cx - (Width / 2)) / (Width / 2)
        integral += err
        integral = max(min(integral, 0.5), -0.5)
        d_err = err - prev_err
        d_err = max(min(d_err, 1.2), -1.2)  # derivada un poco más permisiva

        angular_speed = -(kp * err + ki * integral + kd * d_err)

        # PID acelerador sin integral, velocidad adaptativa ultra agresiva
        d_err_v = err - v_prev_err
        d_err_v = max(min(d_err_v, 1.2), -1.2)

        # Speed factor más agresivo: casi Vmax incluso con errores moderados
        speed_factor = max(0.0, 1.0 - abs(err)*0.5)  # reduce impacto del error
        V = Vmin + (Vmax - Vmin) * speed_factor - (kd_v * abs(d_err_v))
        V = max(Vmin, min(V, Vmax))

        HAL.setV(V)
        HAL.setW(angular_speed)

        prev_err = err
        v_prev_err = err

    else:
        integral = 0.0
        HAL.setV(1)
        HAL.setW(2)

    Frequency.tick(50)
