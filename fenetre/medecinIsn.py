# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'medecinIsn.ui'
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
    QPushButton, QSizePolicy, QWidget)

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
        self.lmot = QLineEdit(self.layoutWidget)
        self.lmot.setObjectName(u"lmot")

        self.gridLayout.addWidget(self.lmot, 0, 1, 1, 1)

        self.motP = QLabel(self.layoutWidget)
        self.motP.setObjectName(u"motP")

        self.gridLayout.addWidget(self.motP, 0, 0, 1, 1)

        self.bouton = QPushButton(self.layoutWidget)
        self.bouton.setObjectName(u"bouton")
        self.bouton.setAutoFillBackground(False)

        self.gridLayout.addWidget(self.bouton, 1, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"ISN PATIENT", None))
        self.motP.setText(QCoreApplication.translate("Form", u"isn patient", None))
        self.bouton.setText(QCoreApplication.translate("Form", u"ENTRER", None))
    # retranslateUi

