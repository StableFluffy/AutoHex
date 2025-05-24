import hashlib
import colorsys

class AutoHex:
    def __init__(self, seed=None, algorithm='vibrant_hsl'):
        self.seed = seed or ''
        self.algorithm = algorithm

    def _hash_text(self, text: str) -> str:
        data = (self.seed + text).encode('utf-8')
        return hashlib.sha256(data).hexdigest()

    def _hsl_to_rgb(self, h: float, s: float, l: float) -> tuple[int, int, int]:
        r, g, b = colorsys.hls_to_rgb(h, l, s)
        return int(r * 255), int(g * 255), int(b * 255)

    def _rgb_to_hex(self, r: int, g: int, b: int) -> str:
        return f'#{r:02x}{g:02x}{b:02x}'

    def gen(self, text: str) -> str:
        hash_hex = self._hash_text(text)
        hash_int = int(hash_hex, 16)

        if self.algorithm == 'vibrant_hsl':
            h = (hash_int % 360) / 360.0
            s_byte = (hash_int >> 8) & 0xFF
            s = 0.7 + (s_byte / 255.0) * 0.3
            l_byte = (hash_int >> 16) & 0xFF
            l = 0.5 + (l_byte / 255.0) * 0.15
            r, g, b = self._hsl_to_rgb(h, s, l)
            return self._rgb_to_hex(r, g, b)
        else:
            raise ValueError(f"Invalid Algorithm: {self.algorithm}")
