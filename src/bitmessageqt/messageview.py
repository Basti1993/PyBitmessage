from PyQt4 import QtCore, QtGui

from safehtmlparser import *

class MessageView(QtGui.QTextBrowser):
    MODE_PLAIN = 0
    MODE_HTML = 1
    TEXT_PLAIN = "HTML detected, click here to display"
    TEXT_HTML = "Click here to disable HTML"
    CONFIRM_TITLE = "Follow external link"
    CONFIRM_TEXT = "The link \"%1\" will open in a browser. It may be a security risk, it could de-anonymise you or download malicious data. Are you sure?"
    
    def __init__(self, parent = 0):
        super(MessageView, self).__init__(parent)
        self.mode = MessageView.MODE_PLAIN 
        self.html = None
        self.setOpenExternalLinks(False)
        self.setOpenLinks(False)
        self.anchorClicked.connect(self.confirmURL)
        self.out = ""
        self.outpos = 0
        self.document().setUndoRedoEnabled(False)
        self.rendering = False
        self.defaultFontPointSize = self.currentFont().pointSize()
        self.verticalScrollBar().valueChanged.connect(self.lazyRender)
    
    def mousePressEvent(self, event):
        #text = textCursor.block().text()
        if event.button() == QtCore.Qt.LeftButton and self.html and self.html.has_html and self.cursorForPosition(event.pos()).block().blockNumber() == 0:
            if self.mode == MessageView.MODE_PLAIN:
                self.showHTML()
            else:
                self.showPlain()
        else:
            super(MessageView, self).mousePressEvent(event)

    def wheelEvent(self, event):
        if (QtGui.QApplication.queryKeyboardModifiers() & QtCore.Qt.ControlModifier) == QtCore.Qt.ControlModifier and event.orientation() == QtCore.Qt.Vertical:
            numDegrees = event.delta() / 8
            numSteps = numDegrees / 15
            zoomDiff = numSteps + self.currentFont().pointSize() - self.defaultFontPointSize
            QtGui.QApplication.activeWindow().statusBar().showMessage(QtGui.QApplication.translate("MainWindow", "Zoom level %1").arg(str(zoomDiff)))
        # super will actually automatically take care of zooming
        super(MessageView, self).wheelEvent(event)

    def confirmURL(self, link):
        reply = QtGui.QMessageBox.warning(self,
            QtGui.QApplication.translate(type(self).__name__, MessageView.CONFIRM_TITLE),
            QtGui.QApplication.translate(type(self).__name__, MessageView.CONFIRM_TEXT).arg(str(link.toString())), 
            QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            QtGui.QDesktopServices.openUrl(link)

    def lazyRender(self):
        if self.rendering:
            return
        self.rendering = True
        position = self.verticalScrollBar().value()
        cursor = QtGui.QTextCursor(self.document())
        while self.outpos < len(self.out) and self.verticalScrollBar().value() >= self.document().size().height() - 2 * self.size().height():
            startpos = self.outpos
            self.outpos += 10240
            # find next end of tag
            if self.mode == MessageView.MODE_HTML:
                pos = self.out.find(">", self.outpos)
                if pos > self.outpos:
                    self.outpos = pos
            cursor.movePosition(QtGui.QTextCursor.End, QtGui.QTextCursor.MoveAnchor)
            cursor.insertHtml(QtCore.QString(self.out[startpos:self.outpos]))
        self.verticalScrollBar().setValue(position)
        self.rendering = False
    
    def showPlain(self):
        self.mode = MessageView.MODE_PLAIN
        out = self.html.raw
        if self.html.has_html:
            out = "<div align=\"center\" style=\"text-decoration: underline;\"><b>" + str(QtGui.QApplication.translate(type(self).__name__, MessageView.TEXT_PLAIN)) + "</b></div><br/>" + out
        self.out = out
        self.outpos = 0
        self.setHtml("")
        self.lazyRender()

    def showHTML(self):
        self.mode = MessageView.MODE_HTML
        out = self.html.sanitised
        out = "<div align=\"center\" style=\"text-decoration: underline;\"><b>" + str(QtGui.QApplication.translate(type(self).__name__, MessageView.TEXT_HTML)) + "</b></div><br/>" + out
        self.out = out
        self.outpos = 0
        self.setHtml("")
        self.lazyRender()

    def setContent(self, data):
        self.html = SafeHTMLParser()
        self.html.allow_picture = True
        self.html.reset()
        self.html.reset_safe()
        self.html.feed(data)
        self.html.close()
        self.showPlain()