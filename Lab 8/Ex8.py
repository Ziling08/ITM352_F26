
import random

requirements = ["Req 1", "Req 2", "Req 3", "Req 4",
                "Req 5", "Req 6", "Req 7"]

remaining = requirements.copy()

R1 = random.choice(remaining)
remaining.remove(R1)

R2 = random.choice(remaining)

print("Assigned requirements:", R1, "and", R2)
