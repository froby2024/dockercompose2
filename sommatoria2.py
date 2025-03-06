# programma che calcola la somma dei numeri interi a partire da 1 fino ad un valore massimo n
# con la condizione che tale somma non superi il valore 1000.
# 1 + 2 + 3 + 4 + ... + n <1000 e 1 + 2 + 3 + 4 + ... + (n+1) >= 1000
# Importazione del modulo Python Flask
from flask import Flask


# Il costruttore di Flask utilizza il nome del modulo corrente
app = Flask(__name__)


# La funzione route() è un decorator,
# Lega un URL a una funzione associata
@app.route('/')
def sommatoria():
    testo="Sommatoria s dei numeri naturali fino a n, con s<1000\n"

    # primo numero naturale
    n = 0
    # variabile per la sommatoria
    s = 0

    # continua a sommare i numeri naturali consecutivi mentre s è minore di 1000
    while s<1000:
        n += 1
        s += n
        testo=testo+ "n ="+str(n)+ "\ts ="+ str(s)+ "\n"

    # quando esce dal ciclo while il valore 1000 è stato raggiunto o superato
    # quindi sottraggo da s l'ultimo n sommato e diminuisco n di 1
    s -= n
    n -= 1

    testo=testo+ "Il risultato richiesto è:\n"
    testo=testo+ "n ="+str(n)
    testo=testo+ "s ="+str(s)
    return testo


# Se il file viene eseguito direttamente
# Eseguire l'applicazione Flask
if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')