# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'acceuilMedecin.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QSplitter, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(586, 524)
        Form.setStyleSheet(u"background-color: rgb(85, 85, 255);")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(130, 20, 311, 31))
        font = QFont()
        font.setFamilies([u"Arial Black"])
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.d = QPushButton(Form)
        self.d.setObjectName(u"d")
        self.d.setGeometry(QRect(210, 390, 171, 24))
        self.splitter = QSplitter(Form)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(20, 230, 531, 24))
        self.splitter.setOrientation(Qt.Horizontal)
        self.c = QPushButton(self.splitter)
        self.c.setObjectName(u"c")
        self.splitter.addWidget(self.c)
        self.cd = QPushButton(self.splitter)
        self.cd.setObjectName(u"cd")
        self.splitter.addWidget(self.cd)
        self.md = QPushButton(self.splitter)
        self.md.setObjectName(u"md")
        self.splitter.addWidget(self.md)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"BIENVENUE", None))
        self.d.setText(QCoreApplication.translate("Form", u"D\u00c9CONNEXION", None))
        self.c.setText(QCoreApplication.translate("Form", u"FAIRE UNE CONSULTATION", None))
        self.cd.setText(QCoreApplication.translate("Form", u"CONSULTER DOSSIER PATIENT", None))
        self.md.setText(QCoreApplication.translate("Form", u"MODIFIER DOSSIER PATIENT", None))
    # retranslateUi

