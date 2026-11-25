import os
from pathlib import Path

FINAL_LINE = "Our team-building exercise was an escape room, and we escaped in nine minutes, because years of dodging our manager had trained us perfectly."


def emit(line: str) -> None:
    target_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    target_dir.mkdir(parents=True, exist_ok=True)
    (target_dir / "entry.txt").write_text(line, encoding="utf-8")


if __name__ == "__main__":
    emit(FINAL_LINE)
