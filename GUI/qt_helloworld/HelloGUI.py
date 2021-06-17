import sys
from PyQt5 import QtWidgets, uic


# class MainGUI(QtWidgets.QDialog):
class MainGUI(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
#         super().__init__(parent)
        super().__init__()
        self.ui = uic.loadUi("MainGUI.ui", self)

    #     # Slot einrichten
    #     self.ui.bt_berechnen.clicked.connect(self.on_berechnen)
    #     self.ui.slider_hubraum.valueChanged.connect(self.on_changed_hubraum)
    #     self.ui.slider_co2.valueChanged.connect(self.on_changed_co2)
    #
    #     # Minimum und Maximum der Slider einrichten
    #     self.ui.slider_hubraum.setMinimum(0)
    #     self.ui.slider_hubraum.setMaximum(5000)
    #     self.ui.slider_co2.setMinimum(0)
    #     self.ui.slider_co2.setMaximum(500)
    #
    # def on_berechnen(self):
    #
    #     # Daten einlesen
    #     f = Fahrzeug()
    #
    #     f.typ = self.ui.tf_typ.text()
    #     f.hubraum = self.ui.slider_hubraum.value()
    #     f.co2 = self.ui.slider_co2.value()
    #     if self.ui.rb_diesel.isChecked():
    #         f.diesel = True
    #     if self.ui.rb_benzin.isChecked():
    #         f.diesel = False
    #
    #     # Methode aufrufen
    #     steuer = f.berechne_steuer()
    #     steuer = round(steuer, 2)
    #
    #     # Daten ausgeben
    #     self.ui.ta_ausgabe.setPlainText("Typ des Fahrzeugs: " + f.typ)
    #     self.ui.ta_ausgabe.appendPlainText("Hubraum (in ccm): " + str(f.hubraum))
    #     self.ui.ta_ausgabe.appendPlainText("CO2-Ausstoß (in g/km): " + str(f.co2))
    #     self.ui.ta_ausgabe.appendPlainText("Die Kfz-Steuer beträgt: " + str(steuer) + " €")
    #
    # def on_changed_hubraum(self):
    #     wert = self.ui.slider_hubraum.value()
    #     self.ui.tf_hubraum.setText(str(wert))
    #
    # def on_changed_co2(self):
    #     wert = self.ui.slider_co2.value()
    #     self.ui.tf_co2.setText(str(wert))


app = QtWidgets.QApplication(sys.argv)
dialog = MainGUI()
dialog.show()
sys.exit(app.exec_())
