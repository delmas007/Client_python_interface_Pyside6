import sys
sys.path.insert(0,r'C:\Users\Delmas brou\Desktop\CMU\clientCmu')
from PySide6 import QtWidgets
from fenetre.medecinIsn import Ui_Form

class isne(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(isne,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("authentification")
        self.connect()
        
    def entrer(self):
        from api.medecin.afficherDossierPatient import appl
        self.isnn = int(self.lmot.text())
        self.close()
        self.mm = appl(isne=self.isnn)
        self.mm.show()
    
    def connect(self):
        self.bouton.clicked.connect(self.entrer)
        
if __name__ == "__main__":
    app = QtWidgets.QApplication()
    window = isne()
    window.show()
    app.exec()