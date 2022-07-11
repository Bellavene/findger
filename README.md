# findger
A [Ranger](https://github.com/ranger/ranger) plugin that adds support for macos Finder. Best used along with auto tiling window manager. Uses finder to preview virtually anything, the rest depends on quicklook plugins you use. Don't judge hard, I am not a coder, just wanted some features and made them as I could. Any advices are welcome.

Features:
```
  1. Support of any file preview right in Finder with Gallery view mode.
  2. Reveals selected file from active Finder window to Ranger.
  3. Reveals selected files from Ranger in Finder. (Code from Ranger's wiki)
  4. Start's fullscreen quicklook on active file in Finder's preview.
  5. Toggle red Finder's and Ranger's tag on files. (Needs a dependency)
```

Installation:

  1. Add contents of this commands.py to your ~/.config/ranger/commands.py file.
  2. Edit the code / change to your terminal application and set your key mappings for directional keys.
  3. Install [Tag](https://github.com/jdberry/tag) for color tags support.
  4. Add key maps to your ~/.config/ranger/rc.conf

```
      Examples:

      map <Space> follow_files
      map <Alt><Space> quicklook
      map <alt>/  show_files_in_finder
      map <alt>?  get_finder
      map ' red_tag
```

Todo: Add better cross support for Finder's color tags.

![Preview](https://github.com/Bellavene/findger/blob/main/Preview.png?raw=true "Preview")
