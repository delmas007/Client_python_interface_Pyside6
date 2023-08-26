import sys
sys.path.insert(0,r'C:\Users\Delmas brou\Desktop\CMU\clientCmu')
from PySide6 import QtWidgets
from fenetre.patient import Ui_Form
from api.conServer import client
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os
import random
import string
import webbrowser

class patientConsultation(QtWidgets.QWidget,Ui_Form):
    def __init__(self,codee):
        super(patientConsultation,self).__init__()
        self.codee = codee
        self.setupUi(self)
        self.setWindowTitle("Dossier Patient")
        self.affiche()
        self.ordonnance()
        
    def affiche(self):
            aff = client.service.afficherConsultation(self.codee)
            print(aff)
            for i in aff:
                self.c = self.code.setText(i["code"])
                self.r = self.reduction.setText(str(i["tauxReduction"])+" %")
                self.dd = self.d.setText(i["ordonnance"])
                self.oo = self.o.setText(i["diagnostic"])
    
    
    def generate_pdf(self, a, b, ordonnance, diagnostic, filename):
        c = canvas.Canvas(filename, pagesize=letter)
        c.setFont("Helvetica", 12)
        c.drawString(100, 750, "Code : {}".format(a))
        c.drawString(100, 730, "Taux de réduction : {}%".format(b))
        c.drawString(100, 700, "Ordonnance :")
        ordonnance_lines = ordonnance.split('\n')
        y_position = 680
        for line in ordonnance_lines:
            c.drawString(120, y_position, line)
            y_position -= 15  
        c.drawString(100, y_position - 20, "Diagnostic :")
        diagnostic_lines = diagnostic.split('\n')
        for line in diagnostic_lines:
            c.drawString(120, y_position - 40, line)
            y_position -= 20 
        c.save()
        
        try:
            webbrowser.open(filename)
        except:
            print("Impossible d'ouvrir le fichier PDF.")

    
    def generer_alphanumerique(self, n):
        caracteres = string.ascii_letters + string.digits
        return ''.join(random.choice(caracteres) for _ in range(n))
    
    def deconnectionn(self):
        from api.authentification import authentificatio
        self.close()
        self.ab = authentificatio()
        self.ab.show()
    
    def ordonnance(self):
        self.enregistrer.clicked.connect(lambda: self.generate_and_save_pdf())
        self.deconnection.clicked.connect(self.deconnectionn)

    def generate_and_save_pdf(self):
        print("1")
        self.f = self.generer_alphanumerique(2)
        user_folder = os.path.expanduser("~")
        desktop_path = os.path.join(user_folder, "Desktop")
        filename = os.path.join(desktop_path, "ordonnance{}.pdf".format(self.f))
        aff = client.service.afficherConsultation(self.codee)
        for i in aff:
            aa=i["ordonnance"]
            bb=i["diagnostic"]
            print(aa)
            self.generate_pdf(i["code"], i["tauxReduction"],aa,bb, filename)
    
    


                
if __name__ == "__main__":
    app = QtWidgets.QApplication()
    window = patientConsultation()
    window.show()
    app.exec()