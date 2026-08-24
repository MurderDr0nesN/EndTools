import os
import sys

# Compatibilità per i colori ANSI su Windows/PowerShell
if os.name == 'nt':
    os.system("title Sherlock - Remodel By Rezhu")
    os.system("") # Attiva il Virtual Terminal del prompt

# Forza la codifica UTF-8 per non corrompere i simboli del banner
sys.stdout.reconfigure(encoding='utf-8')

def banner():
    """Stampa il banner con la sfumatura verde fluida."""
    v1 = "\033[92m"          # Verde chiaro
    v2 = "\033[32m"          # Verde standard
    v3 = "\033[38;5;34m"     # Verde medio
    v4 = "\033[38;5;28m"     # Verde scuro
    v5 = "\033[38;2;0;48;0m" # Vero Verde Scurissimo RGB
    reset = "\033[0m"

    print("\n")
    print(f"          {v1}▄▄▄▄▄▄▄ ▄▄                ▄▄                    ")
    print(f"          {v2}█████▀▀▀ ██                ██             ▄▄     ")
    print(f"          {v3}  ▀████▄  ████▄ ▄█▀▄▄ ████▄ ██ ▄███▄ ▄████ ██ ▄█▀ ")
    print(f"          {v4}   ▀████ ██ ██ ██▄█▀ ██ ▀▀ ██ ██ ██ ██    ████   ")
    print(f"          {v5} ███████▀ ██ ██ ▀█▄▄▄ ██    ██ ▀███▀ ▀████ ██ ▀█▄ ")
    print(f"{reset}\n")

def main():
    while True:
        # Pulisce lo schermo ad ogni ciclo
        os.system('cls' if os.name == 'nt' else 'clear')
        banner()

        verde_chiaro = "\033[92m"
        reset = "\033[0m"
        
        # Prompt interattivo personalizzato
        comando = input(f"          {verde_chiaro}sherlock > {reset}").strip()

        if comando.lower() in ["exit", "esci"]:
            print("\nChiusura in corso...")
            break

        if comando.lower() == "aiuto":
            print(f"\n{verde_chiaro}[INFO]{reset} Comandi disponibili:")
            print("  - aiuto : Mostra questo messaggio")
            print("  - esci  : Chiude l'applicazione")
            input("\nPremi INVIO per tornare al menu...")
        elif comando != "":
            print(f"\nComando '{comando}' ricevuto (Funzione in sviluppo).")
            input("\nPremi INVIO per tornare al menu...")

if __name__ == "__main__":
    main()
