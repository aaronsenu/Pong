import pygame, sys, random

def pong_ball():
    global ball_x_speed, ball_y_speed, player_score, opponent_score, start_time
    collision_tolerance = 10
    ball.x += ball_x_speed
    ball.y += ball_y_speed
    
    
    if ball.bottom>=screen_height or ball.top<=0:
        ball_y_speed *= -1
        
    if ball.right>=screen_width:
        opponent_score += 1
        start_time = pygame.time.get_ticks()
        
    if ball.left<=0:
        player_score += 1
        start_time = pygame.time.get_ticks()

    if ball.colliderect(player):
        if abs(player.top  - ball.bottom) < collision_tolerance and ball_y_speed > 0:
            ball_y_speed *= -1
        if abs(player.bottom - ball.top) < collision_tolerance and ball_y_speed < 0:
            ball_y_speed *= -1
        if abs(player.left - ball.right) < collision_tolerance and ball_x_speed > 0:
            ball_x_speed *= -1
            
    if ball.colliderect(opponent):
        if abs(opponent.top  - ball.bottom) < collision_tolerance and ball_y_speed > 0:
            ball_y_speed *= -1
        if abs(opponent.bottom - ball.top) < collision_tolerance and ball_y_speed < 0:
            ball_y_speed *= -1
        if abs(opponent.right - ball.left) < collision_tolerance and ball_x_speed < 0:
            ball_x_speed *= -1
            
        
def ball_reset():
    global ball_speed_x, ball_speed_y, ball_moving, start_time

    ball.center = (screen_width/2, screen_height/2)
    current_time = pygame.time.get_ticks()

    if current_time - start_time < 700:
        number_three = time_font.render("3",False,pygame.Color('gray99'))
        number_three.set_alpha(90)
        screen.blit(number_three,(screen_width/2-140, screen_height/2 - 250))
    if 700 < current_time - start_time < 1400:
        number_two = time_font.render("2",False,pygame.Color('gray99'))
        number_two.set_alpha(60)
        screen.blit(number_two,(screen_width/2 -140, screen_height/2 -250))
    if 1400 < current_time - start_time < 2100:
        number_one = time_font.render("1",False,pygame.Color('gray99'))
        number_one.set_alpha(30)
        screen.blit(number_one,(screen_width/2 -140, screen_height/2 -250))

    if current_time - start_time < 2100:
        ball_speed_y, ball_speed_x = 0,0
    else:
        ball_speed_x = 7 * random.choice((1,-1))
        ball_speed_y = 7 * random.choice((1,-1))
        start_time = None

def player_animation():
    # General movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player.y -= player_speed
    elif keys[pygame.K_DOWN]:
        player.y += player_speed

    # Borders
    if player.bottom >= screen_height:
        player.bottom = screen_height
    if player.top <= 0:
        player.top = 0

def opponent_ai():
    # General movement
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top < ball.y:
        opponent.top += opponent_speed

    # Borders
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height
    if opponent.top <= 0:
        opponent.top = 0
        
    
        
    


# Setup
pygame.init()
clock = pygame.time.Clock()

# Main window
screen_width,screen_height = 1280,800
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Pong')

# Game objects
ball = pygame.Rect(screen_width/2 - 15,screen_height/2 - 15,30,30)
player = pygame.Rect(screen_width - 20,screen_height/2 ,10,140)
opponent = pygame.Rect(10,screen_height/2 - 70,10,140)

# Colours
bg_colour = pygame.Color('gray8')
#bg_colour = (41,36,33)
#light_grey = (200,200,200)
light_grey = pygame.Color('grey77')
# Game variables
ball_x_speed,ball_y_speed = 7*random.choice((-1,1)),7*random.choice((-1,1))
player_speed,opponent_speed = 7,9

# Score variables
player_score, opponent_score = 0,0
game_font = pygame.font.SysFont("Consolas",200)
time_font = pygame.font.SysFont("arialblack", 350)

# Timer
start_time = True
ball_moving = False

while True:

    # Input handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    # Game animations
    pong_ball()
    player_animation()
    opponent_ai()
    
    # Visuals
    screen.fill(bg_colour)
    pygame.draw.ellipse(screen,light_grey,ball)
    pygame.draw.rect(screen,light_grey,player)
    pygame.draw.rect(screen,light_grey,opponent)
    pygame.draw.aaline(screen,light_grey,(screen_width/2,0),(screen_width/2,screen_height))
  

    if start_time:
        ball_reset()
        

    player_text = game_font.render("{}".format(player_score), True, pygame.Color('grey77'))
    player_text.set_alpha(60)
    screen.blit(player_text,(900, 40))

    opponent_text = game_font.render("{}".format(opponent_score), True, pygame.Color('grey77'))
    opponent_text.set_alpha(60)
    screen.blit(opponent_text,(260,40))
    
    
    
    # Window updating
   
    pygame.display.flip()
    clock.tick(60)
