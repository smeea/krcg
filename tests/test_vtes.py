import json
import pytest

from krcg import vtes


def test_fuzzy_match():
    assert "enchant kidnred" in vtes.VTES
    assert vtes.VTES["enchant kidnred"].name == "Enchant Kindred"


def test_i18n():
    assert "Corneilles noires" in vtes.VTES
    assert vtes.VTES["Corneilles noires"].name == "Carrion Crows"


def test_search_dimensions():
    assert vtes.VTES.search_dimensions == {
        "bonus": ["Bleed", "Capacity", "Intercept", "Stealth", "Trifle", "Votes"],
        "capacity": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
        "clan": [
            "Abomination",
            "Ahrimane",
            "Akunanse",
            "Assamite",
            "Avenger",
            "Baali",
            "Banu Haqim",
            "Blood Brother",
            "Brujah",
            "Brujah antitribu",
            "Caitiff",
            "Daughter of Cacophony",
            "Defender",
            "Follower of Set",
            "Gangrel",
            "Gangrel antitribu",
            "Gargoyle",
            "Giovanni",
            "Guruhi",
            "Harbinger of Skulls",
            "Innocent",
            "Ishtarri",
            "Judge",
            "Kiasyd",
            "Lasombra",
            "Malkavian",
            "Malkavian antitribu",
            "Martyr",
            "Ministry",
            "Nagaraja",
            "Nosferatu",
            "Nosferatu antitribu",
            "Osebo",
            "Pander",
            "Ravnos",
            "Redeemer",
            "Salubri",
            "Salubri antitribu",
            "Samedi",
            "Toreador",
            "Toreador antitribu",
            "Tremere",
            "Tremere antitribu",
            "True Brujah",
            "Tzimisce",
            "Ventrue",
            "Ventrue antitribu",
            "Visionary",
            "none",
        ],
        "discipline": [
            "ABO",
            "ANI",
            "AUS",
            "CEL",
            "CHI",
            "DAI",
            "DEM",
            "DOM",
            "FOR",
            "MEL",
            "MYT",
            "NEC",
            "OBE",
            "OBF",
            "OBT",
            "POT",
            "PRE",
            "PRO",
            "QUI",
            "SAN",
            "SER",
            "SPI",
            "TEM",
            "THA",
            "THN",
            "VAL",
            "VIC",
            "VIS",
            "abo",
            "ani",
            "aus",
            "cel",
            "chi",
            "choice",
            "combo",
            "dai",
            "def",
            "dem",
            "dom",
            "flight",
            "for",
            "inn",
            "jud",
            "maleficia",
            "mar",
            "mel",
            "mono",
            "multi",
            "myt",
            "nec",
            "none",
            "obe",
            "obf",
            "obt",
            "pot",
            "pre",
            "pro",
            "qui",
            "red",
            "san",
            "ser",
            "spi",
            "striga",
            "tem",
            "tha",
            "thn",
            "val",
            "ven",
            "vic",
            "vin",
            "vis",
            "viz",
        ],
        "group": [1, 2, 3, 4, 5, 6, 7],
        "sect": ["Anarch", "Camarilla", "Independent", "Laibon", "Sabbat"],
        "title": [
            "1 vote",
            "2 votes",
            "Archbishop",
            "Baron",
            "Bishop",
            "Cardinal",
            "Imperator",
            "Inner Circle",
            "Justicar",
            "Kholo",
            "Magaji",
            "Primogen",
            "Prince",
            "Priscus",
            "Regent",
        ],
        "city": [
            "Addis Ababa",
            "Algiers",
            "Amsterdam",
            "Aragon",
            "Athens",
            "Atlanta",
            "Barcelona",
            "Belo Horizonte",
            "Berlin",
            "Birmingham",
            "Boston",
            "Brussels",
            "Budapest",
            "Buenos Aires",
            "Cairo",
            "Canberra",
            "Cape Town",
            "Chicago",
            "Cleveland",
            "Columbus",
            "Copenhagen",
            "Cordoba",
            "Corte",
            "Dallas",
            "Detroit",
            "Dublin",
            "Fortaleza",
            "Frankfurt",
            "Geneva",
            "Glasgow",
            "Guadalajara",
            "Guatemala City",
            "Houston",
            "Istanbul",
            "Johannesburg",
            "Lisbon",
            "London",
            "Los Angeles",
            "Manila",
            "Mannheim",
            "Melbourne",
            "Mexico City",
            "Miami",
            "Milan",
            "Milwaukee",
            "Mombasa",
            "Monaco",
            "Montreal",
            "Moscow",
            "Nairobi",
            "New York",
            "Paris",
            "Perth",
            "Philadelphia",
            "Pittsburgh",
            "Port-au-Prince",
            "Prague",
            "Rio de Janeiro",
            "Rome",
            "Rotterdam",
            "San Diego",
            "Santiago",
            "Seattle",
            "Stockholm",
            "Strasbourg",
            "Sydney",
            "Taipei",
            "Tampa",
            "Thessaloniki",
            "Toronto",
            "Venice",
            "Versailles",
            "Washington, D.C.",
        ],
        "trait": [
            "Black Hand",
            "Infernal",
            "Red List",
            "Scarce",
            "Seraph",
            "Slave",
            "Sterile",
        ],
        "type": [
            "Action",
            "Action Modifier",
            "Ally",
            "Combat",
            "Conviction",
            "Crypt",
            "Equipment",
            "Event",
            "Imbued",
            "Library",
            "Master",
            "Political Action",
            "Power",
            "Reaction",
            "Retainer",
            "Vampire",
        ],
        "set": [
            "1996 Promo",
            "2003 Tournament promo",
            "2004 promo",
            "2005 Storyline promo",
            "2005 Tournament promo",
            "2006 Championship promo",
            "2006 EC Tournament promo",
            "2006 Storyline promo",
            "2006 Tournament promo",
            "2007 Promo",
            "2008 Storyline promo",
            "2008 Tournament promo",
            "2009 Tournament / Storyline promo",
            "2010 Storyline promo",
            "2015 Storyline Rewards",
            "2018 Humble Bundle",
            "2019 AC Promo",
            "2019 ACC Promo",
            "2019 DriveThruCards Promo",
            "2019 EC Promo",
            "2019 Grand Prix Promo",
            "2019 NAC Promo",
            "2019 Promo",
            "2019 Promo Pack 1",
            "2019 SAC Promo",
            "2020 GP Promo",
            "2020 Promo Pack 2",
            "2021 Kickstarter Promo",
            "2021 Mind’s Eye Theatre Promo",
            "2021 Promo Pack 3",
            "2021 Resellers Promo",
            "2021 SAC Promo",
            "2022 European GP Promo",
            "Anarch Unbound",
            "Anarchs",
            "Anarchs promo",
            "Ancient Hearts",
            "Anthology",
            "Black Hand",
            "Black Hand promo",
            "Blood Shadowed Court",
            "Bloodlines",
            "Bloodlines promo",
            "Camarilla Edition",
            "Camarilla Edition promo",
            "Danse Macabre",
            "Dark Sovereigns",
            "Ebony Kingdom",
            "Fall 2002 Storyline promo",
            "Fall 2004 Storyline promo",
            "Fall of London",
            "Fifth Edition",
            "Fifth Edition (Anarch)",
            "Final Nights",
            "Final Nights promo",
            "First Blood",
            "Gehenna",
            "Gehenna promo",
            "Heirs to the Blood",
            "Jyhad",
            "Keepers of Tradition",
            "Kindred Most Wanted",
            "Kindred Most Wanted promo",
            "Legacies of Blood",
            "Legacies of Blood promo",
            "Lords of the Night",
            "Lost Kindred",
            "New Blood",
            "Nights of Reckoning",
            "Print on Demand",
            "Prophecies league promo",
            "Sabbat",
            "Sabbat Preconstructed",
            "Sabbat War",
            "Sabbat War promo",
            "Summer 2003 Storyline promo",
            "Sword of Caine",
            "Sword of Caine promo",
            "Tenth Anniversary",
            "The Unaligned",
            "Third Edition",
            "Third Edition promo",
            "Twenty-Fifth Anniversary",
            "Twilight Rebellion",
            "V5 Polish Edition promo",
            "Vampire: The Eternal Struggle",
            "Winter 2002 Storyline promo",
        ],
        "rarity": ["Common", "Rare", "Uncommon", "Vampire"],
        "precon": [
            "2018 Humble Bundle: Humble Bundle",
            "Anarchs: Anarch Barons",
            "Anarchs: Anarch Gang",
            "Anarchs: Gangrel",
            "Anthology: EC Berlin Edition",
            "Black Hand: Malkavian antitribu",
            "Black Hand: Nosferatu antitribu",
            "Black Hand: Toreador antitribu",
            "Black Hand: Tremere antitribu",
            "Camarilla Edition: Brujah",
            "Camarilla Edition: Malkavian",
            "Camarilla Edition: Nosferatu",
            "Camarilla Edition: Toreador",
            "Camarilla Edition: Tremere",
            "Camarilla Edition: Ventrue",
            "Fifth Edition (Anarch): Banu Haqim",
            "Fifth Edition (Anarch): Brujah",
            "Fifth Edition (Anarch): Gangrel",
            "Fifth Edition (Anarch): Ministry",
            "Fifth Edition: Malkavian",
            "Fifth Edition: Nosferatu",
            "Fifth Edition: Toreador",
            "Fifth Edition: Tremere",
            "Fifth Edition: Ventrue",
            "Final Nights: Assamite",
            "Final Nights: Followers of Set",
            "Final Nights: Giovanni",
            "Final Nights: Ravnos",
            "First Blood: Malkavian",
            "First Blood: Nosferatu",
            "First Blood: Toreador",
            "First Blood: Tremere",
            "First Blood: Ventrue",
            "Heirs to the Blood: Gargoyles",
            "Heirs to the Blood: Kiasyd",
            "Heirs to the Blood: Reprint Bundle 1",
            "Heirs to the Blood: Reprint Bundle 2",
            "Heirs to the Blood: Salubri antitribu",
            "Heirs to the Blood: Samedi",
            "Keepers of Tradition: Brujah",
            "Keepers of Tradition: Malkavian",
            "Keepers of Tradition: Reprint Bundle 1",
            "Keepers of Tradition: Reprint Bundle 2",
            "Keepers of Tradition: Toreador",
            "Keepers of Tradition: Ventrue",
            "Kindred Most Wanted: Alastors",
            "Kindred Most Wanted: Anathema",
            "Kindred Most Wanted: Baali",
            "Kindred Most Wanted: Gangrel antitribu",
            "Legacies of Blood: Akunanse",
            "Legacies of Blood: Guruhi",
            "Legacies of Blood: Ishtarri",
            "Legacies of Blood: Osebo",
            "Lords of the Night: Assamite",
            "Lords of the Night: Followers of Set",
            "Lords of the Night: Giovanni",
            "Lords of the Night: Ravnos",
            "New Blood: Malkavian",
            "New Blood: Nosferatu",
            "New Blood: Toreador",
            "New Blood: Tremere",
            "New Blood: Ventrue",
            "Print on Demand: DriveThruCards",
            "Sabbat Preconstructed: Den of Fiends",
            "Sabbat Preconstructed: Libertine Ball",
            "Sabbat Preconstructed: Pact with Nephandi",
            "Sabbat Preconstructed: Parliament of Shadows",
            "Sabbat War: Brujah antitribu",
            "Sabbat War: Lasombra",
            "Sabbat War: Tzimisce",
            "Sabbat War: Ventrue antitribu",
            "Tenth Anniversary: Tin A",
            "Tenth Anniversary: Tin B",
            "The Unaligned: Bundle 1",
            "The Unaligned: Bundle 2",
            "Third Edition: Brujah antitribu",
            "Third Edition: Malkavian antitribu",
            "Third Edition: Starter Kit Brujah antitribu",
            "Third Edition: Starter Kit Malkavian antitribu",
            "Third Edition: Starter Kit Tremere antitribu",
            "Third Edition: Starter Kit Tzimisce",
            "Third Edition: Tremere antitribu",
            "Third Edition: Tzimisce",
        ],
        "artist": [
            "Aaron Acevedo",
            "Aaron Voss",
            "Abrar Ajmal",
            "Alan Rabinowitz",
            "Albrecht",
            "Alejandro Colucci",
            "Alejandro F. Giraldo",
            "Alexander Dunnigan",
            "Amy Weber",
            "Amy Wilkins",
            "Andre Gates",
            "Andrew Bates",
            "Andrew Hepworth",
            "Andrew Robinson",
            "Andrew Trabbold",
            "Andrey Kiselev",
            "André Freitas",
            "Anna Christenson",
            "Anna Evertsdotter",
            "Anson Maddocks",
            "Ari Targownik",
            "Arkady Roytman",
            "Arthur Roberg",
            "Ash Arnett",
            "Atilio Gambedotti",
            "Attila Adorjany",
            "August Bøgedal Hansen",
            "Avery Butterworth",
            "Becky Cloonan",
            "Becky Jollensten",
            "Ben Mirabelli",
            "Beth Trott",
            "Bob Stevlic",
            "Brad Williams",
            "Brian Ashmore",
            "Brian Graupner",
            "Brian Horton",
            "Brian LeBlanc",
            "Brian Miskelley",
            "Brian Snoddy",
            "Britt Martin",
            "Bryon Wackwitz",
            "Caleb Cleaveland",
            "Carmen Cornet",
            "Chad Michael Ward",
            "Chet Masters",
            "Chris McLoughlin",
            "Chris Richards",
            "Chris Stevens",
            "Christel Espenkrona",
            "Christian Byrne",
            "Christopher Rush",
            "Christopher Shy",
            "Cliff Nielson",
            "Clint Langley",
            "Corey Macourek",
            "Cos Koniotis",
            "Craig Grant",
            "Craig Maher",
            "D. Fryendall",
            "Damien Mammoliti",
            "Dan Frazier",
            "Dan Smith",
            "Daniel Gelon",
            "Darryl Elliott",
            "Dave Leri",
            "Dave Roach",
            "Dave Seeley",
            "David Day",
            "David Fooden",
            "David Ho",
            "David Kimmel",
            "Dennis Calero",
            "Diana Vick",
            "Doug Alexander",
            "Doug Gregory",
            "Doug Stambaugh",
            "Douglas Shuler",
            "Drew Tucker",
            "Durwin Talon",
            "E.M. Gist",
            "Ed Tadem",
            "Edouard Noisette",
            "Edward Beard, Jr.",
            "Efrem Palacios",
            "Elli Adams",
            "Eric Deschamps",
            "Eric Kim",
            "Eric LaCombe",
            "Eric Lofgren",
            "Erica Danell",
            "Esther Sanz",
            "Felipe Gaona",
            "Felipe Headley",
            "Francesc Grimalt",
            "Francisco Tébar",
            "Franz Vohwinkel",
            "Fred Harper",
            "Fred Hooper",
            "Gary Chatterton",
            "Gary Leach",
            "Ginés Quiñonero-Santiago",
            "Glen Osterberger",
            "Grant Garvin",
            "Grant Goleash",
            "Greg Boychuk",
            "Greg Loudon",
            "Greg Simanson",
            "Grzegorz Bobrowski",
            "Gábor Németh",
            "Hannibal King",
            "Harold Arthur McNeill",
            "Heather Hudson",
            "Heather J. McKinney",
            "Heather V. Kreiter",
            "Helena García Huang",
            "Ian Hernaiz",
            "Imaginary Friends Studios",
            "J Frederick Y",
            "Jake Smidt",
            "James Allen Higgins",
            "James Richardson",
            "James Stowe",
            "Jami Waggoner",
            "Jared Smith",
            "Jarkko Suvela",
            "Jason Alexander Behnke",
            "Jason Brubaker",
            "Javier Santos",
            'Jeff "el jefe" Holt',
            "Jeff Klimek",
            "Jeff Laubenstein",
            "Jeff Menges",
            "Jeff Miracola",
            "Jeff Rebner",
            "Jenny Frison",
            "Jer Carolina",
            "Jeremy C. Bills",
            "Jeremy McHugh",
            "Jesús Ybarzábal",
            "Jim Di Bartolo",
            "Jim Nelson",
            "Jim Pavelec",
            "Joe Slucher",
            "Joe Ziolkowski",
            "Joel Biske",
            "John Bolton",
            "John Bridges",
            "John Kent",
            "John Matson",
            "John McCrea",
            "John Scotello",
            "John Van Fleet",
            "Josh Timbrook",
            "Juan Antonio Serrano Garcia",
            "Juan Calle",
            "Julian Jackson",
            "Julie Collins",
            "Justin Norman",
            "Kaja Foglio",
            "Kamilla Khaminskaya",
            "Kari Christensen",
            "Karl Waller",
            "Katie McCaskill",
            "Kelly Howlett",
            "Ken Kokoszka",
            "Ken Meyer, Jr.",
            "Kent Williams",
            "Kevin McCann",
            "Kieran Yanner",
            "Kim Aldau",
            "Krasen Maximov",
            "Kyri Koniotis",
            "L. A. Williams",
            "Laia López Tubau",
            "Larry MacDougall",
            "Lawrence Snelly",
            "Lee Carter",
            "Lee Dotson",
            "Lee Fields",
            "Leif Jones",
            "Liz Danforth",
            "Marco Marzoni",
            "Marco Nelor",
            "Margaret Organ-Kean",
            "Marian Churchland",
            "Mark Kelly",
            "Mark Nelson",
            "Mark Poole",
            "Mark Tedin",
            "Marta Ruiz Anguera",
            "Martín de Diego",
            "María Lorén",
            "Mathias Kollros",
            "Matias Tapia",
            "Matt Cavotta",
            "Matt Dixon",
            "Matt Smith",
            "Matt Wilson",
            "Matthew Mitchell",
            "Max Shade Fellwalker",
            "Melissa Benson",
            "Melissa Uran",
            "Michael Astrachan",
            "Michael Dixon",
            "Michael Gaydos",
            "Michael Weaver",
            "Mick Bertilorenzi",
            "Mike Chaney",
            "Mike Danza",
            "Mike Dringenberg",
            "Mike Huddleston",
            "Mike Raabe",
            "Mirko Falloni",
            "Mitch Mueller",
            "Monte Moore",
            "Newel Anderson",
            "Nicola Leonard",
            'Nicolas "Dimple" Bigot',
            "Nicole Cardiff",
            "Nigel Sade",
            "Nilson",
            "Noah Hirka",
            "Noora Hirvonen",
            "Né Né Thomas",
            "Oliver Meinerding",
            "Oscar Salcedo",
            "Othon Nikolaidis",
            "Paolo Puggioni",
            "Pat Loboyko",
            "Pat Morrissey",
            "Patrick Kochakji",
            "Patrick Lambert",
            "Patrick McEvoy",
            "Paul Ballard",
            "Paul Tobin",
            "Pete Burges",
            "Pete Venters",
            "Peter Bergting",
            "Peter Kim",
            "Peter Mohrbacher",
            "Peter Scholtz",
            "Phil Wohr",
            "Phillip Hilliker",
            "Phillip Tan",
            "Quinton Hoover",
            "Randy Asplund",
            "Randy Gallegos",
            "Rebecca Guay",
            "Riccardo Fabiani",
            "Richard Kane Ferguson",
            "Richard Thomas",
            "Rick Berry",
            "Rick O'Brien",
            "Rik Martin",
            "Rob Alexander",
            "Robert McNeill",
            "Robin Chyo",
            "Rodrigo González Toledo",
            "Roel Wielinga",
            "Roger Raupp",
            "Ron Lemon",
            "Ron Spencer",
            "Ron Van Halen",
            "Rubén Bravo",
            "Samuel Araya",
            "Sandra Chang-Adair",
            "Sandra Everingham",
            "Satyr",
            "Scott Fischer",
            "Scott Kirschner",
            "Scott M. Bakal",
            "Shane Coppage",
            "Steve Casper",
            "Steve Eidson",
            "Steve Ellis",
            "Steve Prescott",
            "Stuart Beel",
            "Stuart Sayger",
            "Sue Ann Harkey",
            "Susan Van Camp",
            "Talon Dunning",
            "Ted Naifeh",
            "Terese Nielsen",
            "Thea Maia",
            "Theodore Black",
            "Thomas Baxa",
            "Thomas Denmark",
            "Thomas Manning",
            "Thomas Nairb",
            "Tim Bradstreet",
            "Tom Biondillo",
            "Tom Duncan",
            "Tom Gianni",
            "Tom Wänerstrand",
            'Tomáš "zelgaris" Zahradníček',
            "Tony Harris",
            "Tony Shasteen",
            "Torstein Nordstrand",
            "Travis Ingram",
            "Trevor Claxton",
            "UDON",
            "Vatche Mavlian",
            "Veronica Jones",
            "Vince Locke",
            "Warren Mahy",
            "Will Simpson",
            "William O'Connor",
            "Zina Saunders",
            "matrix von z",
            "rk post",
        ],
    }


def test_search_basic():
    # no parameter returns everything
    assert len(vtes.VTES.search()) >= 3788
    # non-existing dimension raises
    with pytest.raises(ValueError):
        vtes.VTES.search(foo="bar")
    # non-existing value in dimension does not raise
    assert len(vtes.VTES.search(bonus=["foo"])) == 0
    # card text
    assert vtes.VTES.search(card_text="this equipment card represents a location") == {
        vtes.VTES["Catacombs"],
        vtes.VTES["Dartmoor, England"],
        vtes.VTES["Inveraray, Scotland"],
        vtes.VTES["Living Manse"],
        vtes.VTES["Local 1111"],
        vtes.VTES["Lyndhurst Estate, New York"],
        vtes.VTES["Palatial Estate"],
        vtes.VTES["Pier 13, Port of Baltimore"],
        vtes.VTES["Ruins of Ceoris"],
        vtes.VTES["Ruins of Villers Abbey, Belgium"],
        vtes.VTES["Sacré-Cœur Cathedral, France"],
        vtes.VTES["San Lorenzo de El Escorial, Spain"],
        vtes.VTES["San Nicolás de los Servitas"],
        vtes.VTES["The Ankara Citadel, Turkey"],
        vtes.VTES["Winchester Mansion"],
        vtes.VTES["Zaire River Ferry"],
    }
    # flavor text
    assert vtes.VTES.search(flavor_text="Baudelaire") == {
        vtes.VTES["Aching Beauty"],
        vtes.VTES["Blood Sweat"],
        vtes.VTES["Breath of Thanatos"],
        vtes.VTES["Cats' Guidance"],
        vtes.VTES["Earth Meld"],
        vtes.VTES["Form of the Serpent"],
        vtes.VTES["Giuseppe, Gravedigger"],
        vtes.VTES["Gleam of Red Eyes"],
        vtes.VTES["Haven Uncovered"],
        vtes.VTES["Opium Den"],
        vtes.VTES["Order of Hermes Cabal"],
        vtes.VTES["Psychic Veil"],
        vtes.VTES["Rom Gypsy"],
        vtes.VTES["Shade"],
        vtes.VTES["Threats"],
        vtes.VTES["Tongue of the Serpent"],
        vtes.VTES["Vanish from the Mind's Eye"],
    }
    # all text - includes name and flavor, but not clan, discipline, etc.
    assert vtes.VTES.search(text="Brujah") == {
        vtes.VTES["Adana de Sforza"],
        vtes.VTES["Al-Muntathir, God's Witness"],
        vtes.VTES["Amusement Park Hunting Ground"],
        vtes.VTES["Anarch Revolt"],
        vtes.VTES["Artistically Inept"],
        vtes.VTES["Blade of Enoch"],
        vtes.VTES["Blood Weakens"],
        vtes.VTES["Brass Knuckles"],
        vtes.VTES["Brujah Debate"],
        vtes.VTES["Brujah Frenzy"],
        vtes.VTES["Brujah Justicar"],
        vtes.VTES["Carthage Remembered"],
        vtes.VTES["Condemnation: Betrayed"],
        vtes.VTES["Conniver"],
        vtes.VTES["Crusade: Rome"],
        vtes.VTES["Dmitra Ilyanova"],
        vtes.VTES["Dogs of War"],
        vtes.VTES["Don Cruez, The Idealist"],
        vtes.VTES["Emissary"],
        vtes.VTES["Fee Stake: New York"],
        vtes.VTES["Flurry of Action"],
        vtes.VTES["From a Sinking Ship"],
        vtes.VTES["Galaric's Legacy"],
        vtes.VTES["Games of Instinct"],
        vtes.VTES["Gang Territory"],
        vtes.VTES["Gengis"],
        vtes.VTES["Gwendolyn"],
        vtes.VTES["Into the Fire"],
        vtes.VTES["Iron Heart"],
        vtes.VTES["Jack of Both Sides"],
        vtes.VTES["Jaroslav Pascek"],
        vtes.VTES["Judgment: Death to the Brujah!"],
        vtes.VTES["Kevin Jackson (G7)"],
        vtes.VTES["Learjet"],
        vtes.VTES["Magazine"],
        vtes.VTES["Makarios, The Seducer"],
        vtes.VTES["Marcus Vitel (ADV)"],
        vtes.VTES["Miranda Sanova"],
        vtes.VTES["New Carthage"],
        vtes.VTES["Nik"],
        vtes.VTES["Out of Control"],
        vtes.VTES["Peace Treaty"],
        vtes.VTES["Praxis Seizure: Rome"],
        vtes.VTES["Ranjan Rishi, Camarilla Scholar"],
        vtes.VTES["Rant!"],
        vtes.VTES["Rebel"],
        vtes.VTES["Sire's Index Finger"],
        vtes.VTES["Sunset Strip, Hollywood"],
        vtes.VTES["Survivalist"],
        vtes.VTES["Sword of Judgment"],
        vtes.VTES["Tabriz Assembly"],
        vtes.VTES["Tatiana Stepanova, Alastor"],
        vtes.VTES["The Path of the Scorched Heart"],
        vtes.VTES["Tura Vaughn"],
        vtes.VTES["Ublo-Satha"],
        vtes.VTES["Undead Strength"],
        vtes.VTES["Unexpected Coalition"],
        vtes.VTES["Vasilis, The Traitor of Don Cruez"],
        vtes.VTES["Vendetta"],
        vtes.VTES["Ventrue Directorate Assembly"],
    }
    # don't match disciplines trigrams in card text
    # (although with braces, [thn] would match)
    assert not vtes.VTES.search(card_text="thn")
    # city
    assert vtes.VTES.search(city=["Chicago"]) == {
        vtes.VTES["Antón de Concepción"],
        vtes.VTES["Crusade: Chicago"],
        vtes.VTES["Horatio Ballard"],
        vtes.VTES["Kevin Jackson (G7)"],
        vtes.VTES["Lachlan, Noddist"],
        vtes.VTES["Lodin (Olaf Holte)"],
        vtes.VTES["Maldavis (ADV)"],
        vtes.VTES["Maxwell"],
        vtes.VTES["Praxis Seizure: Chicago"],
        vtes.VTES["Sir Walter Nash"],
    }
    # title
    assert vtes.VTES.search(title=["imperator"]) == {
        vtes.VTES["Imperator"],
        vtes.VTES["Karsh (ADV)"],
        vtes.VTES["National Guard Support"],
        vtes.VTES["Persona Non Grata"],
        vtes.VTES["Reinforcements"],
        vtes.VTES["Rubicon"],
        vtes.VTES["Scourge"],
    }
    # discipline (inf matches sup), title
    assert vtes.VTES.search(title=["primogen"], discipline=["ser"]) == {
        vtes.VTES["Amenophobis"]
    }
    # stealth, votes
    assert vtes.VTES.search(bonus=["stealth", "votes"]) == {
        vtes.VTES["Antonio Veradas"],
        vtes.VTES["Bulscu (ADV)"],
        vtes.VTES["Dark Selina"],
        vtes.VTES["Jessica (ADV)"],
        vtes.VTES["Joseph Cambridge"],
        vtes.VTES["Karen Suadela"],
        vtes.VTES["Loki's Gift"],
        vtes.VTES["Maila"],
        vtes.VTES["Maxwell"],
        vtes.VTES["Natasha Volfchek"],
        vtes.VTES["Perfect Paragon"],
        vtes.VTES["Sela (ADV)"],
        vtes.VTES["Suhailah"],
        vtes.VTES["Zayyat, The Sandstorm"],
    }
    # clans, votes provided by master cards
    assert vtes.VTES.search(bonus=["Votes"], clan=["Banu Haqim"], type=["Master"]) == {
        vtes.VTES["Alamut"],
        vtes.VTES["The Black Throne"],
    }
    # votes provided by titles - legacy clan names still work
    assert vtes.VTES.search(bonus=["Votes"], clan=["Assamite"], group=[3]) == {
        vtes.VTES["Rebekah"],
        vtes.VTES["Enam"],
    }
    # title when merged
    assert vtes.VTES.search(clan=["Banu Haqim"], title=["Justicar"]) == {
        vtes.VTES["Kasim Bayar"],
        vtes.VTES["Tegyrius, Vizier (ADV)"],
    }
    # traits
    assert vtes.VTES.search(clan=["Nagaraja"], trait=["Black Hand"]) == {
        vtes.VTES["Sennadurek"],
    }
    assert vtes.VTES.search(clan=["Banu Haqim"], trait=["Red List"]) == {
        vtes.VTES["Jamal"],
        vtes.VTES["Tariq, The Silent (ADV)"],
    }
    # sect
    assert vtes.VTES.search(clan=["Banu Haqim"], sect=["Camarilla"], group=[2]) == {
        vtes.VTES["Al-Ashrad, Amr of Alamut (ADV)"],
        vtes.VTES["Tegyrius, Vizier"],
        vtes.VTES["Tegyrius, Vizier (ADV)"],
    }
    # trait on library card
    assert vtes.VTES.search(type=["Action Modifier"], trait=["Black Hand"]) == {
        vtes.VTES["Circumspect Revelation"],
        vtes.VTES["Seraph's Second"],
        vtes.VTES["The Art of Memory"],
    }
    # title requirement
    assert vtes.VTES.search(type=["Reaction"], title=["Justicar"]) == {
        vtes.VTES["Legacy of Power"],
        vtes.VTES["Second Tradition: Domain"],
    }
    # "Requires titled Sabbat/Camarilla" maps to all possible titles
    assert vtes.VTES.search(bonus=["Intercept"], title=["Archbishop"]) == {
        vtes.VTES["Matteus, Flesh Sculptor"],
        vtes.VTES["National Guard Support"],
        vtes.VTES["Persona Non Grata"],
        vtes.VTES["Under Siege"],
    }
    # reducing intercept is stealth, denying block is stealth
    assert vtes.VTES.search(
        bonus=["Stealth"], discipline=["chi"], type=["Library"]
    ) == {
        vtes.VTES["Fata Morgana"],
        vtes.VTES["Heart's Desire"],
        vtes.VTES["Mirror's Visage"],
        vtes.VTES["Smoke and Mirrors"],
        vtes.VTES["Will-o'-the-Wisp"],
    }
    # reducing stealth is intercept
    assert vtes.VTES.search(
        bonus=["Intercept"], discipline=["chi"], type=["Library"]
    ) == {
        vtes.VTES["Draba"],
        vtes.VTES["Ignis Fatuus"],
        # it has [chi], intercept is on another discipline, but eh.
        vtes.VTES["Netwar"],
        vtes.VTES["Veiled Sight"],
    }
    # no discipline (crypt)
    assert vtes.VTES.search(discipline=["none"], type=["Crypt"]) == {
        vtes.VTES["Anarch Convert"],
        vtes.VTES["Sandra White"],
        vtes.VTES["Smudge the Ignored"],
    }
    # no discipline, sect requirement
    assert vtes.VTES.search(
        discipline=["none"], sect=["Sabbat"], bonus=["Intercept"]
    ) == {
        vtes.VTES["Abbot"],
        vtes.VTES["Harzomatuili"],
        vtes.VTES["Under Siege"],
    }
    assert vtes.VTES.search(type=["Political Action"], sect=["Independent"]) == {
        vtes.VTES["Free States Rant"],
        vtes.VTES["Reckless Agitation"],
    }
    assert vtes.VTES.search(type=["Political Action"], sect=["Anarch"]) == {
        vtes.VTES["Anarch Salon"],
        vtes.VTES["Eat the Rich"],
        # this one does not show here because Anarch is not a requirement
        # could be the other way around, no matter
        # vtes.VTES["Exclusion Principle"],
        # that one should not show here - its anti-Anarch, not Anarch
        # vtes.VTES["Persona Non Grata"],
        vtes.VTES["Firebrand"],
        vtes.VTES["Free States Rant"],
        vtes.VTES["Patsy"],
        vtes.VTES["Reckless Agitation"],
        vtes.VTES["Revolutionary Council"],
        vtes.VTES["Sweeper"],
    }
    # multi-disciplines
    assert vtes.VTES.search(discipline=["multi", "ani"], bonus=["Intercept"]) == {
        vtes.VTES["Deep Ecology"],
        vtes.VTES["Detect Authority"],
        vtes.VTES["Falcon's Eye"],
        vtes.VTES["Read the Winds"],
        vtes.VTES["Speak with Spirits"],
        vtes.VTES["The Mole"],
    }
    assert vtes.VTES.search(discipline=["choice", "ani"], bonus=["Intercept"]) == {
        vtes.VTES["Deep Ecology"],
        vtes.VTES["Detect Authority"],
        vtes.VTES["Falcon's Eye"],
        vtes.VTES["Speak with Spirits"],
        vtes.VTES["The Mole"],
    }
    assert vtes.VTES.search(discipline=["combo", "ani"], bonus=["Intercept"]) == {
        vtes.VTES["Read the Winds"],
    }
    # superior disciplines (vampires only)
    assert vtes.VTES.search(discipline=["OBE"], group=[2]) == {
        vtes.VTES["Blanche Hill"],
        vtes.VTES["Matthias"],
    }
    # artist
    assert vtes.VTES.search(artist=["E.M. Gist"]) == {
        vtes.VTES["Flames of Insurrection"],
        vtes.VTES["Harmony"],
        vtes.VTES["Marcus Vitel"],
        vtes.VTES["Public Enemy"],
        vtes.VTES["Rutor"],
    }


def test_search_i18n():
    # i18n - match the given language in addition to english
    assert vtes.VTES.search(
        text="cette carte d'équipement représente un lieu", lang="fr"
    ) == {
        vtes.VTES["Living Manse"],
        vtes.VTES["The Ankara Citadel, Turkey"],
    }
    # i18n - also works with region codes
    assert vtes.VTES.search(
        text="cette carte d'équipement représente un lieu", lang="fr-fr"
    ) == {
        vtes.VTES["Living Manse"],
        vtes.VTES["The Ankara Citadel, Turkey"],
    }
    # i18n - whatever case is used for the region code
    assert vtes.VTES.search(
        text="cette carte d'équipement représente un lieu", lang="fr_FR"
    ) == {
        vtes.VTES["Living Manse"],
        vtes.VTES["The Ankara Citadel, Turkey"],
    }
    # i18n - do not match translations in other languages
    assert (
        vtes.VTES.search(text="esta carta de equipo representa un lugar", lang="fr")
        == set()
    )
    assert vtes.VTES.search(
        text="esta carta de equipo representa un lugar", lang="es"
    ) == {
        vtes.VTES["Living Manse"],
        vtes.VTES["The Ankara Citadel, Turkey"],
    }


def test_search_ranges():
    assert vtes.VTES.search(group=[1, 2, 3], clan=["kiasyd"]) == {
        vtes.VTES["Bartholomew"],
        vtes.VTES["Béatrice L'Angou"],
        vtes.VTES["Julia Prima"],
        vtes.VTES["Kassiym Malikhair"],
        vtes.VTES["Marconius"],
        vtes.VTES["Quincy, The Trapper"],
    }


def test_search_cornercases():
    # some tricky cards test (add cards for NR tests)
    # providing a stealth action does not register as "stealth" bonus
    assert vtes.VTES["Tracker's Mark"] in vtes.VTES.search(bonus=["intercept"])
    assert vtes.VTES["Tracker's Mark"] not in vtes.VTES.search(bonus=["stealth"])
    assert vtes.VTES["Brainwash"] not in vtes.VTES.search(bonus=["stealth"])
    # Gwen Brand whould show up with superior disciplines
    assert vtes.VTES["Gwen Brand"] in vtes.VTES.search(
        discipline=["AUS", "CHI", "FOR", "ANI"], clan=["Ravnos"], group=[5]
    )
    # The Baron is not Anarch
    assert vtes.VTES["The Baron"] not in vtes.VTES.search(sect=["Anarch"])


def test_vekn():
    test_vtes = vtes._VTES()
    test_vtes.load_from_vekn()
    assert len(test_vtes) >= 3788
    assert set(test_vtes[100001].to_json().keys()) == {
        "_i18n",
        "_name",
        "_set",
        "artists",
        "card_text",
        "id",
        "name",
        "printed_name",
        "pool_cost",
        "ordered_sets",
        "rulings",
        "scans",
        "sets",
        "types",
        "url",
    }
    assert test_vtes[201362].to_json() == {
        "_name": "Theo Bell",
        "_set": "FN:U, CE:PB",
        "artists": ["John Van Fleet"],
        "capacity": 7,
        "card_text": (
            "Camarilla: Theo may enter combat with any ready minion "
            "controlled by another Methuselah as a Ⓓ action. If you control "
            "a ready prince or justicar, blood hunts cannot be called on "
            "Theo."
        ),
        "clans": ["Brujah"],
        "disciplines": ["cel", "dom", "pre", "POT"],
        "group": "2",
        "has_advanced": True,
        "has_evolution": True,
        "id": 201362,
        "name": "Theo Bell (G2)",
        "name_variants": ["Theo Bell"],
        "printed_name": "Theo Bell",
        "ordered_sets": ["Final Nights", "Camarilla Edition"],
        "scans": {
            "Camarilla Edition": (
                "https://static.krcg.org/card/set/camarilla-edition/theobellg2.jpg"
            ),
            "Final Nights": (
                "https://static.krcg.org/card/set/final-nights/theobellg2.jpg"
            ),
        },
        "sets": {
            "Camarilla Edition": [
                {"copies": 1, "precon": "Brujah", "release_date": "2002-08-19"}
            ],
            "Final Nights": [{"rarity": "Uncommon", "release_date": "2001-06-11"}],
        },
        "types": ["Vampire"],
        "url": "https://static.krcg.org/card/theobellg2.jpg",
        "variants": {"G2 ADV": 201363, "G6": 201613},
    }


def test_dump():
    json.dumps(vtes.VTES.to_json())
