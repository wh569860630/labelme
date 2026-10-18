from __future__ import annotations

import os
import sys
from pathlib import Path

_DLL_DIRECTORY_HANDLES: list[object] = []

if os.name == "nt" and getattr(sys, "frozen", False):
    frozen_root = Path(sys._MEIPASS)  # type: ignore[attr-defined]
    for dll_dir in (
        frozen_root,
        frozen_root / "PySide6",
        frozen_root / "shiboken6",
    ):
        if dll_dir.is_dir():
            _DLL_DIRECTORY_HANDLES.append(os.add_dll_directory(dll_dir))
