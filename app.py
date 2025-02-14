from PySide6.QtWidgets import QApplication, QPushButton, QWidget,QVBoxLayout,QGridLayout
import sys

app=QApplication(sys.argv)
botao=QPushButton("Texto do botao")
botao.setStyleSheet('color: red;')
botao2=QPushButton("Esse é o botão 2")
botao2.setStyleSheet('color: blue')
botao3=QPushButton("esse é o terceiro")
botao3.setStyleSheet("color: green")
central_widget = QWidget()
layout=QGridLayout()
central_widget.setLayout(layout)
layout.addWidget(botao2,1,1)
layout.addWidget(botao,1,2)
layout.addWidget(botao3,3,1,1,2)
central_widget.show()
app.exec()




