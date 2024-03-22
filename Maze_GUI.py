#The File Created By Mohammad Hosein Mohseni(402149059) And Mahdi Karimi(402149058).
#Mater: Fatemeh Porgholamali
#Valiasr Rafsanjan University
#Computer Engineering 1402
#Term: 4021

#Import Tkinter Library For GUI
from tkinter import *
import tkinter as tk

#Creating Window
window=Tk()
window.geometry("700x700")
window.title("Maze")

#Opening GUI.txt that generated in C and Convert it to Matrix
maze_gui_file = open("GUI.txt")
M=maze_gui_file.read()
M= M.split()
n = len(M)
for i in range(n):
    M[i]= list(M[i])
m = len(M[0])

#Creating Canvas Widget
cv = Canvas(window, bg='black')
cv.pack(expand=True,fill=BOTH)

#Creating Scrollbar
scrollbar= Scrollbar(window)
scrollbar.pack(side=RIGHT,fill=BOTH)

#Opening Image Files from directory
W = PhotoImage(file='W.png')

S = PhotoImage(file='S.png')
FU = PhotoImage(file='FU.png')
FD = PhotoImage(file='FD.png')
FR = PhotoImage(file='FR.png')
SR = PhotoImage(file='SR.png')
SL = PhotoImage(file='SL.png')
SU = PhotoImage(file='SU.png')
SD = PhotoImage(file='SD.png')

H = PhotoImage(file='H.png')
V = PhotoImage(file='V.png')

R2U = PhotoImage(file='R2U.png')
R2D = PhotoImage(file='R2D.png')
L2U = PhotoImage(file='L2U.png')
L2D = PhotoImage(file='L2D.png')

R2UD = PhotoImage(file='R2UD.png')
L2UD = PhotoImage(file='L2UD.png')
U2RL = PhotoImage(file='U2RL.png')
D2RL = PhotoImage(file='D2RL.png')

HR2U = PhotoImage(file='HR2U.png')
HR2D = PhotoImage(file='HR2D.png')
HL2U = PhotoImage(file='HL2U.png')
HL2D = PhotoImage(file='HL2D.png')
TC = PhotoImage(file='TC.png')

VR2U = PhotoImage(file='VR2U.png')
VR2D = PhotoImage(file='VR2D.png')
VL2U = PhotoImage(file='VL2U.png')
VL2D = PhotoImage(file='VL2D.png')

HP = PhotoImage(file='HP.png')
VP = PhotoImage(file='VP.png')

R = PhotoImage(file='R.png')
L = PhotoImage(file='L.png')
U = PhotoImage(file='U.png')
D = PhotoImage(file='D.png')

R2UP = PhotoImage(file='R2UP.png')
R2DP = PhotoImage(file='R2DP.png')
L2UP = PhotoImage(file='L2UP.png')
L2DP = PhotoImage(file='L2DP.png')

TR = PhotoImage(file='TR.png')
TL = PhotoImage(file='TL.png')
TU = PhotoImage(file='TU.png')
TD = PhotoImage(file='TD.png')

#Function for Create image in spesific coordinates
def cp(x,y,file):
    cv.create_image((y*50)+25, (x*50)+25, image = file)

HD=['#','.']
XO=['0','x']

#Creating Maze with Matrix Conditions
for i in range(n):
     for j in range(m):
        if(M[i][j]=='#'): #Walls
            cp(i,j,W)

        if(M[i][j]=='x'): #Red Lines
            if(j==0):
                if(M[i][j+1]=='x'):
                    cp(i,j,S)
                else:
                     cp(i,j,SR)
            if(i==0):
                if(M[i+1][j]=='x'):
                    cp(i,j,FU)
                else:
                     cp(i,j,SD)
            if(j==m-1):
                if(M[i][j-1]=='x'):
                    cp(i,j,FR)
                else:
                     cp(i,j,SL)
            if(i==n-1):
                if(M[i-1][j]=='x'):
                    cp(i,j,FD)
                else:
                     cp(i,j,SU)

            if(i!=0 and j!=0 and i!=n-1 and j!=m-1):
                if(M[i][j-1]=='x' and M[i][j+1]=='x' and (M[i-1][j] in HD) and (M[i+1][j] in HD)):
                    cp(i,j,H)
                if((M[i][j-1] in HD) and (M[i][j+1] in HD) and M[i-1][j]=='x' and M[i+1][j]=='x'):
                    cp(i,j,V)

                if((M[i][j-1] in HD) and M[i][j+1]=='x' and M[i-1][j]=='x' and (M[i+1][j] in HD)):
                    cp(i,j,R2U)
                if((M[i][j-1] in HD) and M[i][j+1]=='x' and (M[i-1][j] in HD) and M[i+1][j]=='x'):
                    cp(i,j,R2D)
                if(M[i][j-1]=='x' and (M[i][j+1] in HD) and M[i-1][j]=='x' and (M[i+1][j] in HD)):
                    cp(i,j,L2U)
                if(M[i][j-1]=='x' and (M[i][j+1] in HD) and (M[i-1][j] in HD) and M[i+1][j]=='x'):
                    cp(i,j,L2D)

                if((M[i][j-1] in HD) and M[i][j+1]=='0' and M[i-1][j]=='x' and M[i+1][j]=='x'):
                    cp(i,j,R2UD)
                if(M[i][j-1]=='0' and (M[i][j+1] in HD) and M[i-1][j]=='x' and M[i+1][j]=='x'):
                    cp(i,j,L2UD)
                if(M[i][j-1]=='x' and M[i][j+1]=='x' and M[i-1][j]=='0' and (M[i+1][j] in HD)):
                    cp(i,j,U2RL)
                if(M[i][j-1]=='x' and M[i][j+1]=='x' and (M[i-1][j] in HD) and M[i+1][j]=='0'):
                    cp(i,j,D2RL)

                if(M[i][j-1]=='x' and M[i][j+1]=='0' and M[i-1][j]=='x' and (M[i+1][j] in HD)):
                    cp(i,j,HR2U)
                if(M[i][j-1]=='x' and M[i][j+1]=='0' and (M[i-1][j] in HD) and M[i+1][j]=='x'):
                    cp(i,j,HR2D)
                if(M[i][j-1]=='0' and M[i][j+1]=='x' and M[i-1][j]=='x' and (M[i+1][j] in HD)):
                    cp(i,j,HL2U)
                if(M[i][j-1]=='0' and M[i][j+1]=='x' and (M[i-1][j] in HD) and M[i+1][j]=='x'):
                    cp(i,j,HL2D)
                if(M[i][j-1]=='0' and M[i][j+1]=='x' and M[i-1][j]=='0' and M[i+1][j]=='x'):
                     cp(i,j,TC)

                if((M[i][j-1] in HD) and M[i][j+1]=='x' and M[i-1][j]=='0' and M[i+1][j]=='x'):
                    cp(i,j,VR2U)
                if((M[i][j-1] in HD) and M[i][j+1]=='x' and M[i-1][j]=='x' and M[i+1][j]=='0'):
                    cp(i,j,VR2D)
                if(M[i][j-1]=='x' and (M[i][j+1] in HD) and M[i-1][j]=='0' and M[i+1][j]=='x'):
                    cp(i,j,VL2U)
                if(M[i][j-1]=='x' and (M[i][j+1] in HD) and M[i-1][j]=='x' and M[i+1][j]=='0'):
                    cp(i,j,VL2D)

        if(M[i][j]=='0'): #Yellow Lines
            if((M[i][j-1] in XO) and (M[i][j+1] in XO) and M[i-1][j]=='#' and M[i+1][j]=='#'):
                    cp(i,j,HP)
            if(M[i][j-1]=='#' and M[i][j+1]=='#' and (M[i-1][j] in XO) and (M[i+1][j] in XO)):
                    cp(i,j,VP)

            if(M[i][j-1]=='#' and (M[i][j+1] in XO) and M[i-1][j]=='#' and M[i+1][j]=='#'):
                    cp(i,j,R)
            if((M[i][j-1] in XO) and M[i][j+1]=='#' and M[i-1][j]=='#' and M[i+1][j]=='#'):
                    cp(i,j,L)
            if(M[i][j-1]=='#' and M[i][j+1]=='#' and (M[i-1][j] in XO) and M[i+1][j]=='#'):
                    cp(i,j,U)
            if(M[i][j-1]=='#' and M[i][j+1]=='#' and M[i-1][j]=='#' and (M[i+1][j] in XO)):
                    cp(i,j,D)

            if(M[i][j-1]=='#' and (M[i][j+1] in XO) and (M[i-1][j] in XO) and M[i+1][j]=='#'):
                    cp(i,j,R2UP)
            if(M[i][j-1]=='#' and (M[i][j+1] in XO) and M[i-1][j]=='#' and (M[i+1][j] in XO)):
                    cp(i,j,R2DP)
            if((M[i][j-1] in XO) and M[i][j+1]=='#' and (M[i-1][j] in XO) and M[i+1][j]=='#'):
                    cp(i,j,L2UP)
            if((M[i][j-1] in XO) and M[i][j+1]=='#' and M[i-1][j]=='#' and (M[i+1][j] in XO)):
                    cp(i,j,L2DP)

            if(M[i][j-1]=='#' and (M[i][j+1] in XO) and (M[i-1][j] in XO) and (M[i+1][j] in XO)):
                    cp(i,j,TR)
            if((M[i][j-1] in XO) and M[i][j+1]=='#' and (M[i-1][j] in XO) and (M[i+1][j] in XO)):
                    cp(i,j,TL)
            if((M[i][j-1] in XO) and (M[i][j+1] in XO) and (M[i-1][j] in XO) and M[i+1][j]=='#'):
                    cp(i,j,TU)
            if((M[i][j-1] in XO) and (M[i][j+1] in XO) and M[i-1][j]=='#' and (M[i+1][j] in XO)):
                    cp(i,j,TD)
            
scrollbar.config(command=cv.yview)

#Disply The Result
window.mainloop()