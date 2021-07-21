from speedtest import Speedtest

print ("Testing your connection...")
st = Speedtest()

print("Download Speed", round(st.download()/2**20, 2), "Mbps")
print("Upload Speed", round(st.upload()/2**20, 2), "Mbps")
print("Ping", round(st.results.ping), "ms")

# 2^10 -    1024 bytes - stands for 1 KiloByte
# 2^20 - 1048576 bytes - stands for 1 MegaByte