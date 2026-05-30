# sddm-fingerprint

![Version](https://img.shields.io/badge/SDDM-0.21.0-blue)
![Status](https://img.shields.io/badge/Status-Working-brightgreen)
![Arch](https://img.shields.io/badge/Arch-Linux-1793d1?logo=arch-linux)
![AUR](https://img.shields.io/aur/version/sddm-fingerprint)

Patched SDDM with proper parallel fingerprint + password authentication. Touch your finger at the login screen without pressing Enter first — just like Windows Hello or GDM.

---

## What's Different

Stock SDDM only starts PAM authentication after you press Enter, making fingerprint unusable on idle. Two patches are applied here:

| Patch | Author | What it does |
|-------|--------|--------------|
| [PR #1220](https://github.com/sddm/sddm/pull/1220) | Sasasu | Starts fingerprint polling in background when greeter loads |
| Parallel auth fix | xCaptaiN09 | Stops fingerprint process when password is submitted, allowing both methods to work independently |

Without the parallel auth fix, PR #1220 alone causes password login to fail with `Existing authentication ongoing, aborting`.

---

## Install

```bash
yay -S sddm-fingerprint
```

Then add to `/etc/sddm.conf.d/fingerprint.conf`:

```ini
[Fingerprintlogin]
User=yourusername
```

Restart SDDM:

```bash
sudo systemctl restart sddm
```

---

## Requirements

- Fingerprint sensor supported by `libfprint`
- Finger enrolled via `fprintd-enroll`
- For Samsung Galaxy Book 4 (FocalTech FT9365, `2808:6553`): install [`libfprint-ft9365`](https://aur.archlinux.org/packages/libfprint-ft9365) first

---

## Behavior

| Action | Result |
|--------|--------|
| Touch finger at login screen | Instant login |
| Type password + Enter | Login after ~300ms (fingerprint process terminates) |
| Wrong finger | Falls through to password |

---

## PAM Setup

The package installs `/etc/pam.d/sddm-fingerprint`. Your `/etc/pam.d/sddm` should be stock — no manual fprintd lines needed.

---

## Upstream Status

PR #1220 has been open for 6 years and is not merged. This package will be maintained until either:
- PR #1220 merges and SDDM ships native support
- KDE's [plasma-login-manager](https://invent.kde.org/plasma/plasma-login-manager) replaces SDDM

---

## Credits

- **[Sasasu](https://github.com/Sasasu)** — PR #1220, fingerprint background polling
- **[xCaptaiN09](https://github.com/xCaptaiN09)** — parallel auth fix, AUR packaging

---

## License

GPL-2.0-or-later (same as SDDM)
