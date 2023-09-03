import tkinter as tk
from tkinter import ttk, messagebox
from ttkthemes import ThemedStyle


# Função para realizar o cálculo da equação do primeiro grau
def calculate():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        # Condições para tratar diferentes casos de solução
        if a == 0:
            if b == 0:
                if c == 0:
                    solucao_label.config(text="Infinitas soluções")
                else:
                    solucao_label.config(text="Sem solução")
            else:
                x = -c / b
                solucao_label.config(text="Solução: " + str(x))
        else:
            delta = b ** 2 - 4 * a * c
            if delta < 0:
                solucao_label.config(text="Sem solução real")
            elif delta == 0:
                x = -b / (2 * a)
                solucao_label.config(text="Solução: " + str(x))
            else:
                x1 = (-b + delta ** 0.5) / (2 * a)
                x2 = (-b - delta ** 0.5) / (2 * a)
                solucao_label.config(text="Solução x1: " + str(x1) + "\nSolução x2: " + str(x2))
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

    # Limpa os campos de entrada e define o foco no campo "a"
    entry_a.delete(0, tk.END)
    entry_b.delete(0, tk.END)
    entry_c.delete(0, tk.END)
    entry_a.focus()


# Cria a janela principal do aplicativo
app = tk.Tk()
app.title("Calculadora de Equação do Primeiro Grau")

# Configuração do estilo da interface
style = ThemedStyle(app)
style.set_theme("arc")  # Você pode escolher outros temas disponíveis

# Criação do frame para os elementos da interface
frame = ttk.Frame(app)
frame.pack(padx=20, pady=20)

# Rótulo e campo de entrada para o coeficiente "a"
label_a = ttk.Label(frame, text="a:")
label_a.grid(row=0, column=0)
entry_a = ttk.Entry(frame)
entry_a.grid(row=0, column=1)
entry_a.bind("<Return>", lambda event=None: entry_b.focus())

# Rótulo e campo de entrada para o coeficiente "b"
label_b = ttk.Label(frame, text="b:")
label_b.grid(row=1, column=0)
entry_b = ttk.Entry(frame)
entry_b.grid(row=1, column=1)
entry_b.bind("<Return>", lambda event=None: entry_c.focus())

# Rótulo e campo de entrada para o coeficiente "c"
label_c = ttk.Label(frame, text="c:")
label_c.grid(row=2, column=0)
entry_c = ttk.Entry(frame)
entry_c.grid(row=2, column=1)
entry_c.bind("<Return>", lambda event=None: calculate())

# Botão para calcular
calculate_button = ttk.Button(app, text="Calcular", command=calculate)
calculate_button.pack(pady=10)

# Rótulo para exibir a solução
solucao_label = ttk.Label(app, text="Solução:")
solucao_label.pack()

# Define o foco inicial no campo "a"
entry_a.focus()

# Inicia o loop principal da interface
app.mainloop()
