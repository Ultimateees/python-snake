import options as opts

def print_score(score):
    text = opts.SCORE_FONT.render('Score: ' + str(score), True, opts.WHITE)
    opts.GAME_DISPLAY.blit(text, [0, 0])

def draw_snake(snake_block, snake_pixels):
    for x in snake_pixels:
        opts.pygame.draw.rect(opts.GAME_DISPLAY, opts.GREEN, [x[0], x[1], snake_block, snake_block])

def run_game():

    game_over = False
    game_close = False

    x = opts.WIDTH / 2
    y = opts.HEIGHT / 2

    x_speed = 0
    y_speed = 0

    snake_pixels = []
    snake_length = 1

    target_x = round(opts.random.randrange(0, opts.WIDTH - opts.SNAKE_BLOCK) / 10.0) * 10.0
    target_y = round(opts.random.randrange(0, opts.HEIGHT - opts.SNAKE_BLOCK) / 10.0) * 10.0

    while not game_over:

        while game_close:
            opts.GAME_DISPLAY.fill(opts.BLACK)
            game_over_message = opts.MESSAGE_FONT.render('Game Over', True, opts.RED)
            opts.GAME_DISPLAY.blit(game_over_message, [opts.WIDTH / 3, opts.HEIGHT / 3])
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
                if event.key == opts.pygame.K_LEFT:
                    x_speed = -opts.SNAKE_BLOCK
                    y_speed = 0
                elif event.key == opts.pygame.K_RIGHT:
                    x_speed = opts.SNAKE_BLOCK
                    y_speed = 0
                elif event.key == opts.pygame.K_UP:
                    x_speed = 0
                    y_speed = -opts.SNAKE_BLOCK
                elif event.key == opts.pygame.K_DOWN:
                    x_speed = 0
                    y_speed = opts.SNAKE_BLOCK
        
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
            if pixel == [x, y]:
                game_close = True

        draw_snake(opts.SNAKE_BLOCK, snake_pixels)
        print_score(snake_length - 1)

        opts.pygame.display.update()

        if x == target_x and y == target_y:
            target_x = round(opts.random.randrange(0, opts.WIDTH - opts.SNAKE_BLOCK) / 10.0) * 10.0
            target_y = round(opts.random.randrange(0, opts.HEIGHT - opts.SNAKE_BLOCK) / 10.0) * 10.0
            snake_length += 1

        opts.CLOCK.tick(opts.SNAKE_SPEED)

    opts.pygame.quit()
    quit()