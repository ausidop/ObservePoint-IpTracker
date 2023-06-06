ipAddresses = dict()

def requestHandled(ipAddress: str):
    ipAddresses[ipAddress] = ipAddresses.setdefault(ipAddress, 1) + 1

def top100():
    top100 = sorted(ipAddresses, key=lambda x: x[1], reverse=True)
    if len(top100) >= 100:
        return top100[:100]
    return top100

def clear():
    stack = dict()