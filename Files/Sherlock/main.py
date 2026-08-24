import os
import sys
import subprocess

# Configurazione ambiente e colori ANSI
if os.name == 'nt':
    os.system("title Sherlock - Remodel By Rezhu")
    os.system("") 

sys.stdout.reconfigure(encoding='utf-8')

def banner():
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
            print("  - sherlock <username> : Avvia la ricerca OSINT sui social")
            print("  - esci                : Chiude l'applicazione")
            input("\nPremi INVIO per tornare al menu...")
            continue

        if comando_base == "sherlock":
            if len(parti) < 2:
                print(f"\n\033[91m[ERRORE] Devi specificare un nickname! Es: sherlock nomeutente\033[0m")
                input("\nPremi INVIO per riprovare...")
                continue
            
            argomenti = parti[1:]
            print(f"\n\033[92m[OSINT] Avvio della ricerca per l'utente: {argomenti[0]}...\033[0m\n")
            
            try:
                # Richiama il modulo ufficiale di Sherlock posizionandoti nella cartella radice corretta
                cartella_principale = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                subprocess.run(["python", "-m", "sherlock"] + argomenti, cwd=cartella_principale, check=False)
            except Exception as e:
                print(f"\033[91mErrore durante l'esecuzione del core di Sherlock: {e}\033[0m")
                
            input("\nScansione completata. Premi INVIO per tornare al menu...")
        else:
            print(f"\n\033[91mComando sconosciuto. Digita 'sherlock <nome>' o 'aiuto'.\033[0m")
            input("\nPremi INVIO per tornare al menu...")

if __name__ == "__main__":
    main()
