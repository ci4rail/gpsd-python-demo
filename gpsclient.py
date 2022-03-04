import gpsd

# Connect somewhere else
gpsd.connect(host="172.17.0.1", port=2947)

# Get gps position
packet = gpsd.get_current()

# See the inline docs for GpsResponse for the available data
print(packet.position())
