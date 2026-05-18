# Identifying Local Structures in Dipolar Colloid-Polymer Mixtures using Machine Learning

This repository implements an end-to-end pipeline for detecting crystal phases in dipolar colloid systems: LAMMPS molecular dynamics simulations → Steinhardt bond-order feature extraction → autoencoder dimensionality reduction → Gaussian Mixture Model clustering with entropy-based merging.

## 📁 Project Structure

```
crystal-structure-detection/
├── lammps_files/
│   ├── lammps_input.lmp          # MD simulation script (8000 atoms, NVT, LJ units)
│   ├── job_run_slurm.sh          # SLURM HPC batch submission (24 MPI tasks)
│   ├── colloid-eps0.table        # Tabulated pair potential (ε = 0)
│   ├── colloid-eps1.table        # Tabulated pair potential (ε = 1)
│   └── colloid-eps3.25.table     # Tabulated pair potential (ε = 3.25)
├── result_dump_files/            # LAMMPS XYZ dump files (9 simulations)
│   ├── mu0_eps0.xyz  mu0_eps1.xyz  mu0_eps3.25.xyz
│   ├── mu2_eps0.xyz  mu2_eps1.xyz  mu2_eps3.25.xyz
│   └── mu4_eps0.xyz  mu4_eps1.xyz  mu4_eps3.25.xyz
├── utils/
│   ├── __init__.py
│   ├── helpers.py                # Baudry et al. entropy-based cluster merging
│   └── process.py                # LAMMPS trajectory processing & Steinhardt parameters
├── local_structures_detection.ipynb  # Main analysis notebook
├── pyproject.toml
├── requirements.txt
├── uv.lock
├── Thesis.pdf
└── README.md
```

## Honours Thesis

This repository contains the code and data for my **BSc Honours Thesis** in Physics
at Memorial University of Newfoundland:

> *Identifying Local Structures in Dipolar Colloid-Polymer Mixtures using Machine Learning*

The full thesis document is available in this repository:
[📄 View Thesis (PDF)](./Thesis.pdf)

It covers the theoretical background, simulation methodology, machine learning pipeline
design, and results in detail.

## 🔬 Research Overview

The project systematically explores how dipole moment (μ) and dielectric constant (ε) affect crystal phase formation in colloidal systems. Each of the 9 simulations uses 8,000 dipolar sphere atoms in a 20×20×20 simple cubic lattice, run under NVT conditions with Lennard-Jones units and a hybrid Ewald/dipole + tabulated pair potential.

### Parameter Combinations Studied

| μ (dipole moment) | ε (dielectric constant) | Simulation file |
|-------------------|-------------------------|-----------------|
| 0 | 0 | `mu0_eps0.xyz` |
| 0 | 1 | `mu0_eps1.xyz` |
| 0 | 3.25 | `mu0_eps3.25.xyz` |
| 2 | 0 | `mu2_eps0.xyz` |
| 2 | 1 | `mu2_eps1.xyz` |
| 2 | 3.25 | `mu2_eps3.25.xyz` |
| 4 | 0 | `mu4_eps0.xyz` |
| 4 | 1 | `mu4_eps1.xyz` |
| 4 | 3.25 | `mu4_eps3.25.xyz` |

## 🤖 Machine Learning Pipeline

The analysis notebook (`local_structures_detection.ipynb`) implements a four-stage unsupervised pipeline:

### Stage 1 — Feature Extraction: Steinhardt Bond-Order Parameters

For each atom, [PyScaL3](https://github.com/pyscal/pyscal3) identifies neighbors within a cutoff of 1.055 LJ units and computes 8 Steinhardt order parameters (q₂ through q₉):

```
Q_l(i) = sqrt( 4π/(2l+1) × Σ_m |Σ_{j∈neighbors} Y_l^m(r̂_ij)|² )
```

This produces an 8-dimensional feature vector per atom encoding local crystallographic symmetry (e.g., q₆ is sensitive to HCP/FCC distinctions). All 9 simulations (~72,000 atoms total) are combined into a single dataset.

### Stage 2 — Dimensionality Reduction: Autoencoder (8D → 3D)

A symmetric encoder-decoder compresses the Steinhardt features into a 3D latent space for visualization and clustering:

```
Encoder:  Input(8) → Dense(20, ReLU) → Dropout(0.05)
                   → Dense(70, ReLU) → Dropout(0.15)
                   → Dense(3, ReLU)   [bottleneck]

Decoder:  Input(3) → Dense(20, ReLU) → Dropout(0.05)
                   → Dense(70, ReLU) → Dropout(0.15)
                   → Dense(8, linear) [reconstruction]
```

| Hyperparameter | Value |
|----------------|-------|
| Optimizer | Adam (lr = 4×10⁻⁵, L2 weight decay = 0.01) |
| Loss | Mean Squared Error |
| Epochs | 180 |
| Batch size | 512 |
| Train / test split | 75% / 25% |
| Preprocessing | StandardScaler (fit on training set) |

### Stage 3 — Clustering: Gaussian Mixture Models

BIC (Bayesian Information Criterion) analysis over 1–9 components selects the optimal number of clusters. A full-covariance GMM is then fit to the 3D encoded data, yielding soft per-atom membership probabilities.

### Stage 4 — Cluster Merging: Baudry et al. Entropy Criterion

The entropy-based merging algorithm (`utils/helpers.py`) iteratively combines the GMM components that minimize the increase in integrated complete-data likelihood entropy, reducing from the initial BIC-optimal count (typically 4–5) to 2–3 physically meaningful crystal phases (e.g., HCP, FCC, amorphous/liquid).

### Visualization

Final cluster assignments are rendered as 3D atomic structures with OVITO, with atoms colored by phase label.

## 🛠️ Utility Modules

- **`utils/process.py`** — `process_systems()` loads XYZ trajectories, runs neighbor detection, and computes Steinhardt parameters via PyScaL3. Supports optional octant filtering (spatial subdivision into 3D octants).
- **`utils/helpers.py`** — `merge_clusters()` implements the Baudry et al. entropy merging on GMM soft-weight matrices.

## 📂 LAMMPS Files

- **`lammps_input.lmp`** — Simulation script: hybrid dipole-sphere atom style, simple cubic lattice (a = 0.381971863), hybrid overlay force field (tabulated + Ewald/dipole), NVT integrator, 100,000 timesteps at dt = 0.001.
- **`job_run_slurm.sh`** — HPC submission: 24 MPI tasks, 1 GB/CPU, 12 h wall time.
- **`colloid-eps*.table`** — Tabulated colloid-colloid pair potentials (10,001 points each) for ε ∈ {0, 1, 3.25}.

## 🛠️ Requirements

- **Python 3.12+**
- **TensorFlow / Keras** ≥ 2.20 / 3.11
- **scikit-learn** ≥ 1.7 (GMM, StandardScaler)
- **PyScaL3** (installed from source — neighbor finding, Steinhardt parameters)
- **OVITO** ≥ 3.14 (3D atomistic visualization)
- **pandas**, **numpy**, **matplotlib**, **plotly**, **seaborn**
- **uv** (recommended package manager)

### Installation

```bash
# Clone the repository
git clone <repository-url>
cd crystal-structure-detection

# Install with uv (recommended — uses locked dependencies)
uv sync
source .venv/bin/activate       # macOS / Linux
# or: .venv\Scripts\activate    # Windows

# Alternative: pip
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 🚀 Usage

### 1. Run LAMMPS Simulations (optional — output files already included)

```bash
# Local execution
lmp -in lammps_files/lammps_input.lmp

# HPC cluster (SLURM)
sbatch lammps_files/job_run_slurm.sh
```

### 2. Run the Analysis Pipeline

```bash
jupyter notebook local_structures_detection.ipynb
```

Execute cells in order:
1. Initialize parameters and random seed (seed = 142)
2. Load XYZ files and compute Steinhardt features
3. Train autoencoder (8D → 3D)
4. BIC analysis → fit GMM
5. Entropy-based cluster merging
6. Visualize crystal phases with OVITO

## 📄 License

This project is part of academic research. Please refer to the thesis document for detailed methodology and cite appropriately if using this work.

## 👨‍🎓 Author

**Vahid Sheigani** — BSc Honours Thesis, Memorial University of Newfoundland

---

*Full methodology, results, and discussion are available in [Thesis.pdf](./Thesis.pdf).*
