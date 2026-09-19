"""Semantic UI styling roles."""

from enum import StrEnum


class SurfaceRole(StrEnum):
    BACKGROUND = "background"
    CHROME = "chrome"
    PANEL = "panel"
    CARD = "card"
    TRANSPARENT = "transparent"
    OUTLINED = "outlined"
    ACCENT_OUTLINED = "accent-outlined"


class ButtonVariant(StrEnum):
    NAVIGATION = "navigation"
    SECONDARY = "secondary"
    SELECTABLE = "selectable"
    CARD_ACTION = "widgets-action"
    PRIMARY = "primary"
    ACCENT_OUTLINE = "accent-outline"
    THEME_OPTION = "theme-option"
    LINK = "link"
    START = "start"
    INFO = "info"


class TextRole(StrEnum):
    PAGE_TITLE = "page-title"
    PAGE_SUBTITLE = "page-subtitle"
    CARD_TITLE = "widgets-title"
    CAPTION = "caption"
    BODY = "body"
    BODY_MUTED = "body-muted"
    USERNAME = "username"
    SECTION_TITLE = "section-title"
    SECTION_CAPTION = "section-caption"
    WELCOME_TITLE = "welcome-title"
    WELCOME_TITLE_ACCENT = "welcome-title-accent"
    WELCOME_SUBTITLE = "welcome-subtitle"
    WELCOME_BODY = "welcome-body"
    WELCOME_PAGE_TITLE = "welcome-page-title"
    WELCOME_PAGE_SUBTITLE = "welcome-page-subtitle"
    ACCENT_SUBTITLE = "accent-subtitle"
    ACCENT_BODY = "accent-body"
    DANGER = "danger"


class Tone(StrEnum):
    ACCENT = "accent"
    SUCCESS = "success"
    WARNING = "warning"
    DANGER = "danger"


class ProgressRole(StrEnum):
    DEFAULT = "default"


class DividerRole(StrEnum):
    DEFAULT = "default"
    STRONG = "strong"


class ScrollRole(StrEnum):
    DEFAULT = "default"


class InputRole(StrEnum):
    SEARCH = "search"
    EDITOR = "editor"
    COMBO = "combo"
    SCALE = "scale"


class TableRole(StrEnum):
    DEFAULT = "default"


class CheckRole(StrEnum):
    DEFAULT = "default"
