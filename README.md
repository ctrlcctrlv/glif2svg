# Convert UFO glyph files (`.glif`) to SVG

There exists already an `svg2glif`, but for some reason not the opposite operation. My MFEKglif editor treats `.glif` files as first-class entities, so it seemed obvious to me I'd want to edit them with Inkscape sometimes.

```
usage: glif2svg.py [-h] [--output OUTPUT] input

Convert .glif to SVG

positional arguments:
  input            .glif file

optional arguments:
  -h, --help       show this help message and exit
  --output OUTPUT  SVG file; otherwise prints to stdout
```

## Requirements

* fonttools
* Python 3
