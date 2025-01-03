import random

class Scenario:
    def __init__(self, name, plots, locations, enemies, twists):
        self.name = name
        self.plots = plots
        self.locations = locations
        self.enemies = enemies
        self.twists = twists

    def generate_one_shot(self):
        plot = random.choice(self.plots)
        location = random.choice(self.locations)
        enemy = random.choice(self.enemies)
        twist = random.choice(self.twists)
        return {
            "Plot": plot,
            "Location": location,
            "Enemy": enemy,
            "Twist": twist,
        }

# Daten für die Szenarien
fantasy = Scenario(
    "Fantasy",
    plots=[
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
    locations=[
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
    enemies=[
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
    twists=[
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
)
modern = Scenario(
    "Modern",
    plots=[
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
    locations=[
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
    enemies=[
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
    twists=[
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
)
horror = Scenario(
    "Horror",
    plots=[
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
    locations=[
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
    enemies=[
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
    twists=[
        "Der vermeintliche Retter wird selbst zur Bedrohung.",
        "Die Spieler erkennen, dass sie Teil eines Rituals sind.",
        "Der Ort, den sie untersuchen, verändert sich ständig.",
        "Die Gegner scheinen unbesiegbar zu sein, bis ein verborgenes Geheimnis gelüftet wird.",
        "Ein Spieler wird von einer übernatürlichen Macht beeinflusst.",
        "Die Lösung des Problems erfordert ein persönliches Opfer.",
        "Die Spieler finden heraus, dass sie bereits tot sind.",
        "Ein vertrauter NPC entpuppt sich als Antagonist.",
        "Die Bedrohung ist viel größer, als die Spieler ursprünglich dachten.",
        "Das Übernatürliche hat tiefe Verbindungen zur Vergangenheit eines Spielercharakters."
    ]
)
fun = Scenario(
    "Spaß",
    plots=[
        "Die Spieler müssen einen magischen Kuchen für den Geburtstag eines Königs stehlen.",
        "Eine Gruppe von Kobolden hat die Stadtkasse mit Goldbonbons gefüllt, und die Spieler sollen den 'Schatz' zurückholen.",
        "Ein sprechender Hund heuert die Gruppe an, um seine gestohlenen Lieblingssocken zu finden.",
        "Die Spieler sind versehentlich Teilnehmer in einem magischen Kochwettbewerb.",
        "Ein experimenteller Trank hat die Stadt unsichtbar gemacht, und die Spieler müssen den Alchemisten finden, der es verbockt hat.",
        "Ein untoter Barde zwingt die Spieler, in einer Talentshow zu konkurrieren.",
        "Die Spieler müssen einen Drachen babysitten, der sich ständig in Schwierigkeiten bringt.",
        "Ein wütender Bauernverband hat beschlossen, dass die Spieler die Schuld für eine schlechte Ernte tragen.",
        "Ein chaotischer Magier hat die Stadt mit zahmen, aber lästigen Miniatur-Monstern überflutet.",
        "Die Spieler werden angeheuert, um eine legendäre Zutat für die ultimative Suppe zu finden."
    ],
    locations=[
        "Ein magischer Jahrmarkt mit unmöglichen Attraktionen.",
        "Eine Taverne, die auf einem gigantischen Schildkrötenpanzer reist.",
        "Ein schwimmendes Casino auf einem See aus Pudding.",
        "Eine Stadt, in der alle Bewohner ständig singen.",
        "Ein übergroßes Puppenhaus mit lebenden Möbeln.",
        "Ein verzauberter Vergnügungspark voller unkoordinierter Konstrukte.",
        "Ein Feld voller riesiger, aggressiver Karotten.",
        "Eine Akademie für misslungene Zaubersprüche.",
        "Ein überflutetes Dorf, das jetzt von Fischen regiert wird.",
        "Eine verlassene Burg, in der alles aus Käse besteht."
    ],
    enemies=[
        "Ein Koboldkönig, der glaubt, er sei der einzige Herrscher der Welt.",
        "Eine Horde streitlustiger Hühner.",
        "Ein wildgewordener Alchemist mit explosiven Tränken.",
        "Ein riesiger sprechender Pilz, der keinen Humor versteht.",
        "Ein Geist, der schlechte Witze erzählt, um die Spieler zu irritieren.",
        "Eine Gruppe von Clowns, die von einem Chaos-Dämon kontrolliert werden.",
        "Ein Waschbär mit übernatürlichen Diebstahlfähigkeiten.",
        "Ein Golem aus Seife, der zu schnell schmilzt.",
        "Eine Entourage aus frechen Feen, die Unfug treiben.",
        "Eine Horde von Gummibärchen, die zum Leben erweckt wurden."
    ],
    twists=[
        "Der vermeintliche Bösewicht möchte eigentlich nur Freunde finden.",
        "Die Spieler erfahren, dass sie versehentlich den Tag eines nationalen Feiertags ruiniert haben.",
        "Der gestohlene Schatz ist völlig wertlos, aber emotional wichtig.",
        "Die Lösung des Problems erfordert einen besonders peinlichen Tanz.",
        "Die Spieler müssen ein Rätsel lösen, das absichtlich keinen Sinn ergibt.",
        "Die magischen Gegenstände, die sie finden, sind äußerst nutzlos.",
        "Der Bösewicht stellt sich als ein verkleideter NPC heraus, den sie schon kennen.",
        "Der ultimative Gegner ist ein harmlose Kreatur, die sie aus Versehen bedrohen.",
        "Ein mächtiger Verbündeter ist ein schrecklicher Tollpatsch.",
        "Die Mission endet in einem riesigen, chaotischen Bankett."
    ]
)

# Weitere Szenarien (Modern, Horror usw.) können ähnlich definiert werden...

def main():
    scenarios = {
        "Fantasy": fantasy,
        "Modern": modern,
        "Horror": horror,
        "Spaß": fun,
        # Weitere Szenarien hier hinzufügen
    }

    print("Willkommen zum One-Shot-Generator!")
    print("Verfügbare Szenarien:")
    for name in scenarios:
        print(f"- {name}")
    
    choice = input("Wähle ein Szenario: ")
    scenario = scenarios.get(choice)

    if scenario:
        one_shot = scenario.generate_one_shot()
        print("\nDein One-Shot-Abenteuer:")
        for key, value in one_shot.items():
            print(f"{key}: {value}")
    else:
        print("Ungültige Wahl. Bitte versuche es erneut.")

if __name__ == "__main__":
    main()
