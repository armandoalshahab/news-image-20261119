"""Copy entry.png to the make.fun output directory.

Entry for make.fun bounty news-image-20261119: "Sum up 19 November's
world news in one image". The image is a news poster for Thursday
19 November 2026 (Shenzhen summit, Crimea bridge strike, Gulf strikes,
ICJ Rohingya verdict, COP31 Antalya, Bangladesh unrest). This program
only copies the image; it needs no network and uses only the standard
library, so both runs write identical bytes.
"""

import os
import shutil
from pathlib import Path


def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    src = Path(__file__).resolve().parent / "entry.png"
    if not src.is_file():
        raise FileNotFoundError(f"entry.png not found next to main.py: {src}")
    shutil.copyfile(src, out_dir / "entry.png")


if __name__ == "__main__":
    main()
