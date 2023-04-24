available_parts = ['power cord', 'batteries', 'sensor', 'Esp32', 'usb cable' ,'lora module', 'soldering iron']

requested_parts = ['arduino', 'lora module', 'soldering iron', 'lead',]
final_list  = []

for requested_part in requested_parts:
    if requested_part in available_parts:
        print(f"adding {requested_part}")
        #final_list.append(requested_part)
        #print(f"final content available parts: \n{requested_part}")

print("\nFinished making your list")

# adding lora module
# adding soldering iron

# Finished making your list

