# 🟣 Purple Team Simulation

from red.attacker import simulate_attack
from blue.detector import detect
from blue.responder import respond
from purple.optimizer import improve_detection

print("=== Purple Team Simulation ===\n")

# Step 1: Red Team attack
logs = simulate_attack()

# Step 2: Blue Team detection + response
alerts = []

for log in logs:
    alert = detect(log)

    if alert:
        print(alert)
        action = respond(alert)
        print(action)
        alerts.append(alert)

# Step 3: Purple Team improvement
improve_detection(logs, alerts)
