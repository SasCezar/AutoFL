import unittest
from pathlib import Path

from hydra import initialize, compose

from entity.file import File
from parser.extensions import Extension
from parser.parser import ParserFactory, ParserBase


class TestPythonParser(unittest.TestCase):
    def setUp(self) -> None:
        with initialize(version_base='1.3', config_path="../../config/"):
            self.cfg = compose(config_name="test.yaml")

        file_path = Path(self.cfg.test_data_path).joinpath(Path('parser/cgraphics.c'))
        content = self.load_file(file_path)
        rel_path = str(file_path.relative_to(self.cfg.test_data_path))
        self.file = File(path=rel_path, language=Extension.c.name, content=content)
        self.parser: ParserBase = ParserFactory.create_parser(self.file.language, self.cfg.languages_library)
        self.gt = ['SDL_Window', 'screen', 'SDL_GLContext', 'context', 'window_flags', 'window_multisamples',
                   'window_multisamplesbuffs', 'window_antialiasing', 'graphics_viewport_start', 'screen',
                   'SDL_CreateWindow', 'SDL_WINDOWPOS_UNDEFINED', 'SDL_WINDOWPOS_UNDEFINED', 'window_flags', 'screen',
                   'error', 'SDL_GetError', 'graphics_viewport_set_icon', 'P', 'SDL_GL_SetAttribute',
                   'SDL_GL_SHARE_WITH_CURRENT_CONTEXT', 'context', 'SDL_GL_CreateContext', 'screen', 'context', 'error',
                   'SDL_GetError', 'SDL_GL_SetSwapInterval', 'SDL_GL_LoadExtensions', 'glViewport', 'SDL_GLContext',
                   'graphics_context_new', 'SDL_GL_SetAttribute', 'SDL_GL_SHARE_WITH_CURRENT_CONTEXT',
                   'SDL_GL_CreateContext', 'screen', 'graphics_context_delete', 'SDL_GLContext', 'context',
                   'SDL_GL_DeleteContext', 'context', 'graphics_set_multisamples', 'multisamples', 'window_multisamples',
                   'multisamples', 'multisamples', 'window_multisamplesbuffs', 'window_multisamplesbuffs',
                   'graphics_get_fullscreen', 'window_flags', 'SDL_WINDOW_FULLSCREEN_DESKTOP', 'timestamp_string',
                   'screenshot_string', 'graphics_viewport_screenshot', 'image_data', 'graphics_viewport_width',
                   'graphics_viewport_height', 'glReadPixels', 'graphics_viewport_width', 'graphics_viewport_height',
                   'GL_BGRA', 'GL_UNSIGNED_BYTE', 'image_data', 'image', 'i', 'image_new', 'graphics_viewport_width',
                   'graphics_viewport_height', 'image_data', 'image_flip_vertical', 'i', 'image_bgr_to_rgb', 'i',
                   'free', 'image_data', 'timestamp', 'timestamp_string', 'screenshot_string', 'strcat',
                   'screenshot_string', 'strcat', 'screenshot_string', 'timestamp_string', 'strcat',
                   'screenshot_string', 'image_write_to_file', 'i', 'screenshot_string', 'image_delete', 'i']

    def test_identifiers(self):
        identifiers, _ = self.parser.parse(self.file)
        self.assertListEqual(identifiers, self.gt)

    @staticmethod
    def load_file(path):
        with open(path, 'rt') as inf:
            return "".join(inf.readlines())


if __name__ == '__main__':
    unittest.main()
