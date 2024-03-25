# shared-lib

## Installation 
```zsh
pip install -U git+https://github.com/computer-solutions-gr/shared-lib`
```

## Automatically Update Documentation
```zsh
cd docs
sphinx-apidoc -f -o source .. ../*setup* ../tests ../*sandbox*
make html
```