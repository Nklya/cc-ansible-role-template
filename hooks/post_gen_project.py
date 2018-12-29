#!/usr/bin/env python
import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def remove_dir(filepath):
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == "__main__":
    if not {{cookiecutter.defaults_needed}}:
        remove_dir("defaults")
    if not {{cookiecutter.docs_needed}}:
        remove_dir("docs")
    if not {{cookiecutter.files_needed}}:
        remove_dir("files")
    if not {{cookiecutter.handlers_needed}}:
        remove_dir("handlers")
    if not {{cookiecutter.templates_needed}}:
        remove_dir("templates")
    if not {{cookiecutter.vars_needed}}:
        remove_dir("vars")
    if not {{cookiecutter.tests_needed}}:
        remove_file(".kitchen.yml")
        remove_file(".kitchen.docker.yml")
        remove_file("Gemfile")
        remove_dir("test")
