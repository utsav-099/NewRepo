import pygame
import random
import math
pygame.init()
WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ball Smash Game")
bg_img = pygame.image.load(r"C:\Users\Dell\Downloads\download (1).png")
bg_img = pygame.transform.scale(bg_img, (WIDTH, HEIGHT))
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREY = (192, 192, 192)
p_r = 20
p_x = WIDTH // 2
p_y = HEIGHT - 40
p_speed = 10
c_r = 30
circles = []
clock = pygame.time.Clock()
score = 0
font = pygame.font.SysFont(None, 36)
def create_circle():
    x = random.randint(c_r, WIDTH - c_r)
    y = random.randint(-HEIGHT, -c_r)
    angle = random.uniform(0, 2 * math.pi)
    circles.append({"x": x, "y": y, "angle": angle})
def check_collision(circle):
    distance = math.sqrt((circle["x"] - p_x)**2 + (circle["y"] - p_y)**2)
    return distance < (40 + c_r)  

running = True
while running:
    screen.blit(bg_img, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and p_x > 20:
        p_x -= p_speed
    if keys[pygame.K_RIGHT] and p_x < WIDTH - 20:
        p_x += p_speed
    if random.random() < 0.02:
        create_circle()
    for circle in circles[:]:
        circle["y"] += 2
        circle["angle"] += 0.05
        rotated_x = circle["x"] + math.cos(circle["angle"]) * c_r
        rotated_y = circle["y"] + math.sin(circle["angle"]) * c_r
        pygame.draw.circle(screen, WHITE, (int(rotated_x), int(rotated_y)), c_r, 2)
        if check_collision(circle):
            circles.remove(circle)
            score += 1  
        if circle["y"] > HEIGHT + c_r:
            circles.remove(circle)

    pygame.draw.circle(screen, GREY, (p_x, p_y), p_r)
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
