# TP 2 : Application FastAPI Collaborative (DevOps)

Application de référence développée avec **FastAPI** dans le cadre du **TP 2 : Travail collaboratif avec GitLab**.

---

## 🛠️ Installation

1. **Cloner le projet** :
   ```bash
   git clone https://gitlab.com/bellajmohsen7/tp2-fastapi-team.git
   cd tp2-fastapi-team
   ```

2. **Créer et activer l'environnement virtuel** :
   - Sous Windows (PowerShell) :
     ```powershell
     py -m venv .venv
     .venv\Scripts\activate
     ```
   - Sous Linux / macOS :
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```

3. **Installer les dépendances** :
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Commande pour lancer l'application

Pour lancer l'application en mode développement avec rechargement automatique à chaud :

```bash
uvicorn main:app --reload
```
*(ou si uvicorn n'est pas dans le PATH global : `python -m uvicorn main:app --reload`)*

Le serveur démarre sur le port 8000 : **http://localhost:8000** (ou http://127.0.0.1:8000).

---

## 🧪 Comment tester l'application

### 1. Test direct dans le navigateur
- Ouvrez : [http://localhost:8000/](http://localhost:8000/)  
- **Réponse attendue** :
  ```json
  {
    "message": "it works !"
  }
  ```

### 2. Documentation interactive Swagger UI
FastAPI génère automatiquement la documentation interactive :
- Accédez à : [http://localhost:8000/docs](http://localhost:8000/docs)
- Cliquez sur l'endpoint `GET /` $\rightarrow$ **Try it out** $\rightarrow$ **Execute** pour tester la requête.

### 3. En ligne de commande
- Avec `curl` :
  ```bash
  curl http://localhost:8000/
  ```
- Avec PowerShell :
  ```powershell
  Invoke-RestMethod http://localhost:8000/
  ```
