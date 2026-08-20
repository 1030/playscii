#!/bin/sh
set -eu

ROOT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
cd "$ROOT_DIR"

if ! command -v brew >/dev/null 2>&1; then
    echo "Homebrew is required: https://brew.sh" >&2
    exit 1
fi

BREW_PREFIX=$(brew --prefix)
for formula in sdl2_mixer sdl3; do
    if ! brew list --versions "$formula" >/dev/null 2>&1; then
        echo "Missing dependency. Install it with: brew install $formula" >&2
        exit 1
    fi
done

PYTHON=${PYTHON:-python3}
if [ ! -x .venv/bin/python ]; then
    "$PYTHON" -m venv .venv
fi

.venv/bin/python -m pip install --upgrade pip
.venv/bin/python -m pip install -r requirements.txt

export PLAYSCII_BREW_PREFIX="$BREW_PREFIX"
rm -rf build dist
.venv/bin/pyinstaller --noconfirm --clean playscii_mac.spec

codesign --force --deep --sign - dist/Playscii.app
mkdir -p dist/dmg
ln -s /Applications dist/dmg/Applications
cp -R dist/Playscii.app dist/dmg/Playscii.app
rm -f "dist/Playscii-$(cat version)-macOS-arm64.dmg"
hdiutil create -quiet -volname Playscii -srcfolder dist/dmg \
    -ov -format UDZO "dist/Playscii-$(cat version)-macOS-arm64.dmg"
rm -rf dist/dmg

echo "Built dist/Playscii.app"
echo "Built dist/Playscii-$(cat version)-macOS-arm64.dmg"
