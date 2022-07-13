# findger

A [Ranger](https://github.com/ranger/ranger) plugin/script that adds support for macos Finder. Uses Finder to preview virtually anything, the rest depends on quicklook plugins you use.

![screen-gif](./preview.gif)

Features:
```
  1. Support of any file preview right in Finder with Gallery view mode.
  2. Reveals selected file from active Finder window to Ranger.
  3. Reveals selected files from Ranger in Finder. (Code from Ranger's wiki)
  4. Toggle red Finder's and Ranger's tag on selected files. (Needs a dependency)
```

Installation:

  1. Add contents of this commands.py to your ~/.config/ranger/commands.py file.
  2. Edit the code to set your key mappings for directional keys.
  3. Install [Tag](https://github.com/jdberry/tag) for color tags support.
  4. Add key maps to your ~/.config/ranger/rc.conf

```
      Examples:

      map <Space> follow_files
      map <alt>/  show_files_in_finder
      map <alt>?  get_finder
      map ' red_tag
```

Todo: Add better cross support for Finder's color tags.
