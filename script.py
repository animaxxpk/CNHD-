input_file = "channels.txt"
output_file = "HDTv.m3u8"

with open(input_file, "r", encoding="utf-8") as f:
    data = f.read()

# clean M3U build
m3u = "#EXTM3U\n" + data.strip()

with open(output_file, "w", encoding="utf-8") as f:
    f.write(m3u)

print("AUTO IPTV UPDATED")
