# Identifying Local Structures in Dipolar Colloid-Polymer Mixtures using Machine Learning

This repository contains molecular dynamics simulations using LAMMPS (Large-scale Atomic/Molecular Massively Parallel Simulator) for studying crystal structures, particularly HCP (Hexagonal Close-Packed) and FCC (Face-Centered Cubic) crystal systems.

## 📁 Project Structure

```
crystal-structure-detection/
├── lammps_dump_files/
│   ├── mu0_eps0.xyz
│   ├── mu0_eps1.xyz
│   ├── mu0_eps3.25.xyz
│   ├── mu2_eps0.xyz
│   ├── mu2_eps1.xyz
│   ├── mu2_eps3.25.xyz
│   ├── mu4_eps0.xyz
│   ├── mu4_eps1.xyz
│   └── mu4_eps3.25.xyz
├── figures/
│   ├── g4.pdf
│   ├── g7.pdf
│   └── g8.pdf
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

- **`helpers.py`**: General utility functions for data manipulation
- **`process.py`**: Specialized functions for processing LAMMPS data files
- **`__init__.py`**: Package initialization file

## 📈 Visualization

The project includes Gnuplot scripts for generating publication-quality plots:

- **Energy Analysis**: Plots showing potential energy, kinetic energy, total energy
- **Thermodynamic Properties**: Pressure and temperature evolution over time
- **Crystal Structure Visualization**: 3D representations of crystal lattices

## 🛠️ Requirements

### Software Dependencies

- **Python 3.12+**: For data analysis and processing
- **uv**: Fast Python package installer and resolver
- **Jupyter Notebook**: For interactive analysis
- **TensorFlow/Keras**: Machine learning framework
- **PyScaL3**: Crystal structure analysis library
- **Pandas**: Data manipulation and analysis
- **Scikit-learn**: Machine learning algorithms
- **Matplotlib/Plotly/Seaborn**: Data visualization
- **OVITO**: Visualization and analysis of atomistic data
- **Py3DMol**: Interactive 3D molecular visualization
- **PartyCls**: Clustering algorithms for particle systems

### Installation

This project uses [uv](https://github.com/astral-sh/uv) for fast and reliable dependency management. 

#### Prerequisites

1. **Install uv** (if not already installed):
   ```bash
   # On macOS and Linux
   curl -LsSf https://astral.sh/uv/install.sh | sh
   
   # On Windows
   powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
   
   # Or via pip
   pip install uv
   ```

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

1. **Prepare Input Files**: Create LAMMPS input scripts for your crystal system
2. **Run Simulations**: Execute LAMMPS with your input files
3. **Process Data**: Use the provided Jupyter notebook for analysis
4. **Generate Plots**: Use the Gnuplot scripts for visualization

### Example Workflow

```bash
# Run LAMMPS simulation
lmp -in input.lmp

# Analyze results with Jupyter
jupyter notebook local_structures_detection.ipynb

# Generate plots
gnuplot myplot.gnu
```

## 📚 Documentation

- **Thesis**: See `Thesis.pdf` for detailed research methodology and results
- **Notebook**: The Jupyter notebook contains detailed analysis and explanations
- **Data Files**: XYZ format files contain atomic positions and properties

## 🔍 Key Features

- **Multi-Parameter Study**: Systematic exploration of crystal properties across different μ and ε values
- **Octant Analysis**: Detailed spatial analysis of crystal structures
- **Machine Learning Integration**: TensorFlow/Keras models and clustering algorithms for pattern recognition
- **Comprehensive Visualization**: Publication-ready plots and 3D molecular visualizations
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