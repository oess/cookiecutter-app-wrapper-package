#######################################################################
# Copyright (C) 2016-2017 OpenEye Scientific Software, Inc.
#######################################################################
import os
import sys
import tempfile
import subprocess

from openeye import oechem

INSTALL_DIR = os.path.dirname(__file__)

APP_NAME = {{cookiecutter.executable_name}}
MY_APPLICATION_CMD = os.path.join(INSTALL_DIR, APP_NAME)

__version__ = "{{cookiecutter.version}}"


def check_call_with_log(command, log=sys.stderr):
    p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in p.stdout:
        log.write(line.decode('utf-8'))
    p.wait()
    if p.returncode:
        raise subprocess.CalledProcessError(p.returncode, command)
    return p.returncode


def write_molecule(mol):
    # write to a temp file
    tmp_input = tempfile.NamedTemporaryFile(suffix=".oeb")
    ofs = oechem.oemolostream()
    if not ofs.open(tmp_input.name):
        raise Exception("Unable to to create temporary file for writing {} input.".format(APP_NAME))

    oechem.OEWriteMolecule(ofs, mol)
    ofs.close()
    return tmp_input


def run_my_application(ligand, protein, parameter_1=2.5, option_a=True, option_b=False):

    # setup input and output file
    tmp_ligand = write_molecule(ligand)
    tmp_protein = write_molecule(protein)
    tmp_out = tempfile.NamedTemporaryFile(suffix=".oeb")

    # setup application command-line
    cmd = [MY_APPLICATION_CMD, '-ligand', tmp_ligand.name, '-protein', tmp_protein.name, 
           '-parameter_1', parameter_1, '-option_a', option_a, '-option_b', option_b,
           '-out', tmp_out.name]

    # execute application
    try:
        check_call_with_log(cmd, log)
    except subprocess.CalledProcessError:
        log.write("Unable to process {}\n".format(mol.GetTitle()))
        return None

    # read and return multiple output molecules
    ifs = oechem.oemolistream(tmp_out.name)
    if not ifs:
        log.write("Unable to open temporary file for reading {} output.\n".format(MY_APPLICATION_CMD))
        return None

    for mol in ifs.GetOEMols():
        yield mol


