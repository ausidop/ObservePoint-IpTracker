# memory to track IP addresses and frequency in dictionary
# IP address as key and visited number in value
import heapq

class IP_Tracker:
    def __init__(self):
        self.ipAddresses = dict()

    # take IP address string as input and store into the memory
    # memory will take IP address as key and frequency of visits as value
    def requestHandled(self, ipAddress):
        self.ipAddresses[ipAddress] = self.ipAddresses.setdefault(ipAddress, 1) + 1

    # return top 100 ip address with the highest traffic
    def top100(self):
        top100 = heapq.nlargest(100, self.ipAddresses, key=self.ipAddresses.get)
        return top100

    # clear the memory
    def clear(self):
        self.ipAddresses = dict()