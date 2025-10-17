# 🔓 Extraction de clé publique ECC à partir d'une clé privée chiffrée

Ce script Python (`public.py`) permet d’extraire une **clé publique ECC** à partir d’une **clé privée chiffrée** au format PEM.  
Il s’appuie sur la bibliothèque [`cryptography`](https://cryptography.io/en/latest/) pour assurer la sécurité et la compatibilité avec les formats standards X.509.

---

## 📋 Fonctionnalités

- Lit une **clé privée ECC chiffrée** (`ecc_private_key.pem`).
- Demande à l’utilisateur le **mot de passe** pour la déchiffrer.
- Extrait et sauvegarde la **clé publique** au format PEM (`ecc_public_key.pem`).
- Compatible avec les clés générées via `cryptography` (ex. script `generate_cert.py`).

---

## Prérequis

- **Python 3.8** ou supérieur
- Le module [`cryptography`](https://pypi.org/project/cryptography/)

