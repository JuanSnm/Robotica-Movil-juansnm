# PRACTICA 2

Página de Enunciado: `https://jderobot.github.io/RoboticsAcademy/exercises/AutonomousCars/follow_line/`

Vamos a explicar y entender el funcionamiento de FollowLine. Donde el objetivo ha sido crear e implementar usa serie de PIDs para permitir el funcionamiento de un robot sigue lineas cuyo objetivo es completar una vuelta en el menor tiempo posible. (seguimos con la idea de sistema reactivo)

## Funcionamiento PIDs (Genérico)

- CONTROLADOR → P

El controlador proporcional responde en proporción al error. Es importante tener en mente que con kp muy baja casi no compensamos el error y de la misma forma con kp muy alta corrige tanto que generamos error en el sentido opuesto.

Formula: `u = -kp * err`

- CONTROLADOR → PD

El controlador derivativo responde de forma proporcional a la derivada (tendencia en el tiempo) del error. En nuestro ejercicio, las derivadas son restas del error en la iteracion actual menos el error en la iteracion enterior. El controlador D actua como un amortiguador, es decir, reduce los picos y las oscilaciones. 

Formula: `u = -(kp * err + kd * d_err )`

- CONTROLADOR → PID

El controlador integrador va a acomular el error en el tiempo (cuanto más tiempo pasa más actua). Si la ganancia ki es demasiado alta, el integrador puede acumular demasiado error, provocando oscilaciones o respuesta lenta. Por eso normalmente se satura o limita el valor de la integral (como veremos más adelante)

Formula: `u = -(kp * err + kd * d_err + ki * integral)`

## Funcionamiento PIDs (Específico)

El codigo se basa en el funcionamiento de dos PIDs que trabajan de forma coordinada para guiar al robot por la linea. El primero de ellos (Direction PID) es el encargado de controlar la dirección del robot, corrigiendo el error lateral entre el centro de la imagen y la posición de la linea detectada. El segundo (Speed PID) se encarga de se encarga de regular la velocidad lineal del robot en función del mismo error.

### Direrction PID

Este PID ajusta la velocidad angular del robot en función del error (desalineación con la línea), la integral (error acumulado) y la derivada (variación del error). Gracias a este controlador, el robot mantiene la línea centrada en su campo de visión y gira de manera suave y estable.

Adjunto la carpeta (Direction-PID) donde se puede observar la implementación y la evolución del código en cuanto al Direction PID. En dicha carpeta aparecen varias soluciones donde se van añadiendo controladores para obtener un resultado final completo:

    Direction-PID/
    ├── FollowLine-P.py
    ├── FollowLine-PD.py
    └── FollowLine-PID.py

   VIDEO 


https://github.com/user-attachments/assets/eda7276b-c614-4f80-a860-4b68de7393e8


### Speed PID

Cuando el error aumenta (al tomar una curva), el controlador reduce la velocidad para evitar salidas de trayectoria, mientras que en zonas rectas (error pequeño) aumenta la velocidad, y de esta forma, el robot adapta dinámicamente su velocidad a las condiciones del recorrido, combinando precisión y rapidez.

Adjunto la carpeta (Speed-PID) donde se puede observar la implementación y la evolución del código en cuanto al Speed PID funcionando junto a Direction PID. En dicha carpeta aparecen varias soluciones donde se van añadiendo controladores para obtener un resultado final completo:

    Speed-PID/
        ├── FollowLine-P.py
        ├── FollowLine-PD.py
        └── FollowLine-PID.py

   VIDEO 

https://github.com/user-attachments/assets/03842e09-dfcc-4f0a-98ce-a11bbd44b107

Es sorprendente observar la diferencia de tiempo con el uso de ambos PIDs en lugar de usar unicamente uno.

## Mejoras 



