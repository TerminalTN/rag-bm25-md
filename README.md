# 🗄️ RAG sur Base de Données Relationnelle — Partie 1 : Documentation Automatique & BM25

Bienvenue sur le dépôt officiel de la série **RAG sur une Base Relationnelle** par **[TerminalTN](https://github.com/TerminalTN)**.

> 🎯 **Le problème :** Comment poser des questions en langage naturel sur le schéma d'une base de données massive (+90 tables comme *AdventureWorks*) sans exploser la fenêtre de contexte du LLM en lui envoyant tout le schéma SQL d'un seul coup ?

Ce dépôt contient le code de la **Vidéo 1 (Baseline)** : une architecture en **2 passes** qui documente automatiquement chaque table en fichiers Markdown enrichis par un LLM local, puis utilise l'algorithme lexical **Okapi BM25** pour retrouver le Top-5 des tables pertinentes avant de générer la réponse.

📺 **[Voir la Vidéo 1 sur YouTube](https://youtu.be/FlMJh3KRops)**

---

## 🏗️ Architecture du Pipeline (Vidéo 1)

Le pipeline se divise en **3 grandes étapes** :

1. **Ingestion des données (`00_setup`)**
   - Chargement des 91 tables/vues d'**AdventureWorks** depuis des fichiers CSV vers une base locale **DuckDB** (`data/adventureworks.duckdb`).
   - Extraction des clés primaires (`PK`) et clés étrangères (`FK`) depuis une instance MariaDB de référence vers `docs/relationships.yaml`.

2. **Documentation Automatique en 2 Passes (`01_docs`)**
   - **Passe 1 (Squelette) :** Extraction des métadonnées SQL (`DESCRIBE`, `SUMMARIZE` : types, `% null`, valeurs distinctes, `min`, `max`, `avg`, `std`, `median`) et génération d'un fichier `.md` par table via **Jinja2** (`templates/table.md.j2`).
   - **Passe 2 (Enrichissement LLM & Ré-injection) :** Un LLM local (**Qwen3-4B** via LM Studio) génère pour chaque table une description métier, le domaine fonctionnel, des mots-clés (EN/FR) et 3 questions types dans `docs/descriptions.yaml`. Un mécanisme de *guardrail* (`source: human` vs `source: llm`) empêche l'écrasement des corrections manuelles. Les descriptions sont ensuite ré-injectées dans les fichiers `docs/tables/*.md`.

3. **Retrieval Lexical & Génération (`02_rag`)**
   - **Indexation & Recherche BM25 :** Tokenisation des 91 fichiers `.md` et création d'un index inversé caché dans `data/bm25_index.json` (paramètres Okapi BM25 : `k1 = 1.5`, `b = 0.75`).
   - **Synthèse RAG :** Récupération du **Top-5** des tables les plus pertinentes et envoi au LLM local pour une réponse sourcée et sans hallucination.

---

## 🛠️ Tech Stack

* **Langage :** Python 3.12+
* **Base de données locale :** [DuckDB](https://duckdb.org/)
* **Templating :** Jinja2 & PyYAML
* **LLM Local :** Qwen3-4B (servi en local via LM Studio sur `http://127.0.0.1:1234/v1/chat/completions`)
* **Retrieval :** Implémentation pure Python d'**Okapi BM25** (zéro dépendance lourde)

---

## 📂 Structure du Projet

```text
├── data/
│   ├── adventureworks.duckdb       # Base DuckDB générée (91 tables/vues)
│   └── bm25_index.json             # Cache de l'index BM25
├── docs/
│   ├── tables/                     # 91 fichiers Markdown (1 par table)
│   ├── descriptions.yaml           # Descriptions, keywords & questions générés par le LLM
│   ├── relationships.yaml          # Clés primaires et étrangères (PK/FK)
│   └── index.md                    # Catalogue global de navigation humaine
├── scripts/
│   ├── 00_setup/
│   │   ├── extract_adventureworks.py
│   │   └── fetch_relationships.py
│   ├── 01_docs/
│   │   ├── 01_generate_table_docs.py
│   │   ├── 02_enrich_descriptions.py
│   │   ├── 03_generate_index.py
│   │   └── 04_check_docs.py
│   └── 02_rag/
│       ├── bm25.py                 # Moteur d'indexation et de scoring Okapi BM25
│       └── ask.py                  # Pipeline RAG complet (Retrieval Top-5 + LLM)
└── templates/
    └── table.md.j2                 # Template Jinja2 pour les fichiers Markdown
```
---

## 🚀  Installation & Utilisation
### 1. Prérequis
Clonez le dépôt et installez les dépendances dans un environnement virtuel :

```code
git clone https://github.com/TerminalTN/rag-bm25-md.git
cd rag-bm25-md
python -m venv .venv
# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1
# Linux / macOS
source .venv/bin/activate

pip install duckdb pyyaml jinja2
```
Assurez-vous d'avoir **LM Studio** (ou un serveur compatible OpenAI API) lancé sur le port 1234 avec le modèle qwen/qwen3-4b.

### 2. Exécuter le Pipeline de Documentation

```text

# 1. Générer les squelettes Markdown (Passe 1)
python scripts/01_docs/01_generate_table_docs.py

# 2. Enrichir les descriptions avec le LLM local (sur toutes les tables ou une table spécifique)
python scripts/01_docs/02_enrich_descriptions.py "HumanResources.Employee"

# 3. Ré-injecter les descriptions dans les fichiers .md (Passe 2)
python scripts/01_docs/01_generate_table_docs.py
```

### 3. Tester le Recherche BM25 et le RAG

```text
# Construire / rafraîchir l'index BM25
python scripts/02_rag/bm25.py --build

# Tester uniquement le Retrieval BM25 (Top-5)
python scripts/02_rag/bm25.py --top 5 "Can we find a person by their email promotion status?"

# Poser une question complète au système RAG (BM25 + Qwen3-4B)
python scripts/02_rag/ask.py "Which table tracks employee vacation and sick leave?"
```

