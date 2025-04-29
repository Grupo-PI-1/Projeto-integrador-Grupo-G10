
import customtkinter as ctk

def calcular():
    try:
        # Obter valores
        agua = float(ent_agua.get())
        energia = float(ent_energia.get())
        residuos = float(ent_residuos.get())
        reciclados = float(ent_reciclados.get())
        
        # Transportes usados
        transportes = []
        if var_publico.get(): transportes.append("Ônibus/Metrô")
        if var_bike.get(): transportes.append("Bicicleta")
        if var_carro.get(): transportes.append("Carro (gasolina)")
        if var_eletrico.get(): transportes.append("Carro elétrico")
        
        # Criar resultado
        resultado = ""
        
        # Água
        if agua < 110:
            resultado += "Água: Sustentável 🌱\n"
        elif 110 <= agua <= 170:
            resultado += "Água: Mediano ⚠️\n"
        else:
            resultado += "Água: Não sustentável ❌\n"
            
        # Energia
        if energia < 120:
            resultado += "Energia: Sustentável 🌱\n"
        elif 120 <= energia <= 180:
            resultado += "Energia: Mediano ⚠️\n"
        else:
            resultado += "Energia: Não sustentável ❌\n"
            
        # Resíduos
        if residuos < 0.8:
            resultado += "Lixo: Sustentável 🌱\n"
        elif 0.8 <= residuos <= 1.2:
            resultado += "Lixo: Mediano ⚠️\n"
        else:
            resultado += "Lixo: Não sustentável ❌\n"
            
        # Reciclados (quanto mais melhor)
        if reciclados > 1.2:
            resultado += "Reciclagem: Ótimo! ♻️\n"
        elif 0.8 <= reciclados <= 1.2:
            resultado += "Reciclagem: Bom 👍\n"
        else:
            resultado += "Reciclagem: Pode melhorar 👎\n"
            
        # Transportes
        if transportes:
            resultado += "\nTransportes usados:\n- " + "\n- ".join(transportes)
        else:
            resultado += "\nNenhum transporte registrado"
            
        # Mostrar resultado
        texto_resultado.configure(state="normal")
        texto_resultado.delete("1.0", "end")
        texto_resultado.insert("1.0", resultado)
        texto_resultado.configure(state="disabled")
        
    except:
        texto_resultado.configure(state="normal")
        texto_resultado.delete("1.0", "end")
        texto_resultado.insert("1.0", "ERRO: Verifique os valores digitados!")
        texto_resultado.configure(state="disabled")

# Configuração da janela
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

janela = ctk.CTk()
janela.title("Meu Impacto Ambiental")
janela.geometry("500x700")

# Título
titulo = ctk.CTkLabel(janela, text="Calculadora de Sustentabilidade", 
                     font=("Arial", 20, "bold"))
titulo.pack(pady=20)

# Frame dos inputs
frame_inputs = ctk.CTkFrame(janela)
frame_inputs.pack(pady=10, padx=20, fill="x")

# Consumos
ent_agua = ctk.CTkEntry(frame_inputs, placeholder_text="Litros de água consumidos")
ent_agua.pack(pady=5, fill="x")

ent_energia = ctk.CTkEntry(frame_inputs, placeholder_text="Energia (kWh) consumida")
ent_energia.pack(pady=5, fill="x")

ent_residuos = ctk.CTkEntry(frame_inputs, placeholder_text="Resíduos não reciclados (kg)")
ent_residuos.pack(pady=5, fill="x")

ent_reciclados = ctk.CTkEntry(frame_inputs, placeholder_text="Resíduos reciclados (kg)")
ent_reciclados.pack(pady=5, fill="x")

# Frame dos transportes
frame_transportes = ctk.CTkFrame(janela)
frame_transportes.pack(pady=10, padx=20, fill="x")

ctk.CTkLabel(frame_transportes, text="Transportes usados hoje:").pack(anchor="w")

var_publico = ctk.BooleanVar()
cb_publico = ctk.CTkCheckBox(frame_transportes, text="Transporte público", variable=var_publico)
cb_publico.pack(anchor="w", pady=2)

var_bike = ctk.BooleanVar()
cb_bike = ctk.CTkCheckBox(frame_transportes, text="Bicicleta", variable=var_bike)
cb_bike.pack(anchor="w", pady=2)

var_carro = ctk.BooleanVar()
cb_carro = ctk.CTkCheckBox(frame_transportes, text="Carro (gasolina/diesel)", variable=var_carro)
cb_carro.pack(anchor="w", pady=2)

var_eletrico = ctk.BooleanVar()
cb_eletrico = ctk.CTkCheckBox(frame_transportes, text="Carro elétrico", variable=var_eletrico)
cb_eletrico.pack(anchor="w", pady=2)

# Botão calcular
btn_calcular = ctk.CTkButton(janela, text="CALCULAR IMPACTO", command=calcular, 
                            font=("Arial", 14, "bold"), height=40)
btn_calcular.pack(pady=20, padx=20, fill="x")

# Área de resultados
texto_resultado = ctk.CTkTextbox(janela, height=150, font=("Arial", 14))
texto_resultado.pack(pady=10, padx=20, fill="x")
texto_resultado.insert("1.0", "Preencha os dados e clique em calcular...")
texto_resultado.configure(state="disabled")

janela.mainloop()