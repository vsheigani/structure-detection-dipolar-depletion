# Identifying Local Structures in Dipolar Colloid-Polymer Mixtures using Machine Learning

This repository contains molecular dynamics simulations using LAMMPS (Large-scale Atomic/Molecular Massively Parallel Simulator) for studying crystal structures, particularly HCP (Hexagonal Close-Packed) and FCC (Face-Centered Cubic) crystal systems.

## 📁 Project Structure

```
crystal-structure-detection/
├── lammps_files/
│   ├── lammps_input.lmp
│   ├── job_run_slurm.sh
│   ├── colloid-eps0.table
│   ├── colloid-eps1.table
│   └── colloid-eps3.25.table
├── result_dump_files/
│   ├── mu0_eps0.xyz
│   ├── mu0_eps1.xyz
│   ├── mu0_eps3.25.xyz
│   ├── mu2_eps0.xyz
│   ├── mu2_eps1.xyz
│   ├── mu2_eps3.25.xyz
│   ├── mu4_eps0.xyz
│   ├── mu4_eps1.xyz
│   └── mu4_eps3.25.xyz
├── utils/
│   ├── __init__.py
│   ├── helpers.py
│   └── process.py
├── local_structures_detection.ipynb
├── pyproject.toml
├── requirements.txt
├── uv.lock
├── Thesis.pdf
└── README.md
```

## 🔬 Research Overview

This project focuses on molecular dynamics simulations of crystal structures using LAMMPS. The simulations explore different crystal systems with varying parameters:

- **μ (mu)**: Represents different dipole moments or interaction parameters
- **ε (eps)**: Represents different energy parameters or dielectric constants

## Honours Thesis

This repository contains the code and data for my **BSc Honours Thesis** in Physics 
at Memorial University of Newfoundland:

> *Identifying Local Structures in Dipolar Colloid-Polymer Mixtures using Machine Learning*

The full thesis document is available in this repository:
[📄 View Thesis (PDF)](./Thesis.pdf)

It covers the theoretical background, simulation methodology, machine learning pipeline 
design, and results in detail.

### Parameter Combinations Studied

| μ (mu) | ε (eps) | Description |
|--------|---------|-------------|
| 0      | 0       | Baseline crystal structure |
| 0      | 1       | Low energy interaction |
| 0      | 3.25    | Medium energy interaction |
| 2      | 0       | Medium dipole, no energy |
| 2      | 1       | Medium dipole, low energy |
| 2      | 3.25    | Medium dipole, medium energy |
| 4      | 0       | High dipole, no energy |
| 4      | 1       | High dipole, low energy |
| 4      | 3.25    | High dipole, medium energy |

## 📊 Data Analysis

The project includes a comprehensive Jupyter notebook (`local_structures_detection.ipynb`) that contains:

- **Crystal Structure Analysis**: Analysis of HCP and FCC crystal structures
- **Octant Analysis**: Division of simulation space into octants for detailed study
- **LAMMPS Data Processing**: Reading and processing LAMMPS dump files
- **Statistical Analysis**: Clustering and learning algorithms applied to the data
- **Utility Functions**: Helper modules for data processing and analysis

## 🛠️ Utility Modules

The `utils/` directory contains helper modules for data processing and analysis:

- **`helpers.py`**: Cluster merging utilities based on entropy criterion (Baudry et al.)
- **`process.py`**: LAMMPS trajectory processing using PyScaL3 — neighbor finding, Steinhardt parameter calculation, and octant extraction
- **`__init__.py`**: Package initialization file

## 📂 LAMMPS Files

The `lammps_files/` directory contains all files required to run the simulations:

- **`lammps_input.lmp`**: LAMMPS input script defining the simulation protocol (atom style, force field, integrator, output settings)
- **`job_run_slurm.sh`**: SLURM batch script for submitting simulations to an HPC cluster
- **`colloid-eps0.table`**, **`colloid-eps1.table`**, **`colloid-eps3.25.table`**: Tabulated pair potential files for colloid interactions — one table per ε value

The `result_dump_files/` directory contains the XYZ dump files output by LAMMPS after each simulation run, one per (μ, ε) parameter combination.

## 🛠️ Requirements

### Software Dependencies

- **Python 3.12+**: For data analysis and processing
- **uv**: Fast Python package installer and resolver
- **Jupyter Notebook**: For interactive analysis
- **TensorFlow/Keras**: Machine learning framework
- **PyScaL3**: Crystal structure analysis library (installed from source)
- **Pandas**: Data manipulation and analysis
- **Scikit-learn**: Machine learning algorithms
- **Matplotlib/Plotly/Seaborn**: Data visualization
- **OVITO**: Visualization and analysis of atomistic data
- **Py3DMol**: Interactive 3D molecular visualization
- **PartyCls**: Clustering algorithms for particle systems

### Installation

This project uses [uv](https://github.com/astral-sh/uv) for fast and reliable dependency management.

#### Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd crystal-structure-detection
   ```

2. **Create and activate virtual environment with uv**:
   ```bash
   # Create virtual environment and install dependencies
   uv sync
   
   # Activate the virtual environment
   source .venv/bin/activate  # On macOS/Linux
   # or
   .venv\Scripts\activate     # On Windows
   ```

3. **Alternative: Manual setup** (if you prefer pip):
   ```bash
   # Create Python environment
   python3.12 -m venv env
   source env/bin/activate  # On macOS/Linux
   
   # Install dependencies
   pip install -r requirements.txt
   ```

## 🚀 Usage

### Running Simulations

1. **Prepare Input Files**: Edit `lammps_files/lammps_input.lmp` for your crystal system and parameter set
2. **Submit to HPC**: Use the provided SLURM script to run on a cluster
   ```bash
   sbatch lammps_files/job_run_slurm.sh
   ```
3. **Run Locally**: Execute LAMMPS directly with the input file
   ```bash
   lmp -in lammps_files/lammps_input.lmp
   ```
4. **Process Data**: Use the provided Jupyter notebook for analysis
   ```bash
   jupyter notebook local_structures_detection.ipynb
   ```

## 📚 Documentation

- **Thesis**: See the [Honours Thesis (PDF)](./Thesis.pdf) for complete methodology, results, and discussion. This document provides the full academic context for the code in this repository.
- **Notebook**: The Jupyter notebook contains detailed analysis and explanations
- **Data Files**: XYZ format dump files in `result_dump_files/` contain atomic positions output by LAMMPS for each parameter combination

## 🔍 Key Features

- **Multi-Parameter Study**: Systematic exploration of crystal properties across different μ and ε values
- **Octant Analysis**: Detailed spatial analysis of crystal structures
- **Machine Learning Integration**: TensorFlow/Keras models and clustering algorithms for pattern recognition
- **Comprehensive Visualization**: Publication-ready plots and 3D molecular visualizations
- **HPC Support**: SLURM job script included for running on compute clusters
- **Reproducible Research**: Complete workflow from simulation to analysis with uv dependency management
- **Modular Design**: Well-organized utility modules for data processing and analysis
- **Modern Python Stack**: Uses latest Python 3.12+ with modern scientific computing libraries

## 📄 License

This project is part of academic research. Please refer to the thesis document for detailed methodology and cite appropriately if using this work.

## 👨‍🎓 Author

**Vahid** - Honours Thesis Project

## 🤝 Contributing

This is an academic research project. For questions or collaboration opportunities, please refer to the thesis document or contact the author.

---

*This project demonstrates advanced molecular dynamics simulation techniques for studying crystal structures and their properties under various conditions.*
