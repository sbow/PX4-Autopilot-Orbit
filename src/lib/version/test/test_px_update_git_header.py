import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[4]
SCRIPT = REPO_ROOT / "src/lib/version/px_update_git_header.py"


def run_validator(tag: str, tmp_path: Path) -> subprocess.CompletedProcess[str]:
    header = tmp_path / "build_git_version.h"
    return subprocess.run(
        [sys.executable, str(SCRIPT), str(header), "--validate", "--git_tag", tag],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )


def test_accepts_legacy_rc_tag(tmp_path: Path) -> None:
    result = run_validator("v1.6.0rc1-28286-g8d03ec6824", tmp_path)

    assert result.returncode == 0, result.stdout + result.stderr


def test_accepts_current_rc_tag(tmp_path: Path) -> None:
    result = run_validator("v1.9.0-rc3", tmp_path)

    assert result.returncode == 0, result.stdout + result.stderr


def test_rejects_malformed_tag(tmp_path: Path) -> None:
    result = run_validator("not-a-version", tmp_path)

    assert result.returncode != 0
    assert "expected format" in result.stdout
