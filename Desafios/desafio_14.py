from time import sleep

print("Agora com break:")
for i in range(1, 11):
    sleep(0.25)
    if i == 5:
        sleep(0.25)
        print("Interrompido na 5ª iteração")
        break
    print(i)
sleep(0.5)

print("Agora com continue:")
for i in range(1, 11):
    sleep(0.25)
    if i == 5:
        continue
    print(i)