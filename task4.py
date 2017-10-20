import requests
import .create-ticket
import .get-network-devices
import .get-network-hosts



def getnetworkdevicecount():
        count=0
        for i in getNetworkDevices.r_json:
            count+=1
        print(count)
