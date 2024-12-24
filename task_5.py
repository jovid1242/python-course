class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius): 
        return (celsius * 9/5) + 32

    @classmethod
    def from_kelvin(cls, kelvin): 
        celsius = kelvin - 273.15
        return cls(celsius)

    def __init__(self, celsius): 
        self.celsius = celsius

    def __str__(self):
        return f"{self.celsius}°C"
 
temp = TemperatureConverter(25)
print(temp.celsius_to_fahrenheit(25))  
 
kelvin_temp = TemperatureConverter.from_kelvin(300)
print(kelvin_temp)   
