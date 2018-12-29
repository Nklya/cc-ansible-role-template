# Cookiecutter Ansible role template

[![Build Status](https://img.shields.io/travis/cndies/cc-ansible-role-template.svg)](https://travis-ci.com/cndies/cc-ansible-role-template)

This template can be used to generate customized ansible role.

## Options

* `role_name` - What name to use for generated role
* `defaults_needed` - Select if you need defaults folder
* `docs_needed` - Select if you need docs folder
* `files_needed` - Select if you need files folder
* `handlers_needed` - Select if you need handlers folder
* `templates_needed` - Select if you need templates folder
* `vars_needed` - Select if you need vars folder
* `tests_needed` - Select if you need tests folder
* `author` - Author's name & e-mail
* `company` - Name of the company
* `description` - Description about what role does
* `issue_tracker_url` - Link to issues tracker, if exist
* `min_ansible_version` - Minimal Ansible version, default 2.5
* `platforms` - List of platforms, separated by `; and : and ,`, for example: `EL:all;Debian:jessie,stretch;Ubuntu:xenial,bionic`
* `galaxy_tags` - List of tags (separated by `,`)
* `dependencies` - List of dependencies (separated by `,`)

## How to use

1. Install cookiecutter `pip install cookiecutter`
2. Run `cookiecutter https://github.com/cndies/cc-ansible-role-template.git`
3. Answer questions, and after that you will get a new module folder in current directory

## How to modify

1. Add variables to cookiecutter.json
2. Use them in templates as `cookiecutter.<variable_name>`
3. You cannot use dashes `-` in variable name!
