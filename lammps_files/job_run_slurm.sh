#!/bin/bash
#SBATCH --account=<WRITE YOUR ACCOUNT ID>
#SBATCH --ntasks=24              # number of MPI processes
#SBATCH --mem-per-cpu=1024M      # memory; default unit is megabytes
#SBATCH --time=0-12:00           # time (DD-HH:MM)
module load lammps-omp/20210929  # CHANGE LAMMPS version
export OMP_NUM_THREADS=1         # CHANGE number of threads 
srun lmp -in lammps_input.lmp
