import os
import sys
import tkinter as tk
from PIL import Image, ImageTk

# Dizionario dei valori per ciascun simbolo
valori_simboli = {
    "icon1": 0,
    "icon2": 10,
    "icon3": 11,
    "icon4": 20,
    "icon5": 21,
    "icon6": 22
}

bottoni_simboli = {}
simboli_disabilitati = []
storico = []

# Dizionario per le immagini di sfondo
sfondo_pulsanti = {
    "X": None,
    "Y": None,
    "Z": None
}

# Variabili globali per i valori scelti
X_val = None
Y_val = None
Z_val = None
simboli_rimanenti = list(valori_simboli.keys())
immagini = {}

# Funzione per caricare le immagini
def carica_immagine(nome_file, dimensione=(60, 60)):
    if hasattr(sys, '_MEIPASS'):
        percorso = os.path.join(sys._MEIPASS, 'img', nome_file)
    else:
        percorso = os.path.join('img', nome_file)

    try:
        # Ridimensiona l'immagine con le dimensioni specificate
        img = Image.open(percorso).resize(dimensione)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Error loading image {nome_file}: {e}")
        return None

# Funzione per aggiornare la GUI a ogni selezione di variabile
def aggiorna_gui(variabile):
    global immagini

    # Carica le immagini solo la prima volta
    if not immagini:
            immagini[simbolo] = carica_immagine(f"{simbolo}.png")

    frame_simboli.pack_forget()
    frame_risultati.pack_forget()

    for widget in frame_simboli.winfo_children():
        widget.destroy()
    
    # Imposta il colore di sfondo dei pulsanti in base alla variabile corrente
    btn_x.config(bg="#1D8348" if variabile == "X" else "#444444")
    btn_y.config(bg="#1D8348" if variabile == "Y" else "#444444")
    btn_z.config(bg="#1D8348" if variabile == "Z" else "#444444")

    for simbolo in simboli_rimanenti:
        img = immagini[simbolo]
        valore = valori_simboli[simbolo]
        btn = tk.Button(
            frame_simboli,
            image=img,
            command=lambda v=valore, s=simbolo: seleziona_valore(v, s, variabile),
            bg="#444444",
            fg="white",
            activebackground="#555555"
        )
        btn.pack(side="left", padx=10, pady=10)
        bottoni_simboli[simbolo] = btn

        # Controlla se il simbolo deve essere disabilitato
        if simbolo in simboli_disabilitati:  # Lista dei simboli disabilitati
            # Mostra solo il simbolo specifico che è stato disabilitato
            indice_storico = simboli_disabilitati.index(simbolo)
            bottoni_simboli[simbolo].config(
                state="disabled",
                fg="white",
                compound='top',
                text=storico[indice_storico].upper()  # Mostra solo il simbolo specifico
    )

    frame_simboli.pack(pady=10)

    if X_val is None and Y_val is None and Z_val is None:
            back_button.config(state=tk.DISABLED)
            reset_button.config(state=tk.DISABLED)

# Funzione per selezionare la lettera (X, Y, Z)
def seleziona_lettera(lettera):
    aggiorna_gui(lettera)

def seleziona_valore(valore, simbolo, variabile):
    global X_val, Y_val, Z_val
    simbolo_button = None

    # Aggiorna il valore e disabilita il pulsante corrispondente
    if variabile == "X":
        X_val = valore
        
        # abilitazione pulsanti indietro e reset
        back_button.config(state=tk.NORMAL)
        reset_button.config(state=tk.NORMAL)

        # simboli_rimanenti.remove(simbolo)
        bottoni_simboli[simbolo].config(state="disabled", text=variabile, fg="white", compound='top')
        simboli_disabilitati.append(simbolo)
        storico.append(variabile)

        simbolo_button = btn_x
        # simbolo_button.config(state="disabled", text=f"X={X_val}")  # Cambia il testo del pulsante X
        simbolo_button.config(state="disabled")
        
        
        if Y_val is None and Z_val is None:  # Passa a Y se non sono selezionati
            aggiorna_gui("Y")
        elif Y_val is None:  # Passa a Y se solo Y non è selezionato
            aggiorna_gui("Y")
        elif Z_val is None:  # Passa a Z se solo Z non è selezionato
            aggiorna_gui("Z")
        elif Y_val is not None and Z_val is not None:  # Se X, Y e Z sono già selezionati
            calcola_risultati()
        

    elif variabile == "Y":
        Y_val = valore

        # abilitazione pulsanti indietro e reset
        back_button.config(state=tk.NORMAL)
        reset_button.config(state=tk.NORMAL)

        # simboli_rimanenti.remove(simbolo)
        bottoni_simboli[simbolo].config(state="disabled", text=variabile, fg="white", compound='top')
        simboli_disabilitati.append(simbolo)
        storico.append(variabile)

        simbolo_button = btn_y
        # simbolo_button.config(state="disabled", text=f"Y={Y_val}")  # Cambia il testo del pulsante Y
        simbolo_button.config(state="disabled")
        
        
        if X_val is None and Z_val is None:  # Passa a X se non sono selezionati
            aggiorna_gui("X")
        elif X_val is None:  # Passa a X se solo X non è selezionato
            aggiorna_gui("X")
        elif Z_val is None:  # Passa a Z se solo Z non è selezionato
            aggiorna_gui("Z")
        elif X_val is not None and Z_val is not None:  # Se X, Y e Z sono già selezionati
            calcola_risultati()
        

    elif variabile == "Z":
        Z_val = valore

        # abilitazione pulsanti indietro e reset
        back_button.config(state=tk.NORMAL)
        reset_button.config(state=tk.NORMAL)

        # simboli_rimanenti.remove(simbolo)
        bottoni_simboli[simbolo].config(state="disabled", text=variabile, fg="white", compound='top')
        simboli_disabilitati.append(simbolo)
        storico.append(variabile)

        simbolo_button = btn_z
        # simbolo_button.config(state="disabled", text=f"Z={Z_val}")  # Cambia il testo del pulsante Z
        simbolo_button.config(state="disabled")
        
        
        if X_val is None and Y_val is None:  # Passa a X se non sono selezionati
            aggiorna_gui("X")
        elif X_val is None:  # Passa a X se solo X non è selezionato
            aggiorna_gui("X")
        elif Y_val is None:  # Passa a Y se solo Y non è selezionato
            aggiorna_gui("Y")
        elif X_val is not None and Y_val is not None:  # Se X, Y e Z sono già selezionati
            calcola_risultati()
        

    # Disabilita il pulsante corrispondente
    if simbolo_button:
        simbolo_button.config(state="disabled")

# Funzione per calcolare e mostrare i risultati
def calcola_risultati():
    risultato1 = 2 * X_val + 11
    risultato2 = (2 * Z_val + Y_val) - 5
    risultato3 = (Y_val + Z_val) - X_val

    result_text.set(f"{risultato1}   {risultato2}   {risultato3}")

    frame_risultati.pack(pady=10)
    frame_lettere.pack_forget()

    # Rimuovi solo i pulsanti attivi (non disabilitati)
    for simbolo in list(bottoni_simboli.keys()):  # Itera su una copia delle chiavi
        # Ridimensiona l'immagine prima di distruggere il pulsante
        img = carica_immagine(f"{simbolo}.png", dimensione=(32, 32))  # Carica l'immagine del simbolo
        if img:  # Controlla se l'immagine è stata caricata correttamente
                bottoni_simboli[simbolo].config(image=img, width=32, height=40)  # Ridimensiona il pulsante e imposta l'immagine
                bottoni_simboli[simbolo].image = img  # Salva una referenza all'immagine
        if simbolo not in simboli_disabilitati:
            # Rimuovi il pulsante attivo
            bottoni_simboli[simbolo].destroy()  
            del bottoni_simboli[simbolo]  # Elimina il pulsante dalla lista dei bottoni

    # Imposta il colore di sfondo dei pulsanti in base alla variabile corrente
    btn_x.config(bg="#444444")
    btn_y.config(bg="#444444")
    btn_z.config(bg="#444444")

# Funzione di reset
def reset():
    global X_val, Y_val, Z_val, simboli_rimanenti
    X_val = None
    Y_val = None
    Z_val = None
    simboli_rimanenti = list(valori_simboli.keys())
     # Riabilita i pulsanti
    result_text.set("")
    frame_risultati.pack_forget()
    # Riabilita i pulsanti X, Y, Z
    btn_x.config(state=tk.NORMAL, text="X")
    btn_y.config(state=tk.NORMAL, text="Y")
    btn_z.config(state=tk.NORMAL, text="Z")
    simboli_disabilitati.clear()
    storico.clear()
    frame_lettere.pack(pady=10)
    back_button.config(state=tk.DISABLED)
    aggiorna_gui("X")

# Funzione Indietro
def back():
    global X_val, Y_val, Z_val
    ultima_variabile = storico[-1].upper()
    # Trova il simbolo corrispondente alla variabile
    simbolo_corrispondente = None
    for simbolo, btn in bottoni_simboli.items():
        if btn['text'].upper() == ultima_variabile:
            simbolo_corrispondente = simbolo
            break

    if simbolo_corrispondente:
        # Riabilita il frame lettere
        frame_lettere.pack(pady=10)
        # Riabilita il pulsante corrispondente
        bottoni_simboli[simbolo_corrispondente].config(state=tk.NORMAL)

        # Rimuovi il simbolo dai disabilitati
        if simbolo_corrispondente in simboli_disabilitati:
            simboli_disabilitati.remove(simbolo_corrispondente)

        # Cancella il valore dai risultati
        risultato1 = None
        risultato2 = None
        risultato3 = None
        frame_risultati.pack_forget()

        if ultima_variabile == "X": 
            X_val = None
            btn_x.config(state=tk.NORMAL)
        if ultima_variabile == "Y": 
            Y_val = None
            btn_y.config(state=tk.NORMAL)
        if ultima_variabile == "Z": 
            Z_val = None
            btn_z.config(state=tk.NORMAL)

        # Aggiorna la GUI
        aggiorna_gui(ultima_variabile)

        # Rimuovi l'ultimo elemento dallo storico
        storico.pop()

# Creazione della finestra principale
root = tk.Tk()
root.title("BO6 Terminus Tool for Code DRI-11")
root.geometry("550x350")
root.resizable(False, False)
root.configure(bg="#333333")

# Carica le immagini
for icon in simboli_rimanenti:
    immagini[icon] = carica_immagine(f"{icon}.png")

# Intestazione
header = tk.Label(root, text="BO6 Terminus Tool for Code DRI-11", font=("Helvetica", 16, "bold"), bg="#333333", fg="white")
header.pack(pady=10)

# Frame per i pulsanti X, Y, Z
frame_lettere = tk.Frame(root, bg="#444444")  # Imposta lo sfondo del frame per uniformità
frame_lettere.pack(pady=10)

# Pulsanti per selezionare le lettere X, Y, Z, senza spazio aggiuntivo
btn_x = tk.Button(
    frame_lettere,
    text="X",
    command=lambda: seleziona_lettera("X"),
    bg="#444444",
    fg="white",
    activebackground="#555555",
    width=20
)
btn_x.grid(row=0, column=0)

btn_y = tk.Button(
    frame_lettere,
    text="Y",
    command=lambda: seleziona_lettera("Y"),
    bg="#444444",
    fg="white",
    activebackground="#555555",
    width=20
)
btn_y.grid(row=0, column=1)

btn_z = tk.Button(
    frame_lettere,
    text="Z",
    command=lambda: seleziona_lettera("Z"),
    bg="#444444",
    fg="white",
    activebackground="#555555",
    width=20
)
btn_z.grid(row=0, column=2)

# Frame per i simboli
frame_simboli = tk.Frame(root, bg="#333333")
frame_simboli.pack(pady=10)

# Frame per visualizzare i risultati
frame_risultati = tk.Frame(root, bg="#333333")

# Colonna di Risultati
result_text = tk.StringVar()
result_label = tk.Label(frame_risultati, textvariable=result_text, font=("Helvetica", 28, "bold"), fg="orange", bg="#444444", padx=15, pady=10, anchor="center", justify="center")
result_label.pack(pady=1)

# Riduce lo spazio bianco tra i pulsanti e li allinea
frame_lettere.grid_columnconfigure(0, weight=1)
frame_lettere.grid_columnconfigure(1, weight=1)
frame_lettere.grid_columnconfigure(2, weight=1)

# Frame per i pulsanti e l'immagine
bottom_frame = tk.Frame(root, bg="#333333")
bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=2)  # Posiziona il frame in basso

# Pulsante Indietro
back_img = carica_immagine("back.png")
back_button = tk.Button(
    bottom_frame,
    image=back_img,
    command=back,
    bg="#333333",
    activebackground="#555555",
    borderwidth=0
)
back_button.pack(side=tk.LEFT, padx=10)  # Pulsante indietro a sinistra

# Immagine centrale
dri11_img = carica_immagine(f"dri11.png", dimensione=(300, 120))
dri11_label = tk.Label(bottom_frame, image=dri11_img, bg="#333333")
dri11_label.pack(side=tk.LEFT, padx=10)  # Immagine al centro

# Pulsante di reset
reset_img = carica_immagine("reset.png")
reset_button = tk.Button(
    bottom_frame,
    image=reset_img,
    command=reset,
    bg="#333333",
    activebackground="#555555",
    borderwidth=0
)
reset_button.pack(side=tk.LEFT, padx=10)  # Pulsante di reset a destra

# Centro il frame nella finestra principale
bottom_frame.update_idletasks()  # Assicurati che il frame abbia le dimensioni corrette
root_width = root.winfo_width()
frame_width = bottom_frame.winfo_width()

x_offset = (root_width - frame_width) // 2
bottom_frame.place(x=x_offset, rely=1.0, anchor='s')

# Avvio dell'interfaccia grafica
reset()  # Chiamata alla funzione reset per iniziare
root.mainloop()
