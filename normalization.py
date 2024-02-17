import numpy as np

# Esempio di normalizzazione dati tramite tecnica standardizzazione

# Dati di esempio
altezze = np.array([160, 170, 180, 190, 200])  # Altezze in centimetri
pesi = np.array([60, 70, 80, 90, 100])         # Pesi in chilogrammi

# Standardizzazione delle variabili
altezze_normalizzate = (altezze - altezze.mean()) / altezze.std()
pesi_normalizzati = (pesi - pesi.mean()) / pesi.std()

print("Altezze normalizzate:", altezze_normalizzate)
print("Pesi normalizzati:", pesi_normalizzati)


# Esempio di normalizzazione dati tramite tecnica normalizzazione
# Dati di esempio
altezze = np.array([160, 170, 180, 190, 200])  # Altezze in centimetri
pesi = np.array([60, 70, 80, 90, 100])         # Pesi in chilogrammi

# Normalizzazione min-max delle variabili
altezze_normalizzate = (altezze - altezze.min()) / (altezze.max() - altezze.min())
pesi_normalizzati = (pesi - pesi.min()) / (pesi.max() - pesi.min())

print("Altezze normalizzate:", altezze_normalizzate)
print("Pesi normalizzati:", pesi_normalizzati)

