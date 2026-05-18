from ase.io import read
from ase import Atoms
import numpy as np
from typing import List, Union
try:
    import pyscal
except ImportError:
    print("Please install pyscal3. Pyscal3 is required to load and process the systems")
import warnings


def get_system_qvals(atoms: Atoms, bops: List[int], averaged:bool=True) -> np.array:
    qs = pyscal.steinhardt_parameter(atoms, l=bops, averaged=averaged)
    return np.array(qs).T

def process_systems(trajfile:str, method:str, cutoff:Union[str, float]) -> Union[Atoms, List[float]]:
    # reads the last configuration only by default
    atoms = read(trajfile, format='lammps-dump-text')
    dimensions = atoms.cell.lengths()
    middles = [dimensions[i]/2 for i in range(3)]

    with warnings.catch_warnings():
        pyscal.find_neighbors(atoms, method=method, cutoff=cutoff)
    return atoms, middles

def add_distances(atoms: Atoms, axis:int=0, coeff:float=0, gap:float=8.):
    distances = np.zeros(shape=(atoms.get_positions().shape[0], 3))
    dimensions = atoms.cell.lengths()
    shift = coeff * (dimensions[axis] + gap)
    distances[:, axis] = float(shift)
    atoms.set_positions(atoms.get_positions() + distances.astype(np.float16))
