# Ansible Role: pushgateway

[![Build Status](https://travis-ci.com/cloudalchemy/ansible-pushgateway.svg?branch=master)](https://travis-ci.com/cloudalchemy/ansible-pushgateway)
[![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT)
[![Ansible Role](https://img.shields.io/badge/ansible%20role-cloudalchemy.pushgateway-blue.svg)](https://galaxy.ansible.com/cloudalchemy/pushgateway/)
[![GitHub tag](https://img.shields.io/github/tag/cloudalchemy/ansible-pushgateway.svg)](https://github.com/cloudalchemy/ansible-pushgateway/tags)
[![IRC](https://img.shields.io/badge/irc.freenode.net-%23cloudalchemy-yellow.svg)](https://kiwiirc.com/nextclient/#ircs://irc.freenode.net/#cloudalchemy)

## Description

Deploy prometheus [pushgateway](https://github.com/prometheus/pushgateway) using ansible.

## Requirements

- Ansible >= 2.4

## Role Variables

All variables which can be overridden are stored in [defaults/main.yml](defaults/main.yml) file as well as in table below.

| Name           | Default Value | Description                        |
| -------------- | ------------- | -----------------------------------|
| `pushgateway_version` | 0.5.2 | Node exporter package version |
| `pushgateway_web_listen_address` | "0.0.0.0:9091" | Address on which node exporter will listen |
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

The preferred way of locally testing the role is to use Docker and [molecule](https://github.com/metacloud/molecule) (v2.x). You will have to install Docker on your system. See "Get started" for a Docker package suitable to for your system.
We are using tox to simplify process of testing on multiple ansible versions. To install tox execute:
```sh
pip install tox
```
To run tests on all ansible versions (WARNING: this can take some time)
```sh
tox
```
To run a custom molecule command on custom environment with only default test scenario:
```sh
tox -e py27-ansible25 -- molecule test -s default
```
For more information about molecule go to their [docs](http://molecule.readthedocs.io/en/latest/).

If you would like to run tests on remote docker host just specify `DOCKER_HOST` variable before running tox tests.

## Travis CI

Combining molecule and travis CI allows us to test how new PRs will behave when used with multiple ansible versions and multiple operating systems. This also allows use to create test scenarios for different role configurations. As a result we have a quite large test matrix which will take more time than local testing, so please be patient.

## Contributing

See [contributor guideline](CONTRIBUTING.md).

## License

This project is licensed under MIT License. See [LICENSE](/LICENSE) for more details.
