
if __name__ == "__main__":

    class Vehicle:
        """
        - make (str): Марка автомобиля
        - model (str): Модель автомобиля
        - year (int): Год изготовления
        """
        def __init__(self, make: str, model: str, year: int):
            self.make = make
            self.model = model
            self.year = year

        def display_info(self) -> None:
            """
            Отображение информации о транспортном средстве
            """
            print(str(self))

        def __str__(self) -> str:
            """
            Вернуть читаемый текст о Vehicle
            """
            return f"{self.year}, {self.make}, {self.model}"

        def __repr__(self) -> str:
            """

            """
            return f"Vehicle(make={self.make}, model={self.model}, year={self.year})"


    class Car(Vehicle):
        def __init__(self, make: str, model: str, year: int, capacity_engine: int):
            super().__init__(make, model, year)
            self.capacity_engine = capacity_engine

        def display_info(self) -> str:
            """
            Метод перегружаются для добавления информации об объекте
            """
            return f"{self.make} {self.model} - {self.capacity_engine} capacity_engine"

        def __str__(self) -> str:
            return f"{self.year} {self.make} {self.model} - {self.capacity_engine} capacity_engine"


        def __repr__(self) -> str:
            return f"Car(make={self.make}, model={self.model}, year={self.year}, capacity_engine={self.capacity_engine})"
"""print(Car("a","b",2,3))
car = Car("Toyota", "Corolla", 2022, 4)
car_description = car.display_info()
print(car_description)
print(Car)"""
