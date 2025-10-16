import WebGUI
import HAL
import Frequency

import cv2
import numpy as np

# PID volante 
kp = 2.5
ki = 0.05
kd = 1.5

prev_err = 0.0
integral = 0.0

#PID acelerador 
kp_v = 2.8
kd_v = 1.5

Vmin = 4
Vmax = 8

v_prev_err = 0.0

while True:
    image = HAL.getImage()
    Height, Width, _ = image.shape

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Rango rojo bajo
    lower_red1 = np.array([0, 100, 100])
    upper_red1 = np.array([10, 255, 255])
    # Rango rojo alto
    lower_red2 = np.array([160, 100, 100])
    upper_red2 = np.array([179, 255, 255])

    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    # Unimos mascaras
    mask = cv2.bitwise_or(mask1, mask2)

    M = cv2.moments(mask)

    WebGUI.showImage(image)

    if M["m00"] > 0:

        cx = M["m10"] / M["m00"] # centro de masa x
        cy = M["m01"] / M["m00"] # centro de masa y 

        # MUESTRA IMAGEN 
        cv2.circle(image, (int(cx), int(cy)), 5, (0,255,0), -1) 
        # (CHATGPT) para ver el punto y se pueda depurar mejor 


        # Implementamos el PID (VOLANTE)
        err = (cx - (Width / 2)) / (Width / 2) 
        integral += err
        d_err = err - prev_err
        
        integral = max(min(integral, 0.5), -0.5)
        
    
        angular_speed = -(kp * err + ki * integral + kd * d_err)

        # Implementramos el P (ACELERADOR)
        d_err_v = err - v_prev_err
        
        
        V = Vmax -(kp_v * abs(err) + kd_v * abs(d_err_v)) 
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