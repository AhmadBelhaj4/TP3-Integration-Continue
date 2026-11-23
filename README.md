# TP3 - Intégration Continue (CI) avec GitHub Actions

Ce projet étend l'API FastAPI du TP2 en implémentant un pipeline d'Intégration Continue automatisé.

## Nouvelles fonctionnalités
- Ajout de l'endpoint de soustraction (`GET /soustraction`).
- Mise en place d'une suite de tests unitaires automatisés avec `pytest`.
- Mesure et validation de la couverture de code avec `pytest-cov` (seuil > 90%).
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
pytest -v test_main.py --cov=main --cov-report=term-missing --cov-report=xml:coverage.xml --cov-report=html --cov-fail-under=90
```

## Pipeline d'Intégration Continue (GitHub Actions)
Le pipeline défini dans `.github/workflows/ci.yml` s'exécute à chaque push et Pull Request :
1. **pylint** : Vérifie la syntaxe et les standards de code (score 10/10 obligatoire).
2. **run-test** : Exécute les tests unitaires et produit l'artefact `junit-test-report`.
3. **calculate-coverage** : Valide que la couverture dépasse 90% et téléverse les artefacts HTML et XML.
