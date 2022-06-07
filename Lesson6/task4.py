class Car:
    is_police = False

    def __init__(self, name, color, speed):
        self.speed = speed
        self.color = color
        self.name = name
        print(f"Автомобиль {self.name}, имеет {self.color} цвет")

    def go(self, speed=20):
        self.speed = speed
        print(f"Автомобиль {self.name} поехала")

    def stop(self):
        self.speed = 0
        print(f"Автомобиль {self.name} остановился")

    def turn(self, direction):
        print(f'Автомобиль {self.name} повернула {"налево" if direction == 0 else "направо"}')

    def show_speed(self):
        print(f'Автомобиль {self.name} едет со скоростью {self.speed} км/ч')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Автомобиль {self.name} превышает скорость')
        else:
            return f'Автомобиль {self.name} едет со скоростью {self.speed} км/ч'


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Автомобиль {self.name} превышает скорость')
        else:
            return f'Автомобиль {self.name} едет со скоростью {self.speed} км/ч'


class SportCar(Car):
    pass


class PoliceCar(Car):
    is_police = True


town_car = TownCar("Opel", "голубой", 85)
town_car.go()
town_car.stop()
town_car.turn(1)
town_car.show_speed()

work_car = WorkCar("Mitsubishi", "белый", 37)
work_car.go()
work_car.stop()
work_car.turn(1)
work_car.show_speed()

police_car = PoliceCar("KIA", "белый", 60)
police_car.go()
police_car.stop()
police_car.turn(0)
police_car.show_speed()

sport_car = SportCar("Ferrari", "красный", 170)
sport_car.go()
sport_car.stop()
sport_car.turn(0)
sport_car.show_speed()
