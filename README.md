# es-theme-alcamoth

## Inspiration

- [box-art-marquee-and-video-snap-simultaneously-in-themes](https://retropie.org.uk/forum/topic/25795/box-art-marquee-and-video-snap-simultaneously-in-themes?_=1707102279378)
- [box-art-marquee-and-video-snap-simultaneously-in-themes/19](https://retropie.org.uk/forum/topic/25795/box-art-marquee-and-video-snap-simultaneously-in-themes/19?_=1707101595384)
- [es-theme-artbook](https://github.com/anthonycaccese/es-theme-art-book)
- [es-theme-Chicuelo](https://github.com/chicueloarcade/es-theme-Chicuelo)

## Features

- Primarily dark
- Large-ish font sizes
- System view focuses on console or controller images
- Game list on left in detailed view
- Display screenshot (or video if available), box art, marquee, and description/game info
- Focus is on screenshot or video (middle of screen)
- Description below screenshot or video
- Marquee, box art, and game info on right

## Image assets

### Controllers

Most controller images are from Pineapple Graphics (see [Sublicenses](#sublicenses)). A small drop shadow was added to each controller, and the controllers are scaled roughly based on their actual physical sizes (6 px = 1 mm) and placed on a 1560x960 transparent canvas.

### Header images

Most header logos are from Dan Patrick (see [Sublicenses](#sublicenses)). To get the SVGs to display properly in Emulation Station, I had to edit most of them with Inkscape. Generally they had to be flattened and re-saved. If any paths displayed incorrectly when selecting all layers and objects and then flattening, it helped to select each path (e.g. each letter or shape) individually and perform a Path->Union (⌘ + on macOS) operation on it, and then retry flattening all paths, group them, and save.

## Theme

Some notes from [Creating Your Own EmulationStation Theme](https://retropie.org.uk/docs/Creating-Your-Own-EmulationStation-Theme/).

Themes can use:

- `md_description`
- `md_developer`
- `md_genre`
- `md_image`
- `md_thumbnail`
- `md_lastplayed`: Stored as ISO8601 date time format e.g., 2023-03-17T19:14:12+00:00
- `md_playcount`
- `md_players`
- `md_publisher`
- `md_rating`
- `md_marquee`
- `md_releasedate`: Stored as ISO8601 date format e.g., 2023-03-17

Video view can contain `md_video`.

## Licensing

This theme is licensed under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](LICENSE).

### Sublicenses

- Controller images are from [Pineapple Graphic](https://archive.org/details/full-color-pngs), license TBD
- Console logo images are from [Dan Patrick](https://archive.org/details/console-logos-professionally-redrawn-plus-official-versions_202203), license TBD
- RetroPie logos are from [the RetroPie team on Wikimedia Commons](https://commons.wikimedia.org/wiki/File:RetroPie-Icon.svg), licensed under the GPLv3
- Background image is [Micro Carbon Pattern by Atle Mo](https://www.toptal.com/designers/subtlepatterns/micro-carbon/)
