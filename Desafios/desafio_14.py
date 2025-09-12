from time import sleep

for i in range(1, 11):
    sleep(0.25)
    if i == 5:
        break
    print(i)
for i in range(1, 11):
    if i == 5:
        continue
    print(i)