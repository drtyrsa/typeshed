from _typeshed import Self
from abc import abstractmethod
from typing import Pattern, Text, Tuple, TypeVar

_T = TypeVar("_T", bound=Version)

class Version:
    def __repr__(self) -> str: ...
    @abstractmethod
    def __init__(self, vstring: Text | None = ...) -> None: ...
    @abstractmethod
    def parse(self: Self, vstring: Text) -> Self: ...
    @abstractmethod
    def __str__(self) -> str: ...
    @abstractmethod
    def __cmp__(self: _T, other: _T | str) -> bool: ...

class StrictVersion(Version):
    version_re: Pattern[str]
    version: Tuple[int, int, int]
    prerelease: Tuple[Text, int] | None
    def __init__(self, vstring: Text | None = ...) -> None: ...
    def parse(self: Self, vstring: Text) -> Self: ...
    def __str__(self) -> str: ...
    def __cmp__(self: _T, other: _T | str) -> bool: ...

class LooseVersion(Version):
    component_re: Pattern[str]
    vstring: Text
    version: Tuple[Text | int, ...]
    def __init__(self, vstring: Text | None = ...) -> None: ...
    def parse(self: Self, vstring: Text) -> Self: ...
    def __str__(self) -> str: ...
    def __cmp__(self: _T, other: _T | str) -> bool: ...
