# memory to track IP addresses and frequency in dictionary
# IP address as key and visited number in value
import heapq

ipAddresses = dict()


# take IP address string as input and store into the memory
# memory will take IP address as key and frequency of visits as value
def requestHandled(ipAddress):
    ipAddresses[ipAddress] = ipAddresses.setdefault(ipAddress, 1) + 1


# return top 100 ip address with the highest traffic
def top100():
    top100 = heapq.nlargest(100, ipAddresses, key=ipAddresses.get)
    return top100


# clear the memory
def clear():
    stack = dict()
