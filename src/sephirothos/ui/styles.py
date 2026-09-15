from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class AccentPalette:
    """The accent colors lmfao self explanation."""

    base: str
    hover: str
    pressed: str
    focus: str
    glow: str
