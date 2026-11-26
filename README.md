# Calculator v.1

[![CI](https://github.com/NebulaStack-prog/Calculator-v.1/actions/workflows/ci.yml/badge.svg)](https://github.com/NebulaStack-prog/Calculator-v.1/actions/workflows/ci.yml)

<img src="IMG_20260701_003212_702.jpg" width="200" alt="Calculator v.1 emblem">

> The first step in the NESTIMS development journey.

| Project Information | Details |
|---|---|
| Project ID | NS-001 |
| Direction | Infotech |
| Development Phase | Phase I |
| Version | v1.0 |
| Platform | Windows / Python |
| Status | Legacy |

## Overview

Calculator v.1 is a multifunctional desktop calculator developed in Python. It represents the first official software project of the NESTIMS ecosystem.

The application combines arithmetic, number theory, trigonometry and algebra in a graphical interface.

## Features

- Basic arithmetic operations
- Powers, roots and logarithms
- Factorials and double factorials
- Prime number testing and factorization
- GCD and LCM calculations
- Trigonometric functions
- Linear and quadratic equations
- Degree and radian conversion
- Persistent calculation history

## Technology Stack

Python, Tkinter, math and JSON.

## Installation

Download the Windows executable from [GitHub Releases](https://github.com/NebulaStack-prog/Calculator-v.1/releases/tag/v1.0).

To run from source, install Python with Tkinter support:

```bash
python Calculator_v.1.py
```

No third-party Python packages are required.

## Screenshots

![Calculator interface](Calc_v.1_1.jpg)

![Calculation example](Calc_v.1_2.jpg)

## Documentation

- [Russian documentation](Calculator_v.1_RU.md)
- [English documentation](Calculator_v.1_EN.md)
- [Original source code](Calculator_v.1.py)

## Testing

```bash
python -m unittest discover -s tests -v
```

The tests cover mathematical methods without opening the GUI. A known legacy tangent-domain bug at angles such as 270 degrees is marked as an expected failure. GUI behavior is not covered.

## Project Status

This project is preserved as a historical release of NESTIMS Phase I. Its original implementation documents the early stages of the ecosystem's development.

For an extended version with graph plotting, see [Calculator v.2](https://github.com/NebulaStack-prog/Calculator-v.2).

## Explore NESTIMS

[HELLO-USER](https://github.com/NebulaStack-prog/HELLO-USER) · [Infotech](https://github.com/NebulaStack-prog/NebulaStack-Infotech)

---

**NESTIMS · Est. 2025**

© NESTIMS
