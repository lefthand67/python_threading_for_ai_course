#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// A function to simulate some "work" (a CPU-bound calculation)
// The amount of work is variable to upset any rhythm.
void do_work(int iterations);
void* print_numbers(void* arg);
void* print_letters(void* arg);

int main(void)
{
    pthread_t thread1, thread2;

    printf("Main: Starting threads...\n");

    if (pthread_create(&thread1, NULL, print_numbers, (void*)1) != 0) {
        perror("Failed to create thread1");
        return 1;
    }

    if (pthread_create(&thread2, NULL, print_letters, (void*)2) != 0) {
        perror("Failed to create thread2");
        return 1;
    }

    printf("Main: Threads started. Waiting...\n");
    pthread_join(thread1, NULL);
    pthread_join(thread2, NULL);

    printf("Main: Both threads have finished.\n");
}

void do_work(int iterations)
{
    volatile double x = 1.0; // 'volatile' prevents compiler from optimizing the loop away

    for (int i = 0; i < iterations; i++)
        x = x * 1.01;
}

void* print_numbers(void* arg)
{
    int work_base = 1000000;
    srand(time(NULL) ^ ((long)arg + 1)); // Seed RNG uniquely for this thread

    for (int i = 0; i < 5; i++) {
        printf("Number: %d\n", i);
        int iterations = work_base + (rand() % 1000000);
        do_work(iterations);
    }
    return NULL;
}

void* print_letters(void* arg)
{
    // Let's use a variable amount of work for each step
    int work_base = 1000000;
    srand(time(NULL) ^ (long)arg); // Different seed for this thread

    for (char c = 'a'; c <= 'e'; c++) {
        printf("Letter: %c\n", c);
        // Do a random amount of work between steps
        int iterations = work_base + (rand() % 1000000);
        do_work(iterations);
    }
    return NULL;
}
