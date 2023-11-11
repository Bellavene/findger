# findger

A [Ranger](https://github.com/ranger/ranger) plugin/script that adds support for macos Finder. Uses Finder to preview virtually anything, the rest depends on quicklook plugins you use.

![screen-gif](./preview.gif)

Features:
```
  1. Follow selection in Finder. Useful with Gallery view mode (Command+4 in Finder).
  2. Reveals selected file from active Finder window to Ranger.
  3. Reveals selected files from Ranger in Finder. (Code from Ranger's wiki)
  4. Toggle red Finder's and Ranger's tag on selected files.
  5. Instant playback or image preview through mpv
  6. Options to Encode with ffmpeg
  7. Synced playback of video files (up to 4) through mpv.
```

Installation:

  1. Add contents of commands.py to your ~/.config/ranger/commands.py file.
  2. Copy executables to somewhere in the $PATH. (Example: /usr/local/bin/)
  3. Install dependencies: '[brew install](https://brew.sh) [tag](https://github.com/jdberry/tag) [mpv](https://github.com/mpv-player/mpv) [ffmpeg](https://github.com/FFmpeg/FFmpeg)'
  4. Copy setting for mpv from mpv.conf to ~/.config/mpv/mpv.conf
  5. Add key maps to your ~/.config/ranger/rc.conf

Keymap Examples:
```
#Toggle followed file preview
      map <Space> chain show_files_in_finder; toggle_fplug

#Show selected files in Finder
      map <alt>/  show_files_in_finder

#Go to the path of the fron Finder wondow
      map <alt>?  get_finder

#Mark file
      map ' red_tag

#Open Finder's file info on selected file
      map <a-i> shell -f finder-file-info %f

#Create a playlist in mpv from the selected folder
      map MM shell Create-playlist %p

#Append selected to the playlist in mpv
      map Mm shell Append-to-playlist %p

#Play in sync 2 selected video files
      map m2 shell mpv-play-synced %p

#Play in sync 3 selected video files
      map m3 shell mpv-play-synced-3 %p

#Play in sync 4 selected video files
      map m4 shell mpv-play-synced-4 %p

#Encode selected file
      map mm shell encode %s

#Edit encode script settings
      map mM shell nano /usr/local/bin/encode

#Encode directory
      map md console shell encode-dir%space

#Edit encode-dir script settings
      map mD shell nano /usr/local/bin/encode-dir

#Encode selected to mp3
      map ma shell encode-mp3 %s

#Edit mp3 encoding script settings
      map mA shell nano /usr/local/bin/encode-mp3
```

Todo: Add better cross support for Finder's color tags.

<img width="2128" alt="Screenshot 2022-07-18 at 13 55 41" src="https://user-images.githubusercontent.com/77557804/179497347-9f0ba654-f6dc-4c17-834d-77e5b5d670fd.png">
