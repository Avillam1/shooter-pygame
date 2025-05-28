# shooter-pygame
# Los chavalines contra las flipantes aventuras del cohete flipante

## Descripción

Este es un juego sencillo desarrollado con Pygame donde controlas un cohete que debe disparar a enemigos (platillos voladores y asteroides) que descienden por la pantalla. El objetivo es eliminar enemigos para ganar puntos mientras evitas que te toquen, ya que cada colisión reduce tus vidas. El juego termina cuando alcanzas 10 puntos (victoria) o cuando pierdes todas las vidas o dejan pasar demasiados enemigos (derrota).

## Controles

- **A**: Mover el cohete hacia la izquierda.
- **D**: Mover el cohete hacia la derecha.
- **Espacio**: Disparar un proyectil.
- **Clic del ratón** (solo tras finalizar el juego): Reiniciar partida.

## Cómo jugar

- Mueve el cohete lateralmente para esquivar enemigos y dispararles.
- Cada enemigo destruido suma un punto.
- Si un enemigo llega al fondo de la pantalla, se incrementa el contador de enemigos que han pasado.
- Pierdes una vida si un enemigo te toca, pero solo se resta una vida por contacto continuo hasta que te separes.
- El juego termina con victoria si alcanzas 10 puntos.
- El juego termina con derrota si pierdes las 3 vidas o si 5 enemigos logran pasar.

## Características técnicas

- El juego está implementado usando la librería Pygame.
- Se utilizan clases que heredan de `pygame.sprite.Sprite` para manejar jugadores, enemigos, balas y asteroides, facilitando la actualización, dibujo y detección de colisiones.
- Se manejan grupos de sprites para organizar y actualizar múltiples objetos simultáneamente.
- El juego incluye imágenes para fondo, jugador, enemigos, balas, asteroides, y pantallas de victoria y derrota.
- El juego corre a 60 FPS para una experiencia fluida.

## Requisitos

- Python 3.x
- Pygame instalado (`pip install pygame`)

## Archivos necesarios

- `galaxy.jpg` (fondo)
- `rocket.png` (jugador)
- `ufo.png` (enemigos)
- `asteroide.png` (asteroides)
- `bullet.png` (proyectil)
- `victoria.jpg` (pantalla de victoria)
- `derrota.jpg` (pantalla de derrota)

## Cómo ejecutar

1. Asegúrate de tener Python 3 y Pygame instalados.
2. Coloca todas las imágenes en el mismo directorio que el script.
3. Ejecuta el script con Python:

python nombre_del_script.py

text

## Expansiones posibles

- Añadir música y efectos de sonido (comentados en el código).
- Incrementar la dificultad con más enemigos o velocidad creciente.
- Añadir más tipos de enemigos con diferentes comportamientos.
- Implementar animaciones y mejoras visuales.

---

Este juego es un proyecto básico para aprender a manejar sprites, grupos, colisiones y eventos en Pygame, ideal para quienes están comenzando en desarrollo de videojuegos con Python.
