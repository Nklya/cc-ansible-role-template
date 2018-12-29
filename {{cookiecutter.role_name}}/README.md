# {{ cookiecutter.role_name }} ansible role

{{ cookiecutter.description }}

## Requirements

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here.

## Role Variables

Please look at `defaults/main.yml`, `vars/main.yml`

## Dependencies
{% if cookiecutter.dependencies %}
  {%- for i in cookiecutter.dependencies.split(',') %}
- {{ i.strip() }}
  {%- endfor %}
{%- else %}
- None
{%- endif %}

## Example Playbook

```yaml
    - hosts: servers
      roles:
         - {{ cookiecutter.role_name }}
```

## License

{{ cookiecutter.license }}

## Author Information

{{ cookiecutter.author }}, {{ cookiecutter.company }}
