produto = 1000 # mls
dose = int(input("Digite a dose em mls que você deseja administrar: "))
dias = produto / dose
print(f"Você pode administrar {dose}ml por {dias:.0f} dias.")