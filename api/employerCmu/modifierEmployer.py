import sys
sys.path.insert(0,r'C:\Users\Delmas brou\Desktop\CMU\clientCmu')
from PySide6 import QtWidgets
from fenetre.Em import Ui_Form
from api.conServer import client

class modifierEmployer(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(modifierEmployer,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Modifier Dossier Patient")
        self.connecte()
        self.reussi.setVisible(False)
        
    def ajouter(self):
        self.n = self.nom.text()
        self.p = self.prenom.text()
        self.ncm = int(self.ncmu.text())
        self.agee = int(self.age.text())
        self.isnn = int(self.isn.text())
        self.ville = self.vill.text()
        if self.h.text() == "oui":
            self.ho = True
        elif self.h.text() == "non":
            self.ho = False
        if self.f.text() == "oui":
            self.fe = True
        elif self.f.text() == "non":
            self.fe = False
        if self.e.text() == "oui":
            self.en = True
        elif self.e.text() == "non":
            self.en = False
        client.service.modifierDossierPat(self.isnn,self.n,self.p,self.ncm,self.ville,self.agee,self.ho,self.fe,self.en)
        self.nom.clear()
        self.prenom.clear()
        self.ncmu.clear()
        self.age.clear()
        self.isn.clear()
        self.vill.clear()
        self.h.clear()
        self.f.clear()
        self.e.clear()
        self.reussi.setVisible(True)
        
    def deconnectionn(self):
        from api.authentification import authentificatio
        self.close()
        self.ab = authentificatio()
        self.ab.show()
    
    def retoure(self):
        from api.employerCmu.acceuilEmployer import acceuilE
        self.close()
        self.a = acceuilE()
        self.a.show()
        
    def connecte(self):
        self.enregistrer.clicked.connect(self.ajouter)
        self.deconnection.clicked.connect(self.deconnectionn)
        self.retour.clicked.connect(self.retoure)

if __name__ == "__main__":
    app = QtWidgets.QApplication()
    window = modifierEmployer()
    window.show()
    app.exec()