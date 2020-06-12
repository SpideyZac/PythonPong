import pygame

win = pygame.display.set_mode((750, 500))

def pongScore():
    global ballx
    global bally
    ballx = 375
    bally = 250
    pad1y = 200
    pad2y = 200
    pygame.time.delay(1000)

def pongReset():
    global ballx
    global bally
    global ballY_Going
    global ballX_Going
    global ballVel
    global pad1x
    global pad1y
    global pad2x
    global pad2y
    global padVel
    global score1
    global score2
    ballx = 375
    bally = 250
    ballY_Going = "Down"
    ballX_Going = "Left"
    ballVel = 10

    pad1x = 3
    pad1y = 200

    pad2x = 730
    pad2y = 200

    padVel = 10

    score1 = 0
    score2 = 0

def pongFramePlay():
    global ballx
    global bally
    global ballY_Going
    global ballX_Going
    global ballVel
    global pad1x
    global pad1y
    global pad2x
    global pad2y
    global padVel
    global score1
    global score2
    global running

    #BALL MOVES BY ONE FRAME
    pygame.time.delay(100)

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
    if bally + ballVel > 500:
        ballY_Going = "Up"
    if bally - ballVel < 0:
        ballY_Going = "Down"
    if ballY_Going == "Down":
        if ballX_Going == "Left":
            ballx -= ballVel
            bally += ballVel

        if ballX_Going == "Right":
            ballx += ballVel
            bally += ballVel
    if ballY_Going == "Up":
        if ballX_Going == "Left":
            ballx -= ballVel
            bally -= ballVel
        if ballX_Going == "Right":
            ballx += ballVel
            bally -= ballVel
    if ballx < 0:
        ballX_Going = "Right"
        score2 += 1
        pongScore()
    if ballx > 750:
        ballX_Going = "Left"
        score1 += 1
        pongScore()
    win.fill((0, 0, 0))
    ball = pygame.draw.rect(win, (255,255,255), (ballx, bally, 20, 20))
    pad1 = pygame.draw.rect(win, (255,255,255), (pad1x, pad1y, 20, 160))
    pad2 = pygame.draw.rect(win, (255,255,255), (pad2x, pad2y, 20, 160))
    pygame.init()
    font = pygame.font.Font(None, 40)
    text = font.render(str(score1) + "                          " + str(score2), False, (255,255,255))
    win.blit(text, (250, 8))
    if ball.colliderect(pad1):
        if pad1y < 250:
            ballY_Going = "Up"
            ballX_Going = "Right"
        else:
            ballY_Going = "Down"
            ballX_Going = "Right"
    if ball.colliderect(pad2):
        if pad1y < 250:
            ballY_Going = "Up"
            ballX_Going = "Left"
        else:
            ballY_Going = "Down"
            ballX_Going = "Left"
    pygame.display.update()

pongReset()
running = True
while running:
    KEYS = pygame.key.get_pressed()
    if KEYS[pygame.K_w]:
        pad1y -= padVel
    if KEYS[pygame.K_s]:
        pad1y += padVel
    if KEYS[pygame.K_UP]:
        pad2y -= padVel
    if KEYS[pygame.K_DOWN]:
        pad2y += padVel
    pongFramePlay()
