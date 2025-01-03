import random

# Listen mit zufälligen Elementen für verschiedene Kategorien
categories = {
    "Fantasy": {
        "plots": [
            "Die Spieler müssen ein vermisstes Artefakt aus einer verfluchten Ruine bergen.",
            "Ein kleines Dorf wird von mysteriösen Kreaturen heimgesucht, und die Spieler müssen herausfinden, warum.",
            "Ein berühmter Magier hat die Spieler angeheuert, um seinen entführten Lehrling zu retten.",
            "Eine alte Prophezeiung sagt, dass die Helden die Welt vor einer herannahenden Katastrophe retten müssen.",
            "Die Spieler wachen ohne Erinnerung in einer fremden Welt auf und müssen sich ihren Weg zurück erkämpfen.",
            "Ein uralter Wächter verlangt, dass die Spieler drei Prüfungen bestehen, um Zugang zu einem mächtigen Schatz zu erhalten.",
            "Ein mysteriöser Nebel verschlingt eine Stadt, und die Spieler müssen das Geheimnis lüften.",
            "Ein Krieg zwischen zwei verfeindeten Fraktionen zwingt die Spieler, Partei zu ergreifen.",
            "Eine alte Festung, die plötzlich von Geistern heimgesucht wird.",
            "Eine mächtige magische Kreatur bittet die Spieler um Hilfe, obwohl sie selbst gefährlich ist."
        ],
        "locations": [
            "Ein verlassenes Schloss am Rande eines dunklen Waldes.",
            "Eine unterirdische Höhle voller Fallen und Geheimnisse.",
            "Ein geschäftiger Marktplatz in einer magischen Stadt.",
            "Ein verwunschener Friedhof unter einem immerwährenden Vollmond.",
            "Ein schwebendes Luftschiff, das von Banditen übernommen wurde.",
            "Ein versunkenes Reich tief unter dem Ozean.",
            "Ein Lavasee mit schwebenden Inseln, die nur durch Magie erreichbar sind.",
            "Ein alter Tempel, der über einem endlosen Abgrund schwebt.",
            "Eine antike Bibliothek, in der die Bücher lebendig sind.",
            "Ein Dorf, das komplett aus Kristallen besteht und von innen leuchtet."
        ],
        "enemies": [
            "Ein mächtiger Nekromant und seine untoten Diener.",
            "Eine Horde von Goblins, die von einem Troll angeführt wird.",
            "Ein Drache, der sein Nest vor Eindringlingen schützt.",
            "Ein Kult, der ein dunkles Ritual durchführt.",
            "Ein verräterischer Adliger mit einer Gruppe von Söldnern.",
            "Ein Rudel Werwölfe, das den Mond anbetet.",
            "Ein mächtiger Dämon, der aus einer anderen Dimension beschworen wurde.",
            "Eine Armee von mechanischen Konstrukten, die von einem wahnsinnigen Erfinder kontrolliert wird.",
            "Ein bösartiger Feenprinz, der die Spieler austricksen will.",
            "Ein riesiges Monster, das aus den Alpträumen der Spieler erwacht."
        ],
        "twists": [
            "Der Auftraggeber der Spieler ist eigentlich der Bösewicht.",
            "Die vermeintlichen Gegner entpuppen sich als Opfer eines Fluchs.",
            "Ein mächtiger Verbündeter stellt sich gegen die Gruppe.",
            "Die Spieler entdecken ein Portal zu einer anderen Dimension.",
            "Die Zeit läuft ab, und sie müssen innerhalb von einer Stunde Erfolg haben.",
            "Ein altes Relikt, das die Spieler finden, hat einen gefährlichen Nebeneffekt.",
            "Die Gruppe wird von einem unerwarteten Sturm in eine fremde Region verschlagen.",
            "Ein Mitglied der Gruppe wird von einer dunklen Macht korrumpiert.",
            "Die Lösung des Problems erfordert das Opfer eines wertvollen Gegenstands.",
            "Die Spieler erfahren, dass sie nur Figuren in einem magischen Spiel eines mächtigen Zauberers sind."
        ]
    },
    "Modern": {
        "plots": [
            "Ein geheimes Regierungsprojekt ist außer Kontrolle geraten, und die Spieler müssen es aufhalten.",
            "Ein mysteriöser Hacker droht, die Stadt ins Chaos zu stürzen.",
            "Eine geheime Organisation hat ein gefährliches Experiment durchgeführt, das gestoppt werden muss.",
            "Die Spieler müssen eine gefährliche Geiselrettung durchführen.",
            "Eine wertvolle Technologie wurde gestohlen, und die Spieler müssen sie zurückholen.",
            "Ein mächtiger Konzern plant, die Stadt zu übernehmen, und nur die Spieler können ihn aufhalten.",
            "Ein fremder Satellit stürzt ab, und die Spieler müssen das Wrack untersuchen.",
            "Ein rätselhafter Stromausfall hat die Stadt lahmgelegt.",
            "Die Spieler werden in ein tödliches Spiel verwickelt, das live gestreamt wird.",
            "Ein verheerendes Experiment hat eine Zombieplage ausgelöst, und die Spieler müssen überleben."
        ],
        "locations": [
            "Ein Hochsicherheitslabor mitten in der Stadt.",
            "Eine abgelegene Villa im Stil der 80er Jahre.",
            "Ein überfülltes Einkaufszentrum während der Feiertage.",
            "Ein stillgelegtes Industriegebiet voller Geheimnisse.",
            "Eine futuristische U-Bahn-Station tief unter der Erde.",
            "Ein verlassenes Kino, das immer noch alte Filme spielt.",
            "Eine Baustelle für ein modernes Megaprojekt.",
            "Eine verlassene Schule, die für Experimente genutzt wurde.",
            "Ein urbaner Park, der überraschend gefährlich ist.",
            "Ein Luxushotel, in dem etwas nicht stimmt."
        ],
        "enemies": [
            "Ein skrupelloser Konzern mit hochgerüsteten Sicherheitskräften.",
            "Ein technikaffiner Terrorist und seine Hacker-Crew.",
            "Ein korrupter Polizist mit einer Bande von Schlägern.",
            "Ein Cyberpunk-Söldner mit erweiterten Fähigkeiten.",
            "Eine kriminelle Untergrundorganisation, die die Stadt kontrolliert.",
            "Ein von einer KI kontrollierter Roboter.",
            "Ein abtrünniger Wissenschaftler mit einem gefährlichen Plan.",
            "Eine rivalisierende Gruppe von Söldnern, die dasselbe Ziel hat.",
            "Ein paranoider Milliardär mit einer Privatarmee.",
            "Ein gefährlicher Schmuggler mit einer Gruppe von Handlangern."
        ],
        "twists": [
            "Die Spieler werden von einem Insider innerhalb ihrer Gruppe verraten.",
            "Die Technologie, die sie retten sollen, ist gefährlicher als angenommen.",
            "Ein unerwarteter Stromausfall erschwert die Mission.",
            "Die Gegner haben eine unerwartete Verbindung zu einem Spielercharakter.",
            "Die Zeit wird knapp, da eine Bombe tickt.",
            "Die Spieler entdecken, dass sie überwacht werden.",
            "Der vermeintliche Bösewicht ist eigentlich ein Opfer.",
            "Die Mission war eine Ablenkung für etwas Größeres.",
            "Ein Spielercharakter hat eine geheime Vergangenheit, die enthüllt wird.",
            "Die Lösung liegt in einem unerwarteten Ort oder Objekt."
        ]
    },
    "Horror": {
        "plots": [
            "Die Spieler müssen einem Spukhaus entkommen, bevor es zu spät ist.",
            "Ein uraltes Monster terrorisiert eine abgelegene Gemeinde.",
            "Ein unheimlicher Kult hat eine dunkle Zeremonie begonnen, die gestoppt werden muss.",
            "Die Spieler sind in einem Albtraum gefangen, aus dem sie erwachen müssen.",
            "Ein mysteriöser Fremder bringt eine tödliche Bedrohung in eine abgeschiedene Region.",
            "Die Spieler werden in einer Zeitschleife gefangen, die immer tödlicher wird.",
            "Ein verlassenes Dorf birgt ein schreckliches Geheimnis.",
            "Ein mysteriöses Artefakt verleiht den Spielern dunkle Kräfte, aber zu einem hohen Preis.",
            "Ein Fluch breitet sich aus, und die Spieler müssen ihn aufhalten.",
            "Ein dämonisches Wesen nutzt die Träume der Spieler, um sie zu manipulieren."
        ],
                "locations": [
            "Ein verlassenes Sanatorium tief im Wald.",
            "Eine abgelegene Insel im stürmischen Meer.",
            "Ein heruntergekommenes Motel mit düsteren Geheimnissen.",
            "Ein alter Leuchtturm, der plötzlich aktiv wird.",
            "Eine verlassene Mine voller gefährlicher Geheimnisse.",
            "Ein verlassenes Krankenhaus, in dem die Lichter flackern.",
            "Eine stillgelegte U-Bahn-Station, die von Geräuschen erfüllt ist.",
            "Ein schauriges Herrenhaus, das scheinbar endlose Korridore hat.",
            "Ein abgelegenes Ferienlager mit einer blutigen Geschichte.",
            "Ein düsterer Vergnügungspark mit verfallenen Attraktionen."
        ],
        "enemies": [
            "Ein Geist, der von tiefer Trauer erfüllt ist.",
            "Eine Gruppe von wahnsinnigen Kultisten.",
            "Ein alter Vampir, der wieder erwacht ist.",
            "Eine Horde von Zombies, die plötzlich auftauchen.",
            "Ein übernatürlicher Killer mit unheimlichen Kräften.",
            "Eine Kreatur, die in der Dunkelheit lauert.",
            "Ein wahnsinniger Wissenschaftler mit makabren Experimenten.",
            "Ein Dämon, der durch einen Fehler beschworen wurde.",
            "Ein Fluch, der die Umgebung lebendig macht.",
            "Ein Werwolf, der die Spieler jagt."
        ],
        "twists": [
            "Der Bösewicht wird von einem übernatürlichen Lachanfall besiegt.",
            "Die Spieler müssen einen Tanzwettbewerb gewinnen, um weiterzukommen.",
            "Ein Charakter wird in ein Huhn verwandelt und muss so weiterspielen.",
            "Die Gegner verlieren ihre Waffen und greifen mit Essen an.",
            "Ein sprechendes Möbelstück bietet den Spielern wertvolle Hinweise."
        ]
    }
}

def generate_one_shot():
    print("=== One-Shot Generator ===")
    print("Bitte wähle eine Kategorie: Fantasy, Modern, Horror, Witzig")
    category = input("Kategorie: ").strip().capitalize()

    if category not in categories:
        print("Ungültige Kategorie. Bitte versuche es erneut.")
        return

    chosen_category = categories[category]
    plot = random.choice(chosen_category["plots"])
    location = random.choice(chosen_category["locations"])
    enemy = random.choice(chosen_category["enemies"])
    twist = random.choice(chosen_category["twists"])

    print(f"Kategorie: {category}")
    print(f"Plot: {plot}")
    print(f"Schauplatz: {location}")
    print(f"Gegner: {enemy}")
    print(f"Wendung: {twist}")

if __name__ == "__main__":
    generate_one_shot()
