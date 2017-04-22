#!/usr/bin/env python

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *

app = QApplication(sys.argv)

web = QWebView()
web.load(QUrl("http://localhost:63342/particles/particles.html?_ijt=ufj5hjkjubeko0dr7nrqhh5pul"))
web.show()

sys.exit(app.exec_())