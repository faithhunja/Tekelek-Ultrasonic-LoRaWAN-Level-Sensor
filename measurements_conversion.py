#sample_payload = "1000000001121B7701131BAA01121BA90114F274"

def ullage(payload):
        current_ullage = int(payload[8:12], 16)
        print("Current ullage = ",current_ullage,"cm")
        current_temp = int(payload[12:14], 16)
        if current_temp >= 50:
            print("Current ullage = ",-(256 - current_temp),"cm")
        else:
            print("Current temperature = ",current_temp,"°C")

        previous_ullage = int(payload[16:20], 16)
        print("Previous ullage = ",previous_ullage,"cm")
        previous_temp = int(payload[20:22], 16)
        if previous_temp >= 50:
            print("Previous temperature = ",-(256 - previous_temp),"°C")
        else:
            print("Previous temperature = ",previous_temp,"°C")

        previous1_ullage = int(payload[24:28], 16)
        print("Previous ullage(1) = ",previous1_ullage,"cm")
        previous1_temp = int(payload[28:30], 16)
        if previous1_temp >= 50:
            print("Previous temperature(1) = ",-(256 - previous1_temp),"°C")
        else:
            print("Previous temperature(1) = ",previous1_temp,"°C")

        previous2_ullage = int(payload[32:36], 16)
        print("Previous ullage(2) = ",previous2_ullage,"cm")
        previous2_temp = int(payload[36:38], 16)
        if previous2_temp >= 50:
            print("Previous temperature(2) = ",-(256 - previous2_temp),"°C")
        else:
            print("Previous temperature(2) = ",previous2_temp,"°C")

