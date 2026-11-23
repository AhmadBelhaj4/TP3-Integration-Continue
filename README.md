# TP3 - Intégration Continue (CI) avec GitLab CI & GitHub Actions

Ce projet étend l'API FastAPI du TP2 en implémentant un pipeline d'Intégration Continue automatisé.

## Nouvelles fonctionnalités
- Ajout de l'endpoint de soustraction (`GET /soustraction`).
- Mise en place d'une suite de tests unitaires automatisés avec `pytest`.
- Mesure et validation de la couverture de code avec `pytest-cov` (couverture atteinte > 90%).
- Contrôle strict de la qualité du code avec `pylint` (score cible 10/10).

## Commandes de test en local

### 1. Qualité du code
```powershell
pylint main.py --fail-under=10
```

### 2. Tests unitaires et rapport JUnit
```powershell
pytest -v --junitxml=report.xml
```

### 3. Couverture de code
```powershell
pytest -v test_main.py --cov=main --cov-report term-missing --cov-report xml:coverage.xml --cov-report html --cov-fail-under=90
```

## Pipelines d'Intégration Continue (CI)
Le pipeline s'exécute automatiquement lors des pushs et des Pull / Merge Requests :

1. **Stage `code_quality` / Job `pylint`** :
   - Analyse le code source `main.py` avec `pylint`.
   - Échoue si le score est inférieur à 10.00/10.

2. **Stage `test` / Job `run-test`** :
   - Exécute l'ensemble des tests unitaires avec `pytest`.
   - Produit le rapport de test JUnit XML (`report.xml`) archivé comme artefact.

3. **Stage `test` / Job `calculate-coverage`** :
   - Calcule le pourcentage de couverture de code (atteignant 95%).
   - Échoue si la couverture passe sous le seuil de 90%.
   - Génère et conserve le rapport XML Cobertura (`coverage.xml`) et le rapport HTML (`htmlcov/`).

Les configurations sont disponibles dans :
- `.github/workflows/ci.yml` (GitHub Actions)
- `.gitlab-ci.yml` (GitLab CI/CD)
