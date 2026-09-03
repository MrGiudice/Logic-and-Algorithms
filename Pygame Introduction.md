---
title: Pygame Introduction
---

Copy, paste and run this code:

````python
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
````

1. What change do you need to make to:
    1. have the screen open at a different size?
    2. have the player rectangle start in a different position on the screen?
    3. make the square move faster or slower?
    4. make the player rectangle bigger or smaller?
    5. change the colour of the background? *(Colours are given as R, G, B out of 255 — for example, 255, 0, 0 is red.)*
    6. change the colour of the player rectangle?
    7. change the window title from "Move the square" to something else?
    8. make the square move using A, D, W, S instead of the arrow keys?
    9. make the player rectangle a circle? *(read docs https://www.pygame.org/docs/ref/draw.html)*
    2. Create a variable called `colour` at the top of the code, and use it to set the player rectangle's colour — instead of writing the RGB tuple directly in the `draw.rect` call.

2. Keep the player on screen (boundary clamping)
   
   Right now, the player can move off-screen entirely and disappear forever. A simple, high-value fix:

   1. Evaluate  max(0, min(500, 800 - 50))
   1. Evaluate  max(0, min(-50, 800 - 50))
   1. Evaluate  max(0, min(900, 800 - 50))
   1. Write an assignment (e.g. x = ... ) so  that x stays between 0 and 750
   2. Update your code so that the player can't leave the screen

3. pygame.Rect is a built-in helper object for representing rectangles

   See doc for details https://www.pygame.org/docs/ref/rect.html

   Copy, paste and run this code:

   ```python
   import pygame
   
   # --- Setup ---
   pygame.init()
   screen = pygame.display.set_mode((800, 600))
   pygame.display.set_caption("Move the square")
   clock = pygame.time.Clock()
   
   # Player state — now a Rect instead of separate x, y
   player_rect = pygame.Rect(400, 300, 50, 50)  # left, top, width, height
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
           player_rect.x -= speed * dt
       if keys[pygame.K_RIGHT]:
           player_rect.x += speed * dt
       if keys[pygame.K_UP]:
           player_rect.y -= speed * dt
       if keys[pygame.K_DOWN]:
           player_rect.y += speed * dt
   
       # 3. Draw everything
       screen.fill((30, 30, 30))  # clear screen (dark grey)
       pygame.draw.rect(screen, (100, 200, 255), player_rect)  # our "player"
       pygame.display.flip()  # show what we drew
   
   pygame.quit()
   ```

    We created player_rect which has coordinates (player_rect.x, player_rect.y)
    1. Add the boundary clamping code
    2. Create a second Rect called target and draw it
    3. Add collision detection code
    ````python
      if player_rect.colliderect(target):
          print("Overlap!")
    ````
    4. Make the player change colour when a target is detected

4. Using images instead of shapes

   Right now the player is drawn as a plain rectangle using `pygame.draw.rect()`. Real games almost always use images (called *sprites*) instead.

   You'll need a small image file (a `.png` works best, ideally with a transparent background) saved in the same folder as your code. Call it `player.png`.

   Copy, paste and run this code:

   ```python
   import pygame

   # --- Setup ---
   pygame.init()
   screen = pygame.display.set_mode((800, 600))
   pygame.display.set_caption("Move the square")
   clock = pygame.time.Clock()

   # Player state — now a Rect instead of separate x, y
   player_rect = pygame.Rect(400, 300, 50, 50)  # left, top, width, height
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
           player_rect.x -= speed * dt
       if keys[pygame.K_RIGHT]:
           player_rect.x += speed * dt
       if keys[pygame.K_UP]:
           player_rect.y -= speed * dt
       if keys[pygame.K_DOWN]:
           player_rect.y += speed * dt

       player_rect.x = max(0, min(player_rect.x, 800 - 50))
       player_rect.y = max(0, min(player_rect.y, 600 - 50))

       # 3. Draw everything
       screen.fill((30, 30, 30))  # clear screen (dark grey)
       pygame.draw.rect(screen, (100, 200, 255), player_rect)  # our "player"
       pygame.display.flip()  # show what we drew

   pygame.quit()
   ```

   1. Before the game loop, load your image into a variable using `pygame.image.load("player.png").convert_alpha()`. *(`.convert_alpha()` makes the image draw faster and keeps any transparent background working correctly.)*
   2. Replace the `pygame.draw.rect(...)` line with `screen.blit(your_image_variable, player_rect)` — `blit` is pygame's word for "draw this image onto the screen at this position."
   3. Run it. If the image doesn't appear, check the filename in your code matches the actual file exactly, including the `.png` at the end.
   4. `player_rect` is still `50 × 50`, no matter what size your actual image file is. What happens if your image isn't 50 × 50 pixels — does it look stretched, squashed, or cut off?
   5. Instead of guessing the size, you can ask pygame to size the rectangle to match the image automatically, using `your_image_variable.get_rect()`. Look up `get_rect()` in the docs (https://www.pygame.org/docs/ref/surface.html) and use it to fix the sizing issue from the question above.
    
    

