# Project Template

This repository is a template to create your project using Cookiecutter. It includes scripts to install dependencies, generate a new project, and clean up the directory.

## Usage

### Install Dependencies

To install the core and development Python dependencies into the currently activated virtual environment, run:

```sh
make install
```

### Generate Project
To generate a new project using the template, run:
```sh
make generate-project
```

This will create a new project based on the passed repo_name and package_name in the `src` directory and initialize a git repository.