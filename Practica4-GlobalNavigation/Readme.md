# PRACTICA 4

Página de Enunciado: `https://jderobot.github.io/RoboticsAcademy/exercises/AutonomousCars/global_navigation/`

Vamos a explicar y entender el funcionamiento de GlobalNavigation. En esta práctica se implementa un sistema completo de planificación global y navegación local para un coche autónomo.


El objetivo es que el robot sea capaz de:

1. Recibir un destino seleccionado por el usuario.
2. Calcular en la malla de ocupación (grid) el camino óptimo hasta el destino.
3. Evitar obstáculos (bordes y esquinas) usando penalización de seguridad.
4. Generar un sub-destino local para navegar suavemente evitando mínimos locales.
5. Calcular velocidades lineales y angulares para dirigir el robot hasta la meta.


## Path Planning 

Lo primero es entender que el mapa está divido en una cuadricula donde `1` representa carretera navegable y `0` representa obstáculos. Nuestro objetivo será construir un campo (mapa de costes) donde el destino tendrá coste 0, cada celda trendrá un coste acumulado que indica cuanto cuesta atravesarla y las celdas proximas a los obstáculos tendrán una penalización mayor. Como resultado el robot seguirá el gradiente descendente hacia el destino.

Para conseguir esto hemos definido una serie de funciones que vamos a analizar para entender su funcionamiento: 

`def obstacle_penalty()`

Esta función se encarga de elevar el coste de las celdas que están cerca de los obstáculos. De esta forma evitamos que el robot circule pegado a los muros. Veamos más detenidamente su funcionamiento:

  1. Calcula, para cada celda, a cuántas celdas está del obstáculo más cercano usando `distance_transform_edt`
  2. Si una celda está a una distancia menor o igual que el radio indicado, se le asigna un coste extra
  3. Finalmente devuelve un mapa con la penalización: `penalty_map`

De esta forma conseguimos alejar al robot de los bordes, evitar atascos en giros cerrados y crear un mapa de navegación mucho más seguro.


`def wavefront()`

Esta función implementa un algoritmo de expansión de coste desde el destino. Con ella estamos creando un campo donde el destino tiene coste 0, las celdas cercanas al destino tienen coste bajo, cuanto más lejos estés, mayor será el coste y los obstáculos no se expanden ni tienen coste. De forma que todo esto lo cumplimos mediante un algoritmo tipo Dijkstra, usando una cola de prioridad. Veamos más detenidamente su funcionamiento: 

  1. Coloca el destino en una cola de prioridad con coste 0.
  2. Extrae siempre la celda de menor coste
  3. Expande a sus vecinos con un coste adicional: 1 para vecinos horizontales/verticales y √2 para diagonales 
  4. Ignora las celdas que son obstáculos (valor 0 en el mapa).
  5. Llena la cuadrícula con el valor mínimo necesario para llegar al destino.
  6. Se detiene cuando ha expandido suficientemente cerca del robot (hasta el robot y un poco más).
  7. Devuelve el mapa: `wave_map`

Como esta es una de las funciones más importantes de nuestro programa vamos a resaltar algunos puntos importantes: 

Vamos a estudiarlo a traves de un pseudo código para entenderlo mejor conceptualmente
```python
function wavefront(goal, robot, map):

    # Crear una matriz CAMPO del mismo tamaño que el mapa
    CAMPO = matriz del tamaño de map 
    # El destino tiene coste 0 porque es nuestro punto de partida
    CAMPO[goal] = 0

    # Crear una cola de prioridad (Esta estructura siempre extrae la celda con el coste más pequeño)
    heap = cola de prioridad vacía
    # Insertar la celda de destino con coste 0
    heap.insertar(0, goal)

    # Una vez alcanzamos la celda del robot, guardamos su coste
    nivel_robot = None


    # Bucle principal: ejecutar mientras haya celdas pendientes
        cost, cell = heap.pop_min() # Extraemos la celda con menor coste conocido

        si cost > CAMPO[cell]: # Si esta entrada tiene un coste mayor que el almacenado en CAMPO, significa que es una versión antigua y la ignoramos
            continuar
        si cell == robot: # Si hemos llegado a la celda donde está el robot, guardamos su nivel (coste óptimo hasta esa posición)
            nivel_robot = cost

        # Después de haber visto al robot, no expandimos celdas mucho más caras que su coste + margen
        si nivel_robot existe Y cost > nivel_robot + expandir_extra:
            romper el bucle

        # Para cada vecino válido de la celda actual:

             # Ignorar vecinos fuera del mapa o que sean obstáculos

             # Coste acumulado si llegamos a ncell desde cell

             # Actualizar el coste si encontramos una ruta más barata

    devolver CAMPO


```

De esta forma construimos un campo de gradiente descendente, que atrae al robot hacia su objetivo.

Finalmente debemos combinar los dos campos resultantes para obtener `combined_cost = wave_map + penalty_map` que es un mapa que marca el camino óptimo hacia el destino, penaliza las celdas que se encuentren cerca de los obstáculos, es suave y estable y asegura que el robot navegue por calles estrechas y curvas. 

### Vídeo del funcionamiento 
Finalmente obtenemos este funcionamiento como resultado: 

[PathPlaning.webm](https://github.com/user-attachments/assets/10c0ceff-a426-4f26-9dd0-bf7b30e3f5f6)

## Path Navigation


## Vídeo Funcionamiento FINAL 

https://github.com/user-attachments/assets/503bbb39-c83c-4a72-91ec-eeb4d59bc863








