import customtkinter as tk

#verificação
def validção_login():
    nome = entry_nome.get()
    email = entry_email.get()
    senha = entry_senha.get()

    #Dados corretos (Fixos)
    if nome and email and senha:
        entry_nome.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_senha.delete(0, tk.END)
        resultado_login.configure(text='Cadastro feito com sucesso!',text_color='green')
    else:
        resultado_login.configure(text='Não foi possivel completar o Cadastro',text_color='red')



#Janela principal
janela = tk.CTk()
janela.title("Cadastro Sustentavel")
janela.geometry("300x400")

tk.set_appearance_mode('dark')

janela = tk.CTk()
janela.title('Tela de Login')
janela.geometry('300x400')

#Campos de entrada
tk.CTkLabel(janela, text="Nome:",font=("Arial", 16, "bold")).pack()
entry_nome = tk.CTkEntry(janela)
entry_nome.pack(pady=10)

tk.CTkLabel(janela, text="E-mail:",font=("Arial", 16, "bold")).pack()
entry_email = tk.CTkEntry(janela)
entry_email.pack(pady=10)

tk.CTkLabel(janela, text="Senha:",font=("Arial", 16, "bold")).pack()
entry_senha = tk.CTkEntry(janela, show="*")
entry_senha.pack(pady=10)

#Botão
tk.CTkButton(janela, text="Cadastrar").pack(pady=20)

resultado_login = tk.CTkLabel(janela,text='Cadastro realizado com sucesso',text_color='green')
resultado_login.pack(pady=20)

janela.mainloop()
