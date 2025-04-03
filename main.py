import asyncio
import sys
import pygame

from algorithms import StalinSort, BogoSort, BubbleSort, QuickSort, MergeSort, InsertionSort, HeapSort, SelectionSort, \
    TimSort
from dataCreator import DataCreator
from visualizer import Visualizer

waitTime = 0.001
dataAmount = 1000
data = DataCreator(dataAmount).getData()
algorithms = [StalinSort(data),BogoSort(data),BubbleSort(data),QuickSort(data),MergeSort(data),InsertionSort(data),HeapSort(data),SelectionSort(data),TimSort(data)]
index = 5
algorithm = algorithms[index]
visualizer = Visualizer(algorithm)

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