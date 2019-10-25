#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


@pytest.mark.parametrize("name", [
    "debootstrap",
    "schroot",
    "xauth",
])
def test_packages(host, name):
    # type: (testinfra.host.Host, str) -> None
    pkg = host.package(name)
    assert pkg.is_installed


def test_dpkg_archs(host):
    # type: (testinfra.host.Host) -> None
    command = "dpkg --print-foreign-architectures"
    execution = host.run(command)
    assert 'i386' in execution.stdout


def test_schroot_creation(host):
    # type: (testinfra.host.Host) -> None
    command = "schroot -l"
    execution = host.run(command)
    assert 'i386' in execution.stdout


@pytest.mark.parametrize("name", [
])
def test_schroot_packages(host, name):
    # type: (testinfra.host.Host) -> None
    chroot_name = 'ubuntu-xenial-i386'
    schroot_query = host.run(
        'schroot -c ' + chroot_name + ' -u root -- apt-cache policy ' + name)
    assert 'Installed: (none)' not in schroot_query.stdout
