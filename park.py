import time
import threading
from random import randint

class Car(threading.Thread):
    def __init__(self, station, num, carCapacity, rideTime):
        super(Car, self).__init__()
        self.name = f'Car #{num}'
        self.parked = True
        self.capacity = carCapacity
        self.filled = False
        self.numPeople = 0
        self.lock = threading.Condition()
        self.station = station
        self.rideTime = rideTime

    def run(self):
        with self.lock:
            self.lock.wait()
        self.ride()

    def ride(self):
        print(f'{self.name} starting ride')
        time.sleep(self.rideTime)
        print(f'{self.name} finished ride')
        self.filled = False
        self.parked = True
        self.numPeople = 0
        with self.station.lock:
            self.station.lock.notify()

    def loadPerson(self):
        self.numPeople += 1
        if self.numPeople == self.capacity:
            self.filled = True


class Station(threading.Thread):
    def __init__(self, numCars, carCapacity, rideTime):
        super(Station, self).__init__()
        self.cars = [Car(self, i,carCapacity,rideTime) for i in range(numCars)]
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

    def checkParking(self):
        with self.lock:
            print('Checking for parked cars')
            self.lock.wait(0.1)
            print('Done checking')
        print('Car here')
        self.freeCars.append(self.busyCars[0])
        self.busyCars = self.busyCars[1:]

    def simulate(self):
        self.start()
        for i in range(22):
            self.spawnPerson(i)
            time.sleep(randint(0, 3))

    def spawnPerson(self, i):
        print(f'Spawned person {i}')
        self.numPpl += 1
        self.freeCars[0].loadPerson()
        if (self.freeCars[0].filled):
            with self.freeCars[0].lock:
                self.freeCars[0].lock.notify()
            self.busyCars.append(self.freeCars[0])
            self.freeCars = self.freeCars[1:]


class Park(self):
    def __init__(self, numCars = 10, carCapacity = 5, rideTime = 2):
        self.station = Station(numCars, carCapacity, rideTime)

    def simulate(self):
        self.station.simulate()
    
Park().simulate()
