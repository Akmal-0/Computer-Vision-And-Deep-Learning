#!/usr/bin/env python3
"""Build the classification metadata from extracted Earth Block video frames."""

import argparse
import csv
import json
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent
CLASSES = ("Red_Earth_Block", "Blue_Earth_Block", "Sky_Block")


def build_metadata(dataset_root: Path, output: Path) -> int:
    rows = []
    for folder_name in CLASSES:
        folder = dataset_root / folder_name
        csv_path = folder / "frames.csv"
        json_path = folder / "extraction.json"
        if not folder.is_dir() or not csv_path.is_file() or not json_path.is_file():
            raise FileNotFoundError(f"Expected images, frames.csv, and extraction.json in {folder}")
        extraction = json.loads(json_path.read_text(encoding="utf-8"))
        with csv_path.open(newline="", encoding="utf-8") as handle:
            frames = list(csv.DictReader(handle))
        if not frames or not {"image", "frame_index", "seconds_approx", "group"}.issubset(frames[0]):
            raise ValueError(f"Unexpected frames.csv schema: {csv_path}")
        if extraction.get("saved_count") != len(frames):
            raise ValueError(f"saved_count does not match frames.csv in {folder}")
        expected_images = {row["image"] for row in frames}
        actual_images = {path.name for path in folder.glob("*.jpg")}
        if expected_images != actual_images:
            raise ValueError(f"frames.csv/JPEG mismatch in {folder}")

        label = folder_name.lower()
        for frame in frames:
            image_path = folder / frame["image"]
            with Image.open(image_path) as image:
                width, height = image.size
                image.verify()
            rows.append({
                "path": image_path.relative_to(ROOT).as_posix(),
                "label": label,
                "frame_index": int(frame["frame_index"]),
                "seconds_approx": frame["seconds_approx"],
                "group": label,
                "width": width,
                "height": height,
                "split": "",
            })

    output.parent.mkdir(parents=True, exist_ok=True)
    fields = ["path", "label", "frame_index", "seconds_approx", "group", "width", "height", "split"]
    with output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    return len(rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dataset-root", type=Path, default=ROOT / "dataset")
    parser.add_argument("--output", type=Path, default=ROOT / "metadata.csv")
    args = parser.parse_args()
    count = build_metadata(args.dataset_root, args.output)
    print(f"Wrote {count} image records to {args.output}")


if __name__ == "__main__":
    main()
