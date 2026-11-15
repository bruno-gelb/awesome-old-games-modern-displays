# Generic solutions

Wrappers and fix packs that work with many games at once, not just one. If your game isn't in the [per-game solutions](per_game_solutions.md), start here. Back to the [main list](README.md).

## Generic wrappers

Drop-in replacements for old graphics APIs.

- [cnc-ddraw](https://github.com/FunkyFr3sh/cnc-ddraw) - DirectDraw re-implemented on GDI, OpenGL and Direct3D 9 for classic 2D games, with windowed mode, upscaling and shaders.
- [dgVoodoo2](https://github.com/dege-diosg/dgVoodoo2) - Glide and DirectX 1-9 implemented on Direct3D 11/12, with forced resolutions, MSAA and widescreen options.
- [DDrawCompat](https://github.com/narzoul/DDrawCompat) - DirectDraw and Direct3D 1-7 compatibility, performance and visual fixes for Windows Vista through 11.
- [DxWrapper](https://github.com/elishacloud/dxwrapper) - Wraps DirectX DLLs to fix compatibility issues on Windows 10/11, and loads `.asi` plugins.
- [d3d8to9](https://github.com/crosire/d3d8to9) - Converts Direct3D 8 calls to Direct3D 9, so newer tools and wrappers can hook into old games.
- [DXVK](https://github.com/doitsujin/dxvk) - Direct3D 8-11 on Vulkan, mainly for Linux and Wine, but also useful on Windows.

## Fix packs and frameworks

Collections of fixes for many games, and the plumbing they rely on.

- [WidescreenFixesPack](https://github.com/ThirteenAG/WidescreenFixesPack) - Plugins that add or improve widescreen support in dozens of games.
- [AlphaYellowWidescreenFixes](https://github.com/alphayellow1/AlphaYellowWidescreenFixes) - Memory patches that fix resolution, aspect ratio, FOV and HUD in old PC games.
- [Ultimate ASI Loader](https://github.com/ThirteenAG/Ultimate-ASI-Loader) - Proxy DLL that loads `.asi` plugins into any game; most widescreen fixes depend on it.
- [Special K](https://github.com/SpecialKO/SpecialK) - Swiss Army knife of PC gaming: resolution, frame pacing, HDR and windowing tweaks.
