from tkinter import *

co1 = "#feffff" 
co2 = "#38576b"  
co3 = "#ECEFF1"  
co4 = "#FFAB40"  
fundo = "#3b3b3b"  
janela = Tk()
janela.title("Calculadora")
janela.geometry("235x310")
janela.configure(bg=co1)

frame_tela = Frame(janela, width=235, height=50, bg=co2)
frame_tela.grid(row=0, column=0)

frame_quadros = Frame(janela, width=235, height=260, bg=fundo)
frame_quadros.grid(row=1, column=0)

todos_valores = ""
valor_texto = StringVar()

app_tela = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief="flat",
 anchor="e", bd=0, justify=RIGHT, font=('Ivy 18'), bg='#37474F', fg=co1)
app_tela.place(x=0, y=0)

def entrar_valor(event):
    global todos_valores
    todos_valores += str(event)
    valor_texto.set(todos_valores)

def calcular():
    global todos_valores
    try:
        resultado = str(eval(todos_valores))
        valor_texto.set(resultado)
        todos_valores = ""
    except:
        valor_texto.set("Erro")
        todos_valores = ""

def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")

botoes = [
    ("C", limpar_tela, 0, 0, 11),
    ("%", lambda: entrar_valor("%"), 118, 0, 5),
    ("/", lambda: entrar_valor("/"), 177, 0, 5),
    ("7", lambda: entrar_valor("7"), 0, 52, 5),
    ("8", lambda: entrar_valor("8"), 59, 52, 5),
    ("9", lambda: entrar_valor("9"), 118, 52, 5),
    ("*", lambda: entrar_valor("*"), 177, 52, 5),
    ("4", lambda: entrar_valor("4"), 0, 104, 5),
    ("5", lambda: entrar_valor("5"), 59, 104, 5),
    ("6", lambda: entrar_valor("6"), 118, 104, 5),
    ("-", lambda: entrar_valor("-"), 177, 104, 5),
    ("1", lambda: entrar_valor("1"), 0, 156, 5),
    ("2", lambda: entrar_valor("2"), 59, 156, 5),
    ("3", lambda: entrar_valor("3"), 118, 156, 5),
    ("+", lambda: entrar_valor("+"), 177, 156, 5),
    ("0", lambda: entrar_valor("0"), 0, 208, 11),
    (".", lambda: entrar_valor("."), 118, 208, 5),
    ("=", calcular, 177, 208, 5)
]

for texto, comando, x, y, largura in botoes:
    bg_cor = co4 if texto in ["*", "/", "-", "+", "="] else co3
    fg_cor = co1 if texto in ["*", "/", "-", "+", "="] else fundo

    Button(
        frame_quadros,
        text=texto,
        width=largura,
        height=2,
        command=comando,
        bg=bg_cor,
        fg=fg_cor,
        font=('Ivy 13 bold'),
        relief=RAISED,
        overrelief=RIDGE
    ).place(x=x, y=y)

janela.mainloop()



