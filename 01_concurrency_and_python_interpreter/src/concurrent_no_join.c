#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h> // for sleep()

// A simple function that will be run in a thread.
// It takes a void* argument and returns a void*.
// This is the required signature for a thread function.
void* print_numbers(void* arg);
void* print_letters(void* arg);

int main(void)
{
    pthread_t thread1, thread2; // These are handles for our threads, like file descriptors.

    printf("Main: Starting threads...\n");

    // Create the first thread. It will run the print_numbers function.
    if (pthread_create(&thread1, NULL, print_numbers, NULL) != 0) {
        perror("Failed to create thread1");
        return 1;
    }

    // Create the second thread. It will run the print_letters function.
    if (pthread_create(&thread2, NULL, print_letters, NULL) != 0) {
        perror("Failed to create thread2");
        return 1;
    }

    printf("Main: Threads started. Waiting for them to finish...\n");

    // pthread_join is crucial. It makes the main thread WAIT for the other threads to finish.
    // If we didn't do this, main might exit immediately, killing the child threads.
    // pthread_join(thread1, NULL);
    // pthread_join(thread2, NULL);

    printf("Main: Both threads have finished.\n");
    return 0;
}

void* print_numbers(void* arg)
{
    for (int i = 0; i < 5; i++) {
        printf("Number: %d\n", i);
        sleep(1); // 1 sec
    }
    return NULL;
}
void* print_letters(void* arg)
{
    for (char c = 'a'; c <= 'e'; c++) {
        printf("Letter: %c\n", c);
        sleep(1);
    }
    return NULL;
}
