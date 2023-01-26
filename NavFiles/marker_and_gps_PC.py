
import folium
import serial
import time



gps = serial.Serial("COM4", baudrate = 9600)

tooltip = "Click For Details"

def gps_module():
    while True:
        line = gps.readline()
        data = line.decode().split(",")
        if data[0] == "$GPRMC":
            if data[2] == "A":
                curr_lat_nmea = data[3]
                curr_lat_deg = curr_lat_nmea[:2]
                if data[4] =='S':
                    lat = float(curr_lat_deg) * -1
                else:
                    lat = float(curr_lat_deg)
                lat = str(lat).strip('.')
                lat_ddd = curr_lat_nmea[2:10]
                lat_mmm = float(lat_ddd) / 60
                lat_mmm = str(lat_mmm).strip('0.')[:8]
                lat_final = lat + lat_mmm



                curr_long_nmea = data[5]
                curr_long_deg = curr_long_nmea[0:3]
                if data[6] == 'W':
                    long = float(curr_long_deg) * -1
                else:
                    long = float(curr_long_deg)
                long = str(long).strip('.0')
                long_ddd = curr_long_nmea[3:10]
                long_mmm = float(long_ddd) / 60
                long_mmm = str(long_mmm).strip('0.')[:9]
                long_final = long + "." + long_mmm

                print( lat_final, long_final)

                m = folium.Map(location=[lat_final, long_final], zoom_start=9, tiles="Stamen Terrain")

                folium.Marker(
                [lat_final, long_final], popup="<i>Current Location</i>", tooltip=tooltip
                ).add_to(m)

                time.sleep(5)

                m.save("tracker_test.html")

            return lat_final,long_final
    print("end loop")
