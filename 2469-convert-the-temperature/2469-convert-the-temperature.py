class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        # declaring an array where the resulting tempratures will be stored
        temprature = []
        kelvin = celsius + 273.15
        fahrenheit = celsius * 1.80 + 32.00
        # appending the kelvin and fahrenheit into the array
        temprature.append(kelvin)
        temprature.append(fahrenheit)
        
        return temprature