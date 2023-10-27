
# Import the pygame library and initialise the game engine
import pygame
import time
from paddle import Paddle
from ball import Ball
import os
from Day import msg
from Block import block

clock = pygame.time.Clock()

player1 = input('Enter 1st player name?')
player2 = input('Enter 2nd player name?')
player3 = input('Enter 3rd player name?')
player4 = input('Enter 4th player name?')





pygame.init()

# Define some colors
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,139)
GREEN = (0,238,0)
YELLOW = (255,215,0)
RED = (205,38,38)

# Open a new window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("PingPong with SHERY")

pygame.init()
screen = pygame.display.set_mode(size)


pygame.display.update()


# Using draw.rect module of

paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = 10
paddleA.rect.y = 100

paddleB = Paddle(WHITE, 10, 100)
paddleB.rect.x = 680
paddleB.rect.y = 100

paddleC = Paddle(WHITE, 10, 100)
paddleC.rect.x = 10
paddleC.rect.y = 300

paddleD = Paddle(WHITE, 10, 100)
paddleD.rect.x = 680
paddleD.rect.y = 300


ball1 = Ball(WHITE,15,15,20)
ball1.rect.x = 200
ball1.rect.y = 100


ball2 = Ball(WHITE,18,18,20)
ball2.rect.x = 300
ball2.rect.y = 100

paddleE = Paddle(RED, 40, 40)
paddleE.rect.x = 149
paddleE.rect.y = 220

paddleF = Paddle(RED, 40, 40)
paddleF.rect.x = 510
paddleF.rect.y = 220

#This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = pygame.sprite.Group()

# Add the 4 paddles and the balls to the list of objects
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(paddleC)
all_sprites_list.add(paddleD)
all_sprites_list.add(ball1)
all_sprites_list.add(ball2)
all_sprites_list.add(paddleE)
all_sprites_list.add(paddleF)





# The loop will carry on until the user exits the game (e.g. clicks the close button).
carryOn = True

# The second ball appears


# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

#Initialise player scores
scoreA = 0
scoreB = 0


# -------- Main Program Loop -----------
while carryOn:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
              carryOn = False # Flag that we are done so we exit this loop
        elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_x: #Pressing the x Key will quit the game
                     carryOn=False

    #Moving the paddles when the use uses the arrow keys (player A) or "W/S" keys (player B)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.moveUp(5)
    if keys[pygame.K_s]:
        paddleA.moveDown(5)
    if keys[pygame.K_UP]:
        paddleB.moveUp(5)
    if keys[pygame.K_DOWN]:
        paddleB.moveDown(5)
    if keys[pygame.K_r]:
        paddleC.moveUp(5)
    if keys[pygame.K_f]:
        paddleC.moveDown(5)
    if keys[pygame.K_y]:
        paddleD.moveUp(5)
    if keys[pygame.K_j]:
        paddleD.moveDown(5)

    # --- Game logic should go here
    all_sprites_list.update()

    #Check if the ball is bouncing against any of the 4 walls:
    if ball1.rect.x>=685:
        scoreA+=1
        ball1.velocity[0] = -ball1.velocity[0]
    if ball1.rect.x<=0:
        scoreB+=1
        ball1.velocity[0] = -ball1.velocity[0]
    if ball1.rect.y>485:
        ball1.velocity[1] = -ball1.velocity[1]
    if ball1.rect.y<0:
        ball1.velocity[1] = -ball1.velocity[1]

    if ball2.rect.x >= 685:
        scoreA += 1
        ball2.velocity[0] = -ball2.velocity[0]
    if ball2.rect.x <= 0:
        scoreB += 1
        ball2.velocity[0] = -ball2.velocity[0]
    if ball2.rect.y > 485:
        ball2.velocity[1] = -ball2.velocity[1]
    if ball2.rect.y < 0:
        ball2.velocity[1] = -ball2.velocity[1]






    #Detect collisions between the ball and the paddles
    if pygame.sprite.collide_mask(ball1, paddleA) or pygame.sprite.collide_mask(ball1, paddleB) or pygame.sprite.collide_mask(ball1, paddleC) or pygame.sprite.collide_mask(ball1, paddleD):
      ball1.bounce()
    if pygame.sprite.collide_mask(ball2, paddleA) or pygame.sprite.collide_mask(ball2, paddleB) or pygame.sprite.collide_mask(ball2, paddleC) or pygame.sprite.collide_mask(ball2, paddleD):
      ball2.bounce()
    if pygame.sprite.collide_mask(ball2, paddleE) or pygame.sprite.collide_mask(ball2,paddleE) or pygame.sprite.collide_mask(ball2, paddleE) or pygame.sprite.collide_mask(ball2, paddleE):
        ball2.bounce()
    if pygame.sprite.collide_mask(ball1, paddleE) or pygame.sprite.collide_mask(ball1,paddleE) or pygame.sprite.collide_mask(ball1, paddleE) or pygame.sprite.collide_mask(ball1, paddleE):
        ball1.bounce()
    if pygame.sprite.collide_mask(ball1, paddleF) or pygame.sprite.collide_mask(ball1, paddleF) or pygame.sprite.collide_mask(ball1, paddleF) or pygame.sprite.collide_mask(ball1, paddleF):
      ball1.bounce()
    if pygame.sprite.collide_mask(ball2, paddleF) or pygame.sprite.collide_mask(ball2, paddleF) or pygame.sprite.collide_mask(ball2, paddleF) or pygame.sprite.collide_mask(ball2, paddleF):
      ball2.bounce()








    # --- Drawing code should go here
    # First, clear the screen to black.
    screen.fill(BLACK)
    #Draw the net
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)



    #Now let's draw all the sprites in one go. (For now we only have 2 sprites!)
    all_sprites_list.draw(screen)

    #Display scores:
    font = pygame.font.Font(None, 40)

    text = font.render(str(scoreA), 1, GREEN)
    screen.blit(text, (250,10))
    text = font.render(str(scoreB), 1, GREEN)
    screen.blit(text, (430,10))

    #Display Players:
    font1 = pygame.font.Font(None, 20)

    text = font1.render("Team A", 1, YELLOW)
    screen.blit(text, (130, 10))
    text = font1.render("Team B", 1, YELLOW)
    screen.blit(text, (530, 10))

    Block1 = block(WHITE, 90, 90)
    Block1.rect.x = 300
    Block1.rect.y = 150

    all_sprites_list.add(Block1)

    if ball1.rect.colliderect(Block1) and scoreA + scoreB > 5 and scoreA + scoreB < 10:
        ball1.bounce()
    if ball2.rect.colliderect(Block1) and scoreA + scoreB > 5 and scoreA + scoreB < 10:
        ball2.bounce()

    if scoreA + scoreB > 5 and scoreA + scoreB < 10:
        Block1 = pygame.draw.rect(screen, WHITE, [300, 150, 90, 90], 5)

    Block2 = block(WHITE, 100, 100)
    Block2.rect.x = 400
    Block2.rect.y = 400

    all_sprites_list.add(Block2)

    if ball1.rect.colliderect(Block2) and scoreA + scoreB > 10 and scoreA + scoreB < 15:
        ball1.bounce()
    if ball2.rect.colliderect(Block2) and scoreA + scoreB > 10 and scoreA + scoreB < 15:
        ball2.bounce()

    if scoreA + scoreB > 10 and scoreA + scoreB < 15:
        Block2 = pygame.draw.rect(screen, WHITE, [400, 400, 100, 100], 5)



    Block3 = block(WHITE, 100, 100)
    Block3.rect.x = 200
    Block3.rect.y = 200

    all_sprites_list.add(Block3)

    if ball1.rect.colliderect(Block3) and scoreA + scoreB > 15 and scoreA + scoreB < 20:
        ball1.bounce()
    if ball2.rect.colliderect(Block3) and scoreA + scoreB > 15 and scoreA + scoreB < 20:
        ball2.bounce()

    if scoreA + scoreB > 15 and scoreA + scoreB < 20:
        Block3 = pygame.draw.rect(screen, WHITE, [200, 200, 100, 100], 5)

    Block4 = block(WHITE, 150, 150)
    Block4.rect.x = 80
    Block4.rect.y = 80

    all_sprites_list.add(Block4)

    if ball1.rect.colliderect(Block4) and scoreA + scoreB > 20 and scoreA + scoreB < 25:
        ball1.bounce()
    if ball2.rect.colliderect(Block4) and scoreA + scoreB > 20 and scoreA + scoreB < 25:
        ball2.bounce()

    if scoreA + scoreB > 20 and scoreA + scoreB < 25:
        Block4 = pygame.draw.rect(screen, WHITE, [80, 80, 150, 150], 5)



    maxScore = 15

    if scoreA == maxScore:
        font2 = pygame.font.Font(None, 50)
        playerWins = font2.render("Team A Wins!", True, RED)
        screen.blit(playerWins, (700 / 2 - 100, 500 / 2))
        pygame.display.update()
        print("Do you want to continue? yes or no?")
        response = input()
        if response == "no":
            break




    elif scoreB == maxScore:
        font2 = pygame.font.Font(None, 50)
        playerWins = font2.render("Team B Wins!", True, RED)
        screen.blit(playerWins, (700 / 2 - 100, 500 / 2))
        pygame.display.update()
        print("Do you want to continue? yes or no?")
        response = input()
        if response == "no":
            break


    pygame.display.update()

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(30)

    # Importing pygame module
    import pygame


    # initiate pygame and give permission
    # to use pygame's functionality.
    pygame.init()


    


    # Draws the surface object to the screen.
    pygame.display.update()

#Once we have exited the main program loop we can stop the game engine:
pygame.quit()# This is a sample Python script.



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
