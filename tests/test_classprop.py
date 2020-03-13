#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `classprop` package."""

import pytest

from classprop import ClassPropertyMetaClass, classprop


class TestClassWithMetaclass(metaclass=ClassPropertyMetaClass):

    _bar = ""

    @classprop
    def my_class_prop(self) -> str:
        return self._bar

    @my_class_prop.setter
    def my_class_prop(self, value: str) -> None:
        self._bar = value


class TestClass:
    _bar = ""

    @classprop
    def my_class_prop(self) -> str:
        return self._bar

    @my_class_prop.setter
    def my_class_prop(self, value: str) -> None:
        self._bar = value

    @classprop
    @classmethod
    def my_class_prop2(cls) -> str:
        return cls._bar

    @my_class_prop2.setter
    @classmethod
    def my_class_prop2(cls, value: str) -> None:
        cls._bar = value


@pytest.fixture(autouse=True)
def wrap_tests():
    """Make sure to reset class variables for each test"""
    default = "Hello, World"
    TestClassWithMetaclass._bar = default
    TestClass._bar = default
    yield
    TestClassWithMetaclass._bar = default
    TestClass._bar = default


def test_classprop() -> None:
    foo = TestClass()
    assert foo.my_class_prop == "Hello, World"

    baz = TestClass()
    assert baz.my_class_prop == "Hello, World"

    baz.my_class_prop = "Changed"  # type: ignore
    assert foo.my_class_prop == "Changed"

    TestClass.my_class_prop = "Should be same for all instances"  # type: ignore
    assert baz.my_class_prop == "Should be same for all instances"
    assert foo.my_class_prop == "Should be same for all instances"


def test_classprop_metaclass() -> None:
    foo = TestClassWithMetaclass()
    assert foo.my_class_prop == "Hello, World"

    baz = TestClassWithMetaclass()
    assert baz.my_class_prop == "Hello, World"

    baz.my_class_prop = "Changed"  # type: ignore
    assert foo.my_class_prop == "Changed"

    TestClassWithMetaclass.my_class_prop = "Should be same for all instances"  # type: ignore
    assert baz.my_class_prop == "Should be same for all instances"
    assert foo.my_class_prop == "Should be same for all instances"


def test_classprop2() -> None:
    foo = TestClass()
    assert foo.my_class_prop2 == "Hello, World"

    baz = TestClass()
    assert baz.my_class_prop2 == "Hello, World"

    baz.my_class_prop2 = "Changed"  # type: ignore
    assert foo.my_class_prop2 == "Changed"

    TestClass.my_class_prop2 = "Should be same for all instances"  # type: ignore
    assert baz.my_class_prop2 == "Should be same for all instances"
    assert foo.my_class_prop2 == "Should be same for all instances"


def test_classprop_setattr() -> None:
    foo = TestClass()
    assert foo.my_class_prop == "Hello, World"

    baz = TestClass()
    assert baz.my_class_prop == "Hello, World"

    setattr(TestClass, "my_class_prop", "Changed")
    assert foo.my_class_prop == "Changed"

    setattr(TestClass, "my_class_prop", "Should be same for all instances")
    assert baz.my_class_prop == "Should be same for all instances"
    assert foo.my_class_prop == "Should be same for all instances"
