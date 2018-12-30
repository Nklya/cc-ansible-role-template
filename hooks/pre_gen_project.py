#!/usr/bin/env python

assert (
    "-" not in "{{ cookiecutter.role_name }}"
), "Don't include dashes '-' in role_name, use '_'"
