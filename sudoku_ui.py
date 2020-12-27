#interface for sudoku game
#importing required package
import sys
import os
import sudoku_solve
import add_puzzle
from copy import deepcopy
from PyQt5 import QtCore, QtGui, QtWidgets

#user interface for puzzle
class Ui_sudoku_board(object):
    def __init__(self):
        self.current_puzzle=""
        self.files=[]
        self.mat=[]
        self.blist=[]
        self.plist=[]
        self.board=[]
        self.add_form=None
        self.add_ui=None
        self.solution=[]
        self.game_state="stop"
        self.cell=None
        self.count=0

    def setupUi(self, sudoku_board):
        sudoku_board.setObjectName("sudoku_board")
        sudoku_board.resize(628, 554)
        sudoku_board.setToolTipDuration(-15)
        self.load = QtWidgets.QPushButton(sudoku_board)
        self.load.setGeometry(QtCore.QRect(10, 490, 121, 25))
        self.load.setObjectName("load")
        self.refresh = QtWidgets.QPushButton(sudoku_board)
        self.refresh.setGeometry(QtCore.QRect(10, 420, 121, 25))
        self.refresh.setObjectName("refresh")
        self.add = QtWidgets.QPushButton(sudoku_board)
        self.add.setGeometry(QtCore.QRect(10, 520, 121, 25))
        self.add.setObjectName("add")
        self.label = QtWidgets.QLabel(sudoku_board)
        self.label.setGeometry(QtCore.QRect(10, 20, 121, 21))
        self.label.setObjectName("label")
        self.progress = QtWidgets.QProgressBar(sudoku_board)
        self.progress.setGeometry(QtCore.QRect(190, 440, 381, 23))
        self.progress.setProperty("value", 0)
        self.progress.setObjectName("progress")
        self.play = QtWidgets.QPushButton(sudoku_board)
        self.play.setGeometry(QtCore.QRect(190, 480, 101, 25))
        self.play.setObjectName("play")

        self.quit = QtWidgets.QPushButton(sudoku_board)
        self.quit.setGeometry(QtCore.QRect(190, 520, 101, 25))
        self.quit.setObjectName("quit")

        self.reset = QtWidgets.QPushButton(sudoku_board)
        self.reset.setGeometry(QtCore.QRect(480, 520, 89, 25))
        self.reset.setObjectName("reset")
        self.clear = QtWidgets.QPushButton(sudoku_board)
        self.clear.setGeometry(QtCore.QRect(480, 480, 89, 25))
        self.clear.setObjectName("clear")
        self.select1 = QtWidgets.QPushButton(sudoku_board)
        self.select1.setGeometry(QtCore.QRect(330, 470, 25, 25))
        self.select1.setObjectName("select1")
        self.select2 = QtWidgets.QPushButton(sudoku_board)
        self.select2.setGeometry(QtCore.QRect(370, 470, 25, 25))
        self.select2.setObjectName("select2")
        self.select3 = QtWidgets.QPushButton(sudoku_board)
        self.select3.setGeometry(QtCore.QRect(410, 470, 25, 25))
        self.select3.setObjectName("select3")
        self.select4 = QtWidgets.QPushButton(sudoku_board)
        self.select4.setGeometry(QtCore.QRect(330, 500, 25, 25))
        self.select4.setObjectName("select4")
        self.select5 = QtWidgets.QPushButton(sudoku_board)
        self.select5.setGeometry(QtCore.QRect(370, 500, 25, 25))
        self.select5.setObjectName("select5")
        self.select6 = QtWidgets.QPushButton(sudoku_board)
        self.select6.setGeometry(QtCore.QRect(410, 500, 25, 25))
        self.select6.setObjectName("select6")
        self.select7 = QtWidgets.QPushButton(sudoku_board)
        self.select7.setGeometry(QtCore.QRect(330, 530, 25, 25))
        self.select7.setObjectName("select7")
        self.select8 = QtWidgets.QPushButton(sudoku_board)
        self.select8.setGeometry(QtCore.QRect(370, 530, 25, 25))
        self.select8.setObjectName("select8")
        self.select9 = QtWidgets.QPushButton(sudoku_board)
        self.select9.setGeometry(QtCore.QRect(410, 530, 25, 25))
        self.select9.setObjectName("select9")
        self.msg = QtWidgets.QLabel(sudoku_board)
        self.msg.setGeometry(QtCore.QRect(170, -4, 450, 30))
        self.msg.setAlignment(QtCore.Qt.AlignCenter)
        self.msg.setObjectName("msg")
        self.mat10 = QtWidgets.QPushButton(sudoku_board)
        self.mat10.setGeometry(QtCore.QRect(190, 80, 40, 40))
        self.mat10.setText("")
        self.mat10.setObjectName("mat10")
        self.mat00 = QtWidgets.QPushButton(sudoku_board)
        self.mat00.setGeometry(QtCore.QRect(190, 40, 40, 40))
        self.mat00.setText("")
        self.mat00.setObjectName("mat00")
        self.mat01 = QtWidgets.QPushButton(sudoku_board)
        self.mat01.setGeometry(QtCore.QRect(230, 40, 40, 40))
        self.mat01.setText("")
        self.mat01.setObjectName("mat01")
        self.mat02 = QtWidgets.QPushButton(sudoku_board)
        self.mat02.setGeometry(QtCore.QRect(270, 40, 40, 40))
        self.mat02.setText("")
        self.mat02.setObjectName("mat02")
        self.mat22 = QtWidgets.QPushButton(sudoku_board)
        self.mat22.setGeometry(QtCore.QRect(270, 120, 40, 40))
        self.mat22.setText("")
        self.mat22.setObjectName("mat22")
        self.mat04 = QtWidgets.QPushButton(sudoku_board)
        self.mat04.setGeometry(QtCore.QRect(360, 40, 40, 40))
        self.mat04.setText("")
        self.mat04.setObjectName("mat04")
        self.mat05 = QtWidgets.QPushButton(sudoku_board)
        self.mat05.setGeometry(QtCore.QRect(400, 40, 40, 40))
        self.mat05.setText("")
        self.mat05.setObjectName("mat05")
        self.mat13 = QtWidgets.QPushButton(sudoku_board)
        self.mat13.setGeometry(QtCore.QRect(320, 80, 40, 40))
        self.mat13.setText("")
        self.mat13.setObjectName("mat13")
        self.mat14 = QtWidgets.QPushButton(sudoku_board)
        self.mat14.setGeometry(QtCore.QRect(360, 80, 40, 40))
        self.mat14.setText("")
        self.mat14.setObjectName("mat14")
        self.mat15 = QtWidgets.QPushButton(sudoku_board)
        self.mat15.setGeometry(QtCore.QRect(400, 80, 40, 40))
        self.mat15.setText("")
        self.mat15.setObjectName("mat15")
        self.mat21 = QtWidgets.QPushButton(sudoku_board)
        self.mat21.setGeometry(QtCore.QRect(230, 120, 40, 40))
        self.mat21.setText("")
        self.mat21.setObjectName("mat21")
        self.mat12 = QtWidgets.QPushButton(sudoku_board)
        self.mat12.setGeometry(QtCore.QRect(270, 80, 40, 40))
        self.mat12.setText("")
        self.mat12.setObjectName("mat12")
        self.mat11 = QtWidgets.QPushButton(sudoku_board)
        self.mat11.setGeometry(QtCore.QRect(230, 80, 40, 40))
        self.mat11.setText("")
        self.mat11.setObjectName("mat11")
        self.mat55 = QtWidgets.QPushButton(sudoku_board)
        self.mat55.setGeometry(QtCore.QRect(400, 250, 40, 40))
        self.mat55.setText("")
        self.mat55.setObjectName("mat55")
        self.mat50 = QtWidgets.QPushButton(sudoku_board)
        self.mat50.setGeometry(QtCore.QRect(190, 250, 40, 40))
        self.mat50.setText("")
        self.mat50.setObjectName("mat50")
        self.mat40 = QtWidgets.QPushButton(sudoku_board)
        self.mat40.setGeometry(QtCore.QRect(190, 210, 40, 40))
        self.mat40.setText("")
        self.mat40.setObjectName("mat40")
        self.mat30 = QtWidgets.QPushButton(sudoku_board)
        self.mat30.setGeometry(QtCore.QRect(190, 170, 40, 40))
        self.mat30.setText("")
        self.mat30.setObjectName("mat30")
        self.mat20 = QtWidgets.QPushButton(sudoku_board)
        self.mat20.setGeometry(QtCore.QRect(190, 120, 40, 40))
        self.mat20.setText("")
        self.mat20.setObjectName("mat20")
        self.mat52 = QtWidgets.QPushButton(sudoku_board)
        self.mat52.setGeometry(QtCore.QRect(270, 250, 40, 40))
        self.mat52.setText("")
        self.mat52.setObjectName("mat52")
        self.mat51 = QtWidgets.QPushButton(sudoku_board)
        self.mat51.setGeometry(QtCore.QRect(230, 250, 40, 40))
        self.mat51.setText("")
        self.mat51.setObjectName("mat51")
        self.mat42 = QtWidgets.QPushButton(sudoku_board)
        self.mat42.setGeometry(QtCore.QRect(270, 210, 40, 40))
        self.mat42.setText("")
        self.mat42.setObjectName("mat42")
        self.mat41 = QtWidgets.QPushButton(sudoku_board)
        self.mat41.setGeometry(QtCore.QRect(230, 210, 40, 40))
        self.mat41.setText("")
        self.mat41.setObjectName("mat41")
        self.mat32 = QtWidgets.QPushButton(sudoku_board)
        self.mat32.setGeometry(QtCore.QRect(270, 170, 40, 40))
        self.mat32.setText("")
        self.mat32.setObjectName("mat32")
        self.mat31 = QtWidgets.QPushButton(sudoku_board)
        self.mat31.setGeometry(QtCore.QRect(230, 170, 40, 40))
        self.mat31.setText("")
        self.mat31.setObjectName("mat31")
        self.mat28 = QtWidgets.QPushButton(sudoku_board)
        self.mat28.setGeometry(QtCore.QRect(530, 120, 40, 40))
        self.mat28.setText("")
        self.mat28.setObjectName("mat28")
        self.mat27 = QtWidgets.QPushButton(sudoku_board)
        self.mat27.setGeometry(QtCore.QRect(490, 120, 40, 40))
        self.mat27.setText("")
        self.mat27.setObjectName("mat27")
        self.mat26 = QtWidgets.QPushButton(sudoku_board)
        self.mat26.setGeometry(QtCore.QRect(450, 120, 40, 40))
        self.mat26.setText("")
        self.mat26.setObjectName("mat26")
        self.mat18 = QtWidgets.QPushButton(sudoku_board)
        self.mat18.setGeometry(QtCore.QRect(530, 80, 40, 40))
        self.mat18.setText("")
        self.mat18.setObjectName("mat18")
        self.mat17 = QtWidgets.QPushButton(sudoku_board)
        self.mat17.setGeometry(QtCore.QRect(490, 80, 40, 40))
        self.mat17.setText("")
        self.mat17.setObjectName("mat17")
        self.mat16 = QtWidgets.QPushButton(sudoku_board)
        self.mat16.setGeometry(QtCore.QRect(450, 80, 40, 40))
        self.mat16.setText("")
        self.mat16.setObjectName("mat16")
        self.mat08 = QtWidgets.QPushButton(sudoku_board)
        self.mat08.setGeometry(QtCore.QRect(530, 40, 40, 40))
        self.mat08.setText("")
        self.mat08.setObjectName("mat08")
        self.mat07 = QtWidgets.QPushButton(sudoku_board)
        self.mat07.setGeometry(QtCore.QRect(490, 40, 40, 40))
        self.mat07.setText("")
        self.mat07.setObjectName("mat07")
        self.mat06 = QtWidgets.QPushButton(sudoku_board)
        self.mat06.setGeometry(QtCore.QRect(450, 40, 40, 40))
        self.mat06.setText("")
        self.mat06.setObjectName("mat06")
        self.mat25 = QtWidgets.QPushButton(sudoku_board)
        self.mat25.setGeometry(QtCore.QRect(400, 120, 40, 40))
        self.mat25.setText("")
        self.mat25.setObjectName("mat25")
        self.mat24 = QtWidgets.QPushButton(sudoku_board)
        self.mat24.setGeometry(QtCore.QRect(360, 120, 40, 40))
        self.mat24.setText("")
        self.mat24.setObjectName("mat24")
        self.mat23 = QtWidgets.QPushButton(sudoku_board)
        self.mat23.setGeometry(QtCore.QRect(320, 120, 40, 40))
        self.mat23.setText("")
        self.mat23.setObjectName("mat23")
        self.mat03 = QtWidgets.QPushButton(sudoku_board)
        self.mat03.setGeometry(QtCore.QRect(320, 40, 40, 40))
        self.mat03.setText("")
        self.mat03.setObjectName("mat03")
        self.mat54 = QtWidgets.QPushButton(sudoku_board)
        self.mat54.setGeometry(QtCore.QRect(360, 250, 40, 40))
        self.mat54.setText("")
        self.mat54.setObjectName("mat54")
        self.mat53 = QtWidgets.QPushButton(sudoku_board)
        self.mat53.setGeometry(QtCore.QRect(320, 250, 40, 40))
        self.mat53.setText("")
        self.mat53.setObjectName("mat53")
        self.mat45 = QtWidgets.QPushButton(sudoku_board)
        self.mat45.setGeometry(QtCore.QRect(400, 210, 40, 40))
        self.mat45.setText("")
        self.mat45.setObjectName("mat45")
        self.mat44 = QtWidgets.QPushButton(sudoku_board)
        self.mat44.setGeometry(QtCore.QRect(360, 210, 40, 40))
        self.mat44.setText("")
        self.mat44.setObjectName("mat44")
        self.mat43 = QtWidgets.QPushButton(sudoku_board)
        self.mat43.setGeometry(QtCore.QRect(320, 210, 40, 40))
        self.mat43.setText("")
        self.mat43.setObjectName("mat43")
        self.mat35 = QtWidgets.QPushButton(sudoku_board)
        self.mat35.setGeometry(QtCore.QRect(400, 170, 40, 40))
        self.mat35.setText("")
        self.mat35.setObjectName("mat35")
        self.mat34 = QtWidgets.QPushButton(sudoku_board)
        self.mat34.setGeometry(QtCore.QRect(360, 170, 40, 40))
        self.mat34.setText("")
        self.mat34.setObjectName("mat34")
        self.mat33 = QtWidgets.QPushButton(sudoku_board)
        self.mat33.setGeometry(QtCore.QRect(320, 170, 40, 40))
        self.mat33.setText("")
        self.mat33.setObjectName("mat33")
        self.mat58 = QtWidgets.QPushButton(sudoku_board)
        self.mat58.setGeometry(QtCore.QRect(530, 250, 40, 40))
        self.mat58.setText("")
        self.mat58.setObjectName("mat58")
        self.mat57 = QtWidgets.QPushButton(sudoku_board)
        self.mat57.setGeometry(QtCore.QRect(490, 250, 40, 40))
        self.mat57.setText("")
        self.mat57.setObjectName("mat57")
        self.mat56 = QtWidgets.QPushButton(sudoku_board)
        self.mat56.setGeometry(QtCore.QRect(450, 250, 40, 40))
        self.mat56.setText("")
        self.mat56.setObjectName("mat56")
        self.mat48 = QtWidgets.QPushButton(sudoku_board)
        self.mat48.setGeometry(QtCore.QRect(530, 210, 40, 40))
        self.mat48.setText("")
        self.mat48.setObjectName("mat48")
        self.mat47 = QtWidgets.QPushButton(sudoku_board)
        self.mat47.setGeometry(QtCore.QRect(490, 210, 40, 40))
        self.mat47.setText("")
        self.mat47.setObjectName("mat47")
        self.mat46 = QtWidgets.QPushButton(sudoku_board)
        self.mat46.setGeometry(QtCore.QRect(450, 210, 40, 40))
        self.mat46.setText("")
        self.mat46.setObjectName("mat46")
        self.mat38 = QtWidgets.QPushButton(sudoku_board)
        self.mat38.setGeometry(QtCore.QRect(530, 170, 40, 40))
        self.mat38.setText("")
        self.mat38.setObjectName("mat38")
        self.mat37 = QtWidgets.QPushButton(sudoku_board)
        self.mat37.setGeometry(QtCore.QRect(490, 170, 40, 40))
        self.mat37.setText("")
        self.mat37.setObjectName("mat37")
        self.mat36 = QtWidgets.QPushButton(sudoku_board)
        self.mat36.setGeometry(QtCore.QRect(450, 170, 40, 40))
        self.mat36.setText("")
        self.mat36.setObjectName("mat36")
        self.mat62 = QtWidgets.QPushButton(sudoku_board)
        self.mat62.setGeometry(QtCore.QRect(270, 300, 40, 40))
        self.mat62.setText("")
        self.mat62.setObjectName("mat62")
        self.mat61 = QtWidgets.QPushButton(sudoku_board)
        self.mat61.setGeometry(QtCore.QRect(230, 300, 40, 40))
        self.mat61.setText("")
        self.mat61.setObjectName("mat61")
        self.mat60 = QtWidgets.QPushButton(sudoku_board)
        self.mat60.setGeometry(QtCore.QRect(190, 300, 40, 40))
        self.mat60.setText("")
        self.mat60.setObjectName("mat60")
        self.mat65 = QtWidgets.QPushButton(sudoku_board)
        self.mat65.setGeometry(QtCore.QRect(400, 300, 40, 40))
        self.mat65.setText("")
        self.mat65.setObjectName("mat65")
        self.mat64 = QtWidgets.QPushButton(sudoku_board)
        self.mat64.setGeometry(QtCore.QRect(360, 300, 40, 40))
        self.mat64.setText("")
        self.mat64.setObjectName("mat64")
        self.mat63 = QtWidgets.QPushButton(sudoku_board)
        self.mat63.setGeometry(QtCore.QRect(320, 300, 40, 40))
        self.mat63.setText("")
        self.mat63.setObjectName("mat63")
        self.mat82 = QtWidgets.QPushButton(sudoku_board)
        self.mat82.setGeometry(QtCore.QRect(270, 380, 40, 40))
        self.mat82.setText("")
        self.mat82.setObjectName("mat82")
        self.mat81 = QtWidgets.QPushButton(sudoku_board)
        self.mat81.setGeometry(QtCore.QRect(230, 380, 40, 40))
        self.mat81.setText("")
        self.mat81.setObjectName("mat81")
        self.mat80 = QtWidgets.QPushButton(sudoku_board)
        self.mat80.setGeometry(QtCore.QRect(190, 380, 40, 40))
        self.mat80.setText("")
        self.mat80.setObjectName("mat80")
        self.mat72 = QtWidgets.QPushButton(sudoku_board)
        self.mat72.setGeometry(QtCore.QRect(270, 340, 40, 40))
        self.mat72.setText("")
        self.mat72.setObjectName("mat72")
        self.mat71 = QtWidgets.QPushButton(sudoku_board)
        self.mat71.setGeometry(QtCore.QRect(230, 340, 40, 40))
        self.mat71.setText("")
        self.mat71.setObjectName("mat71")
        self.mat70 = QtWidgets.QPushButton(sudoku_board)
        self.mat70.setGeometry(QtCore.QRect(190, 340, 40, 40))
        self.mat70.setText("")
        self.mat70.setObjectName("mat70")
        self.mat76 = QtWidgets.QPushButton(sudoku_board)
        self.mat76.setGeometry(QtCore.QRect(450, 340, 40, 40))
        self.mat76.setText("")
        self.mat76.setObjectName("mat76")
        self.mat85 = QtWidgets.QPushButton(sudoku_board)
        self.mat85.setGeometry(QtCore.QRect(400, 380, 40, 40))
        self.mat85.setText("")
        self.mat85.setObjectName("mat85")
        self.mat84 = QtWidgets.QPushButton(sudoku_board)
        self.mat84.setGeometry(QtCore.QRect(360, 380, 40, 40))
        self.mat84.setText("")
        self.mat84.setObjectName("mat84")
        self.mat83 = QtWidgets.QPushButton(sudoku_board)
        self.mat83.setGeometry(QtCore.QRect(320, 380, 40, 40))
        self.mat83.setText("")
        self.mat83.setObjectName("mat83")
        self.mat75 = QtWidgets.QPushButton(sudoku_board)
        self.mat75.setGeometry(QtCore.QRect(400, 340, 40, 40))
        self.mat75.setText("")
        self.mat75.setObjectName("mat75")
        self.mat74 = QtWidgets.QPushButton(sudoku_board)
        self.mat74.setGeometry(QtCore.QRect(360, 340, 40, 40))
        self.mat74.setText("")
        self.mat74.setObjectName("mat74")
        self.mat73 = QtWidgets.QPushButton(sudoku_board)
        self.mat73.setGeometry(QtCore.QRect(320, 340, 40, 40))
        self.mat73.setText("")
        self.mat73.setObjectName("mat73")
        self.mat68 = QtWidgets.QPushButton(sudoku_board)
        self.mat68.setGeometry(QtCore.QRect(530, 300, 40, 40))
        self.mat68.setText("")
        self.mat68.setObjectName("mat68")
        self.mat67 = QtWidgets.QPushButton(sudoku_board)
        self.mat67.setGeometry(QtCore.QRect(490, 300, 40, 40))
        self.mat67.setText("")
        self.mat67.setObjectName("mat67")
        self.mat66 = QtWidgets.QPushButton(sudoku_board)
        self.mat66.setGeometry(QtCore.QRect(450, 300, 40, 40))
        self.mat66.setText("")
        self.mat66.setObjectName("mat66")
        self.mat88 = QtWidgets.QPushButton(sudoku_board)
        self.mat88.setGeometry(QtCore.QRect(530, 380, 40, 40))
        self.mat88.setText("")
        self.mat88.setObjectName("mat88")
        self.mat87 = QtWidgets.QPushButton(sudoku_board)
        self.mat87.setGeometry(QtCore.QRect(490, 380, 40, 40))
        self.mat87.setText("")
        self.mat87.setObjectName("mat87")
        self.mat86 = QtWidgets.QPushButton(sudoku_board)
        self.mat86.setGeometry(QtCore.QRect(450, 380, 40, 40))
        self.mat86.setText("")
        self.mat86.setObjectName("mat86")
        self.mat78 = QtWidgets.QPushButton(sudoku_board)
        self.mat78.setGeometry(QtCore.QRect(530, 340, 40, 40))
        self.mat78.setText("")
        self.mat78.setObjectName("mat78")
        self.mat77 = QtWidgets.QPushButton(sudoku_board)
        self.mat77.setGeometry(QtCore.QRect(490, 340, 40, 40))
        self.mat77.setText("")
        self.mat77.setObjectName("mat77")
        #self.list_puzzle = QtWidgets.QListView(sudoku_board)
        #self.list_puzzle.setGeometry(QtCore.QRect(10, 40, 121, 381))
        #self.list_puzzle.setObjectName("list_puzzle")
        self.list_puzzle = QtWidgets.QListWidget(sudoku_board)
        self.list_puzzle.setGeometry(QtCore.QRect(10, 40, 121, 381))
        self.list_puzzle.setObjectName("list_puzzle")

        r0=[self.mat00,self.mat01,self.mat02,self.mat03,self.mat04,self.mat05,self.mat06,self.mat07,self.mat08]
        r1=[self.mat10,self.mat11,self.mat12,self.mat13,self.mat14,self.mat15,self.mat16,self.mat17,self.mat18]
        r2=[self.mat20,self.mat21,self.mat22,self.mat23,self.mat24,self.mat25,self.mat26,self.mat27,self.mat28]
        r3=[self.mat30,self.mat31,self.mat32,self.mat33,self.mat34,self.mat35,self.mat36,self.mat37,self.mat38]
        r4=[self.mat40,self.mat41,self.mat42,self.mat43,self.mat44,self.mat45,self.mat46,self.mat47,self.mat48]
        r5=[self.mat50,self.mat51,self.mat52,self.mat53,self.mat54,self.mat55,self.mat56,self.mat57,self.mat58]
        r6=[self.mat60,self.mat61,self.mat62,self.mat63,self.mat64,self.mat65,self.mat66,self.mat67,self.mat68]
        r7=[self.mat70,self.mat71,self.mat72,self.mat73,self.mat74,self.mat75,self.mat76,self.mat77,self.mat78]
        r8=[self.mat80,self.mat81,self.mat82,self.mat83,self.mat84,self.mat85,self.mat86,self.mat87,self.mat88]
        self.board=[r0,r1,r2,r3,r4,r5,r6,r7,r8]
        self.choice=[self.select1,self.select2,self.select3,self.select4,self.select5,self.select6,self.select7,self.select8,self.select9]
        self.retranslateUi(sudoku_board)
        QtCore.QMetaObject.connectSlotsByName(sudoku_board)
        self.list_puzzle_file()

    def retranslateUi(self, sudoku_board):
        _translate = QtCore.QCoreApplication.translate
        sudoku_board.setWindowTitle(_translate("sudoku_board", "SUDOKU"))
        self.load.setToolTip(_translate("sudoku_board", "Load sudoku puzzle"))
        self.load.setText(_translate("sudoku_board", "LOAD"))
        self.refresh.setToolTip(_translate("sudoku_board", "Refresh puzzle list"))
        self.refresh.setText(_translate("sudoku_board", "Refresh"))
        self.add.setToolTip(_translate("sudoku_board", "Add new Puzzle"))
        self.add.setText(_translate("sudoku_board", "ADD "))
        self.label.setText(_translate("sudoku_board", "SUDOKU PUZZLE"))
        self.play.setToolTip(_translate("sudoku_board", "start solving puzzle"))
        self.play.setText(_translate("sudoku_board", "Play"))
        self.quit.setToolTip(_translate("sudoku_board", "quit solving puzzle"))
        self.quit.setText(_translate("sudoku_board", "Quit"))
        self.reset.setToolTip(_translate("sudoku_board", "restart sudoku puzzle"))
        self.reset.setText(_translate("sudoku_board", "restart"))
        self.clear.setText(_translate("sudoku_board", "clear"))
        self.select1.setText(_translate("sudoku_board", "1"))
        self.select2.setText(_translate("sudoku_board", "2"))
        self.select3.setText(_translate("sudoku_board", "3"))
        self.select4.setText(_translate("sudoku_board", "4"))
        self.select5.setText(_translate("sudoku_board", "5"))
        self.select6.setText(_translate("sudoku_board", "6"))
        self.select7.setText(_translate("sudoku_board", "7"))
        self.select8.setText(_translate("sudoku_board", "8"))
        self.select9.setText(_translate("sudoku_board", "9"))
        self.msg.setText(_translate("sudoku_board", "Welcome"))
        self.msg.setStyleSheet('background-color: black;color:white')
        self.play.clicked.connect(lambda:self.play_sudoku())
        self.load.clicked.connect(lambda:self.load_puzzle(self.list_puzzle.currentRow()))
        self.reset.clicked.connect(lambda:self.restart_puzzle(self.files.index(self.current_puzzle)))
        self.quit.clicked.connect(lambda:self.quit_puzzle())
        self.clear.clicked.connect(lambda:self.clear_cell())
        self.add.clicked.connect(lambda:self.add_new_puzzle())
        self.refresh.clicked.connect(lambda:self.list_puzzle_file())
        self.play.setStyleSheet('background-color: silver;color:black')
        self.load.setStyleSheet('background-color: silver;color:black')
        self.add.setStyleSheet('background-color: silver;color:black')
        self.reset.setStyleSheet('background-color: silver;color:black')
        self.quit.setStyleSheet('background-color: silver;color:black')
        self.clear.setStyleSheet('background-color: silver;color:black')
        self.mat00.clicked.connect(lambda:self.set_selected_cell(self.mat00,0,0))
        self.mat01.clicked.connect(lambda:self.set_selected_cell(self.mat01,0,1))
        self.mat02.clicked.connect(lambda:self.set_selected_cell(self.mat02,0,2))
        self.mat03.clicked.connect(lambda:self.set_selected_cell(self.mat03,0,3))
        self.mat04.clicked.connect(lambda:self.set_selected_cell(self.mat04,0,4))
        self.mat05.clicked.connect(lambda:self.set_selected_cell(self.mat05,0,5))
        self.mat06.clicked.connect(lambda:self.set_selected_cell(self.mat06,0,6))
        self.mat07.clicked.connect(lambda:self.set_selected_cell(self.mat07,0,7))
        self.mat08.clicked.connect(lambda:self.set_selected_cell(self.mat08,0,8))
        self.mat10.clicked.connect(lambda:self.set_selected_cell(self.mat10,1,0))
        self.mat11.clicked.connect(lambda:self.set_selected_cell(self.mat11,1,1))
        self.mat12.clicked.connect(lambda:self.set_selected_cell(self.mat12,1,2))
        self.mat13.clicked.connect(lambda:self.set_selected_cell(self.mat13,1,3))
        self.mat14.clicked.connect(lambda:self.set_selected_cell(self.mat14,1,4))
        self.mat15.clicked.connect(lambda:self.set_selected_cell(self.mat15,1,5))
        self.mat16.clicked.connect(lambda:self.set_selected_cell(self.mat16,1,6))
        self.mat17.clicked.connect(lambda:self.set_selected_cell(self.mat17,1,7))
        self.mat18.clicked.connect(lambda:self.set_selected_cell(self.mat18,1,8))
        self.mat20.clicked.connect(lambda:self.set_selected_cell(self.mat20,2,0))
        self.mat21.clicked.connect(lambda:self.set_selected_cell(self.mat21,2,1))
        self.mat22.clicked.connect(lambda:self.set_selected_cell(self.mat22,2,2))
        self.mat23.clicked.connect(lambda:self.set_selected_cell(self.mat23,2,3))
        self.mat24.clicked.connect(lambda:self.set_selected_cell(self.mat24,2,4))
        self.mat25.clicked.connect(lambda:self.set_selected_cell(self.mat25,2,5))
        self.mat26.clicked.connect(lambda:self.set_selected_cell(self.mat26,2,6))
        self.mat27.clicked.connect(lambda:self.set_selected_cell(self.mat27,2,7))
        self.mat28.clicked.connect(lambda:self.set_selected_cell(self.mat28,2,8))
        self.mat30.clicked.connect(lambda:self.set_selected_cell(self.mat30,3,0))
        self.mat31.clicked.connect(lambda:self.set_selected_cell(self.mat31,3,1))
        self.mat32.clicked.connect(lambda:self.set_selected_cell(self.mat32,3,2))
        self.mat33.clicked.connect(lambda:self.set_selected_cell(self.mat33,3,3))
        self.mat34.clicked.connect(lambda:self.set_selected_cell(self.mat34,3,4))
        self.mat35.clicked.connect(lambda:self.set_selected_cell(self.mat35,3,5))
        self.mat36.clicked.connect(lambda:self.set_selected_cell(self.mat36,3,6))
        self.mat37.clicked.connect(lambda:self.set_selected_cell(self.mat37,3,7))
        self.mat38.clicked.connect(lambda:self.set_selected_cell(self.mat38,3,8))
        self.mat40.clicked.connect(lambda:self.set_selected_cell(self.mat40,4,0))
        self.mat41.clicked.connect(lambda:self.set_selected_cell(self.mat41,4,1))
        self.mat42.clicked.connect(lambda:self.set_selected_cell(self.mat42,4,2))
        self.mat43.clicked.connect(lambda:self.set_selected_cell(self.mat43,4,3))
        self.mat44.clicked.connect(lambda:self.set_selected_cell(self.mat44,4,4))
        self.mat45.clicked.connect(lambda:self.set_selected_cell(self.mat45,4,5))
        self.mat46.clicked.connect(lambda:self.set_selected_cell(self.mat46,4,6))
        self.mat47.clicked.connect(lambda:self.set_selected_cell(self.mat47,4,7))
        self.mat48.clicked.connect(lambda:self.set_selected_cell(self.mat48,4,8))
        self.mat50.clicked.connect(lambda:self.set_selected_cell(self.mat50,5,0))
        self.mat51.clicked.connect(lambda:self.set_selected_cell(self.mat51,5,1))
        self.mat52.clicked.connect(lambda:self.set_selected_cell(self.mat52,5,2))
        self.mat53.clicked.connect(lambda:self.set_selected_cell(self.mat53,5,3))
        self.mat54.clicked.connect(lambda:self.set_selected_cell(self.mat54,5,4))
        self.mat55.clicked.connect(lambda:self.set_selected_cell(self.mat55,5,5))
        self.mat56.clicked.connect(lambda:self.set_selected_cell(self.mat56,5,6))
        self.mat57.clicked.connect(lambda:self.set_selected_cell(self.mat57,5,7))
        self.mat58.clicked.connect(lambda:self.set_selected_cell(self.mat58,5,8))
        self.mat60.clicked.connect(lambda:self.set_selected_cell(self.mat60,6,0))
        self.mat61.clicked.connect(lambda:self.set_selected_cell(self.mat61,6,1))
        self.mat62.clicked.connect(lambda:self.set_selected_cell(self.mat62,6,2))
        self.mat63.clicked.connect(lambda:self.set_selected_cell(self.mat63,6,3))
        self.mat64.clicked.connect(lambda:self.set_selected_cell(self.mat64,6,4))
        self.mat65.clicked.connect(lambda:self.set_selected_cell(self.mat65,6,5))
        self.mat66.clicked.connect(lambda:self.set_selected_cell(self.mat66,6,6))
        self.mat67.clicked.connect(lambda:self.set_selected_cell(self.mat67,6,7))
        self.mat68.clicked.connect(lambda:self.set_selected_cell(self.mat68,6,8))
        self.mat70.clicked.connect(lambda:self.set_selected_cell(self.mat70,7,0))
        self.mat71.clicked.connect(lambda:self.set_selected_cell(self.mat71,7,1))
        self.mat72.clicked.connect(lambda:self.set_selected_cell(self.mat72,7,2))
        self.mat73.clicked.connect(lambda:self.set_selected_cell(self.mat73,7,3))
        self.mat74.clicked.connect(lambda:self.set_selected_cell(self.mat74,7,4))
        self.mat75.clicked.connect(lambda:self.set_selected_cell(self.mat75,7,5))
        self.mat76.clicked.connect(lambda:self.set_selected_cell(self.mat76,7,6))
        self.mat77.clicked.connect(lambda:self.set_selected_cell(self.mat77,7,7))
        self.mat78.clicked.connect(lambda:self.set_selected_cell(self.mat78,7,8))
        self.mat80.clicked.connect(lambda:self.set_selected_cell(self.mat80,8,0))
        self.mat81.clicked.connect(lambda:self.set_selected_cell(self.mat81,8,1))
        self.mat82.clicked.connect(lambda:self.set_selected_cell(self.mat82,8,2))
        self.mat83.clicked.connect(lambda:self.set_selected_cell(self.mat83,8,3))
        self.mat84.clicked.connect(lambda:self.set_selected_cell(self.mat84,8,4))
        self.mat85.clicked.connect(lambda:self.set_selected_cell(self.mat85,8,5))
        self.mat86.clicked.connect(lambda:self.set_selected_cell(self.mat86,8,6))
        self.mat87.clicked.connect(lambda:self.set_selected_cell(self.mat87,8,7))
        self.mat88.clicked.connect(lambda:self.set_selected_cell(self.mat88,8,8))
        
        self.select1.clicked.connect(lambda:self.set_choice(self.select1))
        self.select2.clicked.connect(lambda:self.set_choice(self.select2))
        self.select3.clicked.connect(lambda:self.set_choice(self.select3))
        self.select4.clicked.connect(lambda:self.set_choice(self.select4))
        self.select5.clicked.connect(lambda:self.set_choice(self.select5))
        self.select6.clicked.connect(lambda:self.set_choice(self.select6))
        self.select7.clicked.connect(lambda:self.set_choice(self.select7))
        self.select8.clicked.connect(lambda:self.set_choice(self.select8))
        self.select9.clicked.connect(lambda:self.set_choice(self.select9))



#list all availabe puzzle
    def list_puzzle_file(self):
        files = os.listdir("./puzzle")
        self.files =files
        print(files)
        self.list_puzzle.clear()
        for f in files:
            self.list_puzzle.addItem(f)

#load puzzle to interface        
    def load_puzzle(self,row):
        if self.game_state=="play":
            return

        if(row==-1):
            self.msg.setText("Please , select puzzle");
        self.current_puzzle=self.files[row]
        print(row)
        self.mat=[]
        self.blist=[]
        self.plist=[]
        self.attempt = 3
        self.cell=None
        for i in range(0,9):
            for j in range(0,9):
                self.board[i][j].setText("")
                self.board[i][j].setDisabled(False)
                self.board[i][j].setStyleSheet('background-color: white;color:black')

        self.read_file(self.current_puzzle)
        self.progress.setMaximum(len(self.blist))
        self.enable_board()
        self.msg.setText("Attempt remaining "+str(self.attempt))
        self.display(self.mat)
        self.solution = sudoku_solve.solve(deepcopy(self.mat),self.blist)
        if self.solution == None:
            self.game_state="stop"
            self.msg.setText("Corrupt puzzle !");
        else:
            sudoku_solve.display(self.solution)

#restart game
    def restart_puzzle(self,row):
        if self.current_puzzle=="":
            self.msg.setText("Please, Select puzzle")
            return
        self.game_state=="stop"
        self.stop_puzzle()
        self.load_puzzle(row)
        self.play_sudoku()

#clear cell of puzzle
    def clear_cell(self):
        if self.game_state=="stop":
            return
        
        if self.cell==None:
            return
        
        self.mat[self.i][self.j]=0
        self.board[self.i][self.j].setText("")
        sudoku_solve.display(self.mat)
        self.display(self.mat)

#stop puzzle
    def stop_puzzle(self):
        self.game_state="stop"
        self.play.setStyleSheet('background-color: silver;color:black')

#end game
    def quit_puzzle(self):
        if self.game_state=="stop":
            return
        self.game_state="stop"
        self.msg.setText("YOU LOST !")
        for i in range(0,9):
            for j in range(0,9):
                self.mat[i][j]=0
        self.display(self.mat)
        self.stop_puzzle()

#add new puzzle
    def add_new_puzzle(self):
        if self.game_state=="play":
            return
        
        
        if self.add_form is not None:
            self.add_ui.load()
            self.add_form.show()
        print("add")

#information about cell is stored for future used which have been selected
    def set_selected_cell(self,cell_selected,i,j):
        if self.game_state=="stop":
            return
        self.enable_board()
        self.i =i
        self.j =j
        if self.cell is not None:
            self.cell.setStyleSheet('background-color: white;color:black')
        self.cell = cell_selected
        self.cell.setDisabled(True)
        print(i,j)
        self.cell.setStyleSheet('background-color: green;color:white')
        
#set choice from 1-9 to selected cell
    def set_choice(self,choice):
        if self.game_state=="stop":
            return
        t=self.choice.index(choice)+1
        follow_rule=sudoku_solve.checkRule(self.mat,(self.i,self.j),t)
        self.mat[self.i][self.j]=t
        self.display(self.mat)
        sudoku_solve.display(self.mat)
        self.enable_board()
        print(self.choice.index(choice))
        if follow_rule==False:
            self.attempt = self.attempt-1
            self.cell.setStyleSheet('background-color:blue;color:red')
            self.msg.setText(str("Attempt remaining :"+str(self.attempt)))
        else:
            is_solved = False
            print("solution ",self.solution[self.i][self.j])
            if t==self.solution[self.i][self.j]:
                is_solved=True
            print(is_solved)
            if is_solved==False:
                self.attempt = self.attempt-1
                self.cell.setStyleSheet('background-color:blue;color:red')
                self.msg.setText(str("Attempt remaining :"+str(self.attempt)))
            elif self.count==81:
                self.msg.setText("CONGRATULATION! , YOU WON , Try another puzzle")
                self.game_state="stop"
                self.stop_puzzle()
            else:
                self.cell.setStyleSheet('background-color:green;color:black')

        if self.attempt<=0:
            self.msg.setText("sorry!  ,YOU LOST ");
            self.stop_puzzle()

#display matrix information to board
    def display(self,mat):
        self.count=0
        count = 0
        for i in range(0,9):
            for j in range(0,9):
                if mat[i][j] != 0:
                    self.board[i][j].setText(str(mat[i][j]))
                    count = count +1
        self.progress.setValue(count-len(self.plist))
        self.count=count

#read the puzzle
    def read_file(self,fname):
        f=open("./puzzle/"+fname,'r')
        mat=[]
        blist=[]
        plist=[]
        mat=[]
        for line in f.readlines():
            mat.append([int(x) for x in line.split(' ')[0:9]])
        for i in range(9):
            for j in range(9):
                if mat[i][j] == 0 :
                    blist.append((i,j))
                else:
                    plist.append((i,j))
        
        self.mat = mat
        self.blist = blist
        self.plist = plist

#set enable and disable to board cell according to puzzle        
    def enable_board(self):
        for i in range(0,9):
            for j in range(0,9):
                self.board[i][j].setDisabled(False)
        for p in self.plist:
            i,j = p
            self.board[i][j].setDisabled(True)
            self.board[i][j].setStyleSheet('background-color: red;color:black')

#begin game
    def play_sudoku(self):
        if self.current_puzzle=="":
            self.msg.setText("Please, Select puzzle")
            return
        
        self.game_state="play"
        self.play.setStyleSheet('background-color: blue;color:white')
        


if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)

    Form = QtWidgets.QWidget()
    ui = Ui_sudoku_board()
    ui.setupUi(Form)
    Form.show()

    add_Form = QtWidgets.QWidget()
    add_ui = add_puzzle.Ui_add_board()
    add_ui.setupUi(add_Form)
    ui.add_form = add_Form
    ui.add_ui = add_ui
    #add_Form.show()
    
    sys.exit(app.exec_())
	