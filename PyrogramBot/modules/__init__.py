import glob
import importlib
import sys

from os.path import dirname, basename, isfile
from PyrogramBot import log


def __list_all_modules():
    # This generates a list of modules in this
    # folder for the * in __main__ to work.
    mod_paths = glob.glob(dirname(__file__) + "/*.py")
    all_modules = [
        basename(f)[:-3]
        for f in mod_paths
        if isfile(f)
        and f.endswith(".py")
        and not f.endswith("__init__.py")
        and not f.endswith("__main__.py")
    ]


importlib.import_module("PyrogramBot.modules.__main__")
ALL_MODULES = sorted(__list_all_modules())
log.info("Modules loaded: %s", str(ALL_MODULES))
__all__ = ALL_MODULES + ["ALL_MODULES"]
