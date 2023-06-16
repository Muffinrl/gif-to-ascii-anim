/***
 * run.c contains the source code of the main executable,
 * which is used to run the animation in a command line instance.
***/

#include <stdio.h>
#include <stdlib.h>

#ifdef _WIN32
#include <Windows.h>
#else
#include <unistd.h>
#endif

#define MAX_ROWS 1000
#define MAX_COLS 1000

void display_animation(FILE* file, int delay) {
    char line[MAX_COLS];

    while (1) {
        rewind(file);  // Go back to the beginning of the file

        while (fgets(line, sizeof(line), file)) {
            printf("\033[2J");  // Clear the console
            printf("\033[H");   // Move cursor to the top-left position

            // Print current frame
            printf("%s", line);
            while (fgets(line, sizeof(line), file) && line[0] != '\n') {
                printf("%s", line);
            }

            fflush(stdout);

#ifdef _WIN32
            Sleep(delay);  // Delay between frames
#else
            usleep(delay * 1000);  // Delay between frames
#endif
        }
    }
}

int main() {
    FILE* file = fopen("animation.txt", "r");
    if (file == NULL) {
        perror("Error opening file");
        return 1;
    }

    int delay = 40;  // Delay between frames in milliseconds
    display_animation(file, delay);

    fclose(file);
    return 0;
}
