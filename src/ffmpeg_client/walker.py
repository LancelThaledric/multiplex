from pathlib import Path

from typing import Generator

type FileWalkGenerator = Generator[(Path, list[str], list[str])]


class FileWalker:
    """
    A utility class to go cross a list of files and folders and return list of file to be processed
    """

    def __init__(self, paths: list[Path]):
        self._input = [p.resolve() for p in paths]
        self._walked: list[None | FileWalkGenerator | Path] = [None for _ in paths]

    def walk(self, i: int):
        if i < -len(self._input) or i >= len(self._input):
            raise IndexError('list index out of range')
        if self._input[i].is_dir():
            self._walked[i] = self._input[i].walk() if self._walked[i] is None else self._walked[i]
        else:
            self._walked[i] = self._input[i]
        return self._walked[i]

    def __getitem__(self, item):
        return self._input[item]

    def __setitem__(self, key, value):
        self._input[key] = value
        self._walked[key] = None

    def __delitem__(self, key):
        del self._input[key]
        del self._walked[key]

    def iterfiles(self):
        """return an iterator over all files of all input paths walked down"""
        for path_idx, _ in enumerate(self._walked):
            self.walk(path_idx)
            if isinstance(self._walked[path_idx], Path):
                yield self._walked[path_idx]
            else:
                for folder in sorted(self._walked[path_idx]):
                    for file in sorted(folder[2]):
                        yield Path(folder[0]) / file
