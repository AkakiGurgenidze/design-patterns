import pytest

from versionManager.version_manager import VersionManager, FakeHistory, FixedHistory, RecoveryCounter, EmptyHistory


def test_should_bump_patch():
    vm = VersionManager("0.0.1")

    vm.patch()
    assert vm.release() == "0.0.2"

    vm.patch()
    assert vm.release() == "0.0.3"


def test_should_bump_minor():
    vm = VersionManager("0.2.0")

    vm.minor()
    assert vm.release() == "0.3.0"

    vm.minor()
    assert vm.release() == "0.4.0"


def test_should_reset_patch_after_bumping_minor():
    assert VersionManager("0.2.1").minor().release() == "0.3.0"


def test_should_bump_major():
    vm = VersionManager("1.0.0")

    vm.major()
    assert vm.release() == "2.0.0"

    vm.major()
    assert vm.release() == "3.0.0"


def test_should_reset_minor_patch_after_bumping_major():
    assert VersionManager("1.1.1").major().release() == "2.0.0"


def test_should_record_history():
    history = FakeHistory()
    vm = VersionManager("1.1.1", history)

    vm.patch()
    vm.minor()
    vm.major()
    vm.patch()

    assert history.stories == ["1.1.1", "1.1.2", "1.2.0", "2.0.0"]


def test_should_recover_from_history():
    history = FixedHistory("1.1.2")
    vm = VersionManager("1.1.1", history)

    vm.rollback()

    assert vm.release() == "1.1.2"


def test_should_rollback_multiple_versions():
    history = RecoveryCounter()
    vm = VersionManager("1.1.1", history)

    vm.rollback()
    vm.rollback()

    assert history.recovery_count == 2


def test_should_fail_to_rollback_when_history_is_empty():
    vm = VersionManager("1.1.1", EmptyHistory())

    with pytest.raises(IndexError):
        vm.rollback()
