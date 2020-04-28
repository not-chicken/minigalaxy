import os
import sys
from pathlib import Path

LAUNCH_DIR = Path(sys.argv[0]).parent.resolve()

CONFIG_DIR = Path(os.getenv('XDG_CONFIG_HOME', Path('~/.config').expanduser()) / 'minigalaxy')
CONFIG_FILE_PATH = str(CONFIG_DIR / 'config.json')
CACHE_DIR = Path(os.getenv('XDG_CACHE_HOME', Path('~/.cache').expanduser()) / 'minigalaxy')

THUMBNAIL_DIR = CACHE_DIR / 'thumbnails'
DEFAULT_INSTALL_DIR = Path('~/GOG Games').expanduser()

UI_DIR = LAUNCH_DIR / '..' / 'data' / 'ui'
if not UI_DIR.exists():
    UI_DIR = LAUNCH_DIR / '..' / 'share' / 'minigalaxy' / 'ui'

LOGO_IMAGE_PATH = LAUNCH_DIR / '..' / 'data' / 'icons' / '192x192' / 'io.github.sharkwouter.Minigalaxy.png'
if not LOGO_IMAGE_PATH.exists():
    LOGO_IMAGE_PATH = LAUNCH_DIR / '..' / 'share' / 'icons'/ 'hicolor' / '192x192' / 'apps' / 'io.github.sharkwouter.Minigalaxy.png'
LOGO_IMAGE_PATH = str(LOGO_IMAGE_PATH)

ICON_WINE_PATH = LAUNCH_DIR/'..'/'data'/'images'/'winehq_logo_glass.png'
if not ICON_WINE_PATH.exists():
    ICON_WINE_PATH = LAUNCH_DIR / '..' / 'share' / 'minigalaxy' / 'images' / 'winehq_logo_glass.png'
ICON_WINE_PATH = str(ICON_WINE_PATH)

LOCALE_DIR = LAUNCH_DIR / '..' / 'data' / 'mo'
if not LOCALE_DIR.exists:
    LOCALE_DIR = LAUNCH_DIR / '..' / 'share' / 'minigalaxy' / 'translations'
