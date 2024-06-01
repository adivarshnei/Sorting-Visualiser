from prereq import *
from methods import *
from algos import *

pygame.init()
pygame.display.set_caption("Visualizer")

screen = pygame.display.set_mode(dimensions)

randGen()

while running:
    sortExec = False

    clock.tick(15)

    pygame.time.delay(5)

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if (
        keys[pygame.K_b]
        or keys[pygame.K_s]
        or keys[pygame.K_q]
        or keys[pygame.K_i]
        or keys[pygame.K_c]
    ):
        sortExec = True

    if not sortExec:
        screen.fill((0, 0, 0))
        drawElem(elemType, nosDict["randNos"], screen)
        pygame.display.update()

        try:
            if keyboard.is_pressed("r"):
                randGen()
                print(nosDict["randNos"])
                pygame.display.update()

            if keyboard.is_pressed("e"):
                running = False

            if keyboard.is_pressed("t"):
                if elemType == "c":
                    elemType = "r"
                else:
                    elemType = "c"

        except:
            pass

    else:
        if keys[pygame.K_b]:
            bubSort(screen, elemType)
        elif keys[pygame.K_s]:
            selSort(screen, elemType)
        elif keys[pygame.K_q]:
            quickSort(
                nosDict["randNos"],
                nosDict["colorNos"],
                0,
                len(nosDict["randNos"]) - 1,
                screen,
                elemType,
            )
        elif keys[pygame.K_i]:
            insSort(screen, elemType)
        elif keys[pygame.K_c]:
            countSort(screen, elemType)

pygame.quit()
