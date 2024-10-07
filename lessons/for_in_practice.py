dog_names: list[str] = ["Louie", "Bo", "Bear"]

for elem in dog_names:
    print(f"Good boy, {elem}!")

names: list[str] = ["Alyssa", "Janet", "Vrinda"]

for idx in range(0, len(names)):
    print(f"{idx}: {names[idx]}")

for i, name in enumerate(names):
    print(f"{i}: {name}")
