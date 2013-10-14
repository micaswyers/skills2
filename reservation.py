"""
Reservation finder

Along with this file, you'll find two files named units.csv and reservations.csv 
with fields in the following format

location_id, unit_size
location_id, reservation_start_date, reservation_end_date

You will write a simple application that manages a reservation system. 
It will have two commands, 'available' and 'reserve' with the following behaviors:

available <date> <number of occupants> <length of stay>
This will print all available units that match the criteria. 
Any unit with capacity equal or greater to the number of occupants will be printed out.

Example:
SeaBnb> available 10/10/2013 2 4
Unit 10 (Size 3) is available
Unit 20 (Size 2) is available

reserve <unit number> <start date> <length of stay>
This creates a record in your reservations that indicates the unit has been reserved. 
It will print a message indicating its success.

A reservation that ends on any given day may be rebooked for the same evening, ie:
    
    If a reservation ends on 10/10/2013, 
    a different reservation may be made starting on 10/10/2013 as well.

Example:
SeaBnb> reserve 10 10/11/2013 3 
Successfully reserved unit 10 for 3 nights

Reserving a unit must make the unit available for later reservations. Here's a sample session:

SeaBnb> available 10/10/2013 2 4
Unit 10 (Size 3) is available
Unit 20 (Size 2) is available
SeaBnb> reserve 10 10/11/2013 3 
Successfully reserved unit 10 for 3 nights
SeaBnb> available 10/10/2013 2 4
Unit 20 (Size 2) is available
SeaBnb> reserve 10 10/11/2013 3 
Unit 10 is unavailable during those dates
SeaBnb> quit

Notes:
Start first by writing the functions to read in the csv file. 
These have been stubbed for you. 
Then write the availability function, then reservation. 
Test your program at each step (it may be beneficial to write 
    tests in a separate file.)
Use the 'reservations' variable as your database. 
Store all the reservations in there, including the ones from the new ones you will create.

The datetime and timedelta classes will be immensely helpful here, as will the strptime function.
"""

import sys
import datetime
import csv

def parse_one_record(line):
    """Take a line from reservations.csv and return a dictionary representing that record. 
    (hint: use the datetime type when parsing the start and end date columns)"""
    d = {}
    unit = line[0]
    sdate = datetime.datetime.strptime(line[1].strip(), "%m/%d/%Y")
    edate = datetime.datetime.strptime(line[2].strip(), "%m/%d/%Y") 
    #format times??
    d[unit] = d.get(unit, (sdate, edate))

    return d

def read_units(file):
    """Read in the file units.csv and returns a list of all known units."""
    unit_list = []
    with open(file) as csvfile:
        info = csv.reader(csvfile)
        for row in info:
            unit_list.append(row)
    return unit_list

def read_existing_reservations(file):
    """Reads in the file reservations.csv and returns a list of reservations."""
    reservation_list = []
    with open(file) as csvfile:
        info = csv.reader(csvfile)
        for row in info:
            reservation_list.append(row)
    return reservation_list

def available(units, reservations, start_date, occupants, stay_length):
    proposed_start_date = datetime.datetime.strptime(start_date.strip(), "%m/%d/%Y")
    proposed_end_date = proposed_start_date + datetime.timedelta(int(stay_length))

    reservation_dict = {}
    for line in reservations:
        one_reservation = parse_one_record(line)
        # print one_reservation
        key = one_reservation.keys()[0]
        dates = one_reservation.values()
        reservation_dict[key] = reservation_dict.get(key, [])
        reservation_dict[key].extend(dates)

    for item in units:
        unit = item[0]
        occupancy = int(item[1])
     
        if occupancy >= int(occupants): #if a unit doesn't have enough rooms

            if reservation_dict.has_key(unit): #if the unit is already in the dictionary of reserved units
                reserved_dates_list = reservation_dict[unit] #pulls up the list of dates reserved for the given unit

                for date_pair in reserved_dates_list:
                    reserved_start_date = date_pair[0]
                    reserved_end_date = date_pair[1]

                    if not ((proposed_end_date <= reserved_start_date) or (proposed_start_date >= reserved_end_date)):
                        #if the proposed dates overlap with the reservation dates
                        break
                else: #used for-else 
                    print "Unit %s (Size %d) is available." % (unit, occupancy)

            else:
                print "Unit %s (Size %d) is available." % (unit, occupancy)
                    #end, you stupid loop! Rawr!

def reserve(units, reservations, unit_id, start_date, stay_length):
    print "Successfully reserved"

def main():
    units = read_units() #units is the list of all units 
    reservations = read_existing_reservations()  #reservations is the existing reservations

    while True:
        command = raw_input("SeaBnb> ")
        cmd = command.split()
        if cmd[0] == "available":
            # look up python variable arguments for explanation of the *
            available(units, reservations, *cmd[1:])
        elif cmd[0] == "reserve":
            reserve(units, reservations, *cmd[1:])
        elif cmd[0] == "quit":
            sys.exit(0)
        else:
            print "Unknown command"

if __name__ == "__main__":
    main()
