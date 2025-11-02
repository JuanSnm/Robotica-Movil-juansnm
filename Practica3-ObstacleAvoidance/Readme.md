# PRACTICA 3

Página de Enunciado: `https://jderobot.github.io/RoboticsAcademy/exercises/AutonomousCars/obstacle_avoidance`

Vamos a explicar y entender el funcionamiento de ObstacleAvoidance. Donde nuestro objetivo ha sido crear un codigo que contiene un bucle principal (además de ciertas funciones) que se repite continuamente hasta que el coche/robot haya visitado todos los puntos de control, esquivando los obstaculos que se encuentre por el camino.

##  Funciones de Unibotics 

El enunciado de la propia práctica nos proporciona una serie de funciones que nos ayudan a comprender y completar el funcionamiento de nuestro robot. Por eso, es importante entender primero como funcionan estos métodos:

1. `def parse_laser_data(laser_data)`

Toma los datos del sensor laser y los transforma en:

#### Lista de coordenadas polares → `laser_polar`: 
Cada elemento dentro de esta lista es una tupla que contiene la distancia y el ángulo (centrado en el frente del robot) a cualquier objeto que esté cerca de él. Ejemplo: `(1.2, 0.0)` → Elemento a 1.2 metros justo delante.

#### Lista de coordenadas cartesianas → `laser_xy`: 
Cada elemento dentro de esta lista es una tupla (x, y) en el sistema de referencia del robot. De forma que, X significa delante e Y izquierda. Ejemplo: `(1.0, 0.0)` → obstáculo a 1 metro delante y a la misma altura del eje del robot.

En definitiva, a través de esta función somos capaces de calcular las fuerzas repulsivas de cada obstáculo.

2. `def absolute2relative (x_abs, y_abs, robotx, roboty, robott)`

Convierte las coordenadas absolutas del mapa en coordenadas relativas al robot.

Encuanto a la entrada, tenemos `(x_abs, y_abs)` que representan la posición del objetivo en el mapa global. De la misma forma, tenemos `(robotx, roboty)` que representan la posición del robot en el mapa. Y por ultimo, `robott` que representa la orientación del robot en radianes.  

En cuanto a la salida, obtenemos `(x_rel, y_rel)` que representan la posición del objetivo en el sistema del robot, que en este caso es X positivo → adelante e Y positivo → izquierda.

En definitiva, a través de esta función somos capaces de calcular las fuerzas atractivas de cada objetivo para el robot.

## Funcionamiento 

### Vector Atractivo

Nuestro objetivo es obtener una fuerza que empuje al robot hacia el objetivo de forma que apunte en la dirección correcta, que sea más intensa cuanto más lejos se encuentra el robot del objetivo, que tenga un límite máximo y que nos permita comprobar si hemos alcanzado el objetivo.

Los pasos que hemos seguido para consguir este resultado son los siguientes:



### Vector Repulsivo 

### Cálculo de velocidades 


