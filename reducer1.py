import sys

vehicle_info = {}

def flush():
    for key in vehicle_info.keys():
        print ('%s\t%s' % ((vehicle_info[key]["make"],vehicle_info[key]["year"]),vehicle_info[key]["accident_count"]))

for line in sys.stdin:
    line = line.strip()
    vin_num, values = line.split('\t')
    val_arr = [val.replace("'","") .replace("(","").replace(")","") for val in values.split(",")]

    incident_type = val_arr[0]
    current_make = val_arr[1]
    current_year = val_arr[2]

    if vin_num not in vehicle_info:
        vehicle_info[vin_num] = {"make":None,"year":None,"accident_count":0}

    if incident_type == "I":
        vehicle_info[vin_num]["make"] = current_make
        vehicle_info[vin_num]["year"] = current_year

    if incident_type == "A":
        vehicle_info[vin_num]["accident_count"] += 1
	
flush()