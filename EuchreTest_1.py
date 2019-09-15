import Euchre
from GUI import GUIManager
from Manager import Manager

match = Euchre.Match(Manager())
match.start_match()
