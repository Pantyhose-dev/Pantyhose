# ==========================================================
# ULTIMATE ASCII RPG — LEGEND OF THE VOID
# ==========================================================

import random, json, os, sys, time

SAVE_FILE = "ultimate_save.json"
PERMADEATH = False   # set True for hardcore mode

# ------------------ UTILS ------------------
def slow(t, d=0.015):
    for c in t:
        print(c, end="", flush=True)
        time.sleep(d)
    print()

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def line():
    print("=" * 90)

def choose(p, o):
    while True:
        c = input(p).lower().strip()
        if c in o:
            return c
        print("Choose:", ",".join(o))

# ------------------ ASCII ------------------
TITLE = r"""
██╗   ██╗██╗   ██╗████████╗██╗███╗   ███╗ █████╗ ████████╗███████╗
██║   ██║██║   ██║╚══██╔══╝██║████╗ ████║██╔══██╗╚══██╔══╝██╔════╝
██║   ██║██║   ██║   ██║   ██║██╔████╔██║███████║   ██║   █████╗
██║   ██║██║   ██║   ██║   ██║██║╚██╔╝██║██╔══██║   ██║   ██╔══╝
╚██████╔╝╚██████╔╝   ██║   ██║██║ ╚═╝ ██║██║  ██║   ██║   ███████╗
 ╚═════╝  ╚═════╝    ╚═╝   ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝

 An ASCII Python Powered Fantasy Adventure
"""

DRAGON = r"""
            /\_/\  
   __,---,__/ o o )
 /  _      ) =ø= (
/  / \    /  .---'
\  \_/   /  /
 '._      )_/
    '--.____)
"""

MAP = r"""
 [F] Forest ---- [R] Ruins ---- [D] Dungeon
    |               |
 [T] Town ---- [C] Castle ---- [L] Dragon Lair
"""

# ------------------ PLAYER ------------------
class Player:
    def __init__(self, name, cls):
        self.name = name
        self.cls = cls
        self.level = 1
        self.xp = 0
        self.gold = 100
        self.inventory = ["potion"]
        self.weapon = {"name": "Fists", "atk": 0}
        self.armor = {"name": "Cloth", "def": 0}
        self.skills = []

        if cls == "warrior":
            self.max_hp, self.atk, self.mana = 80, 8, 0
        elif cls == "mage":
            self.max_hp, self.atk, self.mana = 55, 4, 40
        else:
            self.max_hp, self.atk, self.mana = 65, 6, 15

        self.hp = self.max_hp

    def power(self):
        return self.atk + self.weapon["atk"]

    def defense(self):
        return self.armor["def"]

    def heal(self):
        if "potion" in self.inventory:
            self.hp = min(self.max_hp, self.hp + 35)
            self.inventory.remove("potion")
            slow("You drink a potion.")
        else:
            slow("No potions!")

    def level_up(self):
        self.level += 1
        self.max_hp += 15
        self.atk += 3
        self.hp = self.max_hp
        self.mana += 10
        slow(f"*** LEVEL {self.level}! Choose a skill! ***")
        skill = choose("(F)ire (I)ce (L)ightning (P)assive: ", ["f","i","l","p"])
        self.skills.append(skill)

# ------------------ ENEMIES ------------------
ENEMIES = [
    {"name":"Goblin","hp":30,"atk":6,"xp":20,"gold":15},
    {"name":"Cultist","hp":35,"atk":7,"xp":30,"gold":20},
    {"name":"Wraith","hp":40,"atk":8,"xp":35,"gold":25},
]

# ------------------ COMBAT ------------------
def combat(p, e):
    slow(f"A {e['name']} appears!")
    while e["hp"] > 0 and p.hp > 0:
        line()
        slow(f"{p.name} HP {p.hp}/{p.max_hp} MP {p.mana}")
        slow(f"{e['name']} HP {e['hp']}")
        slow("(A)ttack (S)kill (P)otion (R)un")
        c = choose("> ", ["a","s","p","r"])

        if c == "a":
            dmg = random.randint(1, p.power())
            e["hp"] -= dmg
            slow(f"You hit for {dmg}.")
        elif c == "s" and p.skills and p.mana >= 5:
            p.mana -= 5
            dmg = random.randint(12,25)
            e["hp"] -= dmg
            slow(f"Magic hits for {dmg}!")
        elif c == "p":
            p.heal()
        elif c == "r" and random.random() < 0.35:
            slow("You escape!")
            return

        if e["hp"] > 0:
            dmg = max(1, random.randint(1, e["atk"]) - p.defense())
            p.hp -= dmg
            slow(f"{e['name']} hits for {dmg}.")

    if p.hp <= 0:
        slow("YOU HAVE FALLEN.")
        if PERMADEATH and os.path.exists(SAVE_FILE):
            os.remove(SAVE_FILE)
        sys.exit()

    slow(f"{e['name']} defeated!")
    p.xp += e["xp"]
    p.gold += e["gold"]
    if p.xp >= p.level * 50:
        p.level_up()

# ------------------ DUNGEON ------------------
def dungeon(p):
    slow("You descend into a procedural dungeon...")
    for _ in range(random.randint(2,4)):
        combat(p, random.choice(ENEMIES).copy())
    slow("You escape the dungeon alive.")

# ------------------ TOWN ------------------
def town(p):
    slow("Town hub:")
    slow("(B)uy potion (10g)  (W)eapon  (A)rmor  (R)est")
    c = choose("> ", ["b","w","a","r"])
    if c == "b" and p.gold >= 10:
        p.gold -= 10
        p.inventory.append("potion")
    elif c == "w":
        p.weapon = {"name":"Sword","atk":5}
    elif c == "a":
        p.armor = {"name":"Plate","def":4}
    elif c == "r":
        p.hp = p.max_hp

# ------------------ DRAGON ------------------
def dragon_lair(p):
    clear()
    print(DRAGON)
    slow("THE DRAGON LORD RISES.")
    dragon = {"name":"Dragon Lord","hp":200,"atk":18,"xp":500,"gold":1000}
    combat(p, dragon)
    slow("ENDING UNLOCKED: LEGEND OF THE VOID")
    sys.exit()

# ------------------ SAVE ------------------
def save(p):
    with open(SAVE_FILE,"w") as f:
        json.dump(p.__dict__, f)
    slow("Game saved.")

def load():
    with open(SAVE_FILE) as f:
        data = json.load(f)
    p = Player(data["name"], data["cls"])
    p.__dict__.update(data)
    return p

# ------------------ MAIN ------------------
def main():
    clear()
    print(TITLE)
    line()

    if os.path.exists(SAVE_FILE):
        slow("(N)ew (L)oad")
        p = load() if choose("> ", ["n","l"]) == "l" else new_game()
    else:
        p = new_game()

    while True:
        line()
        print(MAP)
        slow(f"{p.name} Lv{p.level} HP {p.hp}/{p.max_hp} Gold {p.gold}")
        slow("(F)orest (R)uins (D)ungeon (T)own (L)air (S)ave (Q)uit")
        c = choose("> ", ["f","r","d","t","l","s","q"])

        if c == "f": combat(p, random.choice(ENEMIES).copy())
        elif c == "r": combat(p, random.choice(ENEMIES).copy())
        elif c == "d": dungeon(p)
        elif c == "t": town(p)
        elif c == "l": dragon_lair(p)
        elif c == "s": save(p)
        elif c == "q": break

def new_game():
    slow("Choose class (W)arrior (M)age (R)ogue")
    cls = {"w":"warrior","m":"mage","r":"rogue"}[choose("> ", ["w","m","r"])]
    return Player(input("Name: "), cls)

if __name__ == "__main__":
    main()
