from libqtile.lazy import lazy
from libqtile.config import Key
from libqtile.utils import guess_terminal
from libqtile.log_utils import logger
from stonecharioteer.qtile.inputs import Keyboard, MOD
from stonecharioteer.utils.displays import get_display_info


def configure_keymaps(groups):
    """Configures keymaps"""
    terminal = "/home/stonecharioteer/.local/bin/kitty"
    Super = [MOD.value]
    SuperShift = [MOD.value, Keyboard.SHIFT.value]
    SuperControl = [MOD.value, Keyboard.CTRL.value]
    # Movement keymaps
    keys = [
        # Switch between windows
        Key(Super, "h", lazy.layout.left(), desc="Move focus to left"),
        Key(Super, "l", lazy.layout.right(), desc="Move focus to right"),
        Key(Super, "j", lazy.layout.down(), desc="Move focus down"),
        Key(Super, "k", lazy.layout.up(), desc="Move focus up"),
        Key(
            Super,
            "space",
            lazy.layout.next(),
            desc="Move window focus to other window",
        ),
        # Move windows between left/right columns or move up/down in current stack.
        # Moving out of range in Columns layout will create new column.
        Key(
            SuperShift,
            "h",
            lazy.layout.shuffle_left(),
            desc="Move window to the left",
        ),
        Key(
            SuperShift,
            "l",
            lazy.layout.shuffle_right(),
            desc="Move window to the right",
        ),
        Key(SuperShift, "j", lazy.layout.shuffle_down(), desc="Move window down"),
        Key(SuperShift, "k", lazy.layout.shuffle_up(), desc="Move window up"),
        # Grow windows. If current window is on the edge of screen and direction
        # will be to screen edge - window would shrink.
        Key(SuperControl, "h", lazy.layout.grow_left(), desc="Grow window to the left"),
        Key(
            SuperControl,
            "l",
            lazy.layout.grow_right(),
            desc="Grow window to the right",
        ),
        Key(SuperControl, "j", lazy.layout.grow_down(), desc="Grow window down"),
        Key(SuperControl, "k", lazy.layout.grow_up(), desc="Grow window up"),
        Key(Super, "n", lazy.layout.normalize(), desc="Reset all window sizes"),
        # Toggle between split and unsplit sides of stack.
        # Split = all windows displayed
        # Unsplit = 1 window displayed, like Max layout, but still with
        # multiple stack panes
        Key(
            SuperShift,
            "Return",
            lazy.layout.toggle_split(),
            desc="Toggle between split and unsplit sides of stack",
        ),
        Key(Super, "Return", lazy.spawn(terminal), desc="Launch terminal"),
        # Toggle between different layouts as defined below
        Key(Super, "Tab", lazy.next_layout(), desc="Toggle between layouts"),
        Key(Super, "w", lazy.window.kill(), desc="Kill focused window"),
        Key(SuperControl, "r", lazy.restart(), desc="Restart Qtile and reload config"),
        Key(SuperControl, "q", lazy.shutdown(), desc="Shutdown Qtile"),
        Key(
            Super,
            "r",
            lazy.spawn("""rofi -modi "drun,run,window,ssh" -show drun"""),
            desc="Spawn a command using a prompt widget",
        ),
    ]

    for ix, group in enumerate(groups):
        keys.extend(
            [
                Key(
                    Super,
                    str(ix + 1),
                    lazy.group[group.name].toscreen(),
                    desc=f"Switch to group {group.name}",
                ),
                Key(
                    SuperShift,
                    str(ix + 1),
                    lazy.window.togroup(group.name, switch_group=True),
                    desc=f"Switch to & move focussed window to group {group.name}",
                ),
                Key(
                    SuperControl,
                    str(ix + 1),
                    lazy.window.togroup(group.name),
                    desc=f"Move focussed window to group {group.name}",
                ),
            ]
        )

    display_keys = [
        ("u", "eDP"),
        ("m", "DisplayPort-0"),
        ("y", "DisplayPort-1"),
        ("i", "HDMI-A-0"),
    ]
    try:
        for ix, (key, display) in enumerate(display_keys):
            jerry_command = "jerry -m {}".format(display)
            logger.warning("Monitor = {}".format(display))
            logger.debug(jerry_command)
            keys.append(Key(Super, key, lazy.spawn(jerry_command)))
    except:
        pass

    return keys
