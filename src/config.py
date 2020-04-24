"""Configuration.
"""
from os import path

#: what to download
VEKN_TWDA_URL = "http://www.vekn.fr/decks/twd.htm"
VEKN_VTES_URL = "http://www.vekn.net/images/stories/downloads/vtescsv_utf8.zip"
VEKN_VTES_LIBRARY_FILENAME = "vteslib.csv"
VEKN_VTES_CRYPT_FILENAME = "vtescrypt.csv"
VEKN_VTES_ENCODING = "utf-8"
#: where to store our data
TWDA_FILE = path.join(path.dirname(__file__), "TWDA.pkl")
VTES_FILE = path.join(path.dirname(__file__), "VTES.pkl")
CARDS_RULINGS_FILE = path.join(path.dirname(__file__), "cards-rulings.yaml")
GENERAL_RULINGS_FILE = path.join(path.dirname(__file__), "general-rulings.yaml")
RULINGS_LINK_FILE = path.join(path.dirname(__file__), "rulings-links.yaml")
#: classic headers in deck lists
HEADERS = [
    "master",
    "minion",
    "crypt",
    "library",
    "action",
    "combat",
    "conviction",
    "reaction",
    "retainer",
    "equipment",
    "equip",
    "event",
    "political action",
    "political",
    "politic",
    "power",
    "vote",
    "action modifier",
    "action mod",
    "modifier",
    "mod",
]
#: custom headers some players have used
ADDITIONAL_HEADERS = [
    "combo",
    "combos",
    "multitype",
    "multitypes",
    "mixed",
    "miscellaneous",
    "misc",
    "average",
    "other",
    "others",
    "double",
    "doubles",
    "burn option",
    "equip",
    "total",
]
#: official cards renaming
AKA = {
    # print change not registered in cards "Aka" field
    "mask of 1,000 faces": "Mask of a Thousand Faces",
    # typo in VEKN official file
    "thadius zho": "Thadius Zho{}",
}

CLANS_AKA = {
    "!brujah": "Brujah antitribu",
    "!gangrel": "Gangrel antitribu",
    "!malkavian": "Malkavian antitribu",
    "!malk": "Malkavian antitribu",
    "!nosferatu": "Nosferatu antitribu",
    "!nosfe": "Nosferatu antitribu",
    "!salubri": "Salubri antitribu",
    "!salu": "Salubri antitribu",
    "!toreador": "Toreador antitribu",
    "!tore": "Toreador antitribu",
    "!tremere": "Tremere antitribu",
    "!trem": "Tremere antitribu",
    "!ventrue": "Ventrue antitribu",
    "brujah anti": "Brujah antitribu",
    "gangrel anti": "Gangrel antitribu",
    "malkavian anti": "Malkavian antitribu",
    "malk anti": "Malkavian antitribu",
    "nosferatu anti": "Nosferatu antitribu",
    "nosfe anti": "Nosferatu antitribu",
    "salubri anti": "Salubri antitribu",
    "salu anti": "Salubri antitribu",
    "toreador anti": "Toreador antitribu",
    "tore anti": "Toreador antitribu",
    "tremere anti": "Tremere antitribu",
    "trem anti": "Tremere antitribu",
    "ventrue anti": "Ventrue antitribu",
    "brother": "Blood Brother",
    "brothers": "Blood Brother",
    "giov": "Giovanni",
    "malk": "Malkavian",
    "naga": "Nagaraja",
    "nosfe": "Nosferatu",
    "salu": "Salubri",
    "tore": "Toreador",
    "trem": "Tremere",
    "cacophony": "Daughter of Cacophony",
    "daughter": "Daughter of Cacophony",
    "daughters": "Daughter of Cacophony",
    "set": "Follower of Set",
    "setite": "Follower of Set",
    "follower": "Follower of Set",
    "followers": "Follower of Set",
    "skulls": "Harbinger of Skulls",
    "harbinger": "Harbinger of Skulls",
    "harbingers": "Harbinger of Skulls",
}

DISC_AKA = {
    "abo": "Abombwe",
    "ani": "Animalism",
    "aus": "Auspex",
    "cel": "Celerity",
    "chi": "Chimerstry",
    "dai": "Daimoinon",
    "dem": "Dementation",
    "dom": "Dominate",
    "for": "Fortitude",
    "mal": "Maleficia",
    "mel": "Melpominee",
    "myt": "Mytherceria",
    "nec": "Necromancy",
    "obe": "Obeah",
    "obf": "Obfuscate",
    "obt": "Obtenebration",
    "pot": "Potence",
    "pre": "Presence",
    "pro": "Protean",
    "qui": "Quietus",
    "san": "Sanguinus",
    "ser": "Serpentis",
    "spi": "Spiritus",
    "str": "Striga",
    "tem": "Temporis",
    "tha": "Thaumaturgy",
    "than": "Thanatosis",
    "thau": "Thaumaturgy",
    "thn": "Thanatosis",
    "val": "Valeren",
    "vic": "Vicissitude",
    "vis": "Visceratika",
}

#: custom remap to match players abbreviations and typos
REMAP = {
    # our card parsing removes the dash
    "bang nakh": "Bang Nakh — Tiger's Claws",
    # we not decode HTML properly as most of it is text
    "alia, god=92s messenger": "Alia, God's Messenger",
    "pentex=99 subversion": "Pentex Subversion",
    # traditions - players really do whatever they want
    "the first tradition": "First Tradition: The Masquerade",
    "first tradition": "First Tradition: The Masquerade",
    "1st tradition": "First Tradition: The Masquerade",
    "the second tradition": "Second Tradition: Domain",
    "second tradition": "Second Tradition: Domain",
    "2nd trad": "Second Tradition: Domain",
    "2nd tradition": "Second Tradition: Domain",
    "2nd tradition: domain": "Second Tradition: Domain",
    "the third tradition": "Third Tradition: Progeny",
    "third tradition": "Third Tradition: Progeny",
    "3rd tradition": "Third Tradition: Progeny",
    "the fourth tradition": "Fourth Tradition: The Accounting",
    "fourth tradition": "Fourth Tradition: The Accounting",
    "4th tradition": "Fourth Tradition: The Accounting",
    "the fifth tradition": "Fifth Tradition: Hospitality",
    "fifth tradition": "Fifth Tradition: Hospitality",
    "5th tradition": "Fifth Tradition: Hospitality",
    "the sixth tradition": "Sixth Tradition: Destruction",
    "sixth tradition": "Sixth Tradition: Destruction",
    "6th tradition": "Sixth Tradition: Destruction",
    # hunting grounds
    "academic hg": "Academic Hunting Ground",
    "amusement park hg": "Amusement Park Hunting Ground",
    "asylum hg": "Asylum Hunting Ground",
    "base hg": "Base Hunting Ground",
    "campground hg": "Campground Hunting Ground",
    "corporate hg": "Corporate Hunting Ground",
    "fetish club hg": "Fetish Club Hunting Ground",
    "fetish hg": "Fetish Club Hunting Ground",
    "institution hg": "Institution Hunting Ground",
    "jungle hg": "Jungle Hunting Ground",
    "library hg": "Library Hunting Ground",
    "morgue hg": "Morgue Hunting Ground",
    "palace hg": "Palace Hunting Ground",
    "park hg": "Park Hunting Ground",
    "poacher's hg": "Poacher's Hunting Ground",
    "political hg": "Political Hunting Ground",
    "port hg": "Port Hunting Ground",
    "shanty Town hg": "Shanty Town Hunting Ground",
    "slum hg": "Slum Hunting Ground",
    "society hg": "Society Hunting Ground",
    "temple hg": "Temple Hunting Ground",
    "underworld hg": "Underworld Hunting Ground",
    "university hg": "University Hunting Ground",
    "uptown hg": "Uptown Hunting Ground",
    "warzone hg": "Warzone Hunting Ground",
    "zoo hg": "Zoo Hunting Ground",
    "academic h.g.": "Academic Hunting Ground",
    "amusement park h.g.": "Amusement Park Hunting Ground",
    "asylum h.g.": "Asylum Hunting Ground",
    "base h.g.": "Base Hunting Ground",
    "campground h.g.": "Campground Hunting Ground",
    "corporate h.g.": "Corporate Hunting Ground",
    "fetish club h.g.": "Fetish Club Hunting Ground",
    "institution h.g.": "Institution Hunting Ground",
    "jungle h.g.": "Jungle Hunting Ground",
    "library h.g.": "Library Hunting Ground",
    "morgue h.g.": "Morgue Hunting Ground",
    "palace h.g.": "Palace Hunting Ground",
    "park h.g.": "Park Hunting Ground",
    "poacher's h.g.": "Poacher's Hunting Ground",
    "political h.g.": "Political Hunting Ground",
    "port h.g.": "Port Hunting Ground",
    "shanty Town h.g.": "Shanty Town Hunting Ground",
    "slum h.g.": "Slum Hunting Ground",
    "society h.g.": "Society Hunting Ground",
    "temple h.g.": "Temple Hunting Ground",
    "underworld h.g.": "Underworld Hunting Ground",
    "university h.g.": "University Hunting Ground",
    "uptown h.g.": "Uptown Hunting Ground",
    "warzone h.g.": "Warzone Hunting Ground",
    "zoo h.g.": "Zoo Hunting Ground",
    "acad. hg": "Academic Hunting Ground",
    "univ. hg": "University Hunting Ground",
    "univ hg": "University Hunting Ground",
    # powerbases
    "pb: barranquilla": "Powerbase: Barranquilla",
    "pb: berlin": "Powerbase: Berlin",
    "pb: cape verde": "Powerbase: Cape Verde",
    "pb: chicago": "Powerbase: Chicago",
    "pb: los angeles": "Powerbase: Los Angeles",
    "pb: luanda": "Powerbase: Luanda",
    "pb: madrid": "Powerbase: Madrid",
    "pb:madrid": "Powerbase: Madrid",
    "pb: mexico city": "Powerbase: Mexico City",
    "pb: montreal": "Powerbase: Montreal",
    "pb:montreal": "Powerbase: Montreal",
    "pb: new york": "Powerbase: New York",
    "pb: rome": "Powerbase: Rome",
    "pb: savannah": "Powerbase: Savannah",
    "pb: tshwane": "Powerbase: Tshwane",
    "pb: washington, d.c.": "Powerbase: Washington, D.C.",
    "pb: zurich": "Powerbase: Zürich",
    "pb barranquilla": "Powerbase: Barranquilla",
    "pb berlin": "Powerbase: Berlin",
    "pb cape verde": "Powerbase: Cape Verde",
    "pb chicago": "Powerbase: Chicago",
    "pb los angeles": "Powerbase: Los Angeles",
    "pb luanda": "Powerbase: Luanda",
    "pb madrid": "Powerbase: Madrid",
    "pb mexico city": "Powerbase: Mexico City",
    "pb montreal": "Powerbase: Montreal",
    "pb new york": "Powerbase: New York",
    "pb rome": "Powerbase: Rome",
    "pb savannah": "Powerbase: Savannah",
    "pb tshwane": "Powerbase: Tshwane",
    "pb washington, d.c.": "Powerbase: Washington, D.C.",
    "pb zurich": "Powerbase: Zürich",
    "powerbase zurich": "Powerbase: Zürich",
    # punctuation
    "behind you": "Behind You!",
    "psyche": "Psyche!",
    # known abbreviations
    "antediluvian a.": "Antediluvian Awakening",
    "anthelios, the": "Anthelios, The Red Star",
    "archon inv.": "Archon Investigation",
    "call": "Call, The",
    "carlton": "Carlton Van Wyk",
    "con ag": "Conservative Agitation",
    "coven": "Coven, The",
    "direct": "Direct Intervention",
    "delaying": "Delaying Tactics",
    "dreams": "Dreams of the Sphinx",
    "effective": "Effective Management",
    "elysium": "Elysium: The Arboretum",
    "elysium: versailles": "Elysium: The Palace of Versailles",
    "entice": "Enticement",
    "felix fix": 'Felix "Fix" Hessian (Wraith)',
    "forced": "Forced Awakening",
    "forced aw": "Forced Awakening",
    "foreshadowing": "Foreshadowing Destruction",
    "golconda": "Golconda: Inner Peace",
    "govern": "Govern the Unaligned",
    "gtu": "Govern the Unaligned",
    "heidelberg": "Heidelberg Castle, Germany",
    "heidelburg": "Heidelberg Castle, Germany",
    "info highway": "Information Highway",
    "infohighway": "Information Highway",
    "info hwy": "Information Highway",
    "js simmons": "J. S. Simmons, Esq.",
    "krc": "Kine Resources Contested",
    "krcg": "KRCG News Radio",
    "krcg news": "KRCG News Radio",
    "laptop": "Laptop Computer",
    "laptops": "Laptop Computer",
    "legal manip": "Legal Manipulations",
    "london eve star": "London Evening Star, Tabloid Newspaper",
    "masquer": "Masquer (Wraith)",
    "mister winthrop": "Mr. Winthrop",
    "molotov": "Molotov Cocktail",
    "ohoyo hopoksia": "Ohoyo Hopoksia (Bastet)",
    "owl": "Owl Companion",
    "patagia: flaps": "Patagia: Flaps Allowing Limited Flight",
    "pentex": "Pentex(TM) Subversion",
    "pto": "Protect Thine Own",
    "pulse": "Pulse of the Canaille",
    "rack": "Rack, The",
    "storage": "Storage Annex",
    "sudden": "Sudden Reversal",
    "talaq": "Talaq, The Immortal",
    "true love's kiss": "True Love's Face",
    "temptation of g.p.": "Temptation of Greater Power",
    "ventrue hq": "Ventrue Headquarters",
    "voter cap": "Voter Captivation",
    "wake with ef": "Wake with Evening's Freshness",
    "wake with e.f": "Wake with Evening's Freshness",
    "wake wef": "Wake with Evening's Freshness",
    "wwef": "Wake with Evening's Freshness",
    "wake...": "Wake with Evening's Freshness",
    "wake w/eve. freshness": "Wake with Evening's Freshness",
    "wake w/evening...": "Wake with Evening's Freshness",
    "wake": "Wake with Evening's Freshness",
    "wakes": "Wake with Evening's Freshness",
    "wakeys": "Wake with Evening's Freshness",
    "waste man op": "Waste Management Operation",
    "wmrh": "WMRH Talk Radio",
    # misspellings not fixed by difflib
    "2th tradition": "Second Tradition: Domain",
    "carver's meat packing": "Carver's Meat Packing and Storage",
    "dominate: skillcard": "Dominate",
    "dominat skill": "Dominate",
    "golgonda": "Golconda: Inner Peace",
    "info superhighway": "Information Highway",
    "judgement": "Judgment: Camarilla Segregation",
    "krcg newspaper": "KRCG News Radio",
    "krcg radio station": "KRCG News Radio",
    "obfuscate skill": "Obfuscate",
    "ps: istanbul": "Praxis Seizure: Istanbul",
    "rumour mill tabloid": "Rumor Mill, Tabloid Newspaper, The",
    "soul gems": "Soul Gem of Etrius",
    "tomb of rameses the cheesemonger": "Tomb of Rameses III",
    "truth of a 1000 lies": "Truth of a Thousand Lies",
}
#: type order for deck display
TYPE_ORDER = [
    "Master",
    "Conviction",
    "Action",
    "Action/Combat",
    "Action/Reaction",
    "Political Action",
    "Action Modifier",
    "Action Modifier/Reaction",
    "Action Modifier/Combat",
    "Combat",
    "Combat/Action",
    "Combat/Action Modifier",
    "Combat/Reaction",
    "Reaction",
    "Reaction/Action Modifier",
    "Reaction/Combat",
    "Power",
    "Equipment",
    "Ally",
    "Retainer",
    "Event",
]
