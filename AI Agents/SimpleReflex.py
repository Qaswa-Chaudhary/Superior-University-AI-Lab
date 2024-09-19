# Simple Reflex Aagent 
class SimpleReflex:
    def __init__(self, temp):
        self.desired_temp = temp
        
    def perceive(self, current_temp):
        return current_temp
   
    def act(self, current_temp):
        if current_temp < self.desired_temp:
            action = "Turn on the heater"
        elif current_temp == self.desired_temp:
            return "temprature is alreay set"
        else:
            action = "Turn off the heater"
        return action

rooms = {
    "living room": 30,
    "kitchen": 40,
    "kids room": 22 ,
    "bedroom": 20
}

desired_temperature = 22
agent = SimpleReflex(desired_temperature)

for room, temp in rooms.items():
    current_temp = agent.perceive(temp)
    action = agent.act(current_temp)
    print(f"{room} current temperature: {current_temp} \nAction: {action}")

    

