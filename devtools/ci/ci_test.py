#!/usr/bin/env python
from time import time
from contextlib import contextmanager
import os
import sys
import subprocess

@contextmanager
def change_folder(where):
    here = os.getcwd()
    os.chdir(where)
    yield
    os.chdir(here)


test_task = os.getenv('TEST_TASK', '')
sanderapi_tests = ['test.parm7', 'Fortran', 'Fortran2', 'C', 'CPP', 'Python', 'clean']

if test_task == 'fast':
    programs = ['clean', 'is_amberhome_defined',
                'test.pymsmt',
                'test.cpptraj', 'test.pytraj', 'test.parmed', 'test.pdb4amber',
                'test.leap', 'test.antechamber', 'test.unitcell', 'test.reduce',
                'test.nab', 'test.mdgx', 'test.resp', 'test.sqm',
                'test.gbnsr6', 'test.elsize', 'test.paramfit',
                'test.FEW', 'test.cphstats', 'test.cpinutil']
elif test_task == 'mmpbsa':
    programs = ['clean', 'is_amberhome_defined',
                'test.mmpbsa', 'test.mm_pbsa',]
elif test_task == 'rism':
    programs = ['test.rism1d', 'test.rism3d.periodic']
else:
    print('not sure how to test with test_task = {}'.format(test_task))
    sys.exit(0)

def execute(command):
    then = time()
    # adapted from StackOverflow
    # http://stackoverflow.com/a/4418193
    print(' '.join(command))
    output_lines = []
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    # Poll process for new output until finished
    while True:
        nextline = process.stdout.readline().decode()
        if nextline == '' and process.poll() is not None:
            break
        sys.stdout.write('.')
        sys.stdout.flush()

        output_lines.append(nextline)
    output = ''.join(output_lines)
    now = time()
    time_diff = now - then
    if 'Program error' in output or 'possible FAILURE' in output or 'No rule to make target' in output:
        print('{0:.1f} (s), FAILURE'.format(time_diff))
    else:
        print('{0:.1f} (s), PASSED'.format(time_diff))
    return output

def test_me():
    errors = []
    for me in programs:
        output = execute(['make', me])
        if 'Program error' in output or 'possible FAILURE' in output or 'No rule to make target' in output:
    with change_folder(os.getenv('AMBERHOME') + '/test/sanderapi'):
        for me in sanderapi_tests:
            output = execute(['make', me])
            if 'Program error' in output or 'possible FAILURE' in output or 'No rule to make target' in output:
                errors.append(output)
                errors.append(output)
    if errors:
        for out in errors:
            print(out)
    assert not errors
