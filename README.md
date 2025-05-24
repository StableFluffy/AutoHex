 # AutoHex

Generate unique and vibrant hex color codes from text using deterministic hashing.

## Features

- **Deterministic**: Same input text always produces the same color
- **Vibrant Colors**: Uses HSL color space to generate visually appealing colors
- **Customizable**: Support for seeding and different algorithms
- **Lightweight**: No external dependencies

## Installation

```bash
pip install autohex
```

## Quick Start

```python
from autohex import AutoHex

# Create an instance
generator = AutoHex()

# Generate a hex color from text
color = generator.gen("hello world")
print(color)  # #7c5ab8

# Use a seed for consistent variations
seeded_generator = AutoHex(seed="my-project")
color = seeded_generator.gen("hello world")
print(color)  # Different color due to seed
```

## API Reference

### AutoHex(seed=None, algorithm='vibrant_hsl')

Creates a new color generator instance.

**Parameters:**
- `seed` (str, optional): A seed string to influence color generation
- `algorithm` (str): Color generation algorithm (currently only 'vibrant_hsl')

### gen(text: str) -> str

Generates a hex color code from the input text.

**Parameters:**
- `text` (str): Input text to generate color from

**Returns:**
- `str`: Hex color code (e.g., '#7c5ab8')

## Algorithm

The `vibrant_hsl` algorithm:
1. Hashes the input text using SHA-256
2. Converts hash to HSL color space
3. Ensures vibrant colors by constraining saturation (70-100%) and lightness (50-65%)
4. Converts to RGB and formats as hex

## License

MIT License - see [LICENSE.txt](LICENSE.txt) for details.
