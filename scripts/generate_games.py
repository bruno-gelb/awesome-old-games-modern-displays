"""Generate games.md: a Ctrl+F-searchable index of games and the fixes that support them.

Sources:
- per-game mods listed in README.md (MANUAL below, keep in sync by hand),
- release pages of WidescreenFixesPack and AlphaYellowWidescreenFixes (one release per game),
- the «Supported Games» list in the cnc-ddraw README.

Usage: python scripts/generate_games.py   (set GITHUB_TOKEN to avoid the API rate limit)
"""

import json
import os
import re
import urllib.request
from pathlib import Path

API = "https://api.github.com"
OUT = Path(__file__).resolve().parent.parent / "games.md"

# Game name -> list of (link text, url). Per-game mods from README.md.
MANUAL = {
    "Blitzkrieg": [("BlitzkriegPatch", "https://github.com/brian8544/BlitzkriegPatch")],
    "Disciples: Sacred Lands": [("DisciplesGL", "https://github.com/rootext/disciples-gl-builds")],
    "Disciples II: Dark Prophecy": [("DisciplesGL", "https://github.com/rootext/disciples-gl-builds")],
    "Majesty Gold HD": [
        ("Majesty Gold HD Resolution Mod", "https://github.com/bruno-gelb/mghd_resolution_mod")
    ],
    "Tzar: The Burden of the Crown": [
        ("Tzar Resolution Mod", "https://github.com/bruno-gelb/ttbotc_resolution_mod")
    ],
}

# Emulator tags in WidescreenFixesPack release names.
PLATFORMS = {
    "PPSSPP": "PSP, PPSSPP",
    "PCSX2F": "PS2, PCSX2 Fork",
    "+PCSX2F": "PC and PS2",
    "CXBXR": "Xbox, Cxbx-Reloaded",
    "Dolphin": "GameCube, Dolphin",
}


def get(url: str) -> bytes:
    request = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
    if token := os.environ.get("GITHUB_TOKEN"):
        request.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(request) as response:
        return response.read()


def releases(repo: str) -> list[dict]:
    result, page = [], 1
    while batch := json.loads(get(f"{API}/repos/{repo}/releases?per_page=100&page={page}")):
        result += batch
        page += 1
    return result


def wfp() -> list[tuple[str, str, str]]:
    entries = []
    pattern = re.compile(r"^(.*?)\s+(Fusion Fix|Widescreen Fix|FOV Fix)\s*(?:\[(.+)\])?$")
    for release in releases("ThirteenAG/WidescreenFixesPack"):
        name = release["name"].strip()
        if name.startswith("[Archived]") or not (match := pattern.match(name)):
            continue
        game, kind, tag = match.groups()
        label = f"WidescreenFixesPack: {kind}" + (f" ({PLATFORMS.get(tag, tag)})" if tag else "")
        entries.append((game, label, release["html_url"]))
    return entries


def alphayellow() -> list[tuple[str, str, str]]:
    entries = []
    for release in releases("alphayellow1/AlphaYellowWidescreenFixes"):
        game, sep, kind = release["name"].strip().rpartition(" - ")
        if not sep or "Finder" in kind:
            continue
        entries.append((game, f"AlphaYellow: {kind}", release["html_url"]))
    return entries


def cnc_ddraw() -> list[tuple[str, str, str]]:
    readme = json.loads(get(f"{API}/repos/FunkyFr3sh/cnc-ddraw/readme"))
    text = get(readme["download_url"]).decode()
    section = text.split("### Supported Games", 1)[1].split("\n\n", 1)[0]
    games = [line[2:].strip() for line in section.splitlines() if line.startswith("- ")]
    url = "https://github.com/FunkyFr3sh/cnc-ddraw"
    return [(game, "cnc-ddraw", url) for game in games if game != "..."]


# Source spelling -> one canonical name, for duplicates that normalization in key() can't catch,
# and for abbreviations that Ctrl+F wouldn't find («San Andreas» in «GTA SA»).
ALIASES = {
    "Grand Theft Auto (1)": "Grand Theft Auto",
    "Disciples": "Disciples: Sacred Lands",
    "Carmageddon 2": "Carmageddon II: Carpocalypse Now",
    "Total Annihilation (Unofficial Beta Patch v3.9.02)": "Total Annihilation",
    "GTA III The Definitive Edition": "Grand Theft Auto III: The Definitive Edition",
    "GTA VC The Definitive Edition": "Grand Theft Auto: Vice City - The Definitive Edition",
    "GTA SA The Definitive Edition": "Grand Theft Auto: San Andreas - The Definitive Edition",
    "GTA Chinatown Wars": "Grand Theft Auto: Chinatown Wars",
    "GTA Liberty City Stories": "Grand Theft Auto: Liberty City Stories",
    "Grand Theft Auto Liberty City Stories": "Grand Theft Auto: Liberty City Stories",
    "GTA Vice City Stories": "Grand Theft Auto: Vice City Stories",
    "Grand Theft Auto Vice City Stories": "Grand Theft Auto: Vice City Stories",
}

ROMAN = {"ii": "2", "iii": "3", "iv": "4"}


def key(name: str) -> str:
    """Merge key: case, punctuation, articles, «GTA» and roman numerals don't matter."""
    name = name.lower().replace("&", "and")
    name = re.sub(r"^gta\b", "grand theft auto", name)
    name = re.sub(r"\b(the|a|an)\b", " ", name)
    name = re.sub(r"\b(ii|iii|iv)\b", lambda match: ROMAN[match.group()], name)
    return re.sub(r"[^a-z0-9]", "", name)


def sort_key(name: str) -> str:
    return re.sub(r"[^a-z0-9]", "", name.lower())


def main() -> None:
    games: dict[str, tuple[str, list[tuple[str, str]]]] = {}
    sources = [(game, text, url) for game, links in MANUAL.items() for text, url in links]
    sources += wfp() + alphayellow() + cnc_ddraw()
    for game, text, url in sources:
        game = ALIASES.get(game, game)
        name, links = games.setdefault(key(game), (game, []))
        if (text, url) not in links:
            links.append((text, url))

    by_letter: dict[str, list[tuple[str, list[tuple[str, str]]]]] = {}
    for name, links in sorted(games.values(), key=lambda item: sort_key(item[0])):
        letter = name[0].upper() if name[0].isalpha() else "0-9"
        by_letter.setdefault(letter, []).append((name, links))

    lines = [
        "# Games",
        "",
        "Every game covered by the list, with the fixes that support it. Use Ctrl+F to find yours.",
        "",
        f"{len(games)} games. Generated by [generate_games.py](scripts/generate_games.py) from the per-game mods in the "
        "[README](README.md), the releases of [WidescreenFixesPack](https://github.com/ThirteenAG/WidescreenFixesPack) "
        "and [AlphaYellowWidescreenFixes](https://github.com/alphayellow1/AlphaYellowWidescreenFixes), and the "
        "[supported games](https://github.com/FunkyFr3sh/cnc-ddraw#supported-games) of cnc-ddraw. Don't edit by hand.",
        "",
        "Not finding your game? Generic wrappers like [dgVoodoo2](https://github.com/dege-diosg/dgVoodoo2) and "
        "[DDrawCompat](https://github.com/narzoul/DDrawCompat) work with many games they don't list, and "
        "[PCGamingWiki](https://www.pcgamingwiki.com) has a page for almost every game.",
        "",
        " · ".join(f"[{letter}](#{letter.lower()})" for letter in by_letter),
        "",
    ]
    for letter, entries in by_letter.items():
        lines += [f"## {letter}", "", "| Game | Fixes |", "|---|---|"]
        for name, links in entries:
            fixes = ", ".join(f"[{text}]({url})" for text, url in links)
            lines.append(f"| {name.replace('|', '/')} | {fixes} |")
        lines.append("")
    OUT.write_text("\n".join(lines))
    print(f"{OUT.name}: {len(games)} games")


if __name__ == "__main__":
    main()
