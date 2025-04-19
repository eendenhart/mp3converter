"""
A simple utility to convert different audio files to mp3.
"""
import argparse
import os
import platform
import subprocess
import shutil
from glob import glob

VERSION = "0.1.0"

def get_args(args: list = None):
    parser = argparse.ArgumentParser(
        prog=os.path.basename(__file__),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=__doc__,
    )
    parser.add_argument("input", type=str, help="input dir")
    parser.add_argument(
        "-e",
        "--extensions",
        default=".m4a",
        type=str,
        help="Extensions for converting files (separated by ;)",
    )
    return parser.parse_args(args) if args else parser.parse_args()

def encode_mp3(i_path: str, o_path: str, quality: int):
    """Encode given audio file to mp3 using ffmpeg command."""
    prog = "ffmpeg"
    if "win" in platform.system().lower():
        prog += ".exe"
    cmd = [
        prog,
        "-i", i_path,
        "-f", "mp3",
        "-hide_banner",
        "-loglevel", "error",
        "-c:v", "copy",
        "-b:a", f"{quality}k",
        o_path,
    ]
    print(" ".join(cmd))
    subprocess.run(cmd)

def main(args):
    exts = set(args.extensions.lower().split(";"))  # alleen opgegeven extensies
    filter_func = lambda p: os.path.splitext(p.lower())[-1] in exts
    paths = glob(f"{args.input}/**/*.*", recursive=True)
    paths = sorted(list(filter(filter_func, paths)))
    processed = 0
    for i_path in paths:
        i_path = os.path.abspath(i_path)
        o_path = os.path.splitext(i_path)[0] + ".mp3"

        # Skip als output mp3 recenter is dan originele bestand
        if os.path.isfile(o_path):
            if os.path.getmtime(o_path) > os.path.getmtime(i_path):
                continue  # up-to-date
            os.remove(o_path)

        # Zorg dat map bestaat
        os.makedirs(os.path.dirname(o_path), exist_ok=True)
        encode_mp3(i_path, o_path, 192)
        print(f"{i_path} >> {o_path}")
        processed += 1

    if not processed:
        print("Everything was up-to-date.")

if __name__ == "__main__":
    print(f"{VERSION=}")
    src = os.environ.get("MP3CONVERTER_SRC", None)
    if src:
        args = [src]
        if ext := os.environ.get("MP3CONVERTER_EXT", None):
            args.extend(["-e", ext])
        print(f"{args=}")
        main(get_args(args))
    else:
        main(get_args())
