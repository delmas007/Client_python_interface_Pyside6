import sys
sys.path.insert(0,r'C:\Users\Delmas brou\Desktop\CMU\clientCmu')
from PySide6 import QtWidgets
from fenetre.Es import Ui_Form
from api.conServer import client

class supprimerDossier(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(supprimerDossier,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Supprimer Dossier Patient")
        self.supprime()
        self.op.setVisible(False)
        
    def supprimer(self):
        self.code = self.lmot.text()
        self.a =client.service.supprimerDossierPatientEtConsultations(self.code)
        if(self.a == 1):
            self.op.setVisible(True)  
            
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
        
    def supprime(self):
        self.bouton.clicked.connect(self.supprimer)
        self.d.clicked.connect(self.deconnectionn)
        self.r.clicked.connect(self.retoure)

if __name__ == "__main__":
    app = QtWidgets.QApplication()
    window = supprimerDossier()
    window.show()
    app.exec()