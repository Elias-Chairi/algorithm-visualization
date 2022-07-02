import random
import pygame

pygame.init()

WIDTH, HEIGHT = 700, 700

win = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Linear Search")


the_golden_box = random.randrange(10000)
grid_rects = []
found = False
boxes_searched = 0

def make_rects():
    row = 0
    for i in range(10000):
        if i % 100 == 0 and i != 0:
            row += 1

        column = i 
        while column >= 100:
            column -= 100

        grid_rects.append(pygame.Rect(WIDTH / 100 * column, HEIGHT / 100 * row, WIDTH / 100 - 1, HEIGHT / 100 - 1))

def draw_rects():
    for i in range(len(grid_rects)):
        if i == the_golden_box:
            pygame.draw.rect(win, "gold", grid_rects[i])
        else:
            pygame.draw.rect(win, "gray", grid_rects[i])


searching_index = 0
def find_gold_box():
    global boxes_searched, searching_index
    boxes_searched += 1
    if searching_index == the_golden_box:
        print(f"FOUND IT! the gold box is on index: {str(searching_index)}")
        print(f"I have searched {str(boxes_searched)} boxes")
        pygame.draw.rect(win, "green", grid_rects[searching_index])
        global found
        found = True
        return
    pygame.draw.rect(win, "black", grid_rects[searching_index])
    searching_index += 1

def main():
    running = True
    make_rects()
    draw_rects()

    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
        
        if not found:
            print(clock.get_fps())
            find_gold_box()
            pygame.display.update()
    
    pygame.quit()


if __name__ == "__main__":
    main()
