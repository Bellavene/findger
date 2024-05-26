# Finder plug
class findger(Command):
    def execute(self):
            self.fm.execute_console(f"finder_show")
            self.fm.execute_console(f"finder_toggle")

# Show in Finder
class finder_show(Command):
    def execute(self):
        import subprocess
        files = ",".join(['"{0}" as POSIX file'.format(file.path) for file in self.fm.thistab.get_selection()])
        reveal_script = "tell application \"Finder\" to reveal {{{0}}}".format(files)
        activate_script = "--"
        script = "osascript -e '{0}' -e '{1}'".format(reveal_script, activate_script)
        self.fm.notify(script)
        subprocess.check_output(["osascript", "-e", reveal_script, "-e", activate_script])
        self.fm.execute_console(f"finder_gallery")
        # self.fm.execute_console(f"shell -s finder-gallery")
        self.fm.execute_console(f"shell -s osascript -e 'tell application \"iTerm\" to activate'")

# Finder Gallery and List
class finder_gallery(Command):
    def execute(self):
            self.fm.execute_console(f"shell -s osascript -e 'tell application \"Finder\" to activate' -e 'tell application \"System Events\"' -e'tell process \"Finder\"' -e 'click menu item \"as Gallery\" of menu \"View\" of menu bar 1' -e 'end tell' -e 'end tell'")
class finder_list(Command):
    def execute(self):
            self.fm.execute_console(f"shell -s osascript -e 'tell application \"Finder\" to activate' -e 'tell application \"System Events\"' -e'tell process \"Finder\"' -e 'click menu item \"as List\" of menu \"View\" of menu bar 1' -e 'end tell' -e 'end tell'")

# Toggle_fplug
class finder_toggle(Command):
    def execute(self):
        p = not self.fm.settings["_fplug"]
        self.fm.settings["_fplug"] = p
        self.fm.execute_console(f"fplug {'%s' if p else ''}")
        status = f"fplug {'active' if p else 'off'}"
class fplug(Command):
    def execute(self):
        from pathlib import Path
        p = Path('{f}')
        do_preview = self.fm.settings["_fplug"]
        try:
            f = self.rest(1)
            if not do_preview:
                self.fm.execute_console(f"finder_list")
                self.fm.execute_console(f"shell -s osascript -e 'tell application \"Finder\" to close its front window' -e 'tell application \"iTerm\" to activate'")
            elif not termplug:
                self.fm.notify(f"fplug script not found")
            elif os.path.isfile(f):
                self.fm.execute_console(f"shell -s finder-set-front '{f}'")
            elif os.path.isdir(f):
                self.fm.execute_console(f"shell -s finder-set-front '{f}'")
        except Exception as e:
            self.fm.notify(e)

# Show files from Finder
class finder_get(Command):
    def execute(self):
        import subprocess
        import os
        finder = self.fm.execute_command("osascript -e 'tell app \"Finder\" to POSIX path of (selection as alias)'",
                                      universal_newlines=True, stdout=subprocess.PIPE)
        stdout, _ = finder.communicate()
        if finder.returncode == 0:
            selected = os.path.abspath(stdout.strip())
            if os.path.isdir(selected):
                self.fm.cd(selected)
            else:
                self.fm.select_file(selected)

class finder_info(Command):
    def execute(self):
        import subprocess
        files = ",".join(['"{0}" as POSIX file'.format(file.path) for file in self.fm.thistab.get_selection()])
        reveal_script = "set aFile to {{{0}}} as alias".format(files)
        activate_script = "tell application \"Finder\" to open information window of aFile"
        script = "osascript -e '{0}' -e '{1}'".format(reveal_script, activate_script)
        self.fm.notify(script)
        subprocess.check_output(["osascript", "-e", reveal_script, "-e", activate_script])

# Opens quicklook in fullscreen on active file
class quicklook(Command):
    def execute(self):
            self.fm.execute_console("shell -s osascript -e 'tell application \"Finder\" to activate' -e 'tell application \"System Events\" to keystroke \"y\" using {command down, option down}'")

# AirDrop
class airdrop(Command):
    def execute(self):
            self.fm.notify("Sending %s")
            self.fm.execute_console(f"shell -s airdrop '%s'")

# Toggle Finder's red and ranger's standard tags on selected files
class red_tag(Command):
    def execute(self):
        self.fm.execute_console('shell -s if [ "$(tag -l -N %s)" = "red" ]; then; tag -r "red" %s; elif [ "$(tag -l -N %s)" = "" ]; then; tag -a "red" %s; fi')
        self.fm.execute_console("tag_toggle")

# MPV Preview
import time
class toggle_termplug(Command):
    def execute(self):
        p = not self.fm.settings["_termplug"]
        self.fm.settings["_termplug"] = p
        self.fm.execute_console(f"termplug {'%s' if p else ''}")
        status = f"termplug {'active' if p else 'off'}"
class termplug(Command):
    def execute(self):
        do_preview = self.fm.settings["_termplug"]
        try:
            f = self.rest(1)
            if not do_preview:
                self.fm.execute_console(f"shell -s mpv-close-front")
            elif not termplug:
                self.fm.notify(f"termplug script not found")
            elif os.path.isfile(f):
                self.fm.execute_console(f"shell -s termplug '{f}';osascript -e 'tell application \"iTerm\" to activate'")
                # time.sleep(0.8)
                self.fm.execute_console(f"shell -s osascript -e 'tell application \"iTerm\" to activate'")
            elif os.path.isdir(f):
                self.fm.execute_console(f"shell -s osascript -e 'tell application \"iTerm\" to activate'")
        except Exception as e:
            self.fm.notify(e)

