# Testing of Alloy to TLA translator


This repository is designed to test the translation from Alloy to TLA+, and the performance of the translated models.

## Dependencies:

- tla2tools.jar
- watform-dashplus.jar
- python 3
- bash

The dependencies can be managed externally, or via nix. Running `nix develop ./nix` creates a development environment with all the required dependencies, with no external installation necessary.

`config.py` describes the dependency locations. By default, it is assumed that `dashplus` exists as a sibling repository to `alloy-to-tla-testing`. This can be setup by running:

```
cd ..
git clone https://github.com/WatForm/dashplus
```

## Running scripts:

All scripts are designed to be run from the repository root. The scripts operate on files with the `.als` extension, with intermediate files being produced during tests. These files can be removed by running `./scripts/cleanup.sh`. It is suggested that this be done periodically, to ensure that tlc does not fill up the system memory with state data.

## Overview

### Correctness Tests

* sat/unsat status
* instances
* is fuzz testing possible?

### Performance Tests

### Todo:

- manage dashplus cloning
- running tlc
