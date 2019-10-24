SHELL:=/bin/bash

ROLE=gcoop-libre.chroot

DEBUG ?= -vv
ENV ?= test
SUDO ?=

INVENTORY=inventory/$(ENV)
HOSTS=$(INVENTORY)/hosts
EXTRA='@$(INVENTORY)/extra_vars.yml'

role: requirements
	echo $(EXTRA)
	cd tests && ansible-playbook $(DEBUG) -i $(HOSTS) $(SUDO) -e $(EXTRA) test.yml

requirements:
	mkdir -p tests/roles
	rm -f tests/roles/$(ROLE)
	cd tests/roles && ln -s ../../. $(ROLE)

lint:
	cd tests && ansible-lint $(DEBUG) test.yml

plugins/lookup/pass/lookup_plugins/pass.py:
	mkdir -p tests/plugins/lookup
	cd tests && git clone https://github.com/gcoop-libre/ansible-lookup-plugin-pass.git plugins/lookup/pass

dependencies: plugins/lookup/pass/lookup_plugins/pass.py
