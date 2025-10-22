from pyscal3.traj_process import split_trajectory
from pyscal3 import Atoms, System
import numpy as np
from typing import List, Union
import os
import warnings

def get_system_qvals(system, bops, averaged:bool=True):
    qs = []
    for ord in bops:
        if averaged:
            qs.append(system.atoms.get(f"avg_q{ord}"))
        else:
            qs.append(system.atoms.get(f"q{ord}"))
    return np.array(qs).T

def get_atoms_qvals(atoms, bops, averaged:bool=True):
    qs = []
    for ord in bops:
        if averaged:
            qs.append(atoms.get(f"avg_q{ord}"))
        else:
            qs.append(atoms.get(f"q{ord}"))
    return np.array(qs)

def delete_files(files):
    for file in files:
        os.remove(file)
        


def process_systems(trajfile:str, cutoff:Union[str, float],
                    bops:List[int], threshold:float=2.0,
                    get_octants:bool=False, averaged:bool=False):
    files = split_trajectory(trajfile)
    particle_system = System(files[-1])
    delete_files(files[:-1])
    middles = [particle_system.box_dimensions[i]/2 for i in range(3)]
    if get_octants:
        particle_system.delete(condition=lambda atom: ((atom.positions[0] > middles[0]) or (atom.positions[1] > middles[1]) or (atom.positions[2] > middles[2])))
    with warnings.catch_warnings():
        particle_system.find.neighbors(method='cutoff', cutoff=cutoff,
                                    threshold=threshold)
        particle_system.calculate.steinhardt_parameter(bops, averaged=averaged)
    delete_files([files[-1]])
    return particle_system, middles

def add_atoms(combined_system, particle_system):
    combined_system.atoms.positions = np.concatenate([combined_system.atoms.positions, particle_system.atoms.positions])

def add_distances(particle_system, axis:int=0, coeff:float=0, gap:float=8.):
    distances = np.zeros(shape=(len(particle_system.atoms), 3))
    distances.fill(0.)
    shift = coeff * (particle_system.box_dimensions[axis] + gap)
    distances[:, axis] = np.float16(shift)
    particle_system.atoms.positions = particle_system.atoms.positions + distances.astype(np.float16)
