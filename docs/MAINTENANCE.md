# Maintaining the profile

## Edit and validate

1. Update normal profile copy and product links in the root `README.md`.
2. Edit artwork text and geometry in `scripts/build_assets.py`, then run:

   ```sh
   python3 scripts/build_assets.py
   python3 scripts/validate_assets.py
   python3 scripts/validate_assets.py --check-links
   ```

3. Preview the README on GitHub at desktop and mobile widths, in light and dark themes. Confirm `<picture>` selects each mobile image and all text fits inside SVG boundaries.
4. Commit source and generated assets together. CI checks offline validation and deterministic regeneration. Live URL checks stay manual so temporary website/network failures cannot block copy edits.

Python 3.10+ is sufficient. No pip or npm dependencies are required. The workflow uses the current checkout v7.0.1 release pinned to its immutable commit, with read-only repository permissions. It does not need custom secrets.

## Publishing requirements

The repository must remain public, be named `eyansky` (matching the account name, case insensitive), and have a nonempty root `README.md` on the default branch. No GitHub Pages deployment is needed.

If working from a downloaded copy before publication:

```sh
gh auth status
git init -b main
git add README.md assets docs scripts .github .gitignore
git commit -m "feat(profile): launch premium engineering GitHub profile"
gh repo create Eyansky/eyansky --public --source=. --remote=origin --push
```

Do not rerun repository creation if it already exists. Clone it and apply changes normally instead. Never force-push profile updates. When using HTTPS OAuth authentication, adding a workflow can require the `workflow` scope; SSH push uses the existing SSH authorization.

## Content updates

- Confirm product links still work before changing URLs. Keep a broken product's identity and report the unavailable URL rather than inventing a replacement.
- Add LinkedIn only after confirming the exact account. Email is the address explicitly published on mwangi.dev; update it if that public contact changes.
- Keep employer statements general unless specific roles, dates, and achievements are supplied and approved.
- Do not add unverified achievements, RAG claims, certifications, public-source claims, or activity counts.
- Refresh the pin audit when substantial public repositories change. See `PIN_RECOMMENDATIONS.md`.
- Keep the existing GitHub avatar; this repository does not control it.

## GitHub profile metadata

The launch updated name, bio, location, and website through GitHub's signed-in profile editor and verified them with the public API. The existing CLI token could publish the repository but lacked profile-edit scope; no additional token permissions were requested.

The intended fields are:

```sh
gh api --method PATCH user \
  -f name='Ian Mwangi' \
  -f bio='Senior Software Engineer | Python, Backend, Full-Stack & AI Systems | Building scalable software and products I love.' \
  -f location='Kenya' \
  -f blog='https://www.mwangi.dev' \
  --silent
```

If GitHub rejects this because the CLI lacks `user`/`write:user` permission, edit those four fields at <https://github.com/settings/profile>. There is no reason to change avatar, email visibility, security, or other account settings.
