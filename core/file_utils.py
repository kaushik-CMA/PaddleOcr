from pathlib import Path


SUPPORTED_IMAGES = {
    ".jpg",
    ".jpeg",
    ".png",
    ".bmp",
    ".tif",
    ".tiff",
    ".webp",
}


def get_images(folder):

    folder = Path(folder)

    images = []

    for file in folder.iterdir():

        if file.suffix.lower() in SUPPORTED_IMAGES:
            images.append(file)

    return sorted(images)