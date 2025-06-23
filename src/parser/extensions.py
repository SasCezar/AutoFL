import enum


# Adapted from: https://gist.github.com/ppisarczyk/43962d06686722d26d176fad46879d41
class Extension(enum.Enum):
    c = {".h", ".c"}
    c_sharp = {".cs"}
    cpp = {
        ".h",
        ".inc",
        ".inl",
        ".ipp",
        ".cc",
        ".hpp",
        ".c++",
        ".hxx",
        ".cxx",
        ".tcc",
        ".hh",
        ".cpp",
        ".tpp",
        ".h++",
        ".cp",
    }
    go = {".go"}
    java = {".java"}
    python = {".py"}
