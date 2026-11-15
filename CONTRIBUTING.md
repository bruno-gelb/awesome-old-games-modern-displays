# Contribution guidelines

Pull requests are welcome. To keep the list useful:

- One pull request per suggestion.
- The project must help old games run on modern displays: resolution, aspect ratio, HUD scaling, windowing, or a graphics API that no longer works properly.
- The game must have been originally released before 2013, on any platform. Later ports, remasters and re-releases of such a game count too (Red Dead Redemption, 2010, ported to PC in 2024, is in).
- Only awesome items, nothing unmaintained or archived. Unmaintained means archived, abandoned by its author, no longer working or downloadable, or a work in progress with no release for 2 years. A finished fix for a finished old game is fine even if it hasn't changed in years.
- Link the project's own page (repository or official site), not a mirror or a reupload.
- Use the format `[Name](link) - Description.`: the description starts with a capital letter and ends with a period.
- Put the entry in the right place, and keep entries sorted by game name.
- Tools that work with many games (wrappers, fix packs) go in [generic_solutions.md](generic_solutions.md), not in `README.md`.
- A new per-game mod gets a row in the [per-game solutions](README.md#-per-game-solutions) for each game it fixes, in alphabetical order. Add a row for each name the game is sold under too (expansions, editions, re-releases), so Ctrl+F finds it by any of them. A name that already shows up in the «Solutions» column, such as a remaster listed as the fix for the original, doesn't need a row of its own.
- If a game already has a fix, still add yours to the same row. Every fix in the «Solutions» column is a bullet of its own, `• [Name](link)`, with `<br>` between bullets: we list every working fix for a game and let the gamer decide.
- Check spelling and grammar, and remove trailing whitespace. Don't hard-wrap lines: one line per paragraph or list item.

## Git workflow

- We follow [trunk-based development](https://trunkbaseddevelopment.com/): `main` is the only long-lived branch. Branch off it, keep your branch small and short-lived, and open the pull request against `main`.
- Write commit messages by [the seven rules](https://cbea.ms/git-commit/): a short, capitalized subject in the imperative mood, with no period at the end, then a blank line and a body that explains what and why.

By contributing, you agree that your contribution is released under [CC0 1.0](LICENSE).
