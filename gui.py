# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(322, 534)
        MainWindow.setMinimumSize(QtCore.QSize(322, 534))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.CalculatorViewBox = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.CalculatorViewBox.setGeometry(QtCore.QRect(10, 10, 301, 100))
        self.CalculatorViewBox.setMinimumSize(QtCore.QSize(301, 100))
        self.CalculatorViewBox.setObjectName("CalculatorViewBox")
        self.percentButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.percentButton.setGeometry(QtCore.QRect(10, 120, 64, 50))
        self.percentButton.setMinimumSize(QtCore.QSize(64, 50))
        self.percentButton.setMaximumSize(QtCore.QSize(64, 50))
        self.percentButton.setObjectName("percentButton")
        self.fractionButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.fractionButton.setGeometry(QtCore.QRect(10, 180, 64, 50))
        self.fractionButton.setMinimumSize(QtCore.QSize(64, 50))
        self.fractionButton.setMaximumSize(QtCore.QSize(64, 50))
        self.fractionButton.setObjectName("fractionButton")
        self.sevenButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.sevenButton.setGeometry(QtCore.QRect(10, 240, 64, 50))
        self.sevenButton.setMinimumSize(QtCore.QSize(64, 50))
        self.sevenButton.setMaximumSize(QtCore.QSize(64, 50))
        self.sevenButton.setObjectName("sevenButton")
        self.foutButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.foutButton.setGeometry(QtCore.QRect(10, 300, 64, 50))
        self.foutButton.setMinimumSize(QtCore.QSize(64, 50))
        self.foutButton.setMaximumSize(QtCore.QSize(64, 50))
        self.foutButton.setObjectName("foutButton")
        self.oneButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.oneButton.setGeometry(QtCore.QRect(10, 360, 64, 50))
        self.oneButton.setMinimumSize(QtCore.QSize(64, 50))
        self.oneButton.setMaximumSize(QtCore.QSize(64, 50))
        self.oneButton.setObjectName("oneButton")
        self.flipsignButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.flipsignButton.setGeometry(QtCore.QRect(10, 420, 64, 50))
        self.flipsignButton.setMinimumSize(QtCore.QSize(64, 50))
        self.flipsignButton.setMaximumSize(QtCore.QSize(64, 50))
        self.flipsignButton.setObjectName("flipsignButton")
        self.zeroButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.zeroButton.setGeometry(QtCore.QRect(90, 420, 64, 50))
        self.zeroButton.setMinimumSize(QtCore.QSize(64, 50))
        self.zeroButton.setMaximumSize(QtCore.QSize(64, 50))
        self.zeroButton.setObjectName("zeroButton")
        self.eightButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.eightButton.setGeometry(QtCore.QRect(90, 240, 64, 50))
        self.eightButton.setMinimumSize(QtCore.QSize(64, 50))
        self.eightButton.setMaximumSize(QtCore.QSize(64, 50))
        self.eightButton.setObjectName("eightButton")
        self.clearButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.clearButton.setGeometry(QtCore.QRect(90, 120, 64, 50))
        self.clearButton.setMinimumSize(QtCore.QSize(64, 50))
        self.clearButton.setMaximumSize(QtCore.QSize(64, 50))
        self.clearButton.setObjectName("clearButton")
        self.squareButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.squareButton.setGeometry(QtCore.QRect(90, 180, 64, 50))
        self.squareButton.setMinimumSize(QtCore.QSize(64, 50))
        self.squareButton.setMaximumSize(QtCore.QSize(64, 50))
        self.squareButton.setObjectName("squareButton")
        self.fiveButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.fiveButton.setGeometry(QtCore.QRect(90, 300, 64, 50))
        self.fiveButton.setMinimumSize(QtCore.QSize(64, 50))
        self.fiveButton.setMaximumSize(QtCore.QSize(64, 50))
        self.fiveButton.setObjectName("fiveButton")
        self.twoButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.twoButton.setGeometry(QtCore.QRect(90, 360, 64, 50))
        self.twoButton.setMinimumSize(QtCore.QSize(64, 50))
        self.twoButton.setMaximumSize(QtCore.QSize(64, 50))
        self.twoButton.setObjectName("twoButton")
        self.decimalButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.decimalButton.setGeometry(QtCore.QRect(170, 420, 64, 50))
        self.decimalButton.setMinimumSize(QtCore.QSize(64, 50))
        self.decimalButton.setMaximumSize(QtCore.QSize(64, 50))
        self.decimalButton.setObjectName("decimalButton")
        self.nineButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.nineButton.setGeometry(QtCore.QRect(170, 240, 64, 50))
        self.nineButton.setMinimumSize(QtCore.QSize(64, 50))
        self.nineButton.setMaximumSize(QtCore.QSize(64, 50))
        self.nineButton.setObjectName("nineButton")
        self.piButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.piButton.setGeometry(QtCore.QRect(170, 120, 64, 50))
        self.piButton.setMinimumSize(QtCore.QSize(64, 50))
        self.piButton.setMaximumSize(QtCore.QSize(64, 50))
        self.piButton.setObjectName("piButton")
        self.squarerootButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.squarerootButton.setGeometry(QtCore.QRect(170, 180, 64, 50))
        self.squarerootButton.setMinimumSize(QtCore.QSize(64, 50))
        self.squarerootButton.setMaximumSize(QtCore.QSize(64, 50))
        self.squarerootButton.setObjectName("squarerootButton")
        self.sixButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.sixButton.setGeometry(QtCore.QRect(170, 300, 64, 50))
        self.sixButton.setMinimumSize(QtCore.QSize(64, 50))
        self.sixButton.setMaximumSize(QtCore.QSize(64, 50))
        self.sixButton.setObjectName("sixButton")
        self.threeButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.threeButton.setGeometry(QtCore.QRect(170, 360, 64, 50))
        self.threeButton.setMinimumSize(QtCore.QSize(64, 50))
        self.threeButton.setMaximumSize(QtCore.QSize(64, 50))
        self.threeButton.setObjectName("threeButton")
        self.equalsButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.equalsButton.setGeometry(QtCore.QRect(250, 420, 64, 50))
        self.equalsButton.setMinimumSize(QtCore.QSize(64, 50))
        self.equalsButton.setMaximumSize(QtCore.QSize(64, 50))
        self.equalsButton.setObjectName("equalsButton")
        self.multiplicationButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.multiplicationButton.setGeometry(QtCore.QRect(250, 240, 64, 50))
        self.multiplicationButton.setMinimumSize(QtCore.QSize(64, 50))
        self.multiplicationButton.setMaximumSize(QtCore.QSize(64, 50))
        self.multiplicationButton.setObjectName("multiplicationButton")
        self.backButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(250, 120, 64, 50))
        self.backButton.setMinimumSize(QtCore.QSize(64, 50))
        self.backButton.setMaximumSize(QtCore.QSize(64, 50))
        self.backButton.setObjectName("backButton")
        self.divisionButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.divisionButton.setGeometry(QtCore.QRect(250, 180, 64, 50))
        self.divisionButton.setMinimumSize(QtCore.QSize(64, 50))
        self.divisionButton.setMaximumSize(QtCore.QSize(64, 50))
        self.divisionButton.setObjectName("divisionButton")
        self.subtractionButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.subtractionButton.setGeometry(QtCore.QRect(250, 300, 64, 50))
        self.subtractionButton.setMinimumSize(QtCore.QSize(64, 50))
        self.subtractionButton.setMaximumSize(QtCore.QSize(64, 50))
        self.subtractionButton.setObjectName("subtractionButton")
        self.additionButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.additionButton.setGeometry(QtCore.QRect(250, 360, 64, 50))
        self.additionButton.setMinimumSize(QtCore.QSize(64, 50))
        self.additionButton.setMaximumSize(QtCore.QSize(64, 50))
        self.additionButton.setObjectName("additionButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 322, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.CalculatorViewBox.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"left\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.percentButton.setText(_translate("MainWindow", "%"))
        self.fractionButton.setText(_translate("MainWindow", "1/x"))
        self.sevenButton.setText(_translate("MainWindow", "7"))
        self.foutButton.setText(_translate("MainWindow", "4"))
        self.oneButton.setText(_translate("MainWindow", "1"))
        self.flipsignButton.setText(_translate("MainWindow", "+/-"))
        self.zeroButton.setText(_translate("MainWindow", "0"))
        self.eightButton.setText(_translate("MainWindow", "8"))
        self.clearButton.setText(_translate("MainWindow", "C"))
        self.squareButton.setText(_translate("MainWindow", "x^2"))
        self.fiveButton.setText(_translate("MainWindow", "5"))
        self.twoButton.setText(_translate("MainWindow", "2"))
        self.decimalButton.setText(_translate("MainWindow", "."))
        self.nineButton.setText(_translate("MainWindow", "9"))
        self.piButton.setText(_translate("MainWindow", "π"))
        self.squarerootButton.setText(_translate("MainWindow", "√\'X"))
        self.sixButton.setText(_translate("MainWindow", "6"))
        self.threeButton.setText(_translate("MainWindow", "3"))
        self.equalsButton.setText(_translate("MainWindow", "="))
        self.multiplicationButton.setText(_translate("MainWindow", "×"))
        self.backButton.setText(_translate("MainWindow", "Back"))
        self.divisionButton.setText(_translate("MainWindow", "÷"))
        self.subtractionButton.setText(_translate("MainWindow", "-"))
        self.additionButton.setText(_translate("MainWindow", "+"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())