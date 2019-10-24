# Ansible Role: gcoop-libre.chroot

This role, install and configure chroot enviroment with schroot.

## Requirements

None.

## Role Variables

Available variables with default values in `defaults/main/defaults.yml`.

## Dependencies

None.

## Example Playbook

If you want to configure a chroot Ubuntu Xenial i386.

```yaml
---

- name: Install and configure chroot enviroment
  hosts: [test]

  roles:
    - role: gcoop-libre.chroot
      chroot_arch: i386
      chroot_os: ubuntu
      chroot_users: xenial
      chroot_version: xenial

```

## Use chroot

List all chroots:

```

schroot -l

```

Execute command into chroot:

```

schroot -c ubuntu-xenial-i386 -u xenial -- cat /etc/debian_chroot

```

## License

GNU General Public License, GPLv3.

## Author Information

This role was created in 2019 by
 [Osiris Alejandro Gomez](http://osiux.com/), worker cooperative of
 [gcoop Cooperativa de Software Libre](http://www.gcoop.coop/).
