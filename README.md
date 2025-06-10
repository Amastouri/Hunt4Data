# Hunt4Data 🔍

**Hunt4Data** est un outil open source développé pour scanner les fichiers à la recherche de données sensibles pouvant fuiter accidentellement dans un SI, un dépôt GitHub ou un environnement local.

## 🎯 Objectif

Identifier rapidement :
- Mots de passe en clair
- Clés API (AWS, Google…)
- Emails professionnels
- Cartes bancaires (Visa, Mastercard)
- Tokens JWT
- IPs sensibles
- Fichiers PDF et .env à risque

## 🛠️ Fonctionnalités

- Parcours récursif de répertoires
- Détection via expressions régulières
- Lecture de fichiers `.txt`, `.log`, `.env`, `.json`, `.md`, **et `.pdf`**
- Génération d’un fichier de rapport `.txt` avec les résultats

## 🚀 Utilisation

1. Placez vos fichiers dans un dossier (ex : `Dossier-DS`)
2. Lancez le script :

```bash
python hunt4data.py
```

3. Lisez les résultats dans `rapport_donnees_sensibles.txt`

## 📦 Dépendances

```bash
pip install PyPDF2
```

⚠️ **Utilisez Python 3.10 pour assurer la compatibilité avec PyPDF2**  
(Les versions plus récentes peuvent poser problème pour cette librairie)

## 🧪 Exemple de détection

```
[Email] Dossier-DS/credentials.env (ligne 3) : dev@cyberlab.com
[Clé AWS] Dossier-DS/credentials.env (ligne 4) : AKIAIOSFODNN7EXAMPLE
```

## 👤 Auteur

Projet personnel réalisé par Amine Mastouri, étudiant en cybersécurité, pour s’exercer à la détection d’informations sensibles et renforcer la posture sécurité des environnements de test.

---

**#cybersecurite #infosec #audit #devsecops #dataloss #alternance #Hunt4Data**# Hunt4Data
