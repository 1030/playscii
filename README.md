# Download Playscii for macOS

## [Download the Apple Silicon DMG](https://github.com/1030/playscii/releases/download/macos-arm64-9.16.3/Playscii-9.16.3-macOS-arm64.dmg)

Native arm64 build for modern Macs. See the [release notes](https://github.com/1030/playscii/releases/tag/macos-arm64-9.16.3) for details.

---

# NOTE!!!

**This repo is a fork intended for my own personal use, and is not kept up-to-date with the official project from JP LeBrenton.**

**If you came here looking for instructions for installing playscii on MacOS, see https://github.com/michael-lazar/playscii/issues/3#issuecomment-1146280788**

## Modern macOS Apple Silicon build

This fork includes a native arm64 build for current macOS releases. The app
uses Python 3.12, current Pillow/NumPy/PyOpenGL/PySDL2 releases, and bundles
the SDL2 compatibility, SDL2_mixer, and SDL3 libraries it needs. It also adds
native trackpad two-finger panning and pinch-to-zoom support.

Download the ready-to-run DMG from this repository's GitHub Releases page, or
build it locally:

```sh
brew install python@3.12 sdl2_mixer sdl3
PYTHON="$(brew --prefix python@3.12)/bin/python3.12" ./build_mac.sh
```

The build script creates `dist/Playscii.app` and a compressed arm64 DMG. The
app is ad-hoc signed for local use; it is not Apple-notarized.

# PLAYSCII - an ASCII art and game creation tool

Playscii (pronounced play-skee) is an art, animation, and game creation tool.
The latest version will always be available here:

* [http://jp.itch.io/playscii](http://jp.itch.io/playscii)
* [https://bitbucket.org/JPLeBreton/playscii](https://bitbucket.org/JPLeBreton/playscii)

Playscii's main website is here:

* [http://vectorpoem.com/playscii/](http://vectorpoem.com/playscii/)

## Offline documentation

Playscii now includes its own HTML documentation, which you can find in the
docs/html/ subfolder of the folder where this README resides.

## Online documentation

The latest version of the HTML documentation resides here:

[http://vectorpoem.com/playscii/howto_main.html](http://vectorpoem.com/playscii/howto_main.html)

## Bugs

If you run into any issues with Playscii, please report a bug here:

[https://bitbucket.org/JPLeBreton/playscii/issues?status=new&status=open](https://bitbucket.org/JPLeBreton/playscii/issues?status=new&status=open)

## Roadmap

For possible future features see Playscii's Trello:

[https://trello.com/b/BLQBXn5H/playscii](https://trello.com/b/BLQBXn5H/playscii)

Please don't take anything there as a promise, though. If you'd find something
on there especially valuable, feel free to vote or comment!

## Contact

If you've made something cool with Playscii and/or have any suggestions on how
to improve it, please let JP know!

[http://vectorpoem.com/contact.html](http://vectorpoem.com/contact.html)
