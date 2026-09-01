# Pygame Introduction

Copy, paste and run this code:

```python
import pygame

# --- Setup ---
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Move the square")
clock = pygame.time.Clock()

# Player state (just variables for now)
x, y = 400, 300
speed = 300  # pixels per second

running = True
while running:
    # 1. Handle events (quitting, key presses, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2. Update state based on which keys are currently held
    keys = pygame.key.get_pressed()
    dt = clock.tick(60) / 1000  # seconds since last frame

    if keys[pygame.K_LEFT]:
        x -= speed * dt
    if keys[pygame.K_RIGHT]:
        x += speed * dt
    if keys[pygame.K_UP]:
        y -= speed * dt
    if keys[pygame.K_DOWN]:
        y += speed * dt

    # 3. Draw everything
    screen.fill((30, 30, 30))  # clear screen (dark grey)
    pygame.draw.rect(screen, (100, 200, 255), (x, y, 50, 50))  # our "player"
    pygame.display.flip()  # show what we drew

pygame.quit()
```

1. What change do you need to make to have the:
    1. screen open at a different size?
    2. player rectangle start in a different position on the screen?
    3. square move faster or slower?
    4. player rectangle bigger or smaller?
    1. to change the colour of the background? *(Colours are given as R, G, B out of 255 — for example, 255, 0, 0 is red.)*
    1. make to change the colour of the player rectangle?
    1.  make to change the window title from "Move the square" to something else?
    1.  to make so the square moves using A, D, W, S instead of the arrow keys?
    1. player rectangle be a circle *(read docs https://www.pygame.org/docs/ref/draw.html)*

2. Keep the player on screen (boundary clamping)
   
Right now, the player can move off-screen entirely and disappear forever. A simple, high-value fix:

```python
x = max(0, min(x, 800 - 50))
y = max(0, min(y, 600 - 50))
```
How do you need

