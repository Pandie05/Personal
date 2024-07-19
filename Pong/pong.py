import pygame, sys, random

def ball_animation():
    global ball_spd_x, ball_spd_y

    ball.x += ball_spd_x
    ball.y += ball_spd_y

    if ball.top <= 0 or ball.bottom >= scr_h:
        ball_spd_y *= -1
    
    if ball.left <= 0 or ball.right >= scr_w:
        ball_restart()

    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_spd_x *= -1

def player_animation():
    player1.y += player_speed
    if player1.top <= 0:
        player1.top = 0

    if player1.bottom >= scr_h:
        player1.bottom = scr_h

def player2_ai():
    if player2.top < ball.y:
        player2.top += player2_speed
    
    if player2.bottom > ball.y:
        player2.bottom -= player2_speed

    if player2.top <= 0:
        player2.top = 0

    if player2.bottom >= scr_h:
        player2.bottom = scr_h

def ball_restart():
    global ball_spd_x, ball_spd_y
    ball.center = (scr_w/2, scr_h/2)
    ball_spd_y *= random.choice((1, -1))
    ball_spd_x *= random.choice((1, -1))


pygame.init()
clock = pygame.time.Clock()

#canvas
scr_w = 800
scr_h = 700

scr = pygame.display.set_mode((scr_w, scr_h))

pygame.display.set_caption("pong")

#game shapes
ball = pygame.Rect(scr_w/2 - 15, scr_h/2 - 15, 30, 30)
player1 = pygame.Rect(scr_w - 20, scr_h/2 - 70, 10, 140)
player2 = pygame.Rect(10, scr_h/2 - 70, 10, 140)

bg_color = pygame.Color('grey12')
light_grey = (200,200,200)

ball_spd_x = 7 * random.choice((1, -1))
ball_spd_y = 7 * random.choice((1, -1))
player_speed = 0
player2_speed = 12

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 10
            
            if event.key == pygame.K_UP:
                player_speed -= 10

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 10
            
            if event.key == pygame.K_UP:
                player_speed += 10
            
            
    ball_animation()
    player_animation()
    player2_ai()

    #visuals
    scr.fill(bg_color)
    pygame.draw.rect(scr, light_grey, player1)
    pygame.draw.rect(scr, light_grey, player2)
    pygame.draw.ellipse(scr, light_grey, ball)
    pygame.draw.aaline(scr, light_grey, (scr_w/2, 0), (scr_w/2, scr_h))

    #window update
    pygame.display.flip()
    clock.tick(60)