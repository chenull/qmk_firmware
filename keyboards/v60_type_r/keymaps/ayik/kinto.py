# -*- coding: utf-8 -*-

import re
from xkeysnail.transform import K, define_keymap, pass_through_key

# Use the following for testing terminal keymaps
# terminals = [ "", ... ]
# xbindkeys -mk
terminals = {
    "gnome-terminal": {"brace": True},
    "konsole": {},
    "io.elementary.terminal": {},
    "terminator": {},
    "sakura": {},
    "guake": {},
    "tilda": {},
    "xterm": {},
    "eterm": {},
    "kitty": {},
    "alacritty": {},
    "mate-terminal": {},
    "tilix": {},
    "xfce4-terminal": {},
}
term_str = "|".join(str(x) for x in terminals)

editors = {
    "code": {"ms": True},
    "vscodium": {"ms": True},
    "sublime_text": {"brace": True},

}
editor_str = "|".join(str(x) for x in editors)

browsers = {
    "firefox": {"brace": True},
}
browser_str = "|".join(str(x) for x in browsers)

# Apps that like braces (Super-{ / Super-} to move between tabs/views)
brace_str = "|".join(
    str(key) for key, value in
    {**terminals, **editors, **browsers}.items()
    if value.get("brace") is True
)

# [Global modemap] Change modifier keys as in xmodmap
# define_conditional_modmap(lambda wm_class: wm_class.casefold() not in terminals,{
#     # Default Mac/Win
#     # Key.LEFT_ALT: Key.RIGHT_CTRL,   # WinMac
#     # Key.LEFT_META: Key.LEFT_ALT,    # WinMac
#     # Key.LEFT_CTRL: Key.LEFT_META,   # WinMac
#     # Key.RIGHT_ALT: Key.RIGHT_CTRL,  # WinMac
#     # Key.RIGHT_META: Key.RIGHT_ALT,  # WinMac
#     # Key.RIGHT_CTRL: Key.RIGHT_META, # WinMac
#     Key.LEFT_ALT: Key.LEFT_CTRL,      # WinMac
#     Key.LEFT_META: Key.LEFT_ALT,      # WinMac
#     Key.LEFT_CTRL: Key.LEFT_META,     # WinMac

#     # # Mac Only
#     # Key.LEFT_META: Key.RIGHT_CTRL,  # Mac
#     # Key.LEFT_CTRL: Key.LEFT_META,   # Mac
#     # Key.RIGHT_META: Key.RIGHT_CTRL, # Mac
#     # Key.RIGHT_CTRL: Key.RIGHT_META, # Mac
# })

# [Conditional modmap] Change modifier keys in certain applications
# define_conditional_modmap(re.compile(term_str, re.IGNORECASE), {
#     # # Default Mac/Win
#     # Key.LEFT_ALT: Key.RIGHT_CTRL,   # WinMac
#     # Key.LEFT_META: Key.LEFT_ALT,    # WinMac
#     # Key.LEFT_CTRL: Key.LEFT_CTRL,   # WinMac
#     Key.LEFT_CTRL: Key.RIGHT_CTRL,   # WinMac
#     Key.LEFT_META: Key.LEFT_META,    # WinMac
#     Key.LEFT_CTRL: Key.LEFT_CTRL,   # WinMac
#     # Key.RIGHT_ALT: Key.RIGHT_CTRL,  # WinMac
#     # Key.RIGHT_META: Key.RIGHT_ALT,  # WinMac
#     # Key.RIGHT_CTRL: Key.LEFT_CTRL,  # WinMac

#     # # Mac Only
#     # Key.LEFT_META: Key.RIGHT_CTRL,  # Mac
#     # # Left Ctrl Stays Left Ctrl
#     # Key.RIGHT_META: Key.RIGHT_CTRL, # Mac
#     # Key.RIGHT_CTRL: Key.LEFT_CTRL,  # Mac
# })

# Keybindings for Nautilus
define_keymap(re.compile("org.gnome.nautilus", re.IGNORECASE), {
    K("LC-Up"): K("M-Up"),          # Go Up dir
    K("LC-Down"): K("M-Down"),      # Go Down dir
    K("LC-Left"): K("M-Left"),      # Go Back
    K("LC-Right"): K("M-Right"),    # Go Forward
    K("Super-Backspace"): K("Delete"),    # Move to trash
})

define_keymap(None, {
    # Basic App hotkey functions
    # K("Super-Q"): K("Alt-F4"),
    # K("Super-H"): K("Alt-F9"),
    # Cmd Tab - App Switching Default
    # K("Super-Tab"): K("Alt-Tab"),
    # K("Super-Shift-Tab"): K("Alt-Shift-Tab"),
    # K("Super-Grave"): K("Alt-Grave"),
    # K("Super-Shift-Grave"): K("Alt-Shift-Grave"),

    # home, end
    # K("Super-Left"): {
    #     K("Super-Left"): K("Home"),
    #     K("Ctrl-Left"): K("Home"),
    # },
    # K("Super-Right"): {
    #     K("Super-Right"): K("End"),
    #     K("Ctrl-Right"): K("End"),
    # },
    K("Super-Left"): K("Home"),                      # Home
    K("Ctrl-Left"): K("Home"),                       # Home
    K("Super-Right"): K("End"),                      # End
    K("Ctrl-Right"): K("End"),                       # End
    K("Ctrl-Up"): K("PAGE_UP"),                      # Page UP
    K("Ctrl-Down"): K("PAGE_DOWN"),                  # Page Down
    K("Super-w"): K("Ctrl-w"),                       # Close Window
    K("Super-a"): K("Ctrl-a"),                       # Select All
    K("Super-f"): K("Ctrl-f"),                       # Find
    K("Super-s"): K("Ctrl-s"),                       # Save
    K("Super-z"): K("Ctrl-z"),                       # Undo
    K("Super-Shift-z"): K("Ctrl-Shift-z"),           # Redo
    K("Super-Shift-Left"): K("Shift-Home"),          # Select all to Beginning of Line
    K("Super-Shift-Right"): K("Shift-End"),          # Select all to End of Line
    K("Super-Up"): K("Ctrl-Home"),                   # Beginning of File
    K("Super-Shift-Up"): K("Ctrl-Shift-Home"),       # Select all to Beginning of File
    K("Super-Down"): K("Ctrl-End"),                  # End of File
    K("Super-Shift-Down"): K("Ctrl-Shift-End"),      # Select all to End of File
    K("LC-Backspace"): K("Delete"),                  # Delete
})

define_keymap(lambda wm_class: wm_class.casefold() not in terminals, {
    K("Super-x"): K("Ctrl-x"),                       # Cut
    K("Super-c"): K("Ctrl-c"),                       # Save
    K("Super-v"): K("Ctrl-v"),                       # Undo
})

# define_keymap(lambda wm_class: wm_class.casefold() not in mscodes, {
#    Wordwise remaining - for Everything but VS Code
#    K("M-Left"): K("C-Left"),               # Left of Word
#    K("M-Shift-Left"): K("C-Shift-Left"),   # Select Left of Word
#    K("M-Right"): K("C-Right"),             # Right of Word
#    K("M-Shift-Right"): K("C-Shift-Right"), # Select Right of Word
#    ** VS Code fix **
#      Electron issue precludes normal keybinding fix.
#      Alt menu auto-focus/toggle gets in the way.
#
#      refer to ./xkeysnail-config/vscode_keybindings.json
#    **
#
#    ** Firefox fix **
#      User will need to set "ui.key.menuAccessKeyFocuses"
#      under about:config to false.
#
#      https://superuser.com/questions/770301/pentadactyl-how-to-disable-menu-bar-toggle-by-alt
#    **
#
# })

# Keybindings for VS Code
# define_keymap(re.compile(code_str, re.IGNORECASE), {
#     # Wordwise remaining - for VS Code
#     # Alt-F19 hack fixes Alt menu activation
#     K("M-Left"): [K("M-F19"), K("C-Left")],                  # Left of Word
#     K("M-Right"): [K("M-F19"), K("C-Right")],                # Right of Word
#     K("M-Shift-Left"): [K("M-F19"), K("C-Shift-Left")],      # Select Left of Word
#     K("M-Shift-Right"): [K("M-F19"), K("C-Shift-Right")],    # Select Right of Word
#
#     # K("C-PAGE_DOWN"): pass_through_key,         # cancel next_view
#     # K("C-PAGE_UP"): pass_through_key,           # cancel prev_view
#     K("C-M-Left"): K("C-PAGE_UP"),              # next_view
#     K("C-M-Right"): K("C-PAGE_DOWN"),           # prev_view
#
#     # VS Code Shortcuts
#     K("C-g"): pass_through_key,                 # cancel Go to Line...
#     K("Super-g"): K("C-g"),                     # Go to Line...
#     K("F3"): pass_through_key,                  # cancel Find next
#     K("C-h"): pass_through_key,                 # cancel replace
#     K("C-M-f"): K("C-h"),                       # replace
#     K("C-Shift-h"): pass_through_key,           # cancel replace_next
#     K("C-M-e"): K("C-Shift-h"),                 # replace_next
#     K("f3"): pass_through_key,                  # cancel find_next
#     K("C-g"): K("f3"),                          # find_next
#     K("Shift-f3"): pass_through_key,            # cancel find_prev
#     K("C-Shift-g"): K("Shift-f3"),              # find_prev
#     K("Super-C-g"): K("C-f2"),                  # Default - Sublime - find_all_under
#     # K("C-M-g"): K("C-f2"),                      # Chromebook - Sublime - find_all_under
#     K("Super-Shift-up"): K("M-Shift-up"),       # multi-cursor up
#     K("Super-Shift-down"): K("M-Shift-down"),   # multi-cursor down
#     # K(""): pass_through_key,                    # cancel
#     # K(""): K(""),                               #
# }, "Code")

# Keybindings for Apps who like to brace
define_keymap(re.compile(brace_str, re.IGNORECASE), {
    K("Super-Shift-RIGHT_BRACE"): K("Ctrl-PAGE_DOWN"),  # Next Tab
    K("Super-Shift-LEFT_BRACE"): K("Ctrl-PAGE_UP"),     # Prev Tab
}, "browsers")

# Keybindings for Sublime Text
define_keymap(re.compile("Sublime_text", re.IGNORECASE), {
    # K("C-Super-up"): K("M-o"),                  # Switch file
    # K("C-M-f"): K("f11"),                       # toggle_full_screen
    # K("C-M-v"): [K("C-k"), K("C-v")],           # paste_from_history
    # K("C-up"): pass_through_key,                # cancel scroll_lines up
    # K("Super-M-up"): K("C-up"),                 # scroll_lines up
    # K("C-down"): pass_through_key,              # cancel scroll_lines down
    # K("Super-M-down"): K("C-down"),             # scroll_lines down
    # K("Super-Shift-up"): K("M-Shift-up"),       # multi-cursor up
    # K("Super-Shift-down"): K("M-Shift-down"),   # multi-cursor down
    # K("C-PAGE_DOWN"): pass_through_key,         # cancel next_view
    # K("C-PAGE_UP"): pass_through_key,           # cancel prev_view
    K("Super-d"): K("Ctrl-d"),                          # expand selection to word
    # K("C-M-right"): K("C-PAGE_DOWN"),           # next_view
    # K("C-M-left"): K("C-PAGE_UP"),              # prev_view
    # K("insert"): pass_through_key,              # cancel toggle_overwrite
    # K("C-M-o"): K("insert"),                    # toggle_overwrite
    # K("M-c"): pass_through_key,                 # cancel toggle_case_sensitive
    # K("C-M-c"): K("M-c"),                       # toggle_case_sensitive
    # K("C-h"): pass_through_key,                 # cancel replace
    # K("C-M-f"): K("C-h"),                       # replace
    # K("C-Shift-h"): pass_through_key,           # cancel replace_next
    # K("C-M-e"): K("C-Shift-h"),                 # replace_next
    # K("f3"): pass_through_key,                  # cancel find_next
    # K("C-g"): K("f3"),                          # find_next
    # K("Shift-f3"): pass_through_key,            # cancel find_prev
    # K("C-Shift-g"): K("Shift-f3"),              # find_prev
    # K("C-f3"): pass_through_key,                # cancel find_under
    # K("Super-M-g"): K("C-f3"),                  # find_under
    # K("C-Shift-f3"): pass_through_key,          # cancel find_under_prev
    # K("Super-M-Shift-g"): K("C-Shift-f3"),      # find_under_prev
    # K("M-f3"): pass_through_key,                # Default - cancel find_all_under
    # K("Super-C-g"): K("M-f3"),                  # Default - find_all_under
    # K("C-Shift-up"): pass_through_key,          # cancel swap_line_up
    # K("Super-C-up"): K("C-Shift-up"),           # swap_line_up
    # K("C-Shift-down"): pass_through_key,        # cancel swap_line_down
    # K("Super-C-down"): K("C-Shift-down"),       # swap_line_down
    # K("C-Pause"): pass_through_key,             # cancel cancel_build
    # K("Super-c"): K("C-Pause"),                 # cancel_build
    # K("f9"): pass_through_key,                  # cancel sort_lines case_s false
    # K("f5"): K("f9"),                           # sort_lines case_s false
    # K("Super-f9"): pass_through_key,            # cancel sort_lines case_s true
    # K("Super-f5"): K("Super-f9"),               # sort_lines case_s true
    # K("M-Shift-Key_1"): pass_through_key,       # cancel set_layout
    # K("C-M-Key_1"): K("M-Shift-Key_1"),         # set_layout
    # K("M-Shift-Key_2"): pass_through_key,       # cancel set_layout
    # K("C-M-Key_2"): K("M-Shift-Key_2"),         # set_layout
    # K("M-Shift-Key_3"): pass_through_key,       # cancel set_layout
    # K("C-M-Key_3"): K("M-Shift-Key_3"),         # set_layout
    # K("M-Shift-Key_4"): pass_through_key,       # cancel set_layout
    # K("C-M-Key_4"): K("M-Shift-Key_4"),         # set_layout
    # K("M-Shift-Key_8"): pass_through_key,       # cancel set_layout
    # K("C-M-Shift-Key_2"): K("M-Shift-Key_8"),   # set_layout
    # K("M-Shift-Key_9"): pass_through_key,       # cancel set_layout
    # K("C-M-Shift-Key_3"): K("M-Shift-Key_9"),   # set_layout
    # K("M-Shift-Key_5"): pass_through_key,       # cancel set_layout
    # K("C-M-Shift-Key_5"): K("M-Shift-Key_5"),   # set_layout
    # K(""): pass_through_key,                    # cancel
    # K(""): K(""),                               #
}, "Sublime Text")

define_keymap(re.compile(term_str, re.IGNORECASE), {
    # Converts Cmd to use Ctrl-Shift
    K("RC-Tab"): K("RC-F13"),
    K("RC-Shift-Tab"): K("RC-Shift-F13"),
    K("RC-V"): K("C-Shift-V"),
    K("RC-MINUS"): K("C-Shift-MINUS"),
    K("RC-EQUAL"): K("C-Shift-EQUAL"),
    K("RC-BACKSPACE"): K("C-Shift-BACKSPACE"),
    K("RC-W"): K("C-Shift-W"),
    K("RC-E"): K("C-Shift-E"),
    K("RC-R"): K("C-Shift-R"),
    K("RC-T"): K("C-Shift-t"),
    K("RC-Y"): K("C-Shift-Y"),
    K("RC-U"): K("C-Shift-U"),
    K("RC-I"): K("C-Shift-I"),
    K("RC-O"): K("C-Shift-O"),
    K("RC-P"): K("C-Shift-P"),
    K("RC-A"): K("C-Shift-A"),
    K("RC-S"): K("C-Shift-S"),
    K("RC-D"): K("C-Shift-D"),
    K("RC-F"): K("C-Shift-F"),
    K("RC-G"): K("C-Shift-G"),
    K("RC-H"): K("C-Shift-H"),
    K("RC-J"): K("C-Shift-J"),
    K("RC-K"): K("C-Shift-K"),
    K("RC-L"): K("C-Shift-L"),
    K("RC-SEMICOLON"): K("C-Shift-SEMICOLON"),
    K("RC-APOSTROPHE"): K("C-Shift-APOSTROPHE"),
    K("RC-GRAVE"): K("C-Shift-GRAVE"),
    K("RC-BACKSLASH"): K("C-Shift-BACKSLASH"),
    K("RC-Z"): K("C-Shift-Z"),
    K("RC-X"): K("C-Shift-X"),
    K("RC-C"): K("C-Shift-C"),
    K("RC-V"): K("C-Shift-V"),
    K("RC-B"): K("C-Shift-B"),
    K("RC-N"): K("C-Shift-N"),
    K("RC-M"): K("C-Shift-M"),
    K("RC-COMMA"): K("C-Shift-COMMA"),
    K("RC-DOT"): K("C-Shift-DOT"),
    K("RC-SLASH"): K("C-Shift-SLASH"),
    K("RC-KPASTERISK"): K("C-Shift-KPASTERISK"),
}, "terminals")

# Keybindings for Browsers
define_keymap(re.compile(browser_str, re.IGNORECASE), {
    K("Super-l"): K("Ctrl-l"),                          # Location
    K("Super-t"): K("Ctrl-t"),                          # New Tab
}, "browsers")
