import sys
sys.path.insert(0,r'C:\Users\Delmas brou\Desktop\CMU\clientCmu')
from PySide6 import QtWidgets
from fenetre.acceuilEmployer import Ui_Form

class acceuilE(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(acceuilE,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Acceuil employer")
        self.connectee()
    
    def ajouter(self):
        from api.employerCmu.AjouterDossierPatient import apple
        self.close()
        self.cc = apple()
        self.cc.show()
    
    def modifier(self):
        from api.employerCmu.modifierEmployer import modifierEmployer
        self.close()
        self.dd = modifierEmployer()
        self.dd.show()
    
    def supprimer(self):
        from api.employerCmu.supprimerDossierPatient import supprimerDossier
        self.close()
        self.mm = supprimerDossier()
        self.mm.show()
    
    def deconnection(self):
        from api.authentification import authentificatio
        self.close()
        self.a = authentificatio()
        self.a.show()
    
    def connectee(self):
        self.a.clicked.connect(self.ajouter)
        self.m.clicked.connect(self.modifier)
        self.s.clicked.connect(self.supprimer)
        self.d.clicked.connect(self.deconnection)
        
    
if __name__ == "__main__":
    app = QtWidgets.QApplication()
    window = acceuilE()
    window.show()
    app.exec()