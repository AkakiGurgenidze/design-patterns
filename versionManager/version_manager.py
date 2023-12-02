# https://www.codewars.com/kata/5bc7bb444be9774f100000c3
# Implement a VersionManager class.
#
# It should accept an optional parameter that represents the initial version.
# The input will be in one of the following formats:
#   - "{MAJOR}"
#   - "{MAJOR}.{MINOR}"
#   - "{MAJOR}.{MINOR}.{PATCH}".
# More values may be provided after PATCH, but they should be ignored.
# If these 3 parts are not decimal values,
# raise "Error occured while parsing version!" exception.
# If the initial version is not provided or is an empty string, use "0.0.1" by default.
#
# This class should support the following methods,
# all of which should be chainable (except release):
#
# patch() - increase PATCH by 1
# minor() - increase MINOR by 1, set PATCH to 0
# major() - increase MAJOR by 1, set MINOR and PATCH to 0
# release() - return a string in the format "{MAJOR}.{MINOR}.{PATCH}"
# rollback() - return the MAJOR, MINOR, and PATCH to their previous values.
#   before the last major/minor/patch call, or raise an exception
#   with the message "Cannot roll back!" if there's no version to roll back to.
#   Multiple calls to rollback() should be possible and restore the version history
#


from dataclasses import dataclass, field
from typing import Protocol, Self


class Resettable(Protocol):
    def reset(self) -> None:
        pass


class NoReset:
    def reset(self) -> None:
        pass


@dataclass
class Version:
    value: int

    following: Resettable = field(default_factory=NoReset)

    def bump(self) -> None:
        self.value += 1
        self.following.reset()

    def reset(self) -> None:
        self.value = 0
        self.following.reset()

    def __str__(self) -> str:
        return str(self.value)


class History(Protocol):
    def record(self, story: str) -> None:
        pass

    def recover(self) -> str:
        pass


class NoHistory:
    def record(self, story: str) -> None:
        pass

    def recover(self) -> str:
        pass


@dataclass
class VersionManager:
    initial: str

    history: History = field(default_factory=NoHistory)

    _major: Version = field(init=False)
    _minor: Version = field(init=False)
    _patch: Version = field(init=False)

    def __post_init__(self) -> None:
        self._load(self.initial)

    def _load(self, version: str) -> None:
        major, minor, patch = version.split(".")
        self._patch = Version(int(patch))
        self._minor = Version(int(minor), self._patch)
        self._major = Version(int(major), self._minor)

    def major(self) -> Self:
        self.history.record(self.release())

        self._major.bump()

        return self

    def minor(self) -> Self:
        self.history.record(self.release())

        self._minor.bump()

        return self

    def patch(self) -> Self:
        self.history.record(self.release())

        self._patch.bump()

        return self

    def rollback(self) -> Self:
        self._load(self.history.recover())

        return self

    def release(self) -> str:
        return f"{self._major}.{self._minor}.{self._patch}"


@dataclass
class FakeHistory:
    stories: list[str] = field(default_factory=list)

    def record(self, story: str) -> None:
        self.stories.append(story)

    def recover(self) -> str:
        pass


@dataclass
class FixedHistory:
    story: str

    def record(self, story: str) -> None:
        pass

    def recover(self) -> str:
        return self.story


@dataclass
class RecoveryCounter:
    recovery_count: int = 0

    def record(self, story: str) -> None:
        pass

    def recover(self) -> str:
        self.recovery_count += 1

        return "0.0.0"


class EmptyHistory:
    def record(self, story: str) -> None:
        pass

    def recover(self) -> str:
        raise IndexError
