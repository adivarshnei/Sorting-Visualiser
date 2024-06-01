from prereq import *
from methods import *


def bubSort(displayType, elementType):
    for i in range(len(nosDict["randNos"])):
        swapStat = False

        for j in range(0, len(nosDict["randNos"]) - i - 1):
            if nosDict["randNos"][j] > nosDict["randNos"][j + 1]:
                nosDict["randNos"][j], nosDict["randNos"][j + 1] = (
                    nosDict["randNos"][j + 1],
                    nosDict["randNos"][j],
                )
                nosDict["colorNos"][j], nosDict["colorNos"][j + 1] = (
                    nosDict["colorNos"][j + 1],
                    nosDict["colorNos"][j],
                )
                swapStat = True

            # drawLine(j, displayType)

            displayType.fill((0, 0, 0))

            drawElem(elementType, nosDict["randNos"], displayType)

            pygame.display.update()

        if not swapStat:
            break

        if keyboard.is_pressed(("e")):
            sys.exit(0)


def selSort(displayType, elementType):
    for i in range(len(nosDict["randNos"])):
        minIndex = i

        for j in range(i + 1, len(nosDict["randNos"])):
            if nosDict["randNos"][j] < nosDict["randNos"][minIndex]:
                minIndex = j

        if minIndex != i:
            nosDict["randNos"][i], nosDict["randNos"][minIndex] = (
                nosDict["randNos"][minIndex],
                nosDict["randNos"][i],
            )
            nosDict["colorNos"][i], nosDict["colorNos"][minIndex] = (
                nosDict["colorNos"][minIndex],
                nosDict["colorNos"][i],
            )

            # drawLine(i, displayType)
            # drawLine(minIndex, displayType)

        displayType.fill((0, 0, 0))

        drawElem(elementType, nosDict["randNos"], displayType)

        pygame.time.delay(5)
        pygame.display.update()

        if keyboard.is_pressed(("e")):
            sys.exit(0)


def partition(arr, colArr, low, high, displayType, elementType):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
            colArr[i], colArr[j] = colArr[j], colArr[i]

            displayType.fill((0, 0, 0))

            drawElem(elementType, nosDict["randNos"], displayType)

            pygame.time.delay(5)
            pygame.display.update()

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    colArr[i + 1], colArr[high] = colArr[high], colArr[i + 1]

    displayType.fill((0, 0, 0))

    drawElem(elementType, nosDict["randNos"], displayType)

    pygame.display.update()

    if keyboard.is_pressed(("e")):
        sys.exit(0)

    return i + 1


def quickSort(arr, colArr, low, high, displayType, elementType):
    if low < high:
        pi = partition(arr, colArr, low, high, displayType, elementType)
        # drawLine(pi, displayType)

        if sortCheck(arr):
            return

        quickSort(arr, colArr, low, pi - 1, displayType, elementType)
        quickSort(arr, colArr, pi + 1, high, displayType, elementType)

        if keyboard.is_pressed(("e")):
            sys.exit(0)


def insSort(displayType, elementType):
    for i in range(len(nosDict["randNos"])):
        key = nosDict["randNos"][i]
        colKey = nosDict["colorNos"][i]

        j = i - 1

        while j >= 0 and key < nosDict["randNos"][j]:
            nosDict["randNos"][j + 1] = nosDict["randNos"][j]
            nosDict["colorNos"][j + 1] = nosDict["colorNos"][j]
            j -= 1

            displayType.fill((0, 0, 0))

            drawElem(elementType, nosDict["randNos"], displayType)

            pygame.time.delay(5)
            pygame.display.update()

        nosDict["randNos"][j + 1] = key
        nosDict["colorNos"][j + 1] = colKey

        # drawLine(j + 1, displayType)
        # drawLine(key, displayType)

        pygame.time.delay(5)

        displayType.fill((0, 0, 0))

        drawElem(elementType, nosDict["randNos"], displayType)

        pygame.time.delay(5)
        pygame.display.update()

        if keyboard.is_pressed(("e")):
            sys.exit(0)


def countSort(displayType, elementType):
    colNosTup = []

    for i in range(len(nosDict["randNos"])):
        colNosTup.append((nosDict["randNos"][i], nosDict["colorNos"][i]))

    output = [0 for i in range(len(nosDict["randNos"]))]
    count = [0 for i in range(maxNum + 1)]

    for i in range(len(nosDict["randNos"])):
        count[nosDict["randNos"][i]] += 1

    for i in range(1, maxNum):
        count[i] += count[i - 1]

    i = len(nosDict["randNos"]) - 1

    while i >= 0:
        output[count[nosDict["randNos"][i]] - 1] = nosDict["randNos"][i]
        count[nosDict["randNos"][i]] -= 1
        i -= 1

    for i in range(len(nosDict["randNos"])):
        nosDict["randNos"][i] = output[i]

        for j in range(len(nosDict["randNos"])):
            if nosDict["randNos"][i] == colNosTup[j][0]:
                nosDict["colorNos"][i] = colNosTup[j][1]

        displayType.fill((0, 0, 0))

        drawElem(elementType, nosDict["randNos"], displayType)

        pygame.time.delay(5)
        pygame.display.update()

        if keyboard.is_pressed(("e")):
            sys.exit(0)
