# %% Opdracht 1
Naam = input("Wat is je naam?\n")

Leeftijd = input("Wat is je leeftijd?\n")

print(f"Hallo {Naam}, je bent {Leeftijd} jaar oud.")

# %% Opdracht 2 Kubus

Hoogte = input("Wat is de hoogte van de kubus in cm?\n")

print(f"De hoogte van de kubus is {Hoogte} cm.")

Breedte = input("Wat is de breedte van de kubus in cm?\n")

print(f"De breedte van de kubus is {Breedte} cm.")

# De int functie wordt gebruikt om de string input om te zetten naar een integer zodat we wiskundige berekeningen kunnen uitvoeren.
Volume = int(Hoogte) * int(Breedte) ** 2

print(f"Het volume van de kubus is {Volume/1000000} m³.")

# %% Opdracht 2 Cilinder

Diameter = input("Wat is de diameter van de cilinder in cm?\n")

Hoogte = input("Wat is de hoogte van de cilinder in cm?\n")

volume_cilinder = 3.14 * (int(Diameter)/2) ** 2 * int(Hoogte)

print(f"Het volume van de cilinder is {volume_cilinder/1000000} m³.")

# %% Opdracht 3

Films = ["The Matrix", "Inception", "Interstellar", "The Dark Knight", "Pulp Fiction"]

while():
    Selectie = int(input("Wil je een film toevoegen of verwijderen? 0 voor verwijderen en 1 voor toevoegen\n"))

    if Selectie == 1:
        Film = input("Welke film wil je toevoegen?\n")
        Plaats = int(input("Op welke plaats?"))
        Films.insert(Plaats, Film)

    # Voor het verwijderen van de films wordt de remove functie gebruikt
    if Selectie == 0:
        Film = input("Welke film wil je verwijderen?\n")
        Films.remove(Film)
    print(Films)

print(Films)



# %%
