# Evaluate using https://github.com/github/hub for creating github releases Issue: belbio/project #10

define release_commands

	git push
	git push --tags  # bumpversion adds a tag with the new version and commits it

endef


.PHONY: json
json:
	bin/convert_to_json.sh


.PHONY: release-major
release-major: json
	@echo Releasing major update
	bumpversion major
	@${release_commands}

.PHONY: release-minor
release-minor: json
	@echo Releasing minor update
	bumpversion minor
	@${release_commands}

.PHONY: release-patch
release-patch: json
	@echo Releasing patch update
	bumpversion patch
	@${release_commands}


.PHONY: tests
tests: venv
	@echo Running tests
	py.test tests


# devbuild: venv
# 	.venv/bin/python setup.py install

# Activate VirtualEnv after making sure it's up to date
.PHONY: venv
venv: .venv/bin/activate
venv/bin/activate: requirements.txt
	test -d venv || virtualenv venv
	venv/bin/pip install -Ur requirements.txt
	touch venv/bin/activate


.PHONY: list  # ensures target is NOT mis-identified with a file of the same name
list:
	@$(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'


.PHONY: help
help:
	@echo "List of commands"
	@echo "   release-{major|minor|patch} -- Deploy a tagged release to github"
	@echo "   help -- This listing "
	@echo "   test -- Run tests"

.PHONY: check
check:
	@echo $(HOME)
