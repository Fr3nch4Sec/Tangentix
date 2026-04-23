# 🚀 Tangentix  — Étude de Fonctions

## A python webapp for mathematics function study
**Tangentix** est une application web interactive d'analyse mathématique, similaire à Symbolab. Elle permet de visualiser une fonction, sa tangente en un point, et d'obtenir une étude complète automatique en temps réel.

---

## ✨ Fonctionnalités

- **Saisie de f(x)** avec clavier mathématique intégré et aperçu LaTeX en direct
- **Graphique interactif** : tracé de $f$, $f'$, $f''$ et de la tangente en $x_0$
- **Dérivées** : calcul symbolique de la dérivée première $f'(x)$ et seconde $f''(x)$
- **Tangente** : équation et tracé en tout point $x_0$ via un slider
- **Extremums** : calcul des extremums locaux et globaux
- **Points d'inflexion** : détection automatique
- **Domaine de définition** : calcul de l'ensemble de définition
- **Limites** : en $-\infty$ et $+\infty$
- **Solutions** : racines pour les polynômes de degré 2

---

## ⚙️ Installation

### Prérequis
- Python **3.8+** — [télécharger Python](https://www.python.org/downloads/)

---

### 1. Créer un environnement virtuel

Un environnement virtuel isole les dépendances du projet du reste de ton système.

#### 🪟 Windows
```bash
python -m venv venv
venv\Scripts\activate
```

#### 🐧 Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

#### 🍎 macOS
```bash
python3 -m venv venv
source venv/bin/activate
```

> Une fois activé, ton terminal affiche `(venv)` au début de la ligne. Pour quitter l'environnement virtuel à tout moment : `deactivate`

---

### 2. Installer les dépendances

```bash
pip install dash numpy plotly sympy
```

---

### 3. Lancer la webapp

```bash
python tangentix.py
```

Puis ouvre ton navigateur à l'adresse :

```
http://127.0.0.1:8050
```

---

## 🖥️ Interface

L'application se compose de 4 zones principales :

```
┌──────────────────────────────────────────────┐
│  [Clavier mathématique]                      │
│  [Zone de saisie de f(x)]                    │
│  [Aperçu LaTeX de la fonction]               │
│  [Slider : position de la tangente x₀]       │
│  ┌──────────────────┐  ┌───────────────────┐ │
│  │    Graphique     │  │  Analyse détaillée│ │
│  └──────────────────┘  └───────────────────┘ │
└──────────────────────────────────────────────┘
```

---

## ✏️ Saisir une fonction

### Méthode 1 — Clavier mathématique
Clique sur les boutons en haut de l'écran pour insérer des symboles dans la zone de saisie :

| Bouton | Insère |
|--------|--------|
| `x²` | `**2` (mise au carré) |
| `√x` | `sqrt(` |
| `eˣ` | `exp(` |
| `ln` | `ln(` |
| `sin` / `cos` | `sin(` / `cos(` |
| `π` | `pi` |
| `/` | `/` (division) |
| `(` `)` | parenthèses |

### Méthode 2 — Saisie directe
Tu peux taper directement dans la zone de texte. Utilise la syntaxe Python/SymPy :

| Notation mathématique | Syntaxe à saisir |
|-----------------------|------------------|
| $x^2$ | `x**2` |
| $\sqrt{x}$ | `sqrt(x)` |
| $e^x$ | `exp(x)` |
| $\ln(x)$ | `ln(x)` |
| $\sin(x)$ | `sin(x)` |
| $2x^3 - 5x + 1$ | `2*x**3 - 5*x + 1` |

> ⚠️ **Important :** écris toujours `*` pour les multiplications (`2*x`, pas `2x`).

---

## 📍 Placer la tangente

Le **slider** sous la zone de saisie permet de choisir le point $x_0$ où la tangente sera tracée.

- Plage : de **-10** à **10**
- Pas : **0,1**
- La tangente (en orange pointillé) et le point de contact (point rouge) se mettent à jour automatiquement.

---

## 📊 Lire l'analyse détaillée

Le panneau de droite affiche automatiquement :

- **Équation** : la fonction reconnue en notation mathématique
- **Domaine** : l'ensemble de définition de $f$
- **Dérivée première** $f'(x)$
- **Dérivée seconde** $f''(x)$
- **Limites** en $-\infty$ et $+\infty$
- **Équation de la tangente** en $x_0$ sous la forme $y = ax + b$

---

## 💡 Exemples de fonctions à tester

```
x**2 - 3*x + 2
sin(x) / x
exp(x) - 2*x**2 - 6*x + 3
ln(x**2 + 1)
sqrt(4 - x**2)
```

---

## ❓ Résolution de problèmes

| Problème | Solution |
|----------|----------|
| `⚠️ Erreur` affiché | Vérifie la syntaxe (oubli de `*`, parenthèse non fermée…) |
| Graphique vide | La fonction diverge peut-être trop vite sur l'intervalle |
| Page ne s'affiche pas | Vérifie que le serveur tourne bien sur le port 8050 |

---

## 🛠️ Technologies utilisées

- [Dash](https://dash.plotly.com/) — framework web interactif
- [Plotly](https://plotly.com/python/) — graphiques
- [SymPy](https://www.sympy.org/) — calcul symbolique (dérivées, limites, domaine)
- [NumPy](https://numpy.org/) — calcul numérique

---

## 📅 Changelog

### v1.1.0 — 23/04/2026
- **Champ de saisie amélioré** : la fonction saisie est désormais entièrement visible dans la zone de texte
- **Clavier mathématique** : ajout de touches dédiées pour `√x`, `eˣ`, `sin`, `cos`, `ln`, `π`, facilitant la saisie sans clavier physique
- **Analyse étendue** : calcul des extremums locaux/globaux, points d'inflexion, limites et domaine de définition directement dans le panneau latéral

### v1.0.0 — Version initiale
- Tracé de $f(x)$ et de sa tangente en $x_0$
- Calcul des dérivées première et seconde
- Aperçu LaTeX de la fonction reconnue
