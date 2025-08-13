from os import popen as osPopen
from re import search as reSearch
import numpy as np
import json

if __name__ == "__main__":
    # PING, LOST, ORDER
    with open("dnsdata.json", "r") as f:
        PUBLIC_DNS = json.load(f)
    arrayDNS = np.array([[], [], []])
    chooseBandwith = input("Input your bandwith (Recommended is 32) : ")
    if chooseBandwith != "" and chooseBandwith != "0":
        chooseBandwith = f"-l {chooseBandwith}"
    print("\n")
    for i in PUBLIC_DNS:
        print(f"Testing : {i}")
        with osPopen(f"ping {PUBLIC_DNS[i]} {chooseBandwith} -n 10") as v:
            v = v.read()    
            avg_match = reSearch(r"Average = (\d+)", v)
            lost_match = reSearch(r"(\d+)% loss", v)
            if avg_match and lost_match:
                avg = int(avg_match.group(1))
                lost = int(lost_match.group(1))
                arrayDNS = np.append(
                    arrayDNS, [
                        [avg],
                        [lost],
                        [i]
                    ], axis=1)
                print(f"{avg} ms, {lost}% Lost\n\n")
            else:
                print("Couldn't connect to DNS Server\n\n")
    try:
        ind = np.argmin(arrayDNS[0])
        inf = arrayDNS[2][ind]
        print(
            f"Best DNS for you is : {inf}, {str(arrayDNS[0][ind])}ms, {str(arrayDNS[1][ind])}% lost, {PUBLIC_DNS[inf]}!"
        )
    except:
        print("No DNS servers were reachable.")
    input("Press Enter To Exit : ")
