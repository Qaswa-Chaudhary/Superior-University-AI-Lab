
class ModelBase:
    def __init__(self, desired_temp):
        self.desired_temp = desired_temp
        self.temp        = {}
        
    def perceive(self,room,current_temp):
        self.temp[room] = current_temp
        return current_temp

    def act(self, room):
        # Retrieve the current temperature from the internal state
        current_temp = self.temp[room]
        if current_temp < self.desired_temp:
            action = "Turn on the heater"
        elif current_temp == self.desired_temp:
            action = "Temperature is already set"
        else:
            action = "Turn off the heater"
        return action


# Example room temperatures
rooms = {
    "living room": 30,
    "kitchen": 40,
    "kids room": 22,
    "bedroom": 20
}

desired_temperature = 22
agent = ModelBase(desired_temperature)

for room, temp in rooms.items():
    # Perceive the environment and update the internal state
    current_temp = agent.perceive(room, temp)
    # Decide on the action based on the internal model
    action = agent.act(room)
    print(f"{room} current temperature: {current_temp} \nAction: {action}")
