import sys
sys.path.insert(0,r'C:\Users\Delmas brou\Desktop\CMU\clientCmu')
from PySide6 import QtWidgets
from fenetre.acceuil import Ui_Form
from api.conServer import client

class authentificatio(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(authentificatio,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("authentification")
        self.label_2.setVisible(False)
        self.connect()
        
    
    def connexion(self):
        self.mot = int(self.lmot.text())
        self.co = client.service.authentification(self.mot)
        
        if(self.co == 1):
            from api.medecin import accueilMedecin
            self.close()
            self.a = accueilMedecin.acceuilM()
            self.a.show()
        
        if(self.co == 2):
            from api.employerCmu.acceuilEmployer import acceuilE
            self.close()
            self.a = acceuilE()
            self.a.show()
        
        if(self.co > 4):
            from api.patient.patientConsultation import patientConsultation
            self.close()
            self.a = patientConsultation(codee=self.co)
            self.a.show()
        
        if(self.co == 3):
            self.label_2.setVisible(True)
        
        
        
    
    def connect(self):
        self.bouton.clicked.connect(self.connexion)
                
if __name__ == "__main__":
    app = QtWidgets.QApplication()
    window = authentificatio()
    window.show()
    app.exec()