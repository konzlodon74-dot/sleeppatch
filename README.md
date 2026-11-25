# Fix Human Sleep — Patch Note

[![make.fun](https://make.fun/badge/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27.svg)](https://make.fun/bounty/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27)
[![rank](https://make.fun/badge/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27/konzlodon74-dot/sleeppatch/rank.svg)](https://make.fun/bounty/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27)
[![reward](https://make.fun/badge/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27/konzlodon74-dot/sleeppatch/reward.svg)](https://make.fun/bounty/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27)

Bounty: https://make.fun/bounty/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27

> v9.1.0: Fixed sleep — 'one more episode' loop capped at 1, 3am anxiety reboot now optional, dreams no longer buffer.

## How it works

`main.py` checks the patch note against the 1-160 character single-line gate and writes it as UTF-8 with no trailing newline to `/output/entry.txt`.

## Run

```bash
python3 main.py
```
