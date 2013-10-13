from reservation import *


reservations = read_existing_reservations('reservations.csv')

units = read_units('units.csv')
# print "*" * 20
print "Available:", available(units, reservations, '10/11/2015', '1', '5')

# parse_one_record(['6', ' 9/27/2013', ' 12/1/2013'])
