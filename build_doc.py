#!/usr/bin/env python

#
#   Copyright (c) 2013-2014, Scott J Maddox
#
#   This file is part of openbandparams.
#
#   openbandparams is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as published
#   by the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   openbandparams is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with openbandparams.  If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################

import os
import sys
import subprocess
import shutil

def clear_pycache(path):
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            root, ext = os.path.splitext(filename)
            if ext == '.pyc':
                os.remove(os.path.join(dirpath, filename))
                
def clear_rst_cache(path):
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            root, ext = os.path.splitext(filename)
            if filename.startswith('_') and ext == '.rst':
                os.remove(os.path.join(dirpath, filename))

CLEAN = len(sys.argv) > 1 and sys.argv[1].lower() == 'clean'

CWD = os.getcwd()

# sphinx-apidoc -f -o doc -d 4 src/openbandparams/
SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
SRC_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, 'src'))
EXAMPLES_DIR = os.path.join(SCRIPT_DIR, 'src/openbandparams/examples')
OBP_FILE = os.path.join(SCRIPT_DIR, 'src/openbandparams/__init__.py')
DOC_DIR = os.path.join(SCRIPT_DIR, 'doc')
DOC_EXAMPLES_DIR = os.path.join(SCRIPT_DIR, 'doc/examples')
BUILD_DIR = os.path.join(SCRIPT_DIR, 'doc/_build_examples')
BUILD_EXAMPLES_DIR = os.path.join(SCRIPT_DIR, 'doc/_build_examples')

clear_rst_cache(DOC_EXAMPLES_DIR)

if CLEAN:
    clear_pycache(SRC_DIR)
    if os.path.exists(BUILD_DIR):
        shutil.rmtree(BUILD_DIR)
    if os.path.exists(DOC_EXAMPLES_DIR):
        shutil.rmtree(DOC_EXAMPLES_DIR)
    if os.path.exists(BUILD_EXAMPLES_DIR):
        shutil.rmtree(BUILD_EXAMPLES_DIR)

if not os.path.exists(DOC_EXAMPLES_DIR):
    os.mkdir(DOC_EXAMPLES_DIR)
if not os.path.exists(BUILD_EXAMPLES_DIR):
    os.mkdir(BUILD_EXAMPLES_DIR)


# make sure that python imports the local openbandparams version
os.chdir(SRC_DIR)
sys.path.insert(0, SRC_DIR)
import openbandparams
if openbandparams.__file__ != OBP_FILE and openbandparams.__file__ != OBP_FILE+'c':
    raise RuntimeError('Wrong openbandparams location:\n'
                       '{}\n'
                       'Expected:\n'
                       '{}'.format(openbandparams.__file__,OBP_FILE))

print ''
print 'Building examples...'
examples = []
for root, dirs, files in os.walk(EXAMPLES_DIR):
    for f in files:
        if f.endswith('.py') and not f.startswith('_'):
            examples.append(os.path.relpath(os.path.join(root, f),
                                            EXAMPLES_DIR))

# save a list of the examples
with open(os.path.join(BUILD_EXAMPLES_DIR, 'examples.txt'), 'w') as f:
    for example in examples:
        f.write(example + '\n')

for example in examples:
    # build the result filename
    dir, filename = os.path.split(example)
    root, ext = os.path.splitext(filename)
    if filename.lower().startswith('plot'):
        result_type = 'image'
        result = os.path.join(dir, root + '.png')
    else:
        result_type = 'literalinclude'
        result = os.path.join(dir, root + '.txt')

    # output an rst file for each example
    rst_path = os.path.join(DOC_EXAMPLES_DIR, dir, '_' + root + '.rst')
    # ../../src/openbandparams/examples/
    rst_abs_dir = os.path.dirname(rst_path)
    example_rel = os.path.relpath(os.path.join(EXAMPLES_DIR, example),
                                  rst_abs_dir)
    result_rel = os.path.relpath(os.path.join(BUILD_EXAMPLES_DIR, result),
                                  rst_abs_dir)
    if not os.path.exists(rst_abs_dir):
        os.makedirs(rst_abs_dir)
    with open(rst_path, 'w') as f:
        title = root.replace('_', ' ')
        underline = '=' * len(root)
        f.write('''{title}
{underline}

Source:

.. literalinclude:: {example_rel}

Result:

.. {result_type}:: {result_rel}
'''.format(title=title,
           underline=underline,
           result_type=result_type,
           example_rel=example_rel,
           result_rel=result_rel))

    # get the absolute paths
    example_path = os.path.join(EXAMPLES_DIR, example)
    result_path = os.path.join(BUILD_EXAMPLES_DIR, result)

    # check if changes have been made to the example script
    if (not CLEAN and
        os.path.exists(result_path) and
        os.path.getmtime(example_path) < os.path.getmtime(result_path)):
        # no changes -- skip running it
        continue

    # get the relative paths (for printing)
    example_relpath = os.path.relpath(example_path, CWD)
    result_relpath = os.path.relpath(result_path, CWD)

    # run the script and save the result
    print '  Running "{}"\n    Saving result to "{}"'.format(
                                        example_relpath, result_relpath)
    if not os.path.exists(os.path.dirname(result_path)):
        os.makedirs(os.path.dirname(result_path))
    if result_type == 'image':
        try:
            subprocess.check_call(['python', example_path, result_path],
                                  env=os.environ)
        except Exception as e:
            if os.path.exists(result_path):
                os.remove(result_path)
            raise e
    elif result_type == 'literalinclude':
        try:
            with open(result_path, 'w') as f:
                subprocess.check_call(['python', example_path], stdout=f,
                                      env=os.environ)
        except Exception as e:
            if os.path.exists(result_path):
                os.remove(result_path)
            raise e
    else:
        raise RuntimeError('Unknown result_type: {}'.format(result_type))

print 'Done building examples.'
print ''


os.chdir('../doc')

# Run sphinx-apidoc
subprocess.check_call(['sphinx-apidoc', '-o','apidoc', '../src/openbandparams',
                       # exclude paths:
                       '../src/openbandparams/tests',
                       '../src/openbandparams/examples',
                       ])

# Build html
subprocess.check_call(['make', 'html'])
