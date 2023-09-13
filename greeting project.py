import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
t1 = int(time.strftime("%H"))

if t1 >=5 and t1 <=12  :
    print("good morning")
elif t1 >= 12 and t1 <= 17:
    print("good afternoon")
elif t1 >=17 and t1 <= 20 :
    print("good evening")
elif t1 >=20 and t1 <= 24:
    print("good night")
else:
        ("thanks")