import os
import pytest
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

# Get all the noteboooks in each folder
# Notebooks in this list will be skipped as the problems are very large
large_problems = ["reentrant_cube_capacity.ipynb"]

notebooks = []
for dir in ["laplace", "helmholtz", "maxwell"]:
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), dir)
    for i in os.listdir(path):
        if i.endswith(".ipynb") and i not in large_problems:
            notebooks.append((path, i))


@pytest.mark.parametrize(("path", "notebook"), notebooks)
def test_notebook(path, notebook):
    with open(os.path.join(path, notebook)) as f:
        nb = nbformat.read(f, as_version=4)

    ep = ExecutePreprocessor(timeout=600)

    ep.preprocess(nb, {"metadata": {"path": path}})
