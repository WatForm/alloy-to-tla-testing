# Testing of Alloy to TLA translator


This repository is designed to test the translation from Alloy to TLA+, and the performance of the translated models.


## Running tests

### Externally managed dependencies (without nix flakes)

1) Clone the repository by running `git clone https://github.com/WatForm/alloy-to-tla-testing`

2) Ensure that the java version locally installed is >= 25, by running `java --version`

3) Ensure that `dashplus` is accessible, by running:

```
mkdir -p ./libs
rm -rf ./libs
cd ./libs
git clone https://github.com/WatForm/dashplus
cd ./dashplus
./gradlew spotlessApply && ./gradlew releaseJar
cd ..
cd ..
```

4) Ensure that python is installed locally, by running `python --version`

5) Run the translation script: `python ./scripts/alloy_to_tla_translate.py`

6) To clean up the artefacts, run `./scripts/cleanup.sh`

### Nix managed dependencies

1) Install the nix package manager: [https://nixos.org/download/](https://nixos.org/download/)

2) Enable flakes, which is an experimental feature of nix

3) Run `nix develop ./nix` - this sets up all the dependencies needed, and creates a development shell where all the dependencies are present

4) After testing, exit the shell to remove all dependencies

5) To clean up the artefacts, run `./scripts/cleanup.sh`



## Overview

### Correctness Tests

* sat/unsat status
* instances
* is fuzz testing possible?

### Performance Tests

### Todo:

- manage dashplus cloning
- running tlc
