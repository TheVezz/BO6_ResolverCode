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

# Variabili globali per i valori scelti
X_val = None
Y_val = None
Z_val = None
simboli_rimanenti = list(valori_simboli.keys())
immagini = {}

# Funzione per caricare le immagini
def carica_immagine(nome_file):
    if hasattr(sys, '_MEIPASS'):
        percorso = os.path.join(sys._MEIPASS, 'img', nome_file)
    else:
        percorso = os.path.join('img', nome_file)

    try:
        img = Image.open(percorso).resize((60, 60))
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Errore nel caricamento dell'immagine {nome_file}: {e}")
        return None

# Funzione per aggiornare la GUI a ogni selezione di variabile
def aggiorna_gui(variabile):
    global immagini

    # Carica le immagini solo la prima volta
    if not immagini:
        for simbolo in simboli_rimanenti:
            immagini[simbolo] = carica_immagine(f"{simbolo}.png")

    frame_simboli.pack_forget()
    frame_risultati.pack_forget()

    for widget in frame_simboli.winfo_children():
        widget.destroy()

    label.config(text=f"Seleziona il valore di {variabile}")

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

    frame_simboli.pack(pady=10)

# Funzione per selezionare la lettera (X, Y, Z)
def seleziona_lettera(lettera):
    aggiorna_gui(lettera)

# Funzione per gestire la selezione dei valori
def seleziona_valore(valore, simbolo, variabile):
    global X_val, Y_val, Z_val
    simbolo_button = None

    # Aggiorna il valore e disabilita il pulsante corrispondente
    if variabile == "X":
        X_val = valore
        simboli_rimanenti.remove(simbolo)
        simbolo_button = btn_x
        simbolo_button.config(state="disabled", text=f"X={X_val}")  # Cambia il testo del pulsante X
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
        simboli_rimanenti.remove(simbolo)
        simbolo_button = btn_y
        simbolo_button.config(state="disabled", text=f"Y={Y_val}")  # Cambia il testo del pulsante Y
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
        simboli_rimanenti.remove(simbolo)
        simbolo_button = btn_z
        simbolo_button.config(state="disabled", text=f"Z={Z_val}")  # Cambia il testo del pulsante Z
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

    result_text.set(f"{risultato1} | {risultato2} | {risultato3}")

    frame_risultati.pack(pady=10)
    frame_simboli.pack_forget()
    label.pack_forget()

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
    label.pack()
    # Riabilita i pulsanti X, Y, Z
    btn_x.config(state=tk.NORMAL, text="X")
    btn_y.config(state=tk.NORMAL, text="Y")
    btn_z.config(state=tk.NORMAL, text="Z")
    aggiorna_gui("X")

# Creazione della finestra principale
root = tk.Tk()
root.title("BO6 Terminus Tool for Code DRI-11")
root.geometry("700x450")
root.resizable(False, False)
root.configure(bg="#333333")

# Carica le immagini
for icon in simboli_rimanenti:
    immagini[icon] = carica_immagine(f"{icon}.png")

# Intestazione
header = tk.Label(root, text="BO6 Terminus Tool for Code DRI-11", font=("Helvetica", 16, "bold"), bg="#333333", fg="white")
header.pack(pady=20)

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
    width=10
)
btn_x.grid(row=0, column=0)

btn_y = tk.Button(
    frame_lettere,
    text="Y",
    command=lambda: seleziona_lettera("Y"),
    bg="#444444",
    fg="white",
    activebackground="#555555",
    width=10
)
btn_y.grid(row=0, column=1)

btn_z = tk.Button(
    frame_lettere,
    text="Z",
    command=lambda: seleziona_lettera("Z"),
    bg="#444444",
    fg="white",
    activebackground="#555555",
    width=10
)
btn_z.grid(row=0, column=2)

# Label per guidare la selezione
label = tk.Label(root, text="Seleziona il valore di X", font=("Helvetica", 12), bg="#333333", fg="white")
label.pack()

# Frame per i simboli
frame_simboli = tk.Frame(root, bg="#333333")
frame_simboli.pack(pady=10)

# Frame per visualizzare i risultati
frame_risultati = tk.Frame(root, bg="#333333")

# Colonna di Risultati
result_text = tk.StringVar()
result_label = tk.Label(frame_risultati, textvariable=result_text, font=("Helvetica", 24, "bold"), fg="orange", bg="#444444", padx=15, pady=10, anchor="center", justify="center")
result_label.pack(pady=10)

# Riduce lo spazio bianco tra i pulsanti e li allinea
frame_lettere.grid_columnconfigure(0, weight=1)
frame_lettere.grid_columnconfigure(1, weight=1)
frame_lettere.grid_columnconfigure(2, weight=1)

# Pulsante di reset
reset_button = tk.Button(root, text="Reset", command=reset, bg="#888888", fg="black", activebackground="#999999", width=10)
reset_button.pack(pady=20)

# Avvio dell'interfaccia grafica
reset()  # Chiamata alla funzione reset per iniziare
root.mainloop()
