import sys
sys.path.insert(0,r'C:\Users\Delmas brou\Desktop\CMU\clientCmu')
from PySide6 import QtWidgets
from fenetre.Ma import Ui_Form
from api.conServer import client

class appl(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(appl,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Dossier Patient")
        self.affiche()
        self.connectee()
        
    def affiche(self):
        aff = client.service.afficherDossier(54123)
        print(aff)
        
        for i in aff:
            numeroCmu =str(i["numeroCmu"]) 
            age = str(i["age"])
            self.nom.setText(i["nom"])
            self.prenom.setText(i["prenom"])
            self.ncmu.setText(numeroCmu)
            self.ville.setText(i["ville"])
            self.age.setText(age)
            if i["masculin"] == True:
                self.h.setText("oui")
                self.f.setText("non")
                self.e.setText("non")
            elif i["feminin"] == True and i["enceinte"] == True:
                self.f.setText("oui")
                self.e.setText("oui")
            else:
                self.f.setText("oui")
                self.e.setText("non")
            self.am.setText(i["antecedentsMedicaux"])
            self.hv.setText(i["historiqueVaccination"])
            self.rm.setText(i["resumesMedicaux"])
    
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
        
    def connectee(self):
        self.deconnection.clicked.connect(self.deconnectionn)
        self.retour.clicked.connect(self.retoure)
                
if __name__ == "__main__":
    app = QtWidgets.QApplication()
    window = appl()
    window.show()
    app.exec()