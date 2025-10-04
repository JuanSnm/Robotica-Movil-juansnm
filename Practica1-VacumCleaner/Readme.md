# PRACTICA 1

Página de Enunciado: `https://jderobot.github.io/RoboticsAcademy/exercises/MobileRobots/vacuum_cleaner)`

Vamos a explicar y entender el funcionamiento de VacumCleaner. Donde nuestro objetivo ha sido crear un codigo reactivo (permitiendo que las aplicaciones reaccionen en tiempo real a los cambios en los datos en lugar de esperar a que estos ocurran) que funcione por iteraciones.

## Funcionamiento 

El código dispone de tres estados. Por cada iteración (1 iteración = 1 ejecución completa del bloque de código que está dentro del bucle while) solo podremos acceder a uno de los tres estados, y como estamos usando una Frequency.tick(50), es decir, una frecuencia de 50 Hz, cada bucle while durará `1 / freq = 0.02 s`. De esta forma podemos saber que nuestro tiempo de respuesta es de 20 ms ante cambios y perturbaciones.

Veamos como funciona cada estado: 

1. AVANZAR (en forma de espiral)

2. RETROCEDER

3. GIRAR (aleatoriamente)

El movimiento es sencillo, unicamente establecemos la velocidad lineal a 0 `HAL.setV(0.0)` y establecemos una velocidad angular para que rote sobre si mismo `HAL.setW(0.8) `.

En este estado lo complejo viene a la hora de cómo determinar el ángulo aleatorio y como llegar hasta él. Veamos primero como lo he solucionado yo y luego otras posibles opciones:

En mi caso el angulo aleatorio lo calculamos en el estado de RETROCEDER ya que de esta forma aumentamos la reactividad, evitamos calcular ángulos innecesariamente y mantiene la lógica separada y simple. Además, usa el tiempo de retroceso para preparar el siguiente movimiento: 
```python
while True:

    match state:
        case 0:
            # AVANZAR en espiral
            if bumper_hit:
                # Cambio de estado 
        
        case 1:
            # RETROCEDER
            if iterations_count > 150:
                # calculamos angulo aleatorio y num de iteraciones para girar
                # Cambio de estado

        case 2: 
            # GIRAR aleatoriamente 
            if iterations_count >= iterations_for_angle:
                # Cambio de estado

    Frequency.tick(50)
```
Como ya sabemos en cada iteración pasan 0.02s. De esta forma el tiempo total para una acción `t = iteraciones * 1/Freq`. Por lo que usando la ecuacion `θ(angulo girado) = w(vel angular) * t`
y aplicando la ecuacion del tiempo total para una acción que hemos definido antes, despejamos el número de iteraciones que son necesarias para alcanzar el ángulo deseado finalmente obtejemos: `iteraciones = (θ / w) * freq`. De esta forma, conociendo el número de iteraciones necesarias para alcanzar el ángulo deseado, aplicamos lo visto anteriormente en el estado de RETROCEDER.
