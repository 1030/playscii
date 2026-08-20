# -*- mode: python ; coding: utf-8 -*-

import os
from pathlib import Path

root = Path(SPECPATH)
brew_prefix = Path(os.environ.get("PLAYSCII_BREW_PREFIX", "/opt/homebrew"))

datas = [
    (str(root / "README.md"), "."),
    (str(root / "license.txt"), "."),
    (str(root / "version"), "."),
]
for pattern in ("*.cfg.default", "art", "charsets", "palettes", "artscripts",
                "formats", "shaders", "games", "ui", "docs/html"):
    for path in root.glob(pattern):
        destination = "." if path.is_file() else str(path.relative_to(root))
        datas.append((str(path), destination))

binaries = [
    (str(brew_prefix / "lib/libSDL2-2.0.0.dylib"), "."),
    (str(brew_prefix / "lib/libSDL2_mixer-2.0.0.dylib"), "."),
    # sdl2-compat loads SDL3 with dlopen(), so dependency scanning cannot
    # discover it. Preserve the exact filename its runtime loader requests.
    (str(brew_prefix / "lib/libSDL3.dylib"), "."),
]

a = Analysis(
    [str(root / "playscii.py")],
    pathex=[str(root)],
    binaries=binaries,
    datas=datas,
    hiddenimports=[],
)
pyz = PYZ(a.pure)
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="playscii",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=False,
    target_arch="arm64",
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=False,
    name="playscii",
)
app = BUNDLE(
    coll,
    name="Playscii.app",
    icon=str(root / "ui/playscii.icns"),
    bundle_identifier="net.jplebreton.playscii",
    info_plist={
        "CFBundleDisplayName": "Playscii",
        "CFBundleShortVersionString": (root / "version").read_text().strip(),
        "LSMinimumSystemVersion": "12.0",
        "NSHighResolutionCapable": True,
    },
)
