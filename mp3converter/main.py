"""
A simple utility to convert different audio files to mp3.
"""
import argparse
import os
import platform
import subprocess
import shutil
from glob import glob

VERSION = "0.1.1"

def get_args(args: list = None):
    parser = argparse.ArgumentParser(
        prog=os.path.basename(__file__),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=__doc__,
    )
    parser.add_argument("input", type=str, help="input dir")
    parser.add_argument("output", type=str, help="output dir (can be same as input)")
    parser.add_argument(
        "-e",
        "--extensions",
        default=".m4a",
        type=str,
        help="Extensions for converting files (separated by ;)",
    )
    return parser.parse_args(args) if args else parser.parse_args()

def encode_mp3(i_path: str, o_path: str, quality: int):
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
    subprocess.run(cmd, check=False)

def main(args):
    exts = set(args.extensions.split(";"))
    exts.add(".mp3")  # om bestaande mp3's te detecteren
    paths = glob(f"{args.input}/**/*.*", recursive=True)
    paths = sorted(p for p in paths if os.path.splitext(p.lower())[-1] in exts)

    processed = 0
    for i_path in paths:
        i_path = os.path.abspath(i_path)
        o_path = i_path.replace(args.input,
