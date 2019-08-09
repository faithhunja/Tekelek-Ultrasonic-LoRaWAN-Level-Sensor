#sample_payload = "300000010106360063006300040600181BAA"

def ullage(payload):
      
        current_ullage = int(payload[28:32], 16)
        print("Current ullage = ",current_ullage,"cm")
        current_temp = int(payload[32:34], 16)
        if current_temp >= 50:
            print("Current ullage = ",-(256 - current_temp),"cm")
        else:
            print("Current temperature = ",current_temp,"°C")
        remaining_battery = int(payload[20:22], 16)
        print("Remaining battery = ",remaining_battery,"%")
        schedule_transmit_period = int(payload[26:28], 16)
        print("Schedule transmit period = ",schedule_transmit_period,"hrs")

  
           