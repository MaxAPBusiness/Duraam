import sys
import PyQt6.QtWidgets as qtw
import ui.langUI
import ui.IngresarUI_en
import ui.IngresarUI_es
import ui.registroUI_es
import ui.registroUI_en


# Creamos la ventana principal
class MainWindow(qtw.QMainWindow):
    def __init__(self):
        super().__init__()

        # Creamos la colección de pantallas
        stack = qtw.QStackedWidget()

        # Cargamos las pantallas
        self.lang = ui.langUI.Lenguaje()
        self.ingresarEs = ui.IngresarUI_es.IngresarEs()
        self.ingresarEn = ui.IngresarUI_en.IngresarEn()
        self.registrarEs = ui.registroUI_es.RegistrarEs()
        self.registrarEn = ui.registroUI_en.RegistrarEn()

        # Añadimos las pantallas a la colección
        for i in [self.lang, self.ingresarEs, self.ingresarEn, self.registrarEs, self.registrarEn]:
            stack.addWidget(i)

        # Añadimos la funcionalidad a los botones: hacemos que cambien las distintas pantallas del
        self.lang.button1.clicked.connect(lambda: stack.setCurrentIndex(1))
        self.lang.button2.clicked.connect(lambda: stack.setCurrentIndex(2))
        self.ingresarEs.button1.clicked.connect(
            lambda: stack.setCurrentIndex(3))
        self.ingresarEs.back.clicked.connect(lambda: stack.setCurrentIndex(0))
        self.ingresarEn.button1.clicked.connect(
            lambda: stack.setCurrentIndex(4))
        self.ingresarEn.back.clicked.connect(lambda: stack.setCurrentIndex(0))
        self.registrarEs.button1.clicked.connect(
            lambda: stack.setCurrentIndex(1))
        self.registrarEn.button1.clicked.connect(
            lambda: stack.setCurrentIndex(2))

        # Añadimos la colección a la ventana
        self.setCentralWidget(stack)


app = qtw.QApplication(sys.argv)

if __name__ == "__main__":
    window = MainWindow()
    window.show()
    app.exec()
