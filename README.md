## Overview
`jupyter_ai_cborg` is a Jupyter AI module, a package
that registers custom [CBorg API provider](https://cborg.lbl.gov/) and slash commands for the Jupyter AI
extension.

This package is created using the [Jupyter AI Cookiecutter](https://jupyter-ai.readthedocs.io/en/latest/developers/index.html#jupyter-ai-module-cookiecutter).

The custom model provider, [cborg](./jupyter_ai_cborg/cborg.py), is developed in accordance with the [Jupyter AI Custom Model Providers Guide](https://jupyter-ai.readthedocs.io/en/latest/developers/index.html#custom-model-providers).

## Requirements

- Python 3.8 - 3.12
- JupyterLab 4

## Install

To install the extension, execute:

```bash
cd cdm-jupyter-ai-cborg
pip install -e "."
```

## Uninstall

To remove the extension, execute:

```bash
pip uninstall jupyter_ai_cborg
```