names = """Damini
Matthew
PATRICK
Samantha
Luis
Grace
Will
Joyce
Riccardo
Emily
Esben
Scott
Franziska
Josiah""".split('\n')
from random import shuffle
shuffle(names)

for name in names:
    print(name.title())
