from tkinter import *
from tkinter import ttk

valor_atual = ''
lista_teclas=['0','1','2','3','4','5','6','7','8','9','/','*','-','+','.','enter','=']

janela = Tk()
janela.title = ("Kalk")
janela.geometry("350x430")
janela.config(bg='#1e1e1e')

#Frames
frame_tela = Frame(janela, width = 350, height = 70, bg="#334750", borderwidth='10')
frame_tela.grid(row=0, column=0)
frame_botoes = Frame(janela, width = 350, height = 360, bg="#454545", borderwidth='10')
frame_botoes.grid(row=1, column=0)

#Label
visor = StringVar()
tamanho = '25'
fonte = f"times {str(tamanho)}"

tela_label = Label(frame_tela, textvariable=visor, width = 15, height = 1, relief=FLAT, anchor='e', justify=RIGHT, font = fonte, bg="#334750", fg="#fefefe")
tela_label.place(x=6,y=10)

## Botoes
largura = 4
altura = 2
cor1 = "#dedede"
cor2 = "#dcdcdc"
cor3 = "#dba716"
font = ("calibri 14 bold")
x = 84
y = 70
#Primeira Fileira
btc = Button(frame_botoes, command = lambda: entrada('clear'), text="C", width=11, height=altura, bg=cor1, font=font)
btc.place(x=0,y=0)
btp = Button(frame_botoes, command = lambda: entrada('%'), text="%", width=largura, height=altura, bg=cor2, font =font)
btp.place(x=x*2,y=0)
btb = Button(frame_botoes, command = lambda: entrada('/'), text="/", width=largura, height=altura, bg=cor2, font=font)
btb.place(x=x*3,y=0)
#Segunda Fileira
bt7 = Button(frame_botoes, command = lambda: entrada('7'), text="7", width=largura, height=altura, bg=cor2, font=font)
bt7.place(x=0,y=y)
bt8 = Button(frame_botoes, command = lambda: entrada('8'), text="8", width=largura, height=altura, bg=cor2, font=font)
bt8.place(x=x,y=y)
bt9 = Button(frame_botoes, command = lambda: entrada('9'), text="9", width=largura, height=altura, bg=cor2, font=font)
bt9.place(x=x*2,y=y)
bta = Button(frame_botoes, command = lambda: entrada('*'), text="*", width=largura, height=altura, bg=cor2, font=font)
bta.place(x=x*3,y=y)
#Terceita Fileira
bt4 = Button(frame_botoes, command = lambda: entrada('4'), text="4", width=largura, height=altura, bg=cor2, font=font)
bt4.place(x=0,y=y*2)
bt5 = Button(frame_botoes, command = lambda: entrada('5'), text="5", width=largura, height=altura, bg=cor2, font=font)
bt5.place(x=x,y=y*2)
bt6 = Button(frame_botoes, command = lambda: entrada('6'), text="6", width=largura, height=altura, bg=cor2, font=font)
bt6.place(x=x*2,y=y*2)
btplus = Button(frame_botoes, command = lambda: entrada('+'), text="+", width=largura, height=altura, bg=cor2, font=font)
btplus.place(x=x*3,y=y*2)
#Quarta Fileira
bt1 = Button(frame_botoes, command = lambda: entrada('1'), text="1", width=largura, height=altura, bg=cor2, font=font)
bt1.place(x=0,y=y*3)
bt2 = Button(frame_botoes, command = lambda: entrada('2'), text="2", width=largura, height=altura, bg=cor2, font=font)
bt2.place(x=x,y=y*3)
bt3 = Button(frame_botoes, command = lambda: entrada('3'), text="3", width=largura, height=altura, bg=cor2, font=font)
bt3.place(x=x*2,y=y*3)
btm = Button(frame_botoes, command = lambda: entrada('-'), text="-", width=largura, height=altura, bg=cor2, font=font)
btm.place(x=x*3,y=y*3)
#Quinta Fileira
bt0 = Button(frame_botoes, command = lambda: entrada('0'), text="0", width=11, height=altura, bg=cor2, font=font)
bt0.place(x=0,y=y*4)
btd = Button(frame_botoes, command = lambda: entrada('.'), text=".", width=largura, height=altura, bg=cor2, font=font)
btd.place(x=x*2,y=y*4)
bte = Button(frame_botoes, command = lambda: calcular(), text="=", width=largura, height=altura, bg=cor2, font=font)
bte.place(x=x*3,y=y*4)

#Recebe a entrada e apresenta na tela
def entrada(character):
    global valor_atual
    #Verifica se a tela tem erro ou 0 e limpa
    if valor_atual == 'Erro' or valor_atual == '0':
        valor_atual = ''
        visor.set(valor_atual)
    #Limpa se for apertado o clear
    if character == 'clear':
        valor_atual = ''
    else: # Apresenta na tela o botao apertado
        valor_atual = valor_atual + str(character) 
    visor.set(valor_atual)

#Realiza o calculo do que esta presente na tela
def calcular():
    global valor_atual
    try:
        resultado = eval(valor_atual)
        valor_atual = str(resultado)
        visor.set(resultado)
    except:
        visor.set('Erro')
        valor_atual = 'Erro'

if __name__ == "__main__":
    janela.mainloop()
