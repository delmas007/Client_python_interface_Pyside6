# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'employer-sup.ui'
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
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(50, 150, 471, 271))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.motP = QLabel(self.layoutWidget)
        self.motP.setObjectName(u"motP")

        self.gridLayout.addWidget(self.motP, 0, 0, 1, 1)

        self.lmot = QLineEdit(self.layoutWidget)
        self.lmot.setObjectName(u"lmot")

        self.gridLayout.addWidget(self.lmot, 0, 1, 1, 1)

        self.splitter = QSplitter(self.layoutWidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.r = QPushButton(self.splitter)
        self.r.setObjectName(u"r")
        self.r.setAutoFillBackground(False)
        self.splitter.addWidget(self.r)
        self.bouton = QPushButton(self.splitter)
        self.bouton.setObjectName(u"bouton")
        self.bouton.setAutoFillBackground(False)
        self.splitter.addWidget(self.bouton)
        self.d = QPushButton(self.splitter)
        self.d.setObjectName(u"d")
        self.d.setAutoFillBackground(False)
        self.splitter.addWidget(self.d)

        self.gridLayout.addWidget(self.splitter, 1, 1, 1, 1)

        self.op = QLabel(Form)
        self.op.setObjectName(u"op")
        self.op.setGeometry(QRect(250, 440, 121, 20))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"SUPPRIMER DOSSIER PATIENT", None))
        self.motP.setText(QCoreApplication.translate("Form", u"ISN", None))
        self.r.setText(QCoreApplication.translate("Form", u"RETOUR", None))
        self.bouton.setText(QCoreApplication.translate("Form", u"SUPPRIMER", None))
        self.d.setText(QCoreApplication.translate("Form", u"DECONNECTER", None))
        self.op.setText(QCoreApplication.translate("Form", u"Op\u00e9ration effectu\u00e9e...", None))
    # retranslateUi

