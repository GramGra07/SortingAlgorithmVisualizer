import asyncio
import sys
import pygame
from sortingAlgoVisualizer.algorithms import *
from sortingAlgoVisualizer.dataCreator import DataCreator
from sortingAlgoVisualizer.isSorted import is_sorted
from sortingAlgoVisualizer.visualizer import Visualizer

waitTime = 0.01
dataAmount = 1000
data = DataCreator(dataAmount).getData()
algorithms = [StalinSort(data),BogoSort(data),]
index = 0
algorithm = algorithms[index]
visualizer = Visualizer(algorithms[0])

async def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
        if not running:
            break
        swap1, swap2 = algorithm.step()
        visualizer.update(swap1, swap2, algorithm.arr)
        await asyncio.sleep(waitTime)

    pygame.quit()

if __name__ == "__main__":
    asyncio.run(main())