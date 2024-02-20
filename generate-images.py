#!/usr/bin/env python3

import math

from wand.color import Color
from wand.image import Image


# This script takes a set of source images and scales them based on a pixels per millimeter value,
# adds a drop shadow, and places them on a transparent canvas. It depends on data about the real
# world dimensions of the images, and expects the source images to be named
# "<system short name>-source.png". Dimensions are in millimeters.

controllers = {
    "3do": {
        "dimensions": {"x": 153, "y": 70},
        "source": "https://mathpirate.net/log/wp-content/uploads/2011/03/3DO.jpg",
        "notes": "Estimate based on photo"
    },
    "arcade": {
        "dimensions": {"x": 303, "y": 203},
        "source": "https://www.8bitdo.com/arcade-stick/",
        "notes": (
            "Source image from Pineapple Graphics appears to be based on 8BitDo arcade stick, so "
            "use its dimensions"
        )
    },
    "atari2600": {
        "dimensions": {"x": 104, "y": 170},
        "source": "https://atari.com/products/cx40-joystick"
    },
    "atari7800": {
        "dimensions": {"x": None, "y": 159},
        "source": (
            "https://mathpirate.net/GameSystems/Atari7800/Images/Atari7800_Joystick_Front.jpg"
        ),
    },
    "atarijaguar": {
        "dimensions": {"x": 159, "y": 127},
        "source": "https://mathpirate.net/GameSystems/AtariJaguar/index.html"
    },
    "atarilynx": {
        "dimensions": {"x": 273, "y": 108},
        "source": "https://www.consoledatabase.com/consoleinfo/atarilynx/"
    },
    "auto-allgames": {
        "dimensions": {"x": None, "y": 50},
        "source": None,
        "notes": "Arbitrary dimensions, not an actual controller"
    },
    "auto-favorites": {
        "dimensions": {"x": None, "y": 80},
        "source": None,
        "notes": "Arbitrary dimensions, not an actual controller"
    },
    "auto-lastplayed": {
        "dimensions": {"x": None, "y": 160},
        "source": None,
        "notes": "Arbitrary dimensions, not an actual controller"
    },
    "colecovision": {
        "dimensions": {"x": None, "y": 160},
        "source": None,
        "notes": "Estimate based on console dimensions and photos"
    },
    "dreamcast": {
        "dimensions": {"x": 147, "y": 152},
        "source": "https://www.dimensions.com/element/dreamcast-controller"
    },
    "fds": {
        "dimensions": {"x": 123, "y": 53},
        "source": None,
        "notes": "Couldn't find definitive source, just use same dimensions as NES/Famicom"
    },
    "gameandwatch": {
        "dimensions": {"x": 111, "y": 67},
        "source": (
            "https://collections.vam.ac.uk/item/O1386780/"
            "game--watch-wide-screen-handheld-video-games-nintendo/"
        ),
        "notes": "Dimensions for widescreen version"
    },
    "gamegear": {
        "dimensions": {"x": 210, "y": 113},
        "source": "https://en.wikipedia.org/wiki/Game_Gear"
    },
    "gb": {
        "dimensions": {"x": 90, "y": 148},
        "source": "https://en.wikipedia.org/wiki/Game_Boy"
    },
    "gba": {
        "dimensions": {"x": 144.5, "y": 82},
        "source": "https://en.wikipedia.org/wiki/Game_Boy_Advance"
    },
    "gbc": {
        "dimensions": {"x": 78, "y": 133.5},
        "source": "https://en.wikipedia.org/wiki/Game_Boy_Color"
    },
    "gc": {
        "dimensions": {"x": 140, "y": 100},
        "source": "https://en.wikipedia.org/wiki/GameCube_controller"
    },
    "intellivision": {
        "dimensions": {"x": None, "y": 158},
        "source": "https://www.flickr.com/photos/redbeardmathpirate/5586154720",
        "notes": "Estimate based on image"
    },
    "mastersystem": {
        "dimensions": {"x": 120.5, "y": 51},
        "source": (
            "https://www.reddit.com/r/retrogaming/comments/b9b8fo/"
            "dimensions_of_original_sms_and_nes_controllers/"
        )
    },
    "megadrive": {
        "dimensions": {"x": 165, "y": 98},
        "source": "https://www.dimensions.com/element/sega-genesis-controller-3-button"
    },
    "n64": {
        "dimensions": {"x": 160, "y": 152.6},
        "source": "https://www.dimensions.com/element/nintendo-64-controller"
    },
    "nds": {
        "dimensions": {"x": 133, "y": None},
        "source": "https://en.wikipedia.org/wiki/Nintendo_DS_Lite#Hardware",
        "notes": (
            "Source only has closed dimension, so just skip it; this is also for DS Lite since "
            "that is what the source image is of"
        )
    },
    "neogeo": {
        "dimensions": {"x": 280, "y": 190},
        "source": "https://en.wikipedia.org/wiki/Neo_Geo_(system)#Technical_details"
    },
    "ngpc": {
        "dimensions": {"x": 130, "y": 80},
        "source": "https://www.vgmuseum.com/systems/ngpc/"
    },
    "nes": {
        "dimensions": {"x": 123, "y": 53},
        "source": "https://www.reddit.com/r/RetroPie/comments/b8sgac/nes_controller_dimensions/"
    },
    "pcengine": {
        "dimensions": {"x": 130, "y": 60.2},
        "source": "https://www.8bitdo.com/pce-2-4g/"
    },
    "pokemini": {
        "dimensions": {"x": 58, "y": 74},
        "source": (
            "https://www.nintendo.co.uk/Hardware/Nintendo-History/Pokemon-mini/"
            "Pokemon-mini-627132.html"
        )
    },
    "ps2": {
        "dimensions": {"x": 157, "y": 95},
        "source": "https://en.wikipedia.org/wiki/DualShock"
    },
    "psp": {
        "dimensions": {"x": 170, "y": 74},
        "source": "https://en.wikipedia.org/wiki/PlayStation_Portable"
    },
    "psx": {
        "dimensions": {"x": 157, "y": 95},
        "source": "https://en.wikipedia.org/wiki/DualShock"
    },
    "saturn": {
        "dimensions": {"x": 155, "y": 86},
        "source": "https://www.dimensions.com/element/sega-saturn-controller-model-2"
    },
    "sega32x": {
        "dimensions": {"x": 135, "y": None},
        "source": None,
        "notes": "Estimate based on photo of 6-button Genesis/Mega Drive controller"
    },
    "snes": {
        "dimensions": {"x": 144, "y": 61},
        "source": "https://www.reddit.com/r/snes/comments/aj5uec/comment/eetdqrk/"
    },
    "vectrex": {
        "dimensions": {"x": 305, "y": None},
        "source": None,
        "notes": "Estimate based on photo"
    },
    "virtualboy": {
        "dimensions": {"x": None, "y": 130},
        "source": None,
        "notes": "Estimate based on photo"
    },
    "wii": {
        "dimensions": {"x": None, "y": 160},
        "source": "https://www.dimensions.com/element/wii-remote",
        "notes": "Source image includes Nunchuck, so just include height of Wii Remote"
    }
}
print(f"Processing {len(controllers)} controller images")

# Currently in .gitignore, may include as a submodule later (to prevent git clone, which is how
# the RetroPie setup script installs a theme, from downloading source images unnecessarily)
source_images_dir = "./_inc/source-images/controllers"
dest_images_dir = "./_inc/source-images/test-output"
print(f"Using source and destination image directories {source_images_dir} and {dest_images_dir}")

canvas_size = {
    "x": math.ceil(2560 * 0.5),  # From x dimension of logoSize given 4K display
    "y": math.ceil(1440 * 0.6)   # From y dimension of logoSize given 4K display
}
print(f"Calculated canvas size {canvas_size}")

max_mm_dimensions = {}
for dimension in ["x", "y"]:
    max_mm_dimensions[dimension] = max([
        v["dimensions"][dimension]
        for k, v in controllers.items()
        if v["dimensions"][dimension] is not None
    ])
print(f"Max real-world dimensions are {max_mm_dimensions}")

padding_ratios = {
    "x": 0.1,
    "y": 0.1
}
print(f"Using padding ratios {padding_ratios}")
raw_pixels_per_mm = min([
    (canvas_size["x"] * (1 - padding_ratios["x"])) / max_mm_dimensions["x"],
    (canvas_size["y"] * (1 - padding_ratios["y"])) / max_mm_dimensions["y"],
])
pixels_per_mm = round(raw_pixels_per_mm, 1)
print(f"Calculated raw pixels per millimeter {raw_pixels_per_mm} and rounded to {pixels_per_mm}")

print("Resizing source images")
for k, v in controllers.items():
    with Image(filename=f"{source_images_dir.rstrip('/')}/{k}-source.png") as image:
        print(f"Source size is {image.size}")
        new_dimensions = {}
        for dimension in ["x", "y"]:
            if v["dimensions"][dimension] is None:
                new_dimensions[dimension] = None
            else:
                new_dimensions[dimension] = math.ceil(v["dimensions"][dimension] * pixels_per_mm)
        print(f"New dimensions are {new_dimensions}")
        # Create a geometry string to use with Image.transform()
        new_geometry = ["x"]  # This isn't the x dimension, it's "by"
        if new_dimensions["x"] is not None:
            new_geometry.insert(0, str(new_dimensions["x"]))
        if new_dimensions["y"] is not None:
            new_geometry.append(str(new_dimensions["y"]))
        new_geometry_string = "".join(new_geometry)
        print(f"Generated geometry string {new_geometry_string}")
        with Image(
            width=canvas_size["x"],
            height=canvas_size["y"],
            background=Color('transparent')
        ) as canvas:
            with image.clone() as new_image:
                # Image.transform() is deprecated, but Image.resize() messes up aspect ratio
                new_image.transform(resize=new_geometry_string)
                # new_image.resize(
                #     new_dimensions["x"],
                #     new_dimensions["y"],
                #     filter="undefined",
                #     blur=1
                # )
                # Need to explicitly set this, otherwise Image.extent() makes the background white
                new_image.background_color = Color("transparent")
                new_image.extent(
                    canvas_size["x"],
                    canvas_size["y"],
                    gravity="center"
                )
                with new_image.clone() as shadow_layer:
                    shadow_layer.background_color = "#000000"
                    shadow_layer.shadow(
                        alpha=72,
                        sigma=16
                    )
                    canvas.composite(image=shadow_layer, operator="over")
                    canvas.composite(image=new_image, operator="over")
                    dest_filename = f"{dest_images_dir.rstrip('/')}/{k}.png"
                    print(f"Saving new image for system {k} to {dest_filename}")
                    canvas.save(filename=dest_filename)
