# 🧰 Generic solutions

Wrappers and fix packs that work with many games at once, not just one. If your game isn't in the [per-game solutions](README.md#-per-game-solutions), start here.

## Which one should I try?

### Not technical? Start here

Someone has usually already found the fix for your game. These steps help you find where they wrote it down.

1. **Open the game's [PCGamingWiki](https://www.pcgamingwiki.com) page** and scroll to «Video». The «Widescreen resolution», «Ultra-widescreen» and «4K Ultra HD» rows show whether the game handles them on its own, and if it doesn't, how to fix it, step by step. Often that's just «download this, copy these files into the game's folder».
2. **Check whether you need a fix at all.** GOG versions of old games often come with a fix already set up, Steam re-releases sometimes get official patches, and on Steam Deck or Linux many old games just work through Proton.
3. **Search the game's Steam guides.** On its Steam page, open Community Hub → Guides and search for «widescreen» or «ultrawide»: these guides are written for players, with screenshots.
4. **Search the web** for «*game name* widescreen fix» or «*game name* ultrawide». «Fix» finds more than «mod» or «patch».
5. **Still nothing? Try one by the game's look and age.** A rough rule, not an exact one:
   - Looks 2D, like Diablo, StarCraft or Age of Empires: **cnc-ddraw**. It has a list of games it supports and a settings program, so there's no config file to edit.
   - Looks 3D and came out around 1997-2003: **dgVoodoo2**.
   - Newer than that: **Special K**.

   Each one is a few files you copy into the game's folder. If it doesn't help, delete them and the game is as it was.

### For the technically minded

What decides it is almost always the graphics API the game uses, not the game itself: each wrapper replaces specific DirectX, Glide or OpenGL DLLs.

1. Check for a fix made for your game first: the [per-game solutions](README.md#-per-game-solutions), the releases of WidescreenFixesPack and AlphaYellowWidescreenFixes below (each release is named after its game), and the game's [PCGamingWiki](https://www.pcgamingwiki.com) page. A dedicated fix usually handles the HUD, FOV and menus too.
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
