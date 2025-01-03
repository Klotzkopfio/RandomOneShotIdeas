import random

# Listen mit zufälligen Elementen für den One-Shot
plots = [
    "Die Spieler müssen ein vermisstes Artefakt aus einer verfluchten Ruine bergen.",
    "Ein kleines Dorf wird von mysteriösen Kreaturen heimgesucht, und die Spieler müssen herausfinden, warum.",
    "Ein berühmter Magier hat die Spieler angeheuert, um seinen entführten Lehrling zu retten.",
    "Eine alte Prophezeiung sagt, dass die Helden die Welt vor einer herannahenden Katastrophe retten müssen.",
    "Die Spieler wachen ohne Erinnerung in einer fremden Welt auf und müssen sich ihren Weg zurück erkämpfen."
]

locations = [
    "Ein verlassenes Schloss am Rande eines dunklen Waldes.",
    "Eine unterirdische Höhle voller Fallen und Geheimnisse.",
    "Ein geschäftiger Marktplatz in einer magischen Stadt.",
    "Ein verwunschener Friedhof unter einem immerwährenden Vollmond.",
    "Ein schwebendes Luftschiff, das von Banditen übernommen wurde."
]

enemies = [
    "Ein mächtiger Nekromant und seine untoten Diener.",
    "Eine Horde von Goblins, die von einem Troll angeführt wird.",
    "Ein Drache, der sein Nest vor Eindringlingen schützt.",
    "Ein Kult, der ein dunkles Ritual durchführt.",
    "Ein verräterischer Adliger mit einer Gruppe von Söldnern."
]

twists = [
    "Der Auftraggeber der Spieler ist eigentlich der Bösewicht.",
    "Die vermeintlichen Gegner entpuppen sich als Opfer eines Fluchs.",
    "Ein mächtiger Verbündeter stellt sich gegen die Gruppe.",
    "Die Spieler entdecken ein Portal zu einer anderen Dimension.",
    "Die Zeit läuft ab, und sie müssen innerhalb von einer Stunde Erfolg haben."
]

def generate_one_shot():
    plot = random.choice(plots)
    location = random.choice(locations)
    enemy = random.choice(enemies)
    twist = random.choice(twists)

    print("=== D&D One-Shot Generator ===")
    print(f"Plot: {plot}")
    print(f"Schauplatz: {location}")
    print(f"Gegner: {enemy}")
    print(f"Wendung: {twist}")

if __name__ == "__main__":
    generate_one_shot()
