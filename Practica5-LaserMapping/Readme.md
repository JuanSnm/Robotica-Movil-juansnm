# PRACTICA 5

Página de Enunciado: `https://jderobot.github.io/RoboticsAcademy/exercises/MobileRobots/laser_mapping`

Vamos a explicar y entender el funcionamiento de LaserMapping. Donde el objetivo ha sido implemetar un sistema capaz de explorar de manera autónoma un almacén y construir un mapa de ocupación utilizando únicamente:

- Las lecturas del sensor LIDAR

- La pose conocida del robot (mapping with known positions)

- Un comportamiento reactivo de navegación.

El robot debe recorrer el entorno, detectar obstáculos y actualizar continuamente un mapa probabilístico que represente zonas libres, obstáculos y regiones aún no observadas. Para ello hemos aplicado conceptos clave de robótica móvil: sensado, transformaciones geométricas, occupancy grids, log-odds, ray tracing y control reactivo.

## Teoría 

En esta práctica hemo trabajado con uno de los conceptos fundamentales en robótica móvil:

La construcción de un mapa del entorno usando un LIDAR y la pose conocida del robot, también llamado Mapping with Known Positions. La idea principal es que, dado que conocemos la posición del robot en todo momento (idealmente sin error), podemos transformar directamente las medidas del láser en posiciones globales dentro del mapa.

A continuación se explican los componentes teóricos esenciales utilizados:

### Mapa de Ocupación 

El occupancy grid es una representación del entorno mediante una matriz 2D donde cada celda almacena la probabilidad de estar: `Ocupada` (probabilidad alta), `Libre` (probabilidad baja), `Desconocida` (probabilidad ≈ 0.5)

Este modelo es altamente usado porque permite combinar fácilmente información de sensores ruidosos, crece bien con entornos grandes, es fácil de visualizar y procesar y cada celda refleja el conocimiento acumulado sobre el entorno.

### Modelo Probabilístico con Log-Odds

Trabajar con probabilidades directamente puede ser inestable, ya que multiplicar muchas probabilidades pequeñas conduce a errores numéricos. Por eso en esta práctica usamos log-odds:

Podemos encontrar varias ventajas usando log-odds. En primer lugar, las actualizaciones se hacen con sumas en lugar de productos, lo cual es más estable, además, se puede saturar fácilmente en valores máximos y mínimos y por último es la forma estándar de implementar mapas de ocupación modernos.


### Medidas del LIDAR y Transformaciones Geométricas

El LIDAR proporciona 360 mediciones de distancia, cada una asociada a un ángulo concreto respecto al robot.

Para cada rayo: 

1. Coordenadas en el sistema del robot (polares → cartesiano)

2. Transformación al sistema global del mundo

Usando la pose del robot `(xr, yr, yaw)`, obtenemos dónde se encuentra el impacto del rato en el mundo real. 

3. Conversión a píxeles del mapa

El mapa no es continuo sino discreto, así que necesitamos convertir `(xw,yw)` a `(px,py)`. Esto se hace con, un origen colocado en el centro del mapa y un factor de escala (píxeles por metro). 

Esta parte es crucial para que el mapa se construya de forma coherente.

### Ray Tracing 

Un rayo del LIDAR no solo nos da información sobre el obstáculo final, sino que, también nos dice que todo lo que hay entre el robot y el impacto está libre. Por eso debemos recorrer la línea robot → impacto y actualizar cada celda intermedia como espacio libre.

Esto evita que el mapa tenga agujeros o zonas ambiguas.

## Funcionamiento 

Explicar el funcionamiento es basicamente aplicar la teoría que hemos estudianto anteriormente:

El funcionamiento del sistema se basa en transformar las lecturas del LIDAR en un mapa
probabilístico mientras el robot navega de forma reactiva por el entorno.

`1. Lectura del LIDAR`

En cada iteración se obtienen 360 distancias. Cada rayo indica la posición de un posible
obstáculo y se utiliza para actualizar el mapa.

`2.  Movimiento reactivo`

El robot decide si debe avanzar o girar según las distancias frontales del LIDAR.
Esto permite explorar sin chocar.

`3.Actualización del mapa`

El mapa solo se actualiza cuando el robot avanza una distancia suficiente, evitando
procesar datos redundantes.

`4. Transformación de los rayos`

Cada rayo se convierte en:
- coordenadas del robot → coordenadas globales
- coordenadas globales → píxeles del mapa

De este modo, cada medición del láser se ubica en una celda concreta.

`5. Ray tracing`

Las celdas entre el robot y el punto final del rayo se marcan como **libres** y, si hay impacto,
la celda final se marca como **ocupada**.

`6. Log-odds`

Cada celda del mapa se actualiza sumando evidencia de libre u ocupado. Con el tiempo,
la probabilidad converge a un valor estable.

`7. Visualización`

El mapa se convierte a escala de grises (negro = obstáculo, blanco = libre, gris = desconocido)
y se envía a la interfaz usando `WebGUI.setUserMap()`.






## Conclusión 

El sistema implementado cumple con todos los requisitos de la práctica:

- El robot explora el almacén sin colisionar.

- El mapa se reconstruye progresivamente usando la teoría de occupancy grids y log-odds.

- El uso de ray tracing garantiza un mapa limpio sin huecos.

- La conversión entre sistemas de coordenadas está correctamente implementada.

- El mapa final muestra de forma clara paredes, espacios libres y zonas desconocidas.

De esta forma, hemos aprendido todos los conceptos sobre este tipo de mapa robótico y navegación de robots móviles comprendiendo cómo un sensor LIDAR permite reconstruir el entorno, cómo se combinan lecturas sucesivas mediante modelos probabilísticos como los occupancy grids y log-odds, y cómo un comportamiento reactivo básico puede guiar al robot mientras el mapa se actualiza de manera coherente y consistente.

## Video 
[Grabación de pantalla desde 2025-12-10 17-31-32.webm](https://github.com/user-attachments/assets/3711d5af-5236-4527-b73e-565b0995354e)


