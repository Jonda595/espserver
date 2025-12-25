import time
import random
import sys

def slow(text, d=0.03):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(d)
    print()

health = 100
level = 1

slow("BOOTING SYSTEM...")
time.sleep(1)
slow("ERROR: REALITY UNSTABLE")
slow("Jsi zavřený v místnosti.\n")

while health > 0:
    slow("=== LEVEL {} ===".format(level))
    slow("Zdraví: {}%".format(health))

    event = random.choice(["hack", "wait", "glitch"])

    if event == "hack":
        slow("Našel jsi terminál.")
        slow("1) Hacknout systém")
        slow("2) Ignorovat")

        choice = input("> ")

        if choice == "1":
            if random.random() > 0.4:
                slow("Hack úspěšný! +10 zdraví")
                health += 10
            else:
                slow("Hack selhal! -20 zdraví")
                health -= 20
        else:
            slow("Terminál se vypnul.")

    elif event == "wait":
        slow("Čekáš...")
        dmg = random.randint(5, 15)
        slow("Realita tě poškozuje: -{} zdraví".format(dmg))
        health -= dmg

    else:  # glitch
        slow("!!! GLITCH !!!")
        time.sleep(0.5)
        slow("OBRAZ SE ROZPADÁ")
        dmg = random.randint(10, 25)
        health -= dmg

    level += 1
    time.sleep(1)

slow("\nSYSTÉM ZKOLABOVAL")
slow("Přežil jsi {} kol.".format(level - 1))
