import os
import re
import PyPDF2

# Répertoire à scanner { "." = pour scanner les fichiers sur le meme repertoire } { "/Dossier" = pour scanner les fichiers sur le dossier choisi }
REPERTOIRE = "."

# Extensions de fichiers possibles à scanner
EXTENSIONS_CIBLES = [".txt", ".log", ".env", ".md", ".json", ".pdf"]

# Patterns regex pour données sensibles
PATTERNS = {
    "Carte bancaire (Visa/Mastercard)": r"\b(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14})\b",
    "Email": r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",
    "Clé AWS": r"AKIA[0-9A-Z]{16}",
    "Mot de passe (mot-clé)": r"(motdepasse|mdp|password)[\s:=]+[\w@#$%^&*]+",
    "Adresse IP": r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
    "Token JWT": r"eyJ[a-zA-Z0-9_-]+\.[a-zA-Z0-9_-]+\.[a-zA-Z0-9_-]+",
    "Clé API Google": r"AIza[0-9A-Za-z\-_]{35}"
}

# Résultats du scan
resultats = []

# Parcours du dossier
for dossier, _, fichiers in os.walk(REPERTOIRE):
    for fichier in fichiers:
        chemin_complet = os.path.join(dossier, fichier)
        if any(fichier.endswith(ext) for ext in EXTENSIONS_CIBLES):
            if fichier.endswith(".pdf"):
                try:
                    with open(chemin_complet, "rb") as pdf_file:
                        reader = PyPDF2.PdfReader(pdf_file)
                        for page_num, page in enumerate(reader.pages):
                            texte = page.extract_text() or ""
                            for num_ligne, ligne in enumerate(texte.split("\n"), 1):
                                for type_data, pattern in PATTERNS.items():
                                    for match in re.findall(pattern, ligne):
                                        resultats.append({
                                            "fichier": chemin_complet,
                                            "ligne": f"Page {page_num + 1}, ligne {num_ligne}",
                                            "type": type_data,
                                            "valeur": match.strip()
                                        })
                except Exception as e:
                    print(f"[!] Erreur lecture PDF {chemin_complet} : {e}")
                continue

            # Pour les fichiers texte
            try:
                with open(chemin_complet, "r", encoding="utf-8", errors="ignore") as f:
                    lignes = f.readlines()
                    for num_ligne, ligne in enumerate(lignes, 1):
                        for type_data, pattern in PATTERNS.items():
                            for match in re.findall(pattern, ligne):
                                resultats.append({
                                    "fichier": chemin_complet,
                                    "ligne": num_ligne,
                                    "type": type_data,
                                    "valeur": match.strip()
                                })
            except Exception as e:
                print(f"[!] Erreur lecture fichier {chemin_complet} : {e}")

# Affichage + export
if resultats:
    with open("rapport_donnees_sensibles.txt", "w", encoding="utf-8") as rapport:
        for r in resultats:
            ligne = f"[{r['type']}] {r['fichier']} (ligne {r['ligne']}) : {r['valeur']}"
            print(ligne)
            rapport.write(ligne + "\n")
    print(f"\n✔ Hunt4Data a généré un rapport : rapport_donnees_sensibles.txt ({len(resultats)} alertes)")
else:
    print("✅ Hunt4Data n'as trouvé aucun élément sensible détecté.")