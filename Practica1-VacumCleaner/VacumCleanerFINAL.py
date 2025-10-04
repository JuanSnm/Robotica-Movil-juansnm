import WebGUI
import HAL
import Frequency
import random
import math

EST_1 = 0
EST_2 = 1
EST_3 = 2    
state = EST_1

vel = 0.5
iterations_count = 0
iterations_for_angle = 0
bumper_hit = False
turn_direction = 1

while True:

    if HAL.getBumperData().state:
        bumper_hit = True

    
    match state:
        case 0:
            # AVANZAR en espiral
            HAL.setV(vel)
            HAL.setW(0.8)
            vel += 0.00025

            if bumper_hit:
                state = EST_2 
                bumper_hit = False
                vel = 0.5
                iterations_count = 0
        
        case 1:
            # RETROCEDER
            HAL.setV(-0.4) 
            HAL.setW(0.0)
            iterations_count += 1
            if iterations_count > 150:
                state = EST_3
                iterations_count = 0

                # calculamos angulo aleatorio y num de iteraciones para girar
                angle = random.uniform(0, 2 * math.pi)
                iterations_for_angle = int(angle / 0.8 * 50)
            
                if random.random() > 0.5:
                    turn_direction = 1
                else:
                    turn_direction = -1

        case 2: 
            # GIRAR aleatoriamente 
            HAL.setV(0.0) 
            HAL.setW(turn_direction * 0.8)

            iterations_count += 1

            if iterations_count >= iterations_for_angle:
                state = EST_1
                iterations_count = 0

    Frequency.tick(50)

    # En cada iteración pasan 0.02s (t = 1/freq = 1/50 = 0.02)
    # De esta forma t = iteraciones * 1/Freq

    # Usamos la ecuacion θ(angulo girado) = w(vel angular) * t
    # Ponemos que t  = iteraciones * 1/Freq, y despejamos el num de iteraciones

    # iteraciones = (θ / w) * freq