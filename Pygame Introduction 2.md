---
title: Pygame Introduction 2
---
## 1. Make the target move 

1. Make the target drop from the top of the screen
2. Make the target start at the top when it reaches the bottom
3. Make the target start at a random x value

### Example:

<img width="800" height="600" alt="demo" src="https://github.com/user-attachments/assets/518f3613-2281-4ba3-9fcb-8f49e4568293" />

## 2. Add a text

1. Add the line `font = pygame.font.SysFont(None, 48)` to your initialisation block
2. Add to your draw block:
  ````python
  score_text = font.render("Your Text Here", True, (255, 255, 255))
  screen.blit(score_text, (10, 10))
  ````
3. Change the text printed
4. Change the size of the text
5. Change the colour of the text
6. Change the position of text

## 3. Add a score
1. Add a variable called `score` that increases when the target and the player collide.
2. Change your code so that `score` only increases by one for each target that falls.
3. Change your code so that `score` decreases by one if the target is not caught.

## 4. Add a second target
1. Add a second target
2. Make the targets get smaller as the game progresses
3. Make the targets move faster as the game progresses
4. Add lives
