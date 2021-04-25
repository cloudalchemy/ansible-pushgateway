# Ansible Role: pushgateway

[![Build Status](https://travis-ci.com/cloudalchemy/ansible-pushgateway.svg?branch=master)](https://travis-ci.com/cloudalchemy/ansible-pushgateway)
[![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT)
[![Ansible Role](https://img.shields.io/badge/ansible%20role-cloudalchemy.pushgateway-blue.svg)](https://galaxy.ansible.com/cloudalchemy/pushgateway/)
[![GitHub tag](https://img.shields.io/github/tag/cloudalchemy/ansible-pushgateway.svg)](https://github.com/cloudalchemy/ansible-pushgateway/tags)

## Description

Deploy prometheus [pushgateway](https://github.com/prometheus/pushgateway) using ansible.

## Requirements

- Ansible >= 2.7 (It might work on previous versions, but we cannot guarantee it)

## Role Variables

All variables which can be overridden are stored in [defaults/main.yml](defaults/main.yml) file as well as in table below.

| Name           | Default Value | Description                        |
| -------------- | ------------- | -----------------------------------|
| `pushgateway_version` | 1.3.1 | Pushgateway package version |
| `pushgateway_web_listen_address` | "0.0.0.0:9091" | Address on which pushgateway will listen |
| `pushgateway_web_external_url` | "" | External address on which pushgateway is available. Useful when behind reverse proxy. Ex. http://example.org/pushgateway |
| `pushgateway_persistence` | true | Enable persistence file |
| `pushgateway_config_flags_extra` | {} | Additional configuration flags passed at startup to pushgateway binary |

## Example

### Playbook

Use it in a playbook as follows:
```yaml
- hosts: all
  roles:
    - cloudalchemy.pushgateway
```

### Demo site

We provide demo site for full monitoring solution based on prometheus and grafana. Repository with code and links to running instances is [available on github](https://github.com/cloudalchemy/demo-site) and site is hosted on [DigitalOcean](https://digitalocean.com).

## Local Testing

The preferred way of locally testing the role is to use Docker and [molecule](https://github.com/ansible-community/molecule) (v3.x). You will have to install Docker on your system. See "Get started" for a Docker package suitable to for your system. Running your tests is as simple as executing `molecule test`.

## Continuous Intergation

Combining molecule and circle CI allows us to test how new PRs will behave when used with multiple ansible versions and multiple operating systems. This also allows use to create test scenarios for different role configurations. As a result we have a quite large test matrix which can take more time than local testing, so please be patient.

## Contributing

See [contributor guideline](CONTRIBUTING.md).

## Troubleshooting

See [troubleshooting](TROUBLESHOOTING.md).

## License

This project is licensed under MIT License. See [LICENSE](/LICENSE) for more details.
