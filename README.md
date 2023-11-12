# findger

A [Ranger](https://github.com/ranger/ranger) plugin/script collection that adds cross support for macos Finder and mpv player.
Uses Finder to preview virtually anything, the rest depends on quicklook plugins you use. Or mpv player for instant playback of video files and image previews.

![screen-gif](./preview.gif)

Features:
```
  1. Follow selection in Finder. Useful with Gallery view mode (Command+4 in Finder).
  2. Reveals selected file from active Finder window to Ranger.
  3. Reveals selected files from Ranger in Finder. (Code from Ranger's wiki)
  4. Toggle synced red tag on selection in Finder and Ranger.
  5. Toggle instant playback or image preview through mpv.
  6. Synced playback of video files (up to 4) through mpv.
```

Installation:

  1. Add contents of commands.py to your ~/.config/ranger/commands.py file.
  2. Copy executables to somewhere in the $PATH. (If you don't know: /usr/local/bin/)
  3. Install dependencies: '[brew install](https://brew.sh) [tag](https://github.com/jdberry/tag) [mpv](https://github.com/mpv-player/mpv)'
  4. Copy setting for mpv from mpv.conf to ~/.config/mpv/mpv.conf
  5. Add key maps to your ~/.config/ranger/rc.conf

Keymap Examples:

 Toggle followed file preview with Finder
      `map <Space> chain show_files_in_finder; toggle_fplug`

 Show selected files in Finder
      `map <alt>/  show_files_in_finder`

 Go to path of the front Finder window
      `map <alt>?  get_finder`

 Mark file in ranger and Finder
      `map ' red_tag`

 Open Finder's file info on selected file
      `map <a-i> shell -f finder-file-info %f`

 Toggle instant video playback / Image previews with mpv
      `map p toggle_termplug`

 Play in sync 2 selected video files
      `map m2 shell mpv-play-synced %p`

 Play in sync 3 selected video files
      `map m3 shell mpv-play-synced-3 %p`

 Play in sync 4 selected video files
      `map m4 shell mpv-play-synced-4 %p`

Todo: Add better cross support for Finder's color tags.

<img width="2128" alt="Screenshot 2022-07-18 at 13 55 41" src="https://user-images.githubusercontent.com/77557804/179497347-9f0ba654-f6dc-4c17-834d-77e5b5d670fd.png">

Inspired by [termplug](https://github.com/laktak/termplug)
