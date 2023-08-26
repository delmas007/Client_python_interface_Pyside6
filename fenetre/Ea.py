# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'employer-A.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSplitter, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(672, 530)
        palette = QPalette()
        Form.setPalette(palette)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet(u"background-color: rgb(85, 85, 255);")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(160, 20, 341, 31))
        font = QFont()
        font.setFamilies([u"Arial Black"])
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.splitter_4 = QSplitter(Form)
        self.splitter_4.setObjectName(u"splitter_4")
        self.splitter_4.setGeometry(QRect(10, 480, 641, 24))
        self.splitter_4.setOrientation(Qt.Horizontal)
        self.deconnection = QPushButton(self.splitter_4)
        self.deconnection.setObjectName(u"deconnection")
        self.deconnection.setMaximumSize(QSize(350, 16777215))
        self.splitter_4.addWidget(self.deconnection)
        self.enregistrer = QPushButton(self.splitter_4)
        self.enregistrer.setObjectName(u"enregistrer")
        self.splitter_4.addWidget(self.enregistrer)
        self.retour = QPushButton(self.splitter_4)
        self.retour.setObjectName(u"retour")
        self.splitter_4.addWidget(self.retour)
        self.reussi = QLabel(Form)
        self.reussi.setObjectName(u"reussi")
        self.reussi.setGeometry(QRect(250, 410, 161, 31))
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 80, 651, 321))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(60, 16777215))

        self.gridLayout.addWidget(self.label_8, 2, 0, 1, 1)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(60, 16777215))

        self.gridLayout.addWidget(self.label_6, 1, 4, 1, 1)

        self.ncmu = QLineEdit(self.widget)
        self.ncmu.setObjectName(u"ncmu")

        self.gridLayout.addWidget(self.ncmu, 0, 5, 1, 1)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(60, 0))
        self.label_4.setMaximumSize(QSize(60, 16777215))

        self.gridLayout.addWidget(self.label_4, 0, 4, 1, 1)

        self.age = QLineEdit(self.widget)
        self.age.setObjectName(u"age")

        self.gridLayout.addWidget(self.age, 1, 1, 1, 1)

        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(60, 0))
        self.label_7.setMaximumSize(QSize(60, 16777215))

        self.gridLayout.addWidget(self.label_7, 1, 2, 1, 1)

        self.prenom = QLineEdit(self.widget)
        self.prenom.setObjectName(u"prenom")

        self.gridLayout.addWidget(self.prenom, 0, 3, 1, 1)

        self.vill = QLineEdit(self.widget)
        self.vill.setObjectName(u"vill")

        self.gridLayout.addWidget(self.vill, 1, 3, 1, 1)

        self.nom = QLineEdit(self.widget)
        self.nom.setObjectName(u"nom")

        self.gridLayout.addWidget(self.nom, 0, 1, 1, 1)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setEnabled(True)
        self.label_2.setMinimumSize(QSize(60, 0))
        self.label_2.setMaximumSize(QSize(0, 16777215))

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.h = QLineEdit(self.widget)
        self.h.setObjectName(u"h")

        self.gridLayout.addWidget(self.h, 1, 5, 1, 1)

        self.f = QLineEdit(self.widget)
        self.f.setObjectName(u"f")

        self.gridLayout.addWidget(self.f, 2, 1, 1, 1)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(60, 16777215))

        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(60, 16777215))

        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)

        self.e = QLineEdit(self.widget)
        self.e.setObjectName(u"e")

        self.gridLayout.addWidget(self.e, 2, 5, 1, 1)

        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(60, 16777215))

        self.gridLayout.addWidget(self.label_9, 2, 4, 1, 1)

        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(60, 16777215))

        self.gridLayout.addWidget(self.label_10, 2, 2, 1, 1)

        self.isn = QLineEdit(self.widget)
        self.isn.setObjectName(u"isn")

        self.gridLayout.addWidget(self.isn, 2, 3, 1, 1)

        self.ville = QLabel(Form)
        self.ville.setObjectName(u"ville")
        self.ville.setGeometry(QRect(53, 300, 16, 16))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"CREE DOSSIER PATIENT", None))
        self.deconnection.setText(QCoreApplication.translate("Form", u"DECONNECTION", None))
        self.enregistrer.setText(QCoreApplication.translate("Form", u"ENREGISTRER", None))
        self.retour.setText(QCoreApplication.translate("Form", u"RETOUR", None))
        self.reussi.setText(QCoreApplication.translate("Form", u"enregistrement reussit...", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"FEMME :", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"HOMME :", None))
        self.ncmu.setPlaceholderText(QCoreApplication.translate("Form", u"6 chiffres", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"N'CMU :", None))
        self.age.setPlaceholderText(QCoreApplication.translate("Form", u"chiffre", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"VILLE :", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"NOM :", None))
        self.h.setPlaceholderText(QCoreApplication.translate("Form", u"oui ou non", None))
        self.f.setPlaceholderText(QCoreApplication.translate("Form", u"oui ou non", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"AGE :", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"PRENOM :", None))
        self.e.setPlaceholderText(QCoreApplication.translate("Form", u"oui ou non", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"ENCEINTE :", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"ISN", None))
        self.isn.setPlaceholderText(QCoreApplication.translate("Form", u"5 chiffres", None))
        self.ville.setText("")
    # retranslateUi

