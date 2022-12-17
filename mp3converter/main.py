"""
A simple utility to convert different audio files to mp3.
"""
import argparse
import os
import platform
import subprocess
import shutil
from glob import glob


def get_args():
    parser = argparse.ArgumentParser(
        prog=os.path.basename(__file__),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=__doc__,
    )
    parser.add_argument("input", type=str, help="input dir")
    parser.add_argument("output", type=str, help="output dir")
    return parser.parse_args()


def encode_mp3(i_path: str, o_path: str, quality: int):
    """Encode given audio file to mp3 using ffmpeg command.
    Args:
        i_path (str): input audio file path
        o_path (str): output mp3 file path
        quality (int): quality of output in kbps
    """
    prog = "ffmpeg"
    if "win" in platform.system().lower():
        prog += ".exe"
    cmd = [
        prog,
        "-i",
        i_path,
        "-f",
        "mp3",
        "-hide_banner",
        "-loglevel",
        "error",
        "-c:v",
        "copy",
        "-b:a",
        f"{quality}k",
        o_path,
    ]
    print(" ".join(cmd))
    subprocess.run(cmd)


def path_tree(root):
    tree = {}
    for name in os.listdir(root):
        path = os.path.join(root, name)
        if os.path.isdir(path):
            child = path_tree(path)
            if child:
                tree[name] = child
        else:
            tree[name] = path
    return tree


def main(args):
    exts = {".mp3", ".m4a"}
    filter_func = lambda p: os.path.splitext(p.lower())[-1] in exts
    paths = glob(f"{args.input}/**/*.*", recursive=True)
    paths = sorted(list(filter(filter_func, paths)))
    for i_path in paths:
        o_path = i_path.replace(args.input, args.output, 1)
        o_path = os.path.splitext(o_path.lower())[0] + ".mp3"
        if os.path.isfile(o_path):
            if os.path.getmtime(o_path) > os.path.getmtime(i_path):
                continue  # already up-to-date
            os.remove(o_path)
        os.makedirs(os.path.dirname(o_path), exist_ok=True)
        if i_path.lower().endswith(".mp3"):
            shutil.copy(i_path, o_path)
            print(f"{i_path} >> {o_path}")
        else:
            encode_mp3(i_path, o_path, 192)


def test():
    class dummy:
        pass

    args = dummy()
    args.input = "./downloads"
    args.output = "./backup"
    main(args)


if __name__ == "__main__":
    # test()
    main(get_args())
