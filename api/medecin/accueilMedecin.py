import sys
sys.path.insert(0,r'C:\Users\Delmas brou\Desktop\CMU\clientCmu')
from PySide6 import QtWidgets
from fenetre.acceuilMedecin import Ui_Form




class acceuilM(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(acceuilM,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Acceuil medecin")
        self.connect()
    
    def consultation(self):
        from api.medecin.medecinConsultation import applMedecinConsultation
        self.close()
        self.cc = applMedecinConsultation()
        self.cc.show()
    
    def dossier(self):
        from api.medecin.isn import isne
        self.close()
        self.dd = isne()
        self.dd.show()
    
    def modifier(self):
        from api.medecin.medecinModifier import modifierMedecin
        self.close()
        self.mm = modifierMedecin()
        self.mm.show()
    
    def deconnection(self):
        from api.authentification import authentificatio
        self.close()
        self.a = authentificatio()
        self.a.show()
    
    def connect(self):
        self.c.clicked.connect(self.consultation)
        self.cd.clicked.connect(self.dossier)
        self.md.clicked.connect(self.modifier)
        self.d.clicked.connect(self.deconnection)
    
if __name__ == "__main__":
    app = QtWidgets.QApplication()
    window = acceuilM()
    window.show()
    app.exec()