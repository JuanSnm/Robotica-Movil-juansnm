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

A nivel teórico hay que tener claro que estamos trabajando es un sistema de navegación local de Campos de Potencial VFF, lo que significa que las deciciones de movimiento del robot se toma a través de la información que recoge el robot del entorno. Este tipo de navegación permite que el robot reaccione en tiempo real ante obstáculos o cambios en el entorno, generando vectores atractivos y repulsivos que determinan su dirección y velocidad, que es justamente en lo que se basa el funcionamiento de nuestro programa.

### Vector Repulsivo 

Nuestro objetivo es obtener una fuerza que repela al robot de los objetos (obstaculos, paredes...) 

Los pasos que hemos seguido para conseguir este resultado son los siguientes: 

1. Hemos obtenido la nube de puntos del láser tanto en coordenadas polares como en coordenadas cartesianas usando la función que hemos explicado antes: `def parse_laser_data(laser_data)`.


2. Cáculo de la distancia mínima a cualquier obstáculo detectado: Que hemos cálculado iterando en la lista `laser_polar`.

  
3. Cáculo de `alpha` y `beta`: esenciales para el funcionamiento de nuestro programa, son factores de ponderación que que determinan la influencia de las fuerzas atractiva y repulsiva en el movimiento del robot. De forma que nuestra fuerza resultante se obtiene de:

```python
Fresultantev = α * Fatractiva + β * Frepulsiva
```
Para calculas ambas variables primero calculamos `t`, que nos dice qué tan libre o bloqueado está el entorno del robot y devuelve un valor entre 0 y 1. Si el obstaculo está muy cerca `t ≈ 0` y si esta lejos `t ≈ 1.` Y finalmente calculamos las variables que nos interesan, de forma que, cuanto más lejos estén los obstáculos, mayor será α, es decir, el robot da más importancia al objetivo. Y cuanto más cerca esté un obstáculo, mayor será β, y por tanto el robot reacciona más intensamente para evitar colisiones.

4. Finalmente calculamos la Fuerza repulsiva 


### Vector Atractivo

Nuestro objetivo es obtener una fuerza que empuje al robot hacia el objetivo de forma que apunte en la dirección correcta, que sea más intensa cuanto más lejos se encuentra el robot del objetivo, que tenga un límite máximo y que nos permita comprobar si hemos alcanzado el objetivo.

Los pasos que hemos seguido para consguir este resultado son los siguientes:


### Cálculo de velocidades 

## Video 



https://github.com/user-attachments/assets/f85c3d38-7b66-4546-98f7-609d3f152e26





