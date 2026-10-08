"""Tests for the CLI module."""
import subprocess
import sys

def test_version():
    """Test that version command works."""
    result = subprocess.run(
        [sys.executable, "-m", "git_helper", "--version"],
        capture_output=True,
        text=True,
        cwd="."
    )
    assert result.returncode == 0
    assert "git-helper 0.1.0" in result.stdout

def test_help():
    """Test that help command works."""
    result = subprocess.run(
        [sys.executable, "-m", "git_helper", "--help"],
        capture_output=True,
        text=True,
        cwd="."
    )
    assert result.returncode == 0
    assert "Git workflow helpers" in result.stdout

if __name__ == "__main__":
    test_version()
    test_help()
    print("All tests passed!")
