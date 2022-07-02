import random
import pygame

pygame.init()

WIDTH, HEIGHT = 700, 700

win = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Binary Search")


the_golden_box = random.randrange(10000)
grid_rects = []
found = False
boxes_searched = []

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


def find_gold_box():
    global boxes_searched, low, high

    mid = (low + high) // 2

    boxes_searched.append(mid)

    if mid == the_golden_box:
        print(f"FOUND IT! the gold box is on index: {str(mid)}")
        print(f"I have searched {str(len(boxes_searched))} boxes")
        pygame.draw.rect(win, "green", grid_rects[mid])
        global found
        found = True
        return

    elif mid > the_golden_box:
        high = mid - 1
        for i in range(mid + 1, len(grid_rects)):
            pygame.draw.rect(win, "dark gray", grid_rects[i])
        return

    else:
        low = mid + 1
        for i in range(0, mid):
            pygame.draw.rect(win, "dark gray", grid_rects[i])
        return

def main():
    running = True
    make_rects()
    draw_rects()

    global low, high
    low = 0
    high = len(grid_rects) -1

    while running:
        clock.tick(1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
        
        if not found:
            print(clock.get_fps())
            find_gold_box()
            for i in boxes_searched:
                pygame.draw.rect(win, "black", grid_rects[i])
            if found:
                pygame.draw.rect(win, "green", grid_rects[boxes_searched[len(boxes_searched)-1]])
            pygame.display.update()
    
    pygame.quit()


if __name__ == "__main__":
    main()
