import os
import sys
import subprocess

# Configurazione ambiente e attivazione colori ANSI su Windows/PowerShell
if os.name == 'nt':
    os.system("title Sherlock - Remodel By Rezhu")
    os.system("") 

sys.stdout.reconfigure(encoding='utf-8')

def banner():
    """Stampa il banner con la tua bellissima sfumatura verde."""
    v1 = "\033[92m"          
    v2 = "\033[32m"          
    v3 = "\033[38;5;34m"     
    v4 = "\033[38;5;28m"     
    v5 = "\033[38;2;0;48;0m" 
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
        os.system('cls' if os.name == 'nt' else 'clear')
        banner()

        verde_chiaro = "\033[92m"
        reset = "\033[0m"
        
        # Riceve il comando dal prompt interattivo
        input_utente = input(f"          {verde_chiaro}sherlock > {reset}").strip()

        if not input_utente:
            continue

        parti = input_utente.split()
        comando_base = parti[0].lower()

        if comando_base in ["exit", "esci"]:
            print("\nChiusura del programma...")
            break

        if comando_base == "aiuto":
            print(f"\n{verde_chiaro}[INFO]{reset} Utilizzo del Remodel:")
            print("  - sherlock <username> : Avvia la ricerca OSINT del profilo")
            print("  - esci                : Chiude l'applicazione")
            input("\nPremi INVIO per tornare al menu...")
            continue

        # Se l'utente scrive "sherlock <nomeutente>"
        if comando_base == "sherlock":
            if len(parti) < 2:
                print(f"\n\033[91m[ERRORE] Devi specificare un nickname! Es: sherlock nomeutente\033[0m")
                input("\nPremi INVIO per riprovare...")
                continue
            
            # Prende il nickname ed eventuali parametri extra
            argomenti = parti[1:]
            print(f"\n\033[92m[OSINT] Richiamo del motore originale. Ricerca per: {argomenti}...\033[0m\n")
            
            try:
                # Modificato per richiamare il modulo globale di Windows installato con pip
                subprocess.run(["python", "-m", "sherlock_project"] + argomenti, check=False)
            except Exception as e:
                print(f"\033[91mErrore durante il lancio di Sherlock: {e}\033[0m")
                
            input("\nScansione completata. Premi INVIO per tornare al menu...")
        else:
            print(f"\n\033[91mComando sconosciuto. Digita 'sherlock <nome>' o 'aiuto'.\033[0m")
            input("\nPremi INVIO per tornare al menu...")

if __name__ == "__main__":
    main()
