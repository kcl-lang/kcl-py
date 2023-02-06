# Copyright 2021 The KCL Authors. All rights reserved.

PROJECT_NAME = KCLVM

PWD:=$(shell pwd)

BUILD_IMAGE:=kusionstack/kclvm-builder

# export DOCKER_DEFAULT_PLATFORM=linux/amd64
# or
# --platform linux/amd64

RUN_IN_DOCKER:=docker run -it --rm
RUN_IN_DOCKER+=-v ~/.ssh:/root/.ssh
RUN_IN_DOCKER+=-v ~/.gitconfig:/root/.gitconfig
RUN_IN_DOCKER+=-v ~/go/pkg/mod:/go/pkg/mod
RUN_IN_DOCKER+=-v ${PWD}:/root/kclvm
RUN_IN_DOCKER+=-w /root/kclvm ${BUILD_IMAGE}

run:
	python3 -m kclvm ./samples/hello.k

fmt:
	python3 -m pip install black
	python3 -m black kclvm

lint:
	python3 -m pip install flake8
	python3 -m flake8 kclvm --config .flake8

sh-in-docker:
	${RUN_IN_DOCKER} bash

test-grammar:
	export PYTHONPATH=${PWD} && ./internal/scripts/test_grammar.sh && cd ${PWD}

test-konfig:
	export PYTHONPATH=${PWD} && ./internal/scripts/test_konfig.sh && cd ${PWD}

test-unit:
	export PYTHONPATH=${PWD} && ./internal/scripts/test_unit.sh && cd ${PWD}
