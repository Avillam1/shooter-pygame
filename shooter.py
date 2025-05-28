from pygame import *
from random import randint

init()
BACKGROUND = "galaxy.jpg"
PLAYER1 = "rocket.png"
PLAYER2 = "ufo.png"
FPS = 60
VICTORY = "victoria.jpg"
DERROTA = "derrota.jpg"
ASTEROIDE = "asteroide.png"
SW, SH = 800, 600
ROSA = 240, 231, 231
init()
#mixer.init()
#mixer.music.load("y2mate.com - Tetris 99  Main Theme (1).mp3")
#mixer.music.play()

window = display.set_mode((SW, SH))
display.set_caption('Los chavalines contra las flipantes aventuras del cohete flipante')
background = transform.scale(image.load(BACKGROUND), (SW, SH))

font.init()
font_score = font.SysFont('Arial', 36)  # Fuente para los contadores
font_win = font.SysFont('Arial', 72)   # Fuente para la pantalla de victoria/derrota
font_lives = font.SysFont('Arial', 72)

clock = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self, img, cor_x, cor_y, ancho, alto, speed=0):
        super().__init__()
        self.width = ancho
        self.heigh = alto
        self.image = transform.scale(image.load(img), (self.width, self.heigh))
        self.rect = self.image.get_rect()
        self.rect.x = cor_x
        self.rect.y = cor_y
        self.speed = speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        llaves = key.get_pressed()
        if llaves[K_d] and self.rect.x < SW - 80:
            self.rect.x += self.speed
        if llaves[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed

    def fire(self):
        bullet = Bullet("bullet.png", self.rect.centerx - 10, self.rect.top, 20, 40, -10)
        bullets.add(bullet)
        #kick = mixer.Sound('Tie Fighter Firing laser (Star wars) - Sound Effect.ogg')
        #kick.play()
class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()

class Enemies(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= SH:
            global enemy_count
            enemy_count += 1
            self.rect.y = -100
            self.rect.x = randint(0, SW - 100)
            self.speed = randint(1, 10)

def reset_game():
    global points, enemy_count, bullets, enemies, finish, life, enemy_hit
    points = 0
    enemy_count = 0
    bullets = sprite.Group()
    enemies = sprite.Group()
    for _ in range(3):  # Reducir número inicial de enemigos
        new_enemy = Enemies(ASTEROIDE, randint(0, SW - 100), -100, 100, 100, randint(1, 10))
        enemies.add(new_enemy)
    finish = False
    life = 3  # Reiniciar vidas
    enemy_hit = False  # Variable para controlar si ya se tocó un enemigo

# Inicializar variables
player = Player(PLAYER1, SW // 2, SH // 1.2, 100, 100, 6)
bullets = sprite.Group()
enemies = sprite.Group()
for _ in range(3):  # Reducir número inicial de enemigos
    new_enemy = Enemies(PLAYER2, randint(0, SW - 100), -100, 100, 100, randint(1, 10))
    enemies.add(new_enemy)
asteroids = sprite.Group()
for i in range(1, 4):
    asteroid = Enemies(ASTEROIDE, randint(0, SW - 100), -100, 100, 100, randint(1, 4))
    asteroids.add(asteroid) 
enemy_count = 0  # Contador de enemigos
points = 0       # Contador de puntos
life = 3         # Número de vidas
finish = False
run = True
game_over = False
enemy_hit = False  # Para evitar que el jugador pierda más de una vida por toque

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        if not finish and e.type == KEYDOWN and e.key == K_SPACE:
            player.fire()
        if game_over and e.type == MOUSEBUTTONDOWN:
            reset_game()
            game_over = False

    if not finish:
        window.fill(ROSA)
        window.blit(background, (0, 0))

        # Mostrar contadores en pantalla
        score_text = font_score.render(f"Enemigos: {enemy_count}", True, (255, 255, 255))
        points_text = font_score.render(f"Puntos: {points}", True, (255, 255, 255))
        life_text = font_lives.render(f"Vidas: {life}", True, (132,220,198))
        window.blit(score_text, (10, 10))
        window.blit(points_text, (10, 40))
        window.blit(life_text, (480, 10))  # Mostrar las vidas

        player.reset()
        player.update()

        bullets.update()
        bullets.draw(window)

        enemies.update()
        enemies.draw(window)
                            
        asteroids.update()
        asteroids.draw(window)

        # Verificar colisiones entre balas y enemigos
        collisions = sprite.groupcollide(enemies, bullets, True, True)
        collisions2 = sprite.spritecollide(player, enemies, False)  # Cambiar a False para no eliminar al enemigo al colisionar

        # Si colisiona con un enemigo, restar vida una sola vez
        if collisions2 and not enemy_hit:
            life -= 1
            enemy_hit = True  # Asegurarse de que solo se resta vida una vez por colisión
        # Reaparecer enemigo solo si hay menos de 3 enemigos en pantalla
        for col in collisions:
            points += 1
            if len(enemies) < 3:
                new_enemy = Enemies(PLAYER2, randint(0, SW - 100), -100, 100, 100, randint(1, 10))
                enemies.add(new_enemy)

        # Resetear enemy_hit cuando el jugador ya no está tocando al enemigo
        if not collisions2:
            enemy_hit = False

        # Verificar condiciones de victoria y derrota
        if points >= 10:
            finish = True
        elif enemy_count >= 5 or life <= 0:
            finish = True
            game_over = True

    else:
        window.fill((0, 0, 0))  # Fondo negro para la pantalla de victoria/derrota
        if points >= 10:
            wins = image.load(VICTORY)
            wins = transform.scale(wins, (SW, SH))
            window.blit(wins, (0, 0))
        elif enemy_count >= 5 or life <= 0:
            derrota = image.load(DERROTA)
            derrota = transform.scale(derrota, (SW, SH))
            window.blit(derrota, (0, 0))

    display.update()
    clock.tick(FPS)

quit()
