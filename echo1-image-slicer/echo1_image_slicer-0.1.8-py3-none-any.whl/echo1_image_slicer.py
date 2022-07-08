import argparse, os
from loguru import logger
from .helpers.sahi import get_slice_bboxes, read_image_as_pil


def slice_image(
    file_path="image.tif",
    save_to_file_prefix="",
    save_to_dir="./output",
    slice_width: int = 512,
    slice_height: int = 512,
    overlap_width_ratio: int = 0.2,
    overlap_height_ratio: int = 0.2,
):

    logger.info("Loading the file {}".format(file_path))

    # Read the image from disk
    image_pil = read_image_as_pil(file_path)

    logger.debug("The image shape is {}".format(image_pil.size))

    image_width, image_height = image_pil.size

    if not (image_width != 0 and image_height != 0):
        raise AssertionError("Invalid image size {}".format(image_pil.size))

    logger.debug("Calculating the slice box positions.")

    slice_bboxes = get_slice_bboxes(
        image_height=image_height,
        image_width=image_width,
        slice_height=slice_height,
        slice_width=slice_width,
        overlap_height_ratio=overlap_height_ratio,
        overlap_width_ratio=overlap_width_ratio,
    )

    os.makedirs(save_to_dir, exist_ok=True)

    part = 0

    # Iterate over the slice bounding boxes
    for slice_bbox in slice_bboxes:
        # Crop the image using the sliced bounding box coordinates
        image_pil_slice = image_pil.crop(slice_bbox)

        # Generate an incrementing file name
        save_file_path = save_to_file_prefix + format(part, "04") + ".jpg"

        # Save the file to disk
        image_pil_slice.save(os.path.join(save_to_dir, save_file_path))

        # Increment the file name
        part += 1

    logger.info("Saved {} image slices to {}".format(part, save_to_dir))


def app():

    parser = argparse.ArgumentParser(description="Slices an image into smaller images.")
    parser.add_argument(
        "-f",
        "--file_path",
        help="The path to a directory of images of path to a file.",
        required=True,
        type=str,
    )
    parser.add_argument(
        "-s",
        "--save_to_dir",
        help="The directory to save the slices to.",
        required=True,
        type=str,
    )
    parser.add_argument(
        "-sw",
        "--slice_width",
        help="The width of each slice.",
        required=True,
        type=int,
    )
    parser.add_argument(
        "-sh",
        "--slice_height",
        help="The height of each slice.",
        required=True,
        type=int,
    )
    parser.add_argument(
        "-ow",
        "--overlap_width_ratio",
        help="The overlap width ratio.",
        default=0.2,
        type=float,
    )
    parser.add_argument(
        "-oh",
        "--overlap_height_ratio",
        help="The overlap height ratio.",
        default=0.2,
        type=float,
    )

    # image-slicer -f ./tests/test.jpg -s ./output -sw 500 -sh 500
    args = vars(parser.parse_args())

    # If the file path is a file
    if os.path.isfile(args["file_path"]):
        file_path = args["file_path"]
        file_prefix = os.path.splitext(os.path.basename(file_path))[0] + "-"
        slice_image(
            file_path=args["file_path"],
            save_to_file_prefix=file_prefix,
            save_to_dir=args["save_to_dir"],
            slice_width=args["slice_width"],
            slice_height=args["slice_height"],
            overlap_width_ratio=args["overlap_width_ratio"],
            overlap_height_ratio=args["overlap_height_ratio"],
        )

        return

    if os.path.isdir(args["file_path"]):

        # Create an iterator to walk through the directory
        for root, dirs, files in os.walk(args["file_path"], topdown=False):

            # For each file in the acquisition directory
            for file_name in files:

                if file_name.endswith((".jpg", ".jpeg", ".png")):

                    file_path = os.path.join(root, file_name)
                    file_prefix = os.path.splitext(os.path.basename(file_path))[0] + "-"
                    slice_image(
                        file_path=file_path,
                        save_to_file_prefix=file_prefix,
                        save_to_dir=args["save_to_dir"],
                        slice_width=args["slice_width"],
                        slice_height=args["slice_height"],
                        overlap_width_ratio=args["overlap_width_ratio"],
                        overlap_height_ratio=args["overlap_height_ratio"],
                    )
