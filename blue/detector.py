# Detection

def detect(log):

    if "FAILED LOGIN" in log:
        return "[ALERT] Brute force"

    if "LOGIN SUCCESS - admin" in log:
        return "[ALERT] Compromise"

    if "FILE ACCESS" in log:
        return "[ALERT] Data access"

    return None
