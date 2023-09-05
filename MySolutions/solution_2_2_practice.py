#solution to ex 2_2
import MySolutions.read_ride_memory as readrides
rows = readrides.read_rides_as_dicts('Data/ctabus.csv')
from collections import Counter
#1. How many bus routes exist in Chicago
set_of_routes = {row['route']for row in rows}
num_of_routes = len(set_of_routes)
print(num_of_routes)


#2. How many people rode the number 22 bus on Feburary 2 2011? What about any route on any date of your choosing?
riders = Counter()
for row in rows:
    riders[[row['route'],[row['date']]]+=row['rides']

bus22 = riders['22']
print(bus22)




#3. what is the total number of rides taken on each bust route?




#4 what five bus routes had the greates ten-year increas in ridership from 2001 to 2011


