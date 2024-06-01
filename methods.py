from prereq import *


def randGen():
    nosDict["randNos"].clear()
    nosDict["colorNos"].clear()

    for i in range(numRange):
        nosDict["randNos"].append(random.randint(0, maxNum))

    for i in range(numRange):
        nosDict["colorNos"].append(
            (
                255 - int((255 / maxNum) * nosDict["randNos"][i]),
                int((255 / maxNum) * nosDict["randNos"][i]),
                0,
            )
        )


def drawElem(typ, arr, displayName):
    if typ == "c":
        for i in range(len(nosDict["randNos"])):
            pygame.draw.circle(
                displayName,
                nosDict["colorNos"][i],
                (
                    dimensions[0] / 2 + 20 * (i - (len(arr) / 2 - 1)),
                    dimensions[1] - 3 * (arr[i] + 20),
                ),
                5,
            )
    elif typ == "r":
        for i in range(len(nosDict["randNos"])):
            pygame.draw.rect(
                displayName,
                nosDict["colorNos"][i],
                (
                    dimensions[0] / 2 - 5 + 20 * (i - (len(arr) / 2 - 1)),
                    dimensions[1] - 3 * (arr[i] + 20),
                    10,
                    dimensions[1] - nosDict["randNos"][i],
                ),
            )


def drawLine(j, displayName):
    pygame.draw.line(
        displayName,
        (0, 0, 255),
        (
            dimensions[0] / 2 + 20 * (j - (len(nosDict["randNos"]) / 2 - 1)),
            dimensions[1],
        ),
        (dimensions[0] / 2 + 20 * (j - (len(nosDict["randNos"]) / 2 - 1)), 0),
    )
    pygame.time.delay(15)
    pygame.display.update()


def sortCheck(listArg):
    if len(listArg) == 1 or len(listArg) == 0:
        return True

    return listArg[0] <= listArg[1] and sortCheck(listArg[1:])
