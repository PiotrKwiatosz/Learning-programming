# Przegrana bitwa
# Demonstruje przerazajaca petle nieskonczona

print("Twoj samotny bohater jest otoczony przez ogromna armie trolli.")
print("Wielka masa isch zgnilozielonych cial rozciaga sie az po horyzont.")
print("Bohater wyjmuje miecz z pochwy, gotow do stoczenia swej ostatniej walki.\n")

health = 10
trolls = 0
damage = 3

while health != 0:
    trolls += 1
    health -= damage

    print("Bohater pokonuje zlego trolla, " \
        "ale odnosi obrazenia i traci", damage, "punkty zdrowia.\n")
        
print("Twoj bohater walczyl dzielnie i pokonal", trolls, "trolli.")
print("Lecz niestety Twoj bohater juz nie zyje.")

input("\n\nAby zakonczyc program, nacisnij klawisz ENTER.")