import pygame

pygame.init()

# Set Screen Size
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# Set Title
pygame.display.set_caption("Alex's First Game")

#Set Background
background = pygame.image.load("/Users/alex/Desktop/PYWORKSPACE/pygame_basic/background.png")

#Set Character
character = pygame.image.load("/Users/alex/Desktop/PYWORKSPACE/pygame_basic/yosi.png")
charSize = character.get_rect().size
charWidth = charSize[0]
charHeight = charSize[1]
charSetW = (screen_width / 2) - (charWidth / 2)
charSetH = screen_height - charHeight

#Moving Position
to_LR = 0
to_UD = 0

# Event Loop (Game Progress)
gameRun = True
while gameRun:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRun = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_LR -= 5
            elif event.key == pygame.K_RIGHT:
                to_LR += 5
            elif event.key == pygame.K_UP:
                to_UD -= 5
            elif event.key == pygame.K_DOWN:
                to_UD += 5
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_LR = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_UD = 0
        
   
    screen.blit(background, (0, 0))
    screen.blit(character, (charSetW, charSetH))

    charSetW += to_LR
    charSetH += to_UD
    if charSetW < 0:
        charSetW = 0
    elif charSetW > screen_width - charWidth:
        charSetW = screen_width - charWidth
    if charSetH < 0 :
        charSetH= 0
    elif charSetH > screen_height - charHeight:
        charSetH = screen_height - charHeight
    pygame.display.update()

pygame.quit()