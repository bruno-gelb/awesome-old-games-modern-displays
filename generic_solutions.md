# Generic solutions

Wrappers and fix packs that work with many games at once, not just one. If your game isn't in the [per-game solutions](per_game_solutions.md), start here.

## Which one should I try?

What decides it is almost always the graphics API the game uses, not the game itself: each wrapper replaces specific DirectX, Glide or OpenGL DLLs.

1. Check for a fix made for your game first: the [per-game solutions](per_game_solutions.md), the releases of WidescreenFixesPack and AlphaYellowWidescreenFixes below (each release is named after its game), and the game's [PCGamingWiki](https://www.pcgamingwiki.com) page. A dedicated fix usually handles the HUD, FOV and menus too.
2. Find out which graphics API the game uses: the «API» table near the bottom of its PCGamingWiki page, or the DLLs its executable loads ([Dependencies](https://github.com/lucasg/Dependencies) on Windows, `objdump -p game.exe | grep "DLL Name"` on Linux). Look for `ddraw.dll`, `d3d8.dll`, `d3d9.dll`, `glide2x.dll` / `glide3x.dll` or `opengl32.dll`.
3. Pick the wrappers for that API in the table, and try them one at a time, in order. Most are a DLL you put in the game's folder, so each try is easy to undo. Don't stack two wrappers for the same API.
4. Set the resolution, scaling and window mode in the wrapper's own settings.

| Graphics API | Try, in order |
|---|---|
| DirectDraw, 2D only (`ddraw.dll`) | cnc-ddraw, DDrawCompat, dgVoodoo2 |
| Direct3D 1-7, 3D (`ddraw.dll`) | dgVoodoo2, DDrawCompat, DxWrapper (cnc-ddraw doesn't support Direct3D) |
| Glide, 3dfx (`glide2x.dll`, `glide3x.dll`) | dgVoodoo2 |
| Direct3D 8 (`d3d8.dll`) | d3d8to9 (opens the game to Direct3D 9 tools), dgVoodoo2, DXVK |
| Direct3D 9 (`d3d9.dll`) | Special K, DXVK |
| OpenGL (`opengl32.dll`) | Special K; generic wrappers rarely help, so look for a source port |
| Any of these on Linux or Steam Deck | DXVK for Direct3D 8-11; for older APIs, dgVoodoo2 first, so DXVK gets Direct3D 11 |

This is a starting point, not a compatibility list: some games mix APIs, ship their own `ddraw.dll`, or check the screen size themselves. Each tool's own page has its known issues.

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
