from tkinter import *
from tkinter import ttk

janela = Tk()
janela.title = ("Kalk")
janela.geometry("350x440")
janela.config(bg='#1e1e1e')

#Frames
frame_tela = Frame(janela, width = 350, height = 100, bg="#334750", borderwidth='10')
frame_tela.grid(row=0, column=0)
frame_botoes = Frame(janela, width = 350, height = 340, bg="#454545", borderwidth='10')
frame_botoes.grid(row=1, column=0)

## Botoes
largura = 5
altura = 2
cor1 = "#dedede"
cor2 = "#dcdcdc"
cor3 = "#dba716"
font = ("calibri 12 bold")
x = 84
y = 65
#Primeira Fileira
btc = Button(frame_botoes, text="C", width=13, height=altura, bg=cor1, font=font)
btc.place(x=2,y=0)
btp = Button(frame_botoes, text="%", width=largura, height=altura, bg=cor2, font =font)
btp.place(x=x*2,y=0)
btb = Button(frame_botoes, text="/", width=largura, height=altura, bg=cor2, font=font)
btb.place(x=x*3,y=0)
#Segunda Fileira
bt7 = Button(frame_botoes, text="7", width=largura, height=altura, bg=cor2, font=font)
bt7.place(x=0,y=y)
bt8 = Button(frame_botoes, text="8", width=largura, height=altura, bg=cor2, font=font)
bt8.place(x=x,y=y)
bt9 = Button(frame_botoes, text="9", width=largura, height=altura, bg=cor2, font=font)
bt9.place(x=x*2,y=y)
bta = Button(frame_botoes, text="*", width=largura, height=altura, bg=cor2, font=font)
bta.place(x=x*3,y=y)
#Terceita Fileira
bt4 = Button(frame_botoes, text="4", width=largura, height=altura, bg=cor2, font=font)
bt4.place(x=0,y=y*2)
bt5 = Button(frame_botoes, text="5", width=largura, height=altura, bg=cor2, font=font)
bt5.place(x=x,y=y*2)
bt6 = Button(frame_botoes, text="6", width=largura, height=altura, bg=cor2, font=font)
bt6.place(x=x*2,y=y*2)
btplus = Button(frame_botoes, text="+", width=largura, height=altura, bg=cor2, font=font)
btplus.place(x=x*3,y=y*2)
#Quarta Fileira
bt1 = Button(frame_botoes, text="1", width=largura, height=altura, bg=cor2, font=font)
bt1.place(x=0,y=y*3)
bt2 = Button(frame_botoes, text="2", width=largura, height=altura, bg=cor2, font=font)
bt2.place(x=x,y=y*3)
bt3 = Button(frame_botoes, text="3", width=largura, height=altura, bg=cor2, font=font)
bt3.place(x=x*2,y=y*3)
btm = Button(frame_botoes, text="-", width=largura, height=altura, bg=cor2, font=font)
btm.place(x=x*3,y=y*3)
#Quinta Fileira
bt0 = Button(frame_botoes, text="0", width=13, height=altura, bg=cor2, font=font)
bt0.place(x=2,y=y*4)
btd = Button(frame_botoes, text=".", width=largura, height=altura, bg=cor2, font=font)
btd.place(x=x*2,y=y*4)
bte = Button(frame_botoes, text="=", width=largura, height=altura, bg=cor2, font=font)
bte.place(x=x*3,y=y*4)


janela.mainloop()

