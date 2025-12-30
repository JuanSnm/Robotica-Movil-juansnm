# PRACTICA 6

Página de Enunciado: `https://jderobot.github.io/RoboticsAcademy/exercises/ComputerVision/marker_visual_loc`

Vamos a explicar y entender el funcionamiento de Marker Based Visual Loc. El objetivo de esta práctica es estimar la posición y orientación (pose) de un robot móvil en un entorno 2D mediante la detección y el análisis de marcadores visuales AprilTag.

Para ello, el robot utiliza una cámara frontal con la que detecta etiquetas colocadas en el entorno cuya posición es conocida previamente. A partir de esta información, se aplica un modelo geométrico y matemático que permite calcular la pose absoluta del robot en el mapa, corrigiendo así las imprecisiones de la odometría.

## Estructura 

Primero es necesario hacer una descripción general. La localización visual se basa en una cadena de transformaciones entre distintos sistemas de referencia:
1. Detección del AprilTag en la imagen usando visión por computador.
2. Estimación de la pose del tag respecto a la cámara mediante el algoritmo PnP (Perspective-n-Point).
3. Transformación de la pose del tag al sistema de referencia del mundo, utilizando la información conocida de cada marcador almacenada en un archivo YAML.
4. Conversión de la pose desde la cámara al robot, teniendo en cuenta la posición y orientación fija de la cámara en el robot.
5. Obtención de la pose final del robot en el mapa, que se visualiza en el entorno.


Ahora si, vamos a ver el desarrollo de la práctica,  que se organiza en los siguientes bloques principales:

1. `Detección de AprilTags`

Se emplea la librería pyapriltags para detectar las etiquetas en la imagen obtenida desde la cámara del robot.

De forma que, para cada detección se obtienen:
- El identificador del tag.
- Las coordenadas de sus esquinas en píxeles.
- El centro del marcador en la imagen.

2. `Modelo de cámara`

Se utiliza un modelo de cámara pinhole simplificado, definido por su matriz intrínseca, que relaciona puntos 3D del mundo con puntos 2D en la imagen.

Los parámetros intrínsecos se calculan a partir del tamaño de la imagen, asumiendo:
- Focal igual al ancho de la imagen.
- Centro óptico situado en el centro de la imagen.
- Sin distorsión radial ni tangencial.

Este modelo es suficiente para la correcta resolución de la práctica.

3. `Estimación de la pose mediante PnP`

Conocidas las coordenadas 3D de las esquinas del AprilTag y las coordenadas 2D correspondientes en la imagen, se aplica el algoritmo Perspective-n-Point (PnP) mediante OpenCV (solvePnP) para estimar la rotación y traslación del marcador respecto a la cámara.

4. `Transformaciones entre sistemas de referencia`

Una de las partes más importantes de la práctica es la correcta gestión de los sistemas de referencia.

Se utilizan transformaciones homogéneas para enlazar:
- Sistema de referencia del tag.
- Sistema de referencia de la cámara.
- Sistema de referencia del robot.
- Sistema de referencia del mundo (mapa).

## Conclusión 

Esta práctica permite comprender de forma profunda cómo se realiza la localización absoluta de un robot mediante visión, combinando conceptos de visión por computador, geometría 3D y robótica móvil.


El uso de marcadores visuales proporciona una referencia global fiable que permite corregir los errores acumulados por la odometría, sentando las bases para sistemas más avanzados de localización y fusión sensorial utilizados en robótica real.

## Video






