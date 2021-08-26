import sys

for line in sys.stdin:

    line = line.strip()
    unpacked = line.split(",")
    incident_type=unpacked[1]
    vin_number=unpacked[2] 
    make = unpacked[3] 
    year = unpacked[5]
    
    
    print ('%s\t%s' % (vin_number, (incident_type, make, year)))
