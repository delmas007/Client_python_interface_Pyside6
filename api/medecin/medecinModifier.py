import sys
sys.path.insert(0,r'C:\Users\Delmas brou\Desktop\CMU\clientCmu')
from PySide6 import QtWidgets
from fenetre.Mm import Ui_Form


class modifierMedecin(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(modifierMedecin,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Modifier Dossier Patient")
        self.modifierr()
        self.op.setVisible(False)
        
    def modifier(self):
        from api.conServer import client
        self.isnnn = self.isnn.text()
        self.amm = self.am.toPlainText()
        self.hvv = self.hv.toPlainText()
        self.rmm = self.rm.toPlainText()
        self.s = client.service.modifierdossier(self.isnnn,self.amm,self.hvv,self.rmm)
        self.isnn.clear()
        self.am.clear()
        self.hv.clear()
        self.rm.clear()
        self.op.setVisible(True)
        
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
        
    def modifierr(self):
        self.enregistrer.clicked.connect(self.modifier)
        self.deconnection.clicked.connect(self.deconnectionn)
        self.retour.clicked.connect(self.retoure)
                
if __name__ == "__main__":
    app = QtWidgets.QApplication()
    window = modifierMedecin()
    window.show()
    app.exec()