import os
import json
import shlex
import atexit
import werkzeug
import subprocess

from pathlib import Path
from typing import Optional


class Watcher:

    proc: Optional[subprocess.Popen] = None

    def __init__(self, root_path: str, npm_script_name: str):
        """ Start subprocess to watch TailwindCSS on-the-fly on change.

        Prerequisites: flask app is run in debug mode & second instance started
        by `werkzeug` is running (this second instance is needed in debug mode
        to watch for changes). This ensures that the subprocess is only started
        once.
        """

        is_reloader = werkzeug.serving.is_running_from_reloader()

        if is_reloader:
            self.root_path = root_path
            self.npm_script_name = npm_script_name

            self.run()

        else:
            print(" * TailwindCSS Compiler not started")

            pass

    def run(self):
        """ Run TailwindCSS watcher as subprocess. """

        cwd = os.getcwd()
        app_parent_dir = str(Path(self.root_path).parent)

        os.chdir(app_parent_dir)
        with open("package.json") as f:
            package = json.load(f)

            try:
                cmd = shlex.split(package["scripts"][self.npm_script_name])
                print(" * Watcher for TailwindCSS is active!")
            except KeyError:
                raise ValueError(
                    f"No script with name '{self.npm_script_name}' "
                    "found in `package.json`."
                )

        Watcher.proc = subprocess.Popen(cmd)
        os.chdir(cwd)

        atexit.register(Watcher.terminate_on_exit)

    @classmethod
    def terminate_on_exit(cls):
        print(" * Watcher of TailwindCSS is stopped!")

        Watcher.proc.terminate()
