from lab2_model import ClassroomAgent

agent = ClassroomAgent()
percepts = [(26.1, True), (26.0, True), (26.1, True), (26.0, True)]

for step, percept in enumerate(percepts, 1):
    old, target, cmd = agent.act(percept[0], percept[1])
    print(step, percept, "Prev:", old, "Target:", target, cmd)