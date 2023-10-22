import tkinter as tk
from tkinter import ttk
import os
from datetime import datetime
import time as sleep


# Função para verificar e executar o desligamento
def verificar_hora_desligamento():
    hora_desligamento = hora_desligamento_entry.get()
    hora_atual = datetime.now().strftime('%H:%M')

    if hora_atual == hora_desligamento:
        # Execute aqui o código para abrir o arquivo
        os.startfile('')


# Função para ocultar a janela
def ocultar_janela():
    root.withdraw()


# Função para mostrar a janela
def mostrar_janela():
    root.deiconify()


# Função para atualizar a hora atual na interface
def atualizar_hora_atual():
    hora_atual = datetime.now().strftime('%H:%M:%S')
    hora_atual_label.config(text=f'Hora Atual: {hora_atual}')
    verificar_hora_desligamento()  # Verifique a hora de desligamento a cada atualização
    root.after(1000, atualizar_hora_atual)  # Atualize a cada 1 segundo


# Configuração da interface
root = tk.Tk()
root.title("Verificador e Controlador de Hora de Desligamento")

style = ttk.Style()
style.configure("TButton", padding=6, font=("Helvetica", 12))

frame = ttk.Frame(root, padding=10)
frame.grid(row=0, column=0, padx=10, pady=10)

# Campo de entrada para a hora de desligamento
hora_desligamento_label = ttk.Label(frame, text="Hora de Desligamento (HH:MM):")
hora_desligamento_label.grid(row=0, column=0, padx=5, pady=5)

hora_desligamento_entry = ttk.Entry(frame)
hora_desligamento_entry.grid(row=0, column=1, padx=5, pady=5)

# Botão para verificar e iniciar o desligamento
verificar_button = ttk.Button(frame, text="Verificar e Iniciar", command=verificar_hora_desligamento)
verificar_button.grid(row=1, column=0, columnspan=2, pady=10)

# Rótulo para exibir a hora atual
hora_atual_label = ttk.Label(frame, text="")
hora_atual_label.grid(row=2, column=0, columnspan=2, pady=10)

# Botão para ocultar a janela
ocultar_button = ttk.Button(frame, text="Ocultar Janela", command=ocultar_janela)
ocultar_button.grid(row=3, column=0, columnspan=2, pady=10)

# Iniciar verificação em segundo plano
atualizar_hora_atual()

root.mainloop()
