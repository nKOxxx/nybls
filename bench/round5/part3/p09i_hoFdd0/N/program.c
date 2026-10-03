/*
 * Spinning Cube - terminal ASCII renderer in C.
 *
 * Reconstructed from the video's title/channel/duration only (see notes.md).
 * The program draws a 3D cube in the terminal using a z-buffer and ANSI
 * escape codes, rotating it continuously about all three axes.
 *
 * Build:  cc -O2 -o cube program.c -lm
 * Run:    ./cube        (Ctrl-C to exit)
 */

#include <math.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>

/* Rotation angles (radians). */
float A, B, C;

/* Cube and screen parameters. */
float cubeWidth = 20;
int   width = 160, height = 44;
float zBuffer[160 * 44];
char  buffer[160 * 44];
int   backgroundASCIICode = ' ';
int   distanceFromCam = 100;
float horizontalOffset;
float K1 = 40;           /* projection scale */

float incrementSpeed = 0.6;

float x, y, z;
float ooz;
int   xp, yp;
int   idx;

/* Rotate a point (i, j, k) about X by A, Y by B, Z by C and return
 * the chosen coordinate. */
float calculateX(int i, int j, int k) {
    return j * sin(A) * sin(B) * cos(C) - k * cos(A) * sin(B) * cos(C) +
           j * cos(A) * sin(C) + k * sin(A) * sin(C) + i * cos(B) * cos(C);
}

float calculateY(int i, int j, int k) {
    return j * cos(A) * cos(C) + k * sin(A) * cos(C) -
           j * sin(A) * sin(B) * sin(C) + k * cos(A) * sin(B) * sin(C) -
           i * cos(B) * sin(C);
}

float calculateZ(int i, int j, int k) {
    return k * cos(A) * cos(B) - j * sin(A) * cos(B) + i * sin(B);
}

/* Project one surface point of the cube onto the screen and write it
 * into the character buffer if it is nearer than what is already there. */
void calculateForSurface(float cubeX, float cubeY, float cubeZ, int ch) {
    x = calculateX(cubeX, cubeY, cubeZ);
    y = calculateY(cubeX, cubeY, cubeZ);
    z = calculateZ(cubeX, cubeY, cubeZ) + distanceFromCam;

    ooz = 1 / z;

    xp = (int)(width / 2 + horizontalOffset + K1 * ooz * x * 2);
    yp = (int)(height / 2 + K1 * ooz * y);

    idx = xp + yp * width;
    if (idx >= 0 && idx < width * height) {
        if (ooz > zBuffer[idx]) {
            zBuffer[idx] = ooz;
            buffer[idx] = ch;
        }
    }
}

int main(void) {
    printf("\x1b[2J");          /* clear screen */
    while (1) {
        memset(buffer, backgroundASCIICode, width * height);
        memset(zBuffer, 0, width * height * sizeof(float));

        /* First cube: larger, left of centre. */
        cubeWidth = 20;
        horizontalOffset = -2 * cubeWidth;
        for (float cubeX = -cubeWidth; cubeX < cubeWidth; cubeX += incrementSpeed) {
            for (float cubeY = -cubeWidth; cubeY < cubeWidth; cubeY += incrementSpeed) {
                calculateForSurface(cubeX, cubeY, -cubeWidth, '@');
                calculateForSurface(cubeWidth, cubeY, cubeX, '$');
                calculateForSurface(-cubeWidth, cubeY, -cubeX, '~');
                calculateForSurface(-cubeX, cubeY, cubeWidth, '#');
                calculateForSurface(cubeX, -cubeWidth, -cubeY, ';');
                calculateForSurface(cubeX, cubeWidth, cubeY, '+');
            }
        }

        /* Second cube: medium, centre. */
        cubeWidth = 10;
        horizontalOffset = 1 * cubeWidth;
        for (float cubeX = -cubeWidth; cubeX < cubeWidth; cubeX += incrementSpeed) {
            for (float cubeY = -cubeWidth; cubeY < cubeWidth; cubeY += incrementSpeed) {
                calculateForSurface(cubeX, cubeY, -cubeWidth, '@');
                calculateForSurface(cubeWidth, cubeY, cubeX, '$');
                calculateForSurface(-cubeWidth, cubeY, -cubeX, '~');
                calculateForSurface(-cubeX, cubeY, cubeWidth, '#');
                calculateForSurface(cubeX, -cubeWidth, -cubeY, ';');
                calculateForSurface(cubeX, cubeWidth, cubeY, '+');
            }
        }

        /* Third cube: small, right. */
        cubeWidth = 5;
        horizontalOffset = 8 * cubeWidth;
        for (float cubeX = -cubeWidth; cubeX < cubeWidth; cubeX += incrementSpeed) {
            for (float cubeY = -cubeWidth; cubeY < cubeWidth; cubeY += incrementSpeed) {
                calculateForSurface(cubeX, cubeY, -cubeWidth, '@');
                calculateForSurface(cubeWidth, cubeY, cubeX, '$');
                calculateForSurface(-cubeWidth, cubeY, -cubeX, '~');
                calculateForSurface(-cubeX, cubeY, cubeWidth, '#');
                calculateForSurface(cubeX, -cubeWidth, -cubeY, ';');
                calculateForSurface(cubeX, cubeWidth, cubeY, '+');
            }
        }

        /* Draw the frame. */
        printf("\x1b[H");       /* cursor home */
        for (int k = 0; k < width * height; k++) {
            putchar(k % width ? buffer[k] : '\n');
        }
        fflush(stdout);

        A += 0.05;
        B += 0.05;
        C += 0.01;
        usleep(8000 * 2);
    }
    return 0;
}
