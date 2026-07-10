# WRITE YOUR SOLUTION HERE:
class WeatherStation:
    def __init__(self, name: str):
        self.__name=name
        self.__observations=[]
        
    def add_observation(self, observation: str):
        self.__observations.append(observation)

    def latest_observation(self):
        if not self.__observations:
            return ""
        else:
            return self.__observations[-1]
        
    def number_of_observations(self):
        return len(self.__observations)
    
    def __str__(self):
        return f"{self.__name}, {self.number_of_observations()} observations"
    

