from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, temperature):
        pass

class Subject(ABC):
    @abstractmethod
    def register_observer(self, observer):
        pass
    
    @abstractmethod
    def remove_observer(self, observer):
        pass
    
    @abstractmethod
    def notify_observers(self):
        pass

class TemperatureSensor(Subject):
    def __init__(self):
        self._temperature = 0.0
        self._observers = []
    
    def register_observer(self, observer):
        self._observers.append(observer)
    
    def remove_observer(self, observer):
        self._observers.remove(observer)
    
    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._temperature)
    
    def set_temperature(self, temperature):
        self._temperature = temperature
        self.notify_observers()

class CurrentConditionsDisplay(Observer):
    def __init__(self):
        self._current_temperature = 0.0
    
    def update(self, temperature):
        self._current_temperature = temperature
        self.display()
    
    def display(self):
        print(f"Suhu saat ini: {self._current_temperature}°C")

class StatisticsDisplay(Observer):
    def __init__(self):
        self._temperatures = []
        self._max_temp = float('-inf')
        self._min_temp = float('inf')
        self._total_temp = 0.0
    
    def update(self, temperature):
        self._temperatures.append(temperature)
        self._total_temp += temperature
        
        if temperature > self._max_temp:
            self._max_temp = temperature
        
        if temperature < self._min_temp:
            self._min_temp = temperature
        
        self.display()
    
    def display(self):
        average = self._total_temp / len(self._temperatures)
        print(f"Suhu -> Rata-rata: {average:.1f}°C, "
              f"Maksimum: {self._max_temp}°C, "
              f"Minimum: {self._min_temp}°C")

# main
def main():
    sensor = TemperatureSensor()
    current_display = CurrentConditionsDisplay()
    stats_display = StatisticsDisplay()
    

    sensor.register_observer(current_display)
    sensor.register_observer(stats_display)
    

    for i in range(3):
        try:
            temp = float(input(f"\nMasukkan suhu ke-{i+1} (°C): "))
            sensor.set_temperature(temp)
        except ValueError:
            print("Input salah masukkan angka ")
            continue

if __name__ == "__main__":
    main()