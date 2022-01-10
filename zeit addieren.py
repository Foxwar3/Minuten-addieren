# Die Stunden und Minuten werden definiert und es wird eine Funktion gemacht, welche dafür sorgt, dass die Minuten bei 60 nicht höher
# gehen sondern die Stunden + 1 und die Minuten zurückgesetzt werden, ähnliches bei 24h.
def uhrzeit_minuten_addieren(stunden, minuten, summand):
    while minuten+summand>60:
        stunden=stunden+1
    while stunden>=24:
        stunden=stunden-24
    print(str(stunden)+"."+str(minuten+summand))

# Hier sind die verschieden Uhrzeiten, welche mit Minuten addiert werden sollen.
uhrzeit_minuten_addieren(17, 32, 8) # 17:32 + 8 Min = 17:40



