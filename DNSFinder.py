from os import popen as osPopen
from re import search as reSearch
from subprocess import call


PUBLIC_DNS = {
    "Google": "8.8.8.8",
    "Control D": "76.76.2.0",
    "Quad9": "9.9.9.9",
    "Cloudflare": "1.1.1.1",
    "Alternate DNS": "76.76.19.19",
    "AdGuard DNS": "94.140.14.14",
    "CleanBrowsing": "185.228.168.9",
    "OpenDNS Home": "208.67.222.222",
    "Comodo Secure DNS": "8.26.56.26",
    "Verisign": "64.6.64.6",
    "Yandex DNS": "77.88.8.8",
    "DNS.Watch": "84.200.69.80",
    "Level 3": "209.244.0.3",
    "UncensoredDNS": "91.239.100.100",
    "Next DNS": "45.90.28.231",
}

if __name__ == "__main__":
    # PING, LOST, ORDER
    arrayDNS = [[], [], []]
    chooseBandwith = input("Input your bandwith (Recommended is 32) : ")
    if chooseBandwith != "" and chooseBandwith != "0":
        chooseBandwith = " -l " + chooseBandwith
    print("\n------------------------------------------------------------\n")
    for i in PUBLIC_DNS:
        print("Testing : " + i)
        v = osPopen("ping " + PUBLIC_DNS[i] + chooseBandwith).read()
        try:
            arrayDNS[0].append(int(reSearch(r"\d+", v[v.find("Average = ") :]).group()))
            arrayDNS[1].append(int(reSearch(r"\d+", v[v.find(" (") :]).group()))
            arrayDNS[2].append(i)
            print(
                str(arrayDNS[0][len(arrayDNS[0]) - 1])
                + "ms, "
                + str(arrayDNS[1][len(arrayDNS[0]) - 1])
                + "% Lost\n\n------------------------------------------------------------\n"
            )
        except:
            print(
                "Coudn't connect to DNS Server\n------------------------------------------------------------\n"
            )
    ind = arrayDNS[0].index(min(arrayDNS[0]))
    inf = arrayDNS[2][ind]
    print(
        "Best DNS for You is : {0}, {1}ms, {2}% lost, {3}!".format(
            inf, str(arrayDNS[0][ind]), str(arrayDNS[1][ind]), PUBLIC_DNS[inf]
        )
    )
    input("Press Enter To Exit : ")
