# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'medecin-A.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QSizePolicy, QSplitter, QTextEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(605, 541)
        palette = QPalette()
        brush = QBrush(QColor(85, 85, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        Form.setPalette(palette)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet(u"background-color: rgb(85, 85, 255);")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(130, 20, 341, 31))
        font = QFont()
        font.setFamilies([u"Arial Black"])
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 60, 561, 391))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.layoutWidget)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 6, 0, 1, 1)

        self.am = QTextEdit(self.layoutWidget)
        self.am.setObjectName(u"am")
        self.am.setEnabled(False)

        self.gridLayout.addWidget(self.am, 4, 1, 1, 1)

        self.rm = QTextEdit(self.layoutWidget)
        self.rm.setObjectName(u"rm")
        self.rm.setEnabled(False)

        self.gridLayout.addWidget(self.rm, 6, 1, 1, 1)

        self.hv = QTextEdit(self.layoutWidget)
        self.hv.setObjectName(u"hv")
        self.hv.setEnabled(False)

        self.gridLayout.addWidget(self.hv, 5, 1, 1, 1)

        self.label_10 = QLabel(self.layoutWidget)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 4, 0, 1, 1)

        self.splitter_2 = QSplitter(self.layoutWidget)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.label_7 = QLabel(self.splitter_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(60, 0))
        self.label_7.setMaximumSize(QSize(60, 16777215))
        self.splitter_2.addWidget(self.label_7)
        self.ville = QLabel(self.splitter_2)
        self.ville.setObjectName(u"ville")
        self.splitter_2.addWidget(self.ville)
        self.label_5 = QLabel(self.splitter_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(60, 16777215))
        self.splitter_2.addWidget(self.label_5)
        self.age = QLabel(self.splitter_2)
        self.age.setObjectName(u"age")
        self.splitter_2.addWidget(self.age)
        self.label_6 = QLabel(self.splitter_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(60, 16777215))
        self.splitter_2.addWidget(self.label_6)
        self.h = QLabel(self.splitter_2)
        self.h.setObjectName(u"h")
        self.splitter_2.addWidget(self.h)

        self.gridLayout.addWidget(self.splitter_2, 1, 0, 1, 2)

        self.label_11 = QLabel(self.layoutWidget)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 5, 0, 1, 1)

        self.splitter = QSplitter(self.layoutWidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.label_2 = QLabel(self.splitter)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setEnabled(True)
        self.label_2.setMinimumSize(QSize(60, 0))
        self.label_2.setMaximumSize(QSize(0, 16777215))
        self.splitter.addWidget(self.label_2)
        self.nom = QLabel(self.splitter)
        self.nom.setObjectName(u"nom")
        self.nom.setMinimumSize(QSize(60, 0))
        self.splitter.addWidget(self.nom)
        self.label_3 = QLabel(self.splitter)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(60, 16777215))
        self.splitter.addWidget(self.label_3)
        self.prenom = QLabel(self.splitter)
        self.prenom.setObjectName(u"prenom")
        self.splitter.addWidget(self.prenom)
        self.label_4 = QLabel(self.splitter)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(60, 0))
        self.label_4.setMaximumSize(QSize(60, 16777215))
        self.splitter.addWidget(self.label_4)
        self.ncmu = QLabel(self.splitter)
        self.ncmu.setObjectName(u"ncmu")
        self.splitter.addWidget(self.ncmu)

        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 2)

        self.splitter_3 = QSplitter(self.layoutWidget)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Horizontal)
        self.label_8 = QLabel(self.splitter_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(60, 16777215))
        self.splitter_3.addWidget(self.label_8)
        self.f = QLabel(self.splitter_3)
        self.f.setObjectName(u"f")
        self.splitter_3.addWidget(self.f)
        self.label_9 = QLabel(self.splitter_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(60, 16777215))
        self.splitter_3.addWidget(self.label_9)
        self.e = QLabel(self.splitter_3)
        self.e.setObjectName(u"e")
        self.splitter_3.addWidget(self.e)

        self.gridLayout.addWidget(self.splitter_3, 3, 1, 1, 1)

        self.splitter_4 = QSplitter(Form)
        self.splitter_4.setObjectName(u"splitter_4")
        self.splitter_4.setGeometry(QRect(20, 490, 561, 24))
        self.splitter_4.setOrientation(Qt.Horizontal)
        self.deconnection = QPushButton(self.splitter_4)
        self.deconnection.setObjectName(u"deconnection")
        self.splitter_4.addWidget(self.deconnection)
        self.retour = QPushButton(self.splitter_4)
        self.retour.setObjectName(u"retour")
        self.splitter_4.addWidget(self.retour)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"DOSSIER PATIENT", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"Resumes Medicaux :", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Antecedents Medicaux :", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"VILLE :", None))
        self.ville.setText("")
        self.label_5.setText(QCoreApplication.translate("Form", u"AGE :", None))
        self.age.setText("")
        self.label_6.setText(QCoreApplication.translate("Form", u"HOMME :", None))
        self.h.setText("")
        self.label_11.setText(QCoreApplication.translate("Form", u"Historique Vaccination :", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"NOM :", None))
        self.nom.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"PRENOM :", None))
        self.prenom.setText("")
        self.label_4.setText(QCoreApplication.translate("Form", u"N'CMU :", None))
        self.ncmu.setText("")
        self.label_8.setText(QCoreApplication.translate("Form", u"FEMME :", None))
        self.f.setText("")
        self.label_9.setText(QCoreApplication.translate("Form", u"ENCEINTE :", None))
        self.e.setText("")
        self.deconnection.setText(QCoreApplication.translate("Form", u"DECONNECTION", None))
        self.retour.setText(QCoreApplication.translate("Form", u"RETOUR", None))
    # retranslateUi

