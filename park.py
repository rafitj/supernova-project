import time
import threading
from random import randint


class Car(threading.Thread):
    def __init__(self, station, num):
        super(Car, self).__init__()
        self.name = f'Car #{num}'
        self.parked = True
        self.capacity = 5



class Station(threading.Thread):
    def __init__(self, numCars):
        super(Station, self).__init__()
        self.cars = [Car(self, i) for i in range(numCars)]
        self.freeCars = self.cars
        self.busyCars = []
        self.numCars = numCars
        self.numPpl = 0

    # def simulate(self):
    #     self.start()
    #     for i in range(22):
    #         self.spawnPerson(i)
    #         time.sleep(randint(0, 3))

    def spawnPerson(self, i):
        print(f'Spawned person {i}')
        self.numPpl += 1
        self.freeCars[0].loadPerson()
        if (self.freeCars[0].filled):
            self.busyCars.append(self.freeCars[0])
            self.freeCars = self.freeCars[1:]