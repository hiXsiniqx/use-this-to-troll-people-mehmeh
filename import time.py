import time, socket, random

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = s.getsockname()[0]
s.close()

for i in range(5, 0, -1):
    print(i)
    time.sleep(1)

print("yay times up :p")
for _ in range(15):
    print("\r" + "".join(random.choice("0123456789.") for _ in ip), end="", flush=True)
    time.sleep(0.1)
print("\r" + ip)