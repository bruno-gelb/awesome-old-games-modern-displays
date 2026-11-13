# Awesome Old Games on Modern Displays [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> Mods, wrappers and patches that let old PC games run properly on modern displays: high and widescreen resolutions,
> correct aspect ratios, HUD scaling, borderless windows and working graphics on current Windows, Linux and macOS.

## 🔍 [Find your game](games.md)

**Looking for a fix for a specific game? Open [games.md](games.md) and press Ctrl+F.** It indexes 1,000+ games
and the fixes that support each one.

## About

Old games often lock you into 640×480 or 800×600, stretch on a 16:9 or 21:9 screen, or break on modern graphics
APIs. This list collects the tools that fix that, from generic DirectDraw and Glide wrappers to resolution mods
made for a single game.

## Contents

- [Find your game](games.md)
- [Generic wrappers](#generic-wrappers)
- [Fix packs and frameworks](#fix-packs-and-frameworks)
- [Per-game mods](#per-game-mods)
- [Source ports](#source-ports)
- [References](#references)
- [Related lists](#related-lists)

## Generic wrappers

Drop-in replacements for old graphics APIs. They work with many games at once, not just one.

- [cnc-ddraw](https://github.com/FunkyFr3sh/cnc-ddraw) - DirectDraw re-implemented on GDI, OpenGL and Direct3D 9 for
  classic 2D games, with windowed mode, upscaling and shaders.
- [dgVoodoo2](https://github.com/dege-diosg/dgVoodoo2) - Glide and DirectX 1-9 implemented on Direct3D 11/12, with
  forced resolutions, MSAA and widescreen options.
- [DDrawCompat](https://github.com/narzoul/DDrawCompat) - DirectDraw and Direct3D 1-7 compatibility, performance and
  visual fixes for Windows Vista through 11.
- [DxWrapper](https://github.com/elishacloud/dxwrapper) - Wraps DirectX DLLs to fix compatibility issues on
  Windows 10/11, and loads `.asi` plugins.
- [d3d8to9](https://github.com/crosire/d3d8to9) - Converts Direct3D 8 calls to Direct3D 9, so newer tools and
  wrappers can hook into old games.
- [DXVK](https://github.com/doitsujin/dxvk) - Direct3D 8-11 on Vulkan, mainly for Linux and Wine, but also useful
  on Windows.

## Fix packs and frameworks

Collections of fixes for many games, and the plumbing they rely on.

- [WidescreenFixesPack](https://github.com/ThirteenAG/WidescreenFixesPack) - Plugins that add or improve widescreen
  support in dozens of games.
- [AlphaYellowWidescreenFixes](https://github.com/alphayellow1/AlphaYellowWidescreenFixes) - Memory patches that fix
  resolution, aspect ratio, FOV and HUD in old PC games.
- [Ultimate ASI Loader](https://github.com/ThirteenAG/Ultimate-ASI-Loader) - Proxy DLL that loads `.asi` plugins
  into any game; most widescreen fixes depend on it.
- [Special K](https://github.com/SpecialKO/SpecialK) - Swiss Army knife of PC gaming: resolution, frame pacing, HDR
  and windowing tweaks.

## Per-game mods

Resolution mods and wrappers built for one game or series. Sorted by game.

- [BlitzkriegPatch](https://github.com/brian8544/BlitzkriegPatch) - Blitzkrieg (2003) at resolutions above the
  original limit.
- [DisciplesGL](https://github.com/rootext/disciples-gl-builds) - OpenGL wrapper for Disciples and Disciples II,
  with proper windowed mode and upscale filters on Windows 10/11.
- [Tzar Resolution Mod](https://github.com/bruno-gelb/ttbotc_resolution_mod) - Tzar: The Burden of the Crown (2000)
  at widescreen resolutions, up to 21:9.

## Source ports

Engine re-implementations usually support modern resolutions out of the box, and they deserve a list of their own.
See [Awesome Game Remakes](https://github.com/radek-sprta/awesome-game-remakes).

## References

- [PCGamingWiki](https://www.pcgamingwiki.com) - Per-game pages with known issues and fixes, plus a library of
  unofficial patches.
- [Widescreen Gaming Forum](https://www.wsgf.org) - Widescreen support ratings and fixes per game.
- [VOGONS](https://www.vogons.org) - Forum for running old games on modern hardware; home of many wrappers.

## Related lists

Neighboring lists and collections with a different focus.

- [Awesome Game Remakes](https://github.com/radek-sprta/awesome-game-remakes) - Open-source remakes and source
  ports of classic games.
- [Awesome Unofficial PC Ports](https://github.com/Sebastrion/awesome-unofficial-pc-ports) - Unofficial PC ports of
  console games.
- [OldGameFixes](https://github.com/faithvoid/OldGameFixes) - Compilation of fixes to get older games working on
  newer hardware.
- [OldGamesFixes](https://github.com/Simorss/OldGamesFixes) - Compatibility fixes and patches for older games, with
  some Italian localization patches.

## Contributing

Contributions welcome! Read the [contribution guidelines](contributing.md) first.
