import sys
sys.path.insert(0,r'C:\Users\Delmas brou\Desktop\CMU\clientCmu')
from PySide6 import QtWidgets
from fenetre.MCo import Ui_Form
from api.conServer import client

class applMedecinConsultation(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(applMedecinConsultation,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Consultation")
        self.connecte()
        self.reussi.setVisible(False)
    
    def ajouter(self):
        if(self.ncmu.text() =="" or self.isn.text()=="" or self.ep.toPlainText() == "" or self.ds.toPlainText() == "" or self.d.toPlainText() == "" or self.o.toPlainText() == "") :
            self.reussi.setText("un champ est vide")
            self.reussi.setVisible(True)
            return
        self.ncm = int(self.ncmu.text())
        self.isnn = int(self.isn.text())
        self.epe = self.ep.toPlainText()
        self.dss = self.ds.toPlainText()
        self.dd = self.d.toPlainText()
        self.oo = self.o.toPlainText()
        c =client.service.consultation(self.epe,self.dss,self.dd,self.oo,self.isnn,self.ncm)
        if(c==1):
            self.reussi.setText("numero cmu incorrect ou inexistant")
            self.reussi.setVisible(True)
        else:
            self.ncmu.clear()
            self.isn.clear()
            self.ep.clear()
            self.ds.clear()
            self.d.clear()
            self.o.clear()
            self.reussi.setText("enregistrement reussi...")
            self.reussi.setVisible(True)
    
    def deconnectionn(self):
        from api.authentification import authentificatio
        self.close()
        self.ab = authentificatio()
        self.ab.show()
    
    def retoure(self):
        from api.medecin.accueilMedecin import acceuilM
        self.close()
        self.a = acceuilM()
        self.a.show()
        
    def connecte(self):
        self.enregistrer.clicked.connect(self.ajouter)
        self.deconnection.clicked.connect(self.deconnectionn)
        self.retour.clicked.connect(self.retoure)
        
if __name__ == "__main__":
    app = QtWidgets.QApplication()
    window = applMedecinConsultation()
    window.show()
    app.exec()