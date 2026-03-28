# 🛡️ Response

def respond(alert):

    if "Brute force" in alert:
        return "[ACTION] Block IP"

    if "Compromise" in alert:
        return "[ACTION] Lock account"

    if "Data access" in alert:
        return "[ACTION] Alert SOC"

    return "[ACTION] Monitor"
