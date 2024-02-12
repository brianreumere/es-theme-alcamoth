# es-theme-alcamoth

## Inspiration

These are some other themes and screenshots that inspired the layout of this theme.

- [box-art-marquee-and-video-snap-simultaneously-in-themes](https://retropie.org.uk/forum/topic/25795/box-art-marquee-and-video-snap-simultaneously-in-themes?_=1707102279378)
- [box-art-marquee-and-video-snap-simultaneously-in-themes/19](https://retropie.org.uk/forum/topic/25795/box-art-marquee-and-video-snap-simultaneously-in-themes/19?_=1707101595384)
- [es-theme-artbook](https://github.com/anthonycaccese/es-theme-art-book)
- [es-theme-Chicuelo](https://github.com/chicueloarcade/es-theme-Chicuelo)

The name Alcamoth is just a [cool city name from one of my favorite games](https://xenoblade.fandom.com/wiki/Alcamoth).

## Features

- Primarily dark
- Large-ish font sizes so you can read the game description on a TV across the room
- System carousel view focuses on console or controller images
- Game list on left in detailed view
- Detailed and video views display screenshot or video, box art, game description, and game metadata simultaneously

## Image assets

### Controllers

Controller and handheld console images are from [Pineapple Graphics](https://www.instagram.com/pineapple.graphics/) (see [Sublicenses](#sublicenses)). A small drop shadow was added to each controller, and the controllers are scaled roughly based on their actual physical sizes (6 px = 1 mm) and placed on a 1560x960 transparent canvas.

### Header images

Console header logos are from Dan Patrick (see [Sublicenses](#sublicenses)). To get the SVGs to display properly in Emulation Station, I had to edit most of them with Inkscape. Generally they had to be flattened and re-saved. If any paths displayed incorrectly when selecting all layers and objects and then flattening, it helped to select each path (e.g. each letter or shape) individually and perform a Path->Union (⌘ + on macOS) operation on it, and then retry flattening all paths, group them, and save.

## Theme

[Creating Your Own EmulationStation Theme](https://retropie.org.uk/docs/Creating-Your-Own-EmulationStation-Theme/) and the [EmulationStation themes reference documentation](https://github.com/RetroPie/EmulationStation/blob/master/THEMES.md) were helpful in creating the theme.

### Scraping and game data

[Skyscraper](https://gemba.github.io/skyscraper/) is a great tool for scraping game data and [ScreenScraper](https://screenscraper.fr/) is an incredible resource for game descriptions, screenshots, videos, etc.

This theme expects at least the `cover` and `screenshot` outputs in Skyscraper's `artwork.xml` file. When Skyscraper generates gamelist XML data, this will point each game's `thumbnail` path to the game cover/box art and `image` to a screenshot. You can optionally do fancier things with Skyscraper like add drop shadows or create composites of multiple images, as long as the resulting gamelist XML has the `thumbnail` and `image` paths (the theme will display `thumbnail`  above the game metadata and `image` in the middle of the screen above the game description).

## Licensing

With the exception of any sublicenses listed below, this theme is licensed under the BSD 2-Clause license.

All trademarks and logos used are the property of their respective owners.

### Sublicenses

- Controller images by Pineapple Graphics ([archive.org](https://archive.org/details/full-color-pngs), [Instagram](https://www.instagram.com/pineapple.graphics/))
- Console logos by Dan Patrick ([archive.org](https://archive.org/details/console-logos-professionally-redrawn-plus-official-versions_202203), [LaunchBox forums](https://forums.launchbox-app.com/files/file/3402-v2-platform-logos-professionally-redrawn-official-versions-new-bigbox-defaults/))
- The RetroPie logo by Florian Müller and [licensed under the CC BY-NC-ND 4.0 International license](https://retropie.org.uk/about/logo-and-logo-license/)
- Background image [Micro Carbon Pattern by Atle Mo](https://www.toptal.com/designers/subtlepatterns/micro-carbon/)
- [Nunito font](https://github.com/googlefonts/nunito) by Vernon Adams and [licensed under the Open Font License version 1.1](https://github.com/googlefonts/nunito?tab=OFL-1.1-1-ov-file#readme)
