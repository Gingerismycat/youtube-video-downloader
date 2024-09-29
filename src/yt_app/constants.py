import pathlib

_LOCAL = pathlib.Path(__file__).parent.resolve()
REPO_ROOT = _LOCAL.joinpath("../..").resolve()
VIDEO_DIR = REPO_ROOT.joinpath("videos").resolve()

if __name__ == "__main__":
    print(VIDEO_DIR)
    print(VIDEO_DIR.exists())