# 🟣 Detection improvement engine

def improve_detection(logs, alerts):

    print("\n=== Purple Team Improvement ===\n")

    # Detect missed events
    for log in logs:
        if "PRIVILEGE ESCALATION" in log:
            print("[IMPROVEMENT] Add rule for privilege escalation detection")

    # Summary
    print("\nTotal alerts detected:", len(alerts))
