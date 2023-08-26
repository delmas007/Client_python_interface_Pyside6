# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'patient.ui'
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
        Form.resize(672, 530)
        palette = QPalette()
        Form.setPalette(palette)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet(u"background-color: rgb(85, 85, 255);")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(170, 20, 341, 31))
        font = QFont()
        font.setFamilies([u"Arial Black"])
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.splitter_4 = QSplitter(Form)
        self.splitter_4.setObjectName(u"splitter_4")
        self.splitter_4.setGeometry(QRect(10, 500, 641, 24))
        self.splitter_4.setOrientation(Qt.Horizontal)
        self.deconnection = QPushButton(self.splitter_4)
        self.deconnection.setObjectName(u"deconnection")
        self.deconnection.setMaximumSize(QSize(350, 16777215))
        self.splitter_4.addWidget(self.deconnection)
        self.enregistrer = QPushButton(self.splitter_4)
        self.enregistrer.setObjectName(u"enregistrer")
        self.splitter_4.addWidget(self.enregistrer)
        self.ville = QLabel(Form)
        self.ville.setObjectName(u"ville")
        self.ville.setGeometry(QRect(53, 300, 16, 16))
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 60, 651, 391))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.splitter_2 = QSplitter(self.layoutWidget)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.splitter = QSplitter(self.splitter_2)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.label_11 = QLabel(self.splitter)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(60, 16777215))
        self.splitter.addWidget(self.label_11)
        self.code = QLineEdit(self.splitter)
        self.code.setObjectName(u"code")
        self.code.setEnabled(False)
        self.splitter.addWidget(self.code)
        self.label_5 = QLabel(self.splitter)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(60, 0))
        self.label_5.setMaximumSize(QSize(110, 16777215))
        self.splitter.addWidget(self.label_5)
        self.reduction = QLineEdit(self.splitter)
        self.reduction.setObjectName(u"reduction")
        self.reduction.setEnabled(False)
        self.splitter.addWidget(self.reduction)
        self.splitter_2.addWidget(self.splitter)

        self.gridLayout.addWidget(self.splitter_2, 0, 0, 1, 2)

        self.d = QTextEdit(self.layoutWidget)
        self.d.setObjectName(u"d")
        self.d.setEnabled(False)

        self.gridLayout.addWidget(self.d, 2, 1, 1, 1)

        self.o = QTextEdit(self.layoutWidget)
        self.o.setObjectName(u"o")
        self.o.setEnabled(False)

        self.gridLayout.addWidget(self.o, 3, 1, 1, 1)

        self.label_12 = QLabel(self.layoutWidget)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 3, 0, 1, 1)

        self.label_14 = QLabel(self.layoutWidget)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout.addWidget(self.label_14, 2, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"CONSULTATION", None))
        self.deconnection.setText(QCoreApplication.translate("Form", u"DECONNECTION", None))
        self.enregistrer.setText(QCoreApplication.translate("Form", u"G\u00c9N\u00c9RER RE\u00c7U", None))
        self.ville.setText("")
        self.label_11.setText(QCoreApplication.translate("Form", u"CODE :", None))
        self.code.setPlaceholderText("")
        self.label_5.setText(QCoreApplication.translate("Form", u"TAUX REDUCTION :", None))
        self.reduction.setPlaceholderText("")
        self.label_12.setText(QCoreApplication.translate("Form", u"Ordonnance               :", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"Diagnostic                  :", None))
    # retranslateUi

