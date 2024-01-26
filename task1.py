import os
import sys


class AlreadyExists(Exception):
    ...


class Copyfier:
    def __init__(self, path: str, destination: str) -> None:
        self._path: str = self.__get_clean_path(path=path)
        self._destination: str = self.__get_clean_path(path=destination)
        self.__absolute_paths_of_copying_files: list[str] = []
        self.__inner_paths: dict[str, str] = {}

    def __get_inner_path_for_extention(self, extension: str) -> str:
        if extension not in self.__inner_paths.keys():
            self.__inner_paths[extension] = self.__get_clean_path(
                f"{self._destination}/{extension}"
            )
            os.makedirs(name=self.__inner_paths[extension])
        return self.__inner_paths[extension]

    def __get_clean_path(self, path: str) -> str:
        if path[-1] == "/":
            path = path[:-1]
        return path

    def __get_file_extension(self, filename: str) -> str:
        if "." not in filename:
            return "txt"
        filename = self.__get_clean_path(path=filename)
        return filename[filename.rfind(".") + 1 :]

    def __get_files_of(self, path: str) -> None:
        path = self.__get_clean_path(path)
        for file in os.listdir(path=path):
            file_path = f"{path}/{file}"
            if os.path.isfile(path=file_path):
                self.__absolute_paths_of_copying_files.append(file_path)
            else:
                self.__get_files_of(path=file_path)

    def __get_filename(self, path: str) -> str:
        path = self.__get_clean_path(path=path)
        if "/" not in path:
            return path
        return path[path.rfind("/") + 1 :]

    def execute(self) -> None:
        if os.path.exists(path=self._destination):
            raise AlreadyExists(f"Directory {self._destination} already exists")
        os.makedirs(name=self._destination)
        self.__get_files_of(path=self._path)
        for path in self.__absolute_paths_of_copying_files:
            filename = self.__get_filename(path=path)
            destination = self.__get_inner_path_for_extention(
                extension=self.__get_file_extension(filename=filename)
            )
            os.popen(f"cp {path} {destination}/{filename}")


path: str = sys.argv[1] if len(sys.argv) > 1 else ""
if path[-1] == "/":
    path = path[:-1]

destination: str = sys.argv[2] if len(sys.argv) > 2 else f"{path}/dist" if path else ""

copyfier = Copyfier(path=path, destination=destination)

copyfier.execute()
