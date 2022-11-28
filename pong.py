import pygame,sys

pygame.init()
clock = pygame.time.Clock()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))

col = {'black':(0,0,0), 'white': (255,255,255),
       'red': (255,0,0), 'blue': (0,0,255),
       'yellow': (0,0,255), 'green': (0,128,0), 'purple': (128,128,0)}


ball = pygame.Rect(400,300,20,20)
x_speed, y_speed = 5,5

paddle1=pygame.Rect(5, 260, 15, 90)
paddle2=pygame.Rect(780, 260, 15, 90)
vel=7

def pong_ball():
    #ball
    pygame.draw.rect(screen, col['red'], ball)

    #motion
    global x_speed, y_speed
    ball.x+=x_speed
    ball.y+=y_speed

    #collision with borders
    if ball.right>=screen_width or ball.left<=0:
        x_speed*=-1
    if ball.bottom>=screen_height or ball.top<=0:
        y_speed*=-1


    #collision with paddles
    collision_tolerance=10
    if ball.colliderect(paddle1):
        if abs(paddle1.top - ball.bottom)<collision_tolerance and y_speed>0:
            y_speed*=-1
        elif abs(paddle1.bottom - ball.top)<collision_tolerance and y_speed<0:
            y_speed*=-1
        elif abs(paddle1.right - ball.left)<collision_tolerance and x_speed<0:
            x_speed*=-1
            
    if ball.colliderect(paddle2):
        if abs(paddle2.top - ball.bottom)<collision_tolerance and y_speed>0:
            y_speed*=-1
        elif abs(paddle2.bottom - ball.top)<collision_tolerance and y_speed<0:
            y_speed*=-1
        elif abs(paddle2.left - ball.right)<collision_tolerance and x_speed>0:
            x_speed*=-1
    
def paddle():
    pygame.draw.rect(screen, col['white'], paddle1)
    pygame.draw.rect(screen, col['white'], paddle2)

    keys = pygame.key.get_pressed()
    if keys[ord('w')]:
        paddle1.y-=vel

    elif keys[ord('s')]:
        paddle1.y+=vel
    
    if keys[pygame.K_UP]:
        paddle2.y-=vel

    elif keys[pygame.K_DOWN]:
        paddle2.y+=vel


#main         
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    screen.fill(col['black'])
    
    pong_ball()
    paddle()
    

    
    pygame.display.flip()
    clock.tick(60)
