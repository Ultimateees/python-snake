import options as opts
import random

# Printing the score
def print_score(score):
    text = opts.SCORE_FONT.render('Score: ' + str(score), True, opts.WHITE)
    opts.GAME_DISPLAY.blit(text, [0, 0])

# Drawing the snake blocks
def draw_snake(snake_block, snake_pixels):
    for idx, x in enumerate(snake_pixels):
        color = opts.DARK_GREEN if idx == len(snake_pixels) - 1 else opts.LIGHT_GREEN
        opts.pygame.draw.rect(opts.GAME_DISPLAY, color, [x[0], x[1], snake_block, snake_block])

# Creating the target in a random position
def new_target_position(snake_pixels, width, height, snake_block):
    while True:
        target_x = round(random.randrange(0, width - snake_block) / 10) * 10
        target_Y = round(random.randrange(0, height - snake_block) / 10) * 10
        if not any(pixel == [target_x, target_Y] for pixel in snake_pixels):
            return target_x, target_Y

# Main game loop
def run_game():
    game_over = False
    game_close = False

    x = opts.WIDTH / 2
    y = opts.HEIGHT / 2

    x_speed = 0
    y_speed = 0
    
    snake_length = 3
    snake_pixels = [[x - i * opts.SNAKE_BLOCK, y] for i in range(3)]
    init_state = True

    target_x, target_y = new_target_position(snake_pixels, opts.WIDTH, opts.HEIGHT, opts.SNAKE_BLOCK)

    current_direction = None
    new_direction = None

    while not game_over:
        while game_close:
            opts.GAME_DISPLAY.fill(opts.BLACK)
            game_over_message = opts.MESSAGE_FONT.render('Game Over', True, opts.RED)
            instruction_message = opts.MESSAGE_FONT.render('Press R to restart or Q to quit', True, opts.WHITE)
            opts.GAME_DISPLAY.blit(game_over_message, [opts.WIDTH / 3, opts.HEIGHT / 3])
            opts.GAME_DISPLAY.blit(instruction_message, [opts.WIDTH / 5, opts.HEIGHT / 2])
            print_score(snake_length - 1)
            opts.pygame.display.update()

            for event in opts.pygame.event.get():
                if event.type == opts.pygame.KEYDOWN:
                    if event.key == opts.pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == opts.pygame.K_r:
                        run_game()
                if event.type == opts.pygame.QUIT:
                    game_over = True
                    game_close = False

        for event in opts.pygame.event.get():
            if event.type == opts.pygame.QUIT:
                game_over = True
            if event.type == opts.pygame.KEYDOWN:
                if event.key == opts.pygame.K_LEFT and current_direction != 'RIGHT':
                    new_direction = 'LEFT'
                elif event.key == opts.pygame.K_RIGHT and current_direction != 'LEFT':
                    new_direction = 'RIGHT'
                elif event.key == opts.pygame.K_UP and current_direction != 'DOWN':
                    new_direction = 'UP'
                elif event.key == opts.pygame.K_DOWN and current_direction != 'UP':
                    new_direction = 'DOWN'

        if new_direction:
            current_direction = new_direction

        if current_direction == "LEFT":
            x_speed = -opts.SNAKE_BLOCK
            y_speed = 0
        elif current_direction == "RIGHT":
            x_speed = opts.SNAKE_BLOCK
            y_speed = 0
        elif current_direction == "UP":
            x_speed = 0
            y_speed = -opts.SNAKE_BLOCK
        elif current_direction == "DOWN":
            x_speed = 0
            y_speed = opts.SNAKE_BLOCK

        new_direction = None                

        if x >= opts.WIDTH or x < 0 or y >= opts.HEIGHT or y < 0:
            game_close = True

        x += x_speed
        y += y_speed

        opts.GAME_DISPLAY.fill(opts.BLACK)
        opts.pygame.draw.rect(opts.GAME_DISPLAY, opts.RED, [target_x, target_y, opts.SNAKE_BLOCK, opts.SNAKE_BLOCK])

        snake_pixels.append([x, y])

        if len(snake_pixels) > snake_length:
            del snake_pixels[0]

        for pixel in snake_pixels[:-1]:
            if pixel == [x, y] and not init_state:
                game_close = True

        draw_snake(opts.SNAKE_BLOCK, snake_pixels)
        print_score(snake_length - 1)

        opts.pygame.display.update()

        if x == target_x and y == target_y:
            target_x, target_y = new_target_position(snake_pixels, opts.WIDTH, opts.HEIGHT, opts.SNAKE_BLOCK)
            snake_length += 1
            init_state = False

        opts.CLOCK.tick(opts.SNAKE_SPEED)

    opts.pygame.quit()
    quit()