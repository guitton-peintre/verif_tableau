## 🧭 Objectif

Ce dépôt contient **une clé publique officielle** (`ecc_public_key.pem`).  
Elle permet à **n’importe qui** de **vérifier l’authenticité d’un tableau** par Guitton Francois.

> 💡 En résumé : cette clé permet de **vérifier une signature**, mais **pas de signer ni de modifier** quoi que ce soit.

---

## 🔍 À quoi sert cette clé publique ?

Chaque tableau ou certificat numérique créé par **Guitton François** est accompagné d’un **fichier de signature** (par exemple `mon_tableau.sig`) qui prouve son authenticité.

- 🖼️ Le tableau (ou son fichier numérique) → `mon_tableau.jpg`
- ✍️ La signature numérique → `mon_tableau.sig`
- 🔑 La clé publique (fournie ici) → `ecc_public_key.pem`

Grâce à cette clé publique, vous pouvez **vérifier que la signature correspond bien au tableau**.

---

## 🧰 Ce qu’il vous faut

- **Python 3.8 ou plus**
- Le module Python [`cryptography`](https://pypi.org/project/cryptography/)

### Installation (une seule fois) :
```bash
pip install cryptography
