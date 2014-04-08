/*
 * gcc -O3 -Wall -o multiple_ones_c multiple_ones_c.c
 * Given any integer 0 <= n <= 10000 not [evenly] divisible by 2 or 5,
 * find the number of digits in the smallest [integer] multiple of n
 * that is a number which in decimal notation is a sequence of 1's.
 *
 * -9999 -> 0m0.067s
 * -99999 -> 0m5.135s
 * -999999 -> 7m22.756s
 */

#include <stdio.h>
#include <stdlib.h>

int findNdigits(int n) {
    /* Finds the number of digits in the smallest integer multiple of n.
     * 111 mod n = ((100 mod n) + (10 mod n) + (1 mod n)) mod n
     * 100 mod n = (10 * (10 mod n)) mod n
     */
    int digmodulus, ndigits, modulus;

    digmodulus = 1;
    ndigits = 1;
    modulus = 1 % n;

    while (modulus != 0) {
      digmodulus = (digmodulus * 10) % n;
      modulus = (modulus + digmodulus) % n;
      ndigits++;
    }

    return(ndigits);
}

int main(int argc, char * argv[]) {
    int n, i, maxdigits, maxdigitsi, ndigits;

    if (argc != 2) {
        printf("ERROR: invalid or missing argument\n");
        printf("USAGE: %s n\n", argv[0]);
        return(1);
    }
    n = atoi(argv[1]);
    if (n % 2 == 0 || n % 5 == 0) {
        printf("ERROR: Invalid argument.  n must not be divisible by 2 or 5.\n");
        return(1);
    }

    if (n < 0) {
        maxdigits = 0;
        maxdigitsi = 0;
        for (i = 1; i < -n; i++) {
            if (i % 2 != 0 && i % 5 != 0) {
                ndigits = findNdigits(i);
                printf("%6d: %d\n", i, ndigits);
                if (maxdigits < ndigits) {
                    maxdigits = ndigits;
                    maxdigitsi = i;
                }
            }
        }
        printf("max ndigits = %d for n = %d\n", maxdigits, maxdigitsi);
    } else {
        ndigits = findNdigits(n);
        printf("%6d: %d\n", n, ndigits);
    }

    return(0);
}
