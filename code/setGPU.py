"""Compatibility stub for Windows.

The upstream code does `import setGPU`, a Linux-only package that selects a GPU by
setting CUDA_VISIBLE_DEVICES and re-executing the interpreter. Windows has no
equivalent, so this stub keeps certify.py / predict.py importable without touching
the upstream sources.
"""