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

Lo primero es entender que el mapa está divido en una cuadricula donde `1` representa carretera navegable y `0` representa obstáculos. Nuestro objetivo será construir un campo donde el destino tendrá coste 0, cada celda trendrá un coste acumulado que indica cuanto cuesta atravesarla y las celdas proximas a los obstáculos tendrán una penalización mayor. Como resultado el robot seguirá el gradiente descendente hacia el destino.

Para conseguir esto hemos definido una serie de funciones que vamos a analizar para entender su funcionamiento: 

`def obstacle_penalty()`



`def wavefront()`


### Vídeo del funcionamiento 
Finalmente obtenemos este funcionamiento como resultado: 

[PathPlaning.webm](https://github.com/user-attachments/assets/10c0ceff-a426-4f26-9dd0-bf7b30e3f5f6)

## Path Navigation


## Vídeo Funcionamiento FINAL 

https://github.com/user-attachments/assets/503bbb39-c83c-4a72-91ec-eeb4d59bc863






