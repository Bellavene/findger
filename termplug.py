import ranger.api
import os
import sys

old_hook_init = ranger.api.hook_init


def hook_init(fm):
    def on_move(signal):
        if fm.thisfile and fm.settings["_termplug"] and signal.new:
            f = signal.new.path
            fm.execute_console(f"termplug {f}")

    fm.settings["_termplug"] = False
    fm.signal_bind("move", on_move)
    return old_hook_init(fm)


ranger.api.hook_init = hook_init
