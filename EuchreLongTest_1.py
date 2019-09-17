import Euchre
from GUI import GUIManager
from Manager import Manager
import pandas as pd

for i in range(10000):
    match = Euchre.Match(Manager())
    match.start_match()

data = pd.read_csv('game.log', header = None)
counts = data.groupby([0])
print(counts.size())
