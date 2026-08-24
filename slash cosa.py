import os
import subprocess

def main():
    # 1. Percorso della cartella target
    percorso_cartella = r"C:\ToolDOX\Prova-EndTools\Files\slash-main\slash-main"
    
    # 2. FIX: Usiamo 'python' invece di 'bash' per avviare il file .py
    comando_powershell = "python Slash.py"
    
    print(f"[Automation] Apertura di PowerShell nella cartella: {percorso_cartella}")
    print(f"[Automation] Esecuzione del comando: {comando_powershell}\n")
    
    try:
        # Avviamo il processo PowerShell
        subprocess.run(
            ["powershell.exe", "-NoExit", "-Command", comando_powershell],
            cwd=percorso_cartella,
            check=True
        )
    except Exception as e:
        print(f"Errore durante l'automazione: {e}")
        input("\nPremi INVIO per chiudere...")

if __name__ == "__main__":
    main()
