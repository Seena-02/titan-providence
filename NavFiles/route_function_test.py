import osmnx as ox
import networkx as nx
import folium
#from marker_and_gps_PC import gps_module
from route_function import make_route

#==================================BASIC WAYPOINT TO WAYPOINT NAV, NO AI INTERACTIONS=========================================


ox.settings.log_console=True
ox.settings.use_cache=True

#define the start and end locations in latlng
#Route made is from front of TSU to the library
#start_latlng = (37.78497,-122.43327)
#end_latlng = (37.78071,-122.41445)

shortest_route, list_of_x, list_of_y = make_route(37.78497,-122.43327,37.78071,-122.41445 )

current_x, current_y = gps_module() #current latitude and Longitude, Destination will be the last element of waypoint lists

print("List of X")
print(list_of_x)
print(len(list_of_x))

print("List of Y")
print(list_of_y)
print(len(list_of_y))
#In the example, the last element of the lists is index 54

while current_x != list_of_x[54] and current_y != list_of_y[54]: #while robot is not at its destination
    for i in list_of_x: #list of x and y will always have the same number of indecies
        bearing = ox.bearing.calculate_bearing(current_x, current_y, list_of_x[i], list_of_y[i]) #find bearing in degrees between current location and next waypoint
        while bearing != robot_bearing:
            if bearing > 180 and bearing < 360:
                #turn left
            if bearing < 180 and bearing > 0:
                #turn right
        while current_x != list_of_x[i] and current_y != list_of_y[i]: #while robot is not at the next waypoint
            #head forward
