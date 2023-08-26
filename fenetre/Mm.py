# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'medecin-M.ui'
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
    QPushButton, QSizePolicy, QSplitter, QTextEdit,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(603, 562)
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
        self.splitter_4 = QSplitter(Form)
        self.splitter_4.setObjectName(u"splitter_4")
        self.splitter_4.setGeometry(QRect(30, 530, 539, 24))
        self.splitter_4.setOrientation(Qt.Horizontal)
        self.deconnection = QPushButton(self.splitter_4)
        self.deconnection.setObjectName(u"deconnection")
        self.splitter_4.addWidget(self.deconnection)
        self.enregistrer = QPushButton(self.splitter_4)
        self.enregistrer.setObjectName(u"enregistrer")
        self.splitter_4.addWidget(self.enregistrer)
        self.retour = QPushButton(self.splitter_4)
        self.retour.setObjectName(u"retour")
        self.splitter_4.addWidget(self.retour)
        self.op = QLabel(Form)
        self.op.setObjectName(u"op")
        self.op.setGeometry(QRect(260, 490, 121, 20))
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 60, 541, 411))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.hv = QTextEdit(self.widget)
        self.hv.setObjectName(u"hv")
        self.hv.setEnabled(True)

        self.gridLayout.addWidget(self.hv, 2, 1, 1, 1)

        self.am = QTextEdit(self.widget)
        self.am.setObjectName(u"am")
        self.am.setEnabled(True)

        self.gridLayout.addWidget(self.am, 1, 1, 1, 1)

        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 1, 0, 1, 1)

        self.label_12 = QLabel(self.widget)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 3, 0, 1, 1)

        self.rm = QTextEdit(self.widget)
        self.rm.setObjectName(u"rm")
        self.rm.setEnabled(True)

        self.gridLayout.addWidget(self.rm, 3, 1, 1, 1)

        self.label_11 = QLabel(self.widget)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 2, 0, 1, 1)

        self.splitter_2 = QSplitter(self.widget)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.splitter = QSplitter(self.splitter_2)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.label_4 = QLabel(self.splitter)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(60, 0))
        self.label_4.setMaximumSize(QSize(60, 16777215))
        self.splitter.addWidget(self.label_4)
        self.splitter_2.addWidget(self.splitter)
        self.isnn = QLineEdit(self.splitter_2)
        self.isnn.setObjectName(u"isnn")
        self.splitter_2.addWidget(self.isnn)

        self.gridLayout.addWidget(self.splitter_2, 0, 0, 1, 2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"MODIFIER DOSSIER PATIENT", None))
        self.deconnection.setText(QCoreApplication.translate("Form", u"DECONNECTION", None))
        self.enregistrer.setText(QCoreApplication.translate("Form", u"ENREGISTRER", None))
        self.retour.setText(QCoreApplication.translate("Form", u"RETOUR", None))
        self.op.setText(QCoreApplication.translate("Form", u"operation effectu\u00e9e...", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Antecedents Medicaux :", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"Resumes Medicaux :", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Historique Vaccination :", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"ISN          :", None))
    # retranslateUi

