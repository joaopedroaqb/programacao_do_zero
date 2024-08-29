import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Definições da tela e cores
LARGURA = 800
ALTURA = 600
COR_FUNDO = (0, 0, 255)  # Azul
COR_CIRCULO = (255, 255, 255)  # Branco
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Círculo Móvel")

# Propriedades do círculo
x_circulo = LARGURA // 2
y_circulo = ALTURA // 2
velocidade_circulo = 5
raio_circulo = 20

# Configuração do relógio
clock = pygame.time.Clock()

# Loop principal do jogo
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Controle do círculo com setas do teclado
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        x_circulo -= velocidade_circulo
    if teclas[pygame.K_RIGHT]:
        x_circulo += velocidade_circulo
    if teclas[pygame.K_UP]:
        y_circulo -= velocidade_circulo
    if teclas[pygame.K_DOWN]:
        y_circulo += velocidade_circulo

    # Atualização da tela
    tela.fill(COR_FUNDO)
    pygame.draw.circle(tela, COR_CIRCULO, (x_circulo, y_circulo), raio_circulo)
    pygame.display.flip()

    # Controlar o FPS
    clock.tick(60)
