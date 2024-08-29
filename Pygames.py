import pygame
import sys

# Inicializando o Pygame
pygame.init()

# Definindo as cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)

# Configurações da tela
LARGURA = 800
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Mini Pong")

# Configurações do jogador
largura_raquete = 100
altura_raquete = 10
raquete_x = (LARGURA - largura_raquete) / 2
raquete_y = ALTURA - 40
velocidade_raquete = 10

# Configurações da bola
raio_bola = 10
bola_x = LARGURA / 2
bola_y = ALTURA / 2
velocidade_bola_x = 4
velocidade_bola_y = 4

# Configurações do botão de início
botao_inicio = pygame.Rect((LARGURA / 2 - 100, ALTURA / 2 - 25), (200, 50))
fonte = pygame.font.Font(None, 36)
texto_botao_inicio = fonte.render("Iniciar Jogo", True, BRANCO)

# Configurações do relógio
clock = pygame.time.Clock()
jogo_iniciado = False

# Função para desenhar a raquete
def desenhar_raquete(x, y):
    pygame.draw.rect(tela, BRANCO, (x, y, largura_raquete, altura_raquete))

# Função para desenhar a bola
def desenhar_bola(x, y):
    pygame.draw.circle(tela, BRANCO, (x, y), raio_bola)

# Função para desenhar o botão de início
def desenhar_botao_inicio():
    pygame.draw.rect(tela, VERDE, botao_inicio)
    tela.blit(texto_botao_inicio, (LARGURA / 2 - 80, ALTURA / 2 - 20))

# Loop principal do jogo
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Verificar clique no botão de início
        if evento.type == pygame.MOUSEBUTTONDOWN:
            pos_mouse = pygame.mouse.get_pos()
            if botao_inicio.collidepoint(pos_mouse):
                jogo_iniciado = True

    if jogo_iniciado:
        # Movimentação da raquete com as setas do teclado
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and raquete_x > 0:
            raquete_x -= velocidade_raquete
        if teclas[pygame.K_RIGHT] and raquete_x < LARGURA - largura_raquete:
            raquete_x += velocidade_raquete

        # Movimentação da bola
        bola_x += velocidade_bola_x
        bola_y += velocidade_bola_y

        # Colisão da bola com as bordas
        if bola_x - raio_bola <= 0 or bola_x + raio_bola >= LARGURA:
            velocidade_bola_x = -velocidade_bola_x
        if bola_y - raio_bola <= 0:
            velocidade_bola_y = -velocidade_bola_y

        # Colisão da bola com a raquete
        if (raquete_y < bola_y + raio_bola < raquete_y + altura_raquete and
                raquete_x < bola_x < raquete_x + largura_raquete):
            velocidade_bola_y = -velocidade_bola_y

        # Verificar se a bola saiu da tela
        if bola_y > ALTURA:
            print("Game Over!")
            jogo_iniciado = False
            bola_x = LARGURA / 2
            bola_y = ALTURA / 2
            velocidade_bola_x = 4
            velocidade_bola_y = 4

        # Atualização da tela
        tela.fill(PRETO)  # Limpa a tela
        desenhar_raquete(raquete_x, raquete_y)
        desenhar_bola(bola_x, bola_y)
    else:
        # Tela de início
        tela.fill(PRETO)  # Limpa a tela
        desenhar_botao_inicio()

    pygame.display.flip()
    clock.tick(60)  # Controla o FPS do jogo
