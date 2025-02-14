from PySide6.QtWidgets import QApplication, QPushButton, QWidget,QVBoxLayout
import sys

app=QApplication(sys.argv)
botao=QPushButton("TExto do botao")
botao.setStyleSheet('font-size: 40px; color: red;')
botao2=QPushButton("Esse é o botão 2")
botao2.setStyleSheet('color: blue')
central_widget = QWidget()
layout=QVBoxLayout()
central_widget.setLayout(layout)
layout.addWidget(botao2)
layout.addWidget(botao)
central_widget.show()
app.exec()




