---
title: Pygame Introduction 3
---

## 1. Add Gravity

Add this to your setup:

```python
vy = 0          # vertical velocity — positive = falling, negative = rising
gravity = 1000  # pixels per second squared — tune this to taste
jump_strength = -500  # negative = upward
```

Add this to the game loop:

```python
if keys[pygame.K_UP] :
    vy = jump_strength  # start the jump

vy += gravity * dt          # update velocity
player_rect.y += vy * dt    # apply velocity to position

if player_rect.y > 600 - player_rect.h:  # hit the ground
    player_rect.y = 600 - player_rect.h
    vy = 0
```
