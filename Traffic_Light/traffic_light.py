from enum import Enum    

NEXT_LIGHT = {
    "RED": "GREEN",
    "GREEN": "YELLOW",
    "YELLOW": "RED"
}

class TrafficLight(Enum):
    RED = 30
    GREEN = 25
    YELLOW = 5
    
    def next(self):
        if self == TrafficLight.RED:
            return TrafficLight.GREEN
        elif self == TrafficLight.GREEN:
            return TrafficLight.YELLOW
        else:
            return TrafficLight.RED

    def display(self):
        print(f"{self.name} ({self.value}s)")
        return True

if __name__ == "__main__":
    light = TrafficLight.RED
    for _ in range(6):
        light.display()
        light = light.next()