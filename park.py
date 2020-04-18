import time
import threading
from random import randint


class Car(threading.Thread):
    def __init__(self, station, num):
        super(Car, self).__init__()
        self.name = f'Car #{num}'
        self.parked = True
        self.capacity = 5
        self.atStation = True
        self.filled = False
        self.numPeople = 0
        self.station = station

    def ride(self):
        print(f'{self.name} starting ride')
        time.sleep(2)
        print(f'{self.name} finished ride')
        self.filled = False
        self.parked = True
        self.numPeople = 0

    def loadPerson(self):
        self.numPeople += 1
        if self.numPeople == self.capacity:
            self.filled = True


class Station(threading.Thread):
    def __init__(self, numCars):
        super(Station, self).__init__()
        self.cars = [Car(self, i) for i in range(numCars)]
        self.freeCars = self.cars
        self.busyCars = []
        self.numCars = numCars
        self.numPpl = 0
        self.lock = threading.Condition()
        self.lock.acquire()
        for car in self.cars:
            car.start()

    def run(self):
        print(f'Running station thread')

    def simulate(self):
        self.start()
        for i in range(22):
            self.spawnPerson(i)
            time.sleep(randint(0, 3))
            with self.lock:
                print('Checking for parked cars')
                self.lock.wait(0.1)
                    
                print('Done checking')

    def spawnPerson(self, i):
        print(f'Spawned person {i}')
        self.numPpl += 1
        self.freeCars[0].loadPerson()
        if (self.freeCars[0].filled):
            with self.freeCars[0].lock:
                self.freeCars[0].lock.notify()
            self.busyCars.append(self.freeCars[0])
            self.freeCars = self.freeCars[1:]


Station(10).simulate()
