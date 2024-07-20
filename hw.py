from multiprocessing import Process
import random
import time

def write_file(filee):
    time.sleep(1)
    r = random.randint(1,100)
    with open(filee,'w') as file:
        file.write(str(r))

start_time1 = time.time()

for i in range(10):#1000
    files = f"r_{i}.txt"
    write_file(files)

end_time1 = time.time()

print(f"время выполнения без мультипроц: {end_time1 - start_time1}")

start_time2 = time.time()

lst = []
for i in range(10):#1000
    files = f"r_{i}.txt"
    p = Process(target=write_file, args=(files,))
    p.start()
    lst.append(p)

for p in lst:
    p.join()


end_time2 = time.time()
print(f"время выполнения с мультипроц: {end_time2 - start_time2}")