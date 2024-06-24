import tkinter as tk    

valor_atual = ''
lista_teclas=['0','1','2','3','4','5','6','7','8','9','/','*','-','+','.','Return', 'KP_Enter','=', 'BackSpace', 'Escape']

## Criação da janela principal ##
janela = tk.Tk()
janela.title("Kalk")
janela.geometry("300x400")
janela.config(bg='#1e1e1e')


## Frames ##
frame_tela = tk.Frame(janela, bg="#292929", borderwidth='1')
frame_tela.grid(row=0, column=0, sticky="nsew")

frame_botoes = tk.Frame(janela, bg="#454545", borderwidth='1')
frame_botoes.grid(row=1, column=0, sticky="nsew")

## Configuração dos grids ##
janela.grid_rowconfigure(0, weight=1)
janela.grid_rowconfigure(1, weight=5)
janela.grid_columnconfigure(0, weight=1)
frame_tela.grid_columnconfigure(0, weight=1)
frame_tela.grid_rowconfigure(0, weight=1)
frame_botoes.grid_columnconfigure((0, 1, 2, 3), weight=1)
frame_botoes.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)

## Label ##
visor = tk.StringVar()
tamanho = '22'
fonte = f"times {str(tamanho)}"
tela_label = tk.Label(frame_tela, textvariable=visor, relief=tk.FLAT, anchor='e', justify=tk.RIGHT, font=fonte, bg="#292929", fg="#fafafa")
tela_label.grid(row=0, column=0, sticky="nsew", padx=6, pady=2)

#### Botões ####
cor1 = "#c0c0c0"
cor2 = "#FFA500"
font = ("calibri 14 bold")

# Primeira Fileira
btc = tk.Button(frame_botoes, command=lambda: entrada('clear'), text="C", bg=cor1, font=font)
btc.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=3, pady=3)
btp = tk.Button(frame_botoes, command=lambda: entrada('%'), text="%", bg=cor2, font=font)
btp.grid(row=0, column=2, sticky="nsew", padx=3, pady=3)
btb = tk.Button(frame_botoes, command=lambda: entrada('/'), text="/", bg=cor2, font=font)
btb.grid(row=0, column=3, sticky="nsew", padx=3, pady=3)
# Segunda Fileira
bt7 = tk.Button(frame_botoes, command = lambda: entrada('7'), text="7", bg=cor1, font=font)
bt7.grid(row=1,column=0, sticky="nsew", padx=3, pady=3)
bt8 = tk.Button(frame_botoes, command = lambda: entrada('8'), text="8", bg=cor1, font=font)
bt8.grid(row=1,column=1, sticky="nsew", padx=3, pady=3)
bt9 = tk.Button(frame_botoes, command = lambda: entrada('9'), text="9", bg=cor1, font=font)
bt9.grid(row=1,column=2, sticky="nsew", padx=3, pady=3)
bta = tk.Button(frame_botoes, command = lambda: entrada('*'), text="*", bg=cor2, font=font)
bta.grid(row=1,column=3, sticky="nsew", padx=3, pady=3)
# Terceita Fileira
bt4 = tk.Button(frame_botoes, command = lambda: entrada('4'), text="4", bg=cor1, font=font)
bt4.grid(row=2,column=0, sticky="nsew", padx=3, pady=3)
bt5 = tk.Button(frame_botoes, command = lambda: entrada('5'), text="5", bg=cor1, font=font)
bt5.grid(row=2,column=1, sticky="nsew", padx=3, pady=3)
bt6 = tk.Button(frame_botoes, command = lambda: entrada('6'), text="6", bg=cor1, font=font)
bt6.grid(row=2,column=2, sticky="nsew", padx=3, pady=3)
btplus = tk.Button(frame_botoes, command = lambda: entrada('+'), text="+", bg=cor2, font=font)
btplus.grid(row=2,column=3, sticky="nsew", padx=3, pady=3)
# Quarta Fileira
bt1 = tk.Button(frame_botoes, command = lambda: entrada('1'), text="1", bg=cor1, font=font)
bt1.grid(row=3,column=0, sticky="nsew", padx=3, pady=3)
bt2 = tk.Button(frame_botoes, command = lambda: entrada('2'), text="2", bg=cor1, font=font)
bt2.grid(row=3,column=1, sticky="nsew", padx=3, pady=3)
bt3 = tk.Button(frame_botoes, command = lambda: entrada('3'), text="3", bg=cor1, font=font)
bt3.grid(row=3,column=2, sticky="nsew", padx=3, pady=3)
btm = tk.Button(frame_botoes, command = lambda: entrada('-'), text="-", bg=cor2, font=font)
btm.grid(row=3,column=3, sticky="nsew", padx=3, pady=3)
# Quinta Fileira
bt0 = tk.Button(frame_botoes, command = lambda: entrada('0'), text="0", bg=cor1, font=font)
bt0.grid(row=4,column=0, columnspan=2, sticky="nsew", padx=3, pady=3)
btd = tk.Button(frame_botoes, command = lambda: entrada('.'), text=".", bg=cor1, font=font)
btd.grid(row=4,column=2, sticky="nsew", padx=3, pady=3)
bte = tk.Button(frame_botoes, command = lambda: calcular(), text="=", bg=cor2, font=font)
bte.grid(row=4,column=3, sticky="nsew", padx=3, pady=3)

#Recebe a entrada e apresenta na tela
def entrada(character):
    global valor_atual
    #Verifica se a tela tem erro ou 0 e / ou botao clear apertado e limpa
    if valor_atual == 'Erro' or valor_atual == '0' or valor_atual == 'clear' or valor_atual[-1:] == '~':
        valor_atual = ''
        if character == 'clear':
            valor_atual == ''
            visor.set(valor_atual)
        elif character == 'backspace':
            valor_atual == ''
            visor.set(valor_atual)
        else:
            valor_atual = str(character) 
            visor.set(valor_atual)
    elif character == 'clear':
        valor_atual = ''
        visor.set(valor_atual)
    elif character == 'backspace':
        valor_atual = valor_atual[:-1]
        visor.set(valor_atual)
    else:
        valor_atual = valor_atual + str(character) 
        visor.set(valor_atual)

#Realiza o calculo do que esta presente na tela
def calcular():
    global valor_atual
    if valor_atual == 'Erro' or valor_atual == '' or valor_atual == '0':
        valor_atual = ''
        visor.set(valor_atual)
    else:
    #Uso de try para apresentar erro na tela caso aconteça algum erro
        try:
            #Calcula
            resultado = eval(valor_atual)
            #Verifica se é inteiro e transforma em inteiro se for
            if resultado == int(resultado):
                resultado = int(resultado)
            #Transforma em string
            str_resultado = str(resultado)
            #Define o valor atual como o valor do resultado e seta o visor com o valor
            valor_atual = str_resultado
            visor.set(valor_atual)
        except Exception as erro:
            visor.set('Erro')
            valor_atual = 'Erro'
            print(erro)

###Bindando as teclas###
# Função para associar as teclas do teclado aos botões
def tecla_pressionada(event):
    if event.char in lista_teclas or event.keysym in lista_teclas:
        if event.keysym == 'KP_Enter' or event.keysym == 'Return' or event.char == '=':
            calcular()
        elif event.char in '0123456789/*-+.%':
            entrada(event.char)
        elif event.keysym == 'BackSpace':
            entrada('backspace')
        elif event.keysym == 'Escape':
            entrada('clear')   

# Vincula as teclas à função tecla_pressionada

if __name__ == "__main__":
    janela.bind('<Key>', tecla_pressionada)
    janela.mainloop()
