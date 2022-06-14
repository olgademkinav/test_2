import time


class TrafficLight:
    __color = ['red', 'yellow', 'green']

    def running(self):
        self.__color = 'red'
        print(self.__color)
        time.sleep(7)
        self.__color = 'yellow'
        print(self.__color)
        time.sleep(3)
        self.__color = 'green'
        print(self.__color)
        time.sleep(7)


traffic = TrafficLight()
traffic.running()
