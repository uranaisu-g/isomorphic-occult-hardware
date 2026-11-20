# The Isomorphic Hardware of Occult Systems (Version 1.2)

> **A Deterministic Mechanical Architecture Unifying Aristotelian Physical Primitives, Dorothean Triplicities, and Wu Xing Dynamics**

[![Specification Version](https://img.shields.io/badge/spec-v1.2-blue.svg)](SPECIFICATION.md)
[![Audit Status](https://img.shields.io/badge/audit-PASSED%20(100%25%20Deterministic)-success.svg)](#audit-verdict)
[![License: MIT / CC BY 4.0](https://img.shields.io/badge/License-MIT%20%2F%20CC--BY--4.0-green.svg)](LICENSE)

---

## Authors & Affiliation
- **Lead Theorist:** Polar Mikami (Studio uranaisu)
- **Systems Architecture & Compiler Implementation:** Nanota Yuzu (Studio uranaisu)
- **Date of First Publication:** November 11, 2026
- **Revision:** November 21, 2026 (Version 1.2)
- **Repository:** [uranaisu-g/isomorphic-occult-hardware](https://github.com/uranaisu-g/isomorphic-occult-hardware)

---

## Executive Summary

For two millennia, traditional astrological and occult systems have suffered from continuous narrative degradation, regressing into moralistic, psychological, and subjective folklore.

This repository establishes the **Version 1.2 specification**, which deconstructs these ancient frameworks into a single, cohesive, deterministic computational hardware model based strictly on:

1. **Four Aristotelian Thermodynamic Primitives:** Hot (Affect/Thrust), Cold (Adapt/Seizure), Dry (Severance/Grid), and Wet (Permeation/Liquid).
2. **Pamela Colman Smith's 1909 Anatomical/Chromatic Encoding:** The absolute mathematical derivation of the Rider-Waite-Smith Minor Arcana Aces through hand anatomy (Clenched Fist vs. Open Palm) and chromatic vectors.
3. **Dorothean Planetary Triplicity Engines:** Hellenistic three-planetary coalitions (e.g., Venus + Mars + Moon) operating as high-friction structural mechanisms.
4. **Isomorphism with Chinese Wu Xing Dynamics:** The materialist thermodynamic proof that **"Metal is Earth" (金は土)** via the physics of the agricultural harvest (desiccation and cold storage). Metal (金) is identical to the *Western earth triplicity* (Taurus / Virgo / Capricorn) because both are Cold × Dry; Wu Xing Earth (土) is the boundary between the hemispheres, not a fifth element of the plane.
5. **Two Diagrams of One Phase Space:** The Taijitu compared with the Cartesian element plane — same two hemispheres and four states, a boundary with thickness rather than a wall, and a seed of the opposite state inside each extreme.
6. **Direction, Season, and Declination:** The four gates (子 north, 卯 east, 未 south, 酉 west), the 24 solar terms as the sun's declination at fifteen-degree intervals, Eastern **Six Harmonies (支合)** as Hellenistic **Solstitial Antiscia**, and **Six Clashes (六冲)** as **180° oppositions**.
7. **Cultural Parallels, Recorded as Parallels:** Five Japanese inheritances that organise practice around the same seasonal mechanics — the refused bride (五黄の寅・丙午), Tori-no-ichi (酉の市), Daikokuten and the rat (大黒天と鼠), the snake's money (巳の金運), and the boar's charge (亥の猪突猛進・亥の子). Each is marked as corroboration only, never as a derivation.

### One name, two things: Western Earth vs. Wu Xing Earth

The specification uses two expressions that must never be swapped:

| Term | What it is | Where it appears |
| :--- | :--- | :--- |
| **Western Earth Triplicity** | Taurus / Virgo / Capricorn = Cold × Dry = **Metal (金)**. A zodiacal element and the Pentacles suit. | §§3, 4.4, 5.1, Figure 1 |
| **Wu Xing Earth (土)** | The extra-elemental **Phase Buffer Interface (`&`)** between the Hot and Cold hemispheres: the centre, the 土用 (Doyō) nodes, the S-curve of the Taijitu. No sign, no suit, no engine — an operator, not a member. | §§5.1, 6 |

### What this specification does *not* claim

Version 1.1 matched each Wu Xing phase to a triple of Earthly Branches and called that triple the phase's "root signs". **That correspondence is withdrawn in 1.2** — a branch is a position on the ecliptic dial and a triplicity is a set of signs, and the match was asserted rather than derived. A phase is defined by its two primitives and by nothing else. The compiler enforces this: `assert_terminology()` fails if any sign or branch table is reintroduced.

---

## Repository Structure

```
.
├── README.md                      # Executive overview and quickstart
├── SPECIFICATION.md               # Complete academic specification paper (v1.2)
├── CITATION.cff                   # Citation metadata for academic indexing
├── LICENSE                        # Dual MIT / Creative Commons Attribution 4.0
├── compiler/
│   └── core_primitives.py         # Python reference compiler & validation assertions
└── figures/
    ├── figure1_minor_arcana_matrix.png     # Minor Arcana Aces x Dorothean engines
    ├── figure2_taijitu_solstice.png        # Taijitu solstitial reversal cores
    └── figure3_celestial_compass.png       # 24-solar-term celestial compass
```

---

## Architectural Diagrams

**Figure 1 — Minor Arcana Aces & Dorothean Planetary Engines** (§3)

![Figure 1: Minor Arcana Matrix](figures/figure1_minor_arcana_matrix.png)

**Figure 2 — Taijitu Solstitial Reversal Cores** (§5.1)

![Figure 2: Taijitu Solstitial Reversal Cores](figures/figure2_taijitu_solstice.png)

**Figure 3 — Celestial Compass & Winter Solstice Sector** (§5.2)

![Figure 3: Celestial Compass](figures/figure3_celestial_compass.png)

---

## Python Reference Compiler Quickstart

The reference compiler provides automated verification against poetic narrative drift:

```bash
cd compiler
python3 core_primitives.py
```

### Programmatic Assertion Example

```python
from compiler.core_primitives import UniversalOccultCompiler, KernelViolationError

# Valid structural statement (PASSES)
valid_stmt = "The Ace of Swords executes sovereign structural constraint via Saturn-Mercury mechanics."
assert UniversalOccultCompiler.validate_statement(valid_stmt)

# Narrative poetic contamination (RAISES KernelViolationError)
try:
    invalid_stmt = "The Cup represents emotional healing vibe and unconditional love."
    UniversalOccultCompiler.validate_statement(invalid_stmt)
except KernelViolationError as e:
    print("System Fault Cleared:", e)

# A phase is a state of two primitives, not a list of signs
assert UniversalOccultCompiler.compile_phase("METAL (金)")["state"] == ("COLD", "DRY")
assert UniversalOccultCompiler.compile_phase("EARTH (土)")["operator"] == "&"

# v1.2 terminology and scope guard: no branch table, no root signs
assert UniversalOccultCompiler.assert_terminology()
```

---

## What Changed in Version 1.2 (2026-11-21)

- **The root-sign table is withdrawn.** The claim that each Wu Xing phase is rooted in a triple of Earthly Branches (三合) matched one-to-one to a Western triplicity is removed from the Abstract, §5, §6, the compiler and this README. `WUXING_ZODIAC_MAPPING`, its `root_signs` fields and the `EARTH_BUFFER` entry built on them are gone; `assert_terminology()` now fails if a sign or branch table returns.
- **The 4-versus-3 count argument is withdrawn** with it. The Western Earth / Wu Xing Earth distinction stands, and is carried by the geometry of the two diagrams (§5.1) instead of by an arithmetic of engines and roots.
- **Figure 1 (Integrated Isomorphic Hardware Matrix) deleted**, with its image file: it condensed the withdrawn branch correspondence and mixed two coordinate systems on one surface. The remaining figures are renumbered in order of appearance (1 Minor Arcana, 2 Taijitu, 3 compass), and every reference follows.
- **§5 rebuilt with three pillars:** the Taijitu against the element plane (§5.1); direction and season against the measured sky (§5.2); five cultural parallels, stated as parallels (§5.3).
- **§5.3 added:** the refused bride (五黄の寅・丙午), Tori-no-ichi (酉の市), Daikokuten and the rat (大黒天と鼠), the snake's money (巳の金運), the boar's charge (亥の猪突猛進・亥の子).
- **Compiler:** `WUXING_ZODIAC_MAPPING` replaced by `WUXING_PHASES` (state, Western equivalent, mechanical definition — no signs); `CULTURAL_PARALLELS` added, each carrying `status: "corroboration only"`; `compile_phase()` added; the §6 listing remains byte-identical to the repository file.
- **Figures re-rendered:** compass inscription corrected to 23:30–01:30, colliding labels at true north separated, the four cardinal branches (子午卯酉) marked, Minor Arcana plate retitled as Figure 1 with Pentacles named as the Western earth triplicity, planetary glyphs drawn in a font that carries them.
- **Appendix plates renumbered** to follow the figures (A1 Minor Arcana, A2 Taijitu, A3 compass).
- **Kept from 1.1:** the Cold Reading / Cold Case / Cold-Pressed triad of §2.1, the Western Earth / Wu Xing Earth terminology split, and the Unicode planetary glyphs.

---

## Citation & Academic Prior Art

If referencing or deriving from this specification, please cite:

```bibtex
@misc{mikami2026isomorphic,
  author = {Mikami, Polar and Yuzu, Nanota},
  title = {The Isomorphic Hardware of Occult Systems: Unifying Aristotelian Physical Primitives, Dorothean Triplicities, and Wu Xing Dynamics (Version 1.2)},
  year = {2026},
  publisher = {GitHub},
  journal = {GitHub repository},
  note = {First release November 11, 2026; revised November 21, 2026},
  howpublished = {\url{https://github.com/uranaisu-g/isomorphic-occult-hardware}}
}
```

---

## License

This project is dual-licensed under:
- **MIT License** for code and programmatic implementations (`compiler/`).
- **Creative Commons Attribution 4.0 International (CC BY 4.0)** for textual specifications and diagrams (`SPECIFICATION.md`, `figures/`).
