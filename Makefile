.PHONY: all check clean force

objects = $(wildcard *.in)
outputs := $(objects:.in=.txt)

all: $(outputs)

update:
	- touch *.in

force: update all

install: all
	- pip-sync requirements-test.txt

%.txt: %.in
	pip-compile -v --output-file $@ $<

requirements-test.txt: requirements.txt

test.txt: base.txt

check:
	@which pip-compile > /dev/null

clean: check
	- rm *.txt
