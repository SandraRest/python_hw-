import itertools
import time

class TrafficLight:
    __color = [["Красный", [7, 31]], ["Желтый", [2, 33]], ["Зеленый", [5, 32], ["Желтый", [2, 33]]]]

    def running(self):
        for Light in itertools.cycle(self.__color):
            print(f"\r033[{Light[1][1]}m\033[1m{Light[0]}\033[0m", end="")
            time.sleep(Light[1][0])
TrafficLight_1 = TrafficLight()
TrafficLight_1.running()
