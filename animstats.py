import subprocess
import pickle

# import the main window object (mw) from aqt
from aqt import mw
# import the "show info" tool from utils.py
from aqt.utils import showInfo
# import all of the Qt GUI library
from aqt.qt import *

import view

# We're going to add a menu item below. First we want to create a function to
# be called when the menu item is activated.

def testFunction():
    # view.main()
    from ankidata import repetition_iterator
    import ankidata

    all_reps = []
    r = repetition_iterator()
    while 1:
        try:
            all_reps.append(r.next())
        except StopIteration:
            break
    # with open("/home/vottivott/hannes_anki_repetitions.pickle", "wr") as file:
    #     pickle.dump(all_reps, file)
    showInfo("Done!\nstart_date = " + str(ankidata.start_date))
    view.main()



# create a new menu item, "test"
action = QAction("test", mw)
# set it to call testFunction when it's clicked
action.triggered.connect(testFunction)
# and add it to the tools menu
mw.form.menuTools.addAction(action)

