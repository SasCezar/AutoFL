// Adapted from https://github.com/orangeduck/Corange/blob/master/src/cgraphics.c
#include "cgraphics.h"
#include "casset.h"

#include "assets/image.h"

static SDL_Window* screen = NULL;
static SDL_GLContext* context = NULL;

static int window_flags = 0;
static int window_multisamples = 0;
static int window_multisamplesbuffs = 0;
static int window_antialiasing = 0;

static void graphics_viewport_start() {

  screen = SDL_CreateWindow("Corange",
                          SDL_WINDOWPOS_UNDEFINED,
                          SDL_WINDOWPOS_UNDEFINED,
                          800, 600,
                          window_flags);

  if (screen == NULL) {
    error("Could not create SDL window: %s", SDL_GetError());
  }

  graphics_viewport_set_icon(P("$CORANGE/ui/corange.bmp"));

  SDL_GL_SetAttribute(SDL_GL_SHARE_WITH_CURRENT_CONTEXT, 1);
  context = SDL_GL_CreateContext(screen);

  if (context == NULL) {
    error("Could not create SDL context: %s", SDL_GetError());
  }

  SDL_GL_SetSwapInterval(1);
  SDL_GL_LoadExtensions();

  glViewport(0, 0, 800, 600);

}

SDL_GLContext* graphics_context_new() {
  SDL_GL_SetAttribute(SDL_GL_SHARE_WITH_CURRENT_CONTEXT, 1);
  return SDL_GL_CreateContext(screen);
}

void graphics_context_delete(SDL_GLContext* context) {
  SDL_GL_DeleteContext(context);
}


void graphics_set_multisamples(int multisamples) {
  window_multisamples = multisamples;
  if (multisamples > 0) {
    window_multisamplesbuffs = 1;
  } else {
    window_multisamplesbuffs = 0;
  }
}

bool graphics_get_fullscreen() {
  if (window_flags & SDL_WINDOW_FULLSCREEN_DESKTOP) {
    return true;
  } else {
    return false;
  }
}

static char timestamp_string[256];
static char screenshot_string[256];

void graphics_viewport_screenshot() {
  unsigned char* image_data = malloc( sizeof(unsigned char) * graphics_viewport_width() * graphics_viewport_height() * 4 );
  glReadPixels( 0, 0, graphics_viewport_width(), graphics_viewport_height(), GL_BGRA, GL_UNSIGNED_BYTE, image_data );

  image* i = image_new(graphics_viewport_width(), graphics_viewport_height(), image_data);
  image_flip_vertical(i);
  image_bgr_to_rgb(i);

  free(image_data);

  timestamp(timestamp_string);

  screenshot_string[0] = '\0';
  strcat(screenshot_string, "./corange_");
  strcat(screenshot_string, timestamp_string);
  strcat(screenshot_string, ".tga");

  image_write_to_file(i, screenshot_string);

  image_delete(i);

}
