import math
import tkinter as tk
from tkinter import ttk, messagebox


def calculate():
    try:
        speed = float(entry_speed.get())
        rate = float(entry_rate.get())
        unit = combo_unit.get()

        if rate <= 0 or speed <= 0:
            messagebox.showerror(
                "Σφάλμα", "Οι τιμές πρέπει να είναι θετικοί αριθμοί."
            )
            return

        # Μετατροπή ταχύτητας σε m/s
        if unit == "Knots":
            v_ms = speed * 0.514444
        else:  # km/h
            v_ms = speed / 3.6

        # Μετατροπή ρυθμού στροφής σε rad/s
        omega = math.radians(rate)

        # Υπολογισμοί
        radius_m = v_ms / omega
        diameter_m = 2 * radius_m

        radius_nm = radius_m / 1852
        diameter_nm = diameter_m / 1852

        # Ενημέρωση αποτελεσμάτων
        lbl_radius.config(
            text=f"Ακτίνα (R): {radius_m:.2f} m  ({radius_nm:.3f} NM)"
        )
        lbl_diameter.config(
            text=f"Διάμετρος (D): {diameter_m:.2f} m  ({diameter_nm:.3f} NM)"
        )

    except ValueError:
        messagebox.showerror(
            "Σφάλμα Εισαγωγής", "Παρακαλώ εισάγετε έγκυρους αριθμούς."
        )


# Δημιουργία κεντρικού παραθύρου
root = tk.Tk()
root.title("Υπολογιστής Κύκλου Στροφής")
root.geometry("400x300")
root.resizable(False, False)

# Διάταξη (Padding)
frame = ttk.Frame(root, padding="20")
frame.pack(fill=tk.BOTH, expand=True)

# Εισαγωγή Ταχύτητας
ttk.Label(frame, text="Ταχύτητα:").grid(
    row=0, column=0, sticky=tk.W, pady=5
)
entry_speed = ttk.Entry(frame, width=12)
entry_speed.grid(row=0, column=1, pady=5)

combo_unit = ttk.Combobox(
    frame, values=["Knots", "km/h"], width=8, state="readonly"
)
combo_unit.current(0)
combo_unit.grid(row=0, column=2, padx=5, pady=5)

# Εισαγωγή Ρυθμού Στροφής
ttk.Label(frame, text="Ρυθμός Στροφής (°/sec):").grid(
    row=1, column=0, sticky=tk.W, pady=5
)
entry_rate = ttk.Entry(frame, width=12)
entry_rate.grid(row=1, column=1, pady=5)

# Κουμπί Υπολογισμού
btn_calc = ttk.Button(
    frame, text="Υπολογισμός", command=calculate
)
btn_calc.grid(row=2, column=0, columnspan=3, pady=15)

# Περιοχή Αποτελεσμάτων
lbl_radius = ttk.Label(
    frame, text="Ακτίνα (R): -", font=("Helvetica", 10, "bold")
)
lbl_radius.grid(row=3, column=0, columnspan=3, sticky=tk.W, pady=5)

lbl_diameter = ttk.Label(
    frame, text="Διάμετρος (D): -", font=("Helvetica", 10, "bold")
)
lbl_diameter.grid(row=4, column=0, columnspan=3, sticky=tk.W, pady=5)

# Εκτέλεση εφαρμογής
root.mainloop()