
class ClassroomAgent:
    def __init__(self):
        self.previous_mode = None
    def act(self, temp, occupied):
        if not occupied:
            target_mode = "ECO"
        elif temp > 26:
            target_mode = "COOL"
        elif temp < 20:
            target_mode = "WARM"
        else:
            target_mode = "IDLE"
        previous_mode = self.previous_mode
        if target_mode != previous_mode:
            command = "SEND"
        else:
            command = "NO SEND"
        self.previous_mode = target_mode
        return previous_mode, target_mode, command
agent = ClassroomAgent()
percepts = [
    (29, True),
    (29, True),
    (20, True),
    (26, True),
    (19, True),
    (29, False)
]
for step, percept in enumerate(percepts, 1):
    previous, target, command = agent.act(*percept)
    print(
        step,
        "Previous mode:", previous,
        "Percept:", percept,
        "Target:", target,
        "Outcome:", command
    )
