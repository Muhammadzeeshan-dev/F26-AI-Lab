class ClassroomAgent:
    def __init__(self):
        self.last_mode = None

    def act(self, temp, occupied):
        if not occupied:
            target = "ECO"
        elif temp > 26:
            target = "COOL"
        elif temp < 20:
            target = "WARM"
        else:
            target = "IDLE"

        old = self.last_mode

        if target == self.last_mode:
            command = "NO_COMMAND"
        else:
            command = "SEND_COMMAND"
            self.last_mode = target

        return old, target, command

agent = ClassroomAgent()
percepts = [(29, True), (29, True), (26, True),
            (20, True), (19, True), (29, False)]

for step, percept in enumerate(percepts, 1):
    old, target, cmd = agent.act(percept[0], percept[1])
    print(step, "Percept:", percept, "Prev:", old, "Target:", target, "Action:", cmd)