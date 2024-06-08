# findger

A [Ranger](https://github.com/ranger/ranger) plugin/script collection that adds cross support for macos Finder and mpv player.
Uses Finder to preview virtually anything, the rest depends on quicklook plugins you use. Or mpv player for instant playback of video files and image previews.

![screen-gif](./preview.gif)

# Features

  1. Follow selection in Finder. Useful with Gallery view mode (Command+4 in Finder).
  2. Reveals selected file from active Finder window to Ranger.
  3. Reveals selected files from Ranger to Finder.
  4. Toggle synced red tag on selection in Finder and Ranger.
  5. Toggle instant playback or image preview through mpv.
  6. Synced playback of selected video files (up to 4) through mpv.

# Installation

  1. Add the contents of commands.py to your `~/.config/ranger/commands.py` file.
  2. Copy fplug.py and termplug.py to ~/.config/ranger/plugins
  3. Copy executables to somewhere in the $PATH(If you don't know: /usr/local/bin/). If they don't run, use `chmod +x` on them.
  4. Install dependencies: `brew install tag mpv iterm2` (If you are using another terminal application, then change iterm in the scripts to desired manually.)
  5. Copy setting for mpv from mpv.conf to `~/.config/mpv/mpv.conf`
  6. Add key maps to your `~/.config/ranger/rc.conf`
  7. Grant permissions in `System Settings > Privacy & Security > Accessibility` to `iTerm` and `osascript`

# Keymap Examples

```
map <Space> findger                       # Toggle followed file preview through Finder
map <alt>/  finder_show                   # Show selected files in Finder
map <alt>?  finder_get                    # Go to path of the front Finder window
map '       red_tag                       # Mark file red in ranger and Finder
map <a-i>   finder_info %f                # Open Finder's file info on selection
map p       findger_mpv                   # Toggle instant video playback / Image previews with mpv
map ms      shell mpv-play-synced %p      # Play in sync up to 4 selected video files
```

Todo: Add better cross support for Finder's color tags.

<img width="2128" alt="Screenshot 2022-07-18 at 13 55 41" src="https://user-images.githubusercontent.com/77557804/179497347-9f0ba654-f6dc-4c17-834d-77e5b5d670fd.png">

Inspired by [termplug](https://github.com/laktak/termplug)
