# Reveal files in Finder
class show_files_in_finder(Command):

    def execute(self):
        import subprocess
        files = ",".join(['"{0}" as POSIX file'.format(file.path) for file in self.fm.thistab.get_selection()])
        reveal_script = "tell application \"Finder\" to reveal {{{0}}}".format(files)
        activate_script = "tell application \"Finder\" to set frontmost to true"
        script = "osascript -e '{0}' -e '{1}'".format(reveal_script, activate_script)
        self.fm.notify(script)
        subprocess.check_output(["osascript", "-e", reveal_script, "-e", activate_script])

class toggle_fplug(Command):

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
                self.fm.execute_console(f"shell -s osascript -e 'tell application \"Finder\" to close its front window'")
            elif not termplug:
                self.fm.notify(f"fplug script not found")
            elif os.path.isfile(f):
                self.fm.execute_console(f"shell -s finder-set-front '{f}'")
            elif os.path.isdir(f):
                self.fm.execute_console(f"shell -s finder-set-front '{f}'")
        except Exception as e:
            self.fm.notify(e)

# Reveal file from Finder
class get_finder(Command):

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

# Opens quicklook in fullscreen on active file
class quicklook(Command):

    def execute(self):
            self.fm.execute_console("shell -s osascript -e 'tell application \"Finder\" to activate' -e 'tell application \"System Events\" to keystroke \"y\" using {command down, option down}'")

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
                # self.fm.execute_console(f"shell -s killall mpv-bundle")
                self.fm.execute_console(f"shell -s mpv-close-front")
            elif not termplug:
                self.fm.notify(f"termplug script not found")
            elif os.path.isfile(f):
                self.fm.execute_console(f"shell -s termplug '{f}'")
                # self.fm.execute_console(f"shell -s osascript -e 'tell application \"iTerm\" to activate'")
                self.fm.execute_console(f"shell -s osascript -e 'tell application \"mpv\" to set frontmost to false'")
            elif os.path.isdir(f):
                self.fm.execute_console(f"shell -s osascript -e 'tell application \"mpv\" to set frontmost to false'")
                # self.fm.execute_console(f"shell -s osascript -e 'tell application \"iTerm\" to activate'")
        except Exception as e:
            self.fm.notify(e)


# MPV create playlist
class Append_playlist(Command):

    def execute(self):
        self.fm.execute_console('shell -s ls -1 $@ >> ~/Music/Music.m3u')

class Create_playlist(Command):

    def execute(self):
        self.fm.execute_console('shell -s ls -1 $@ > ~/Music/Music.m3u')

