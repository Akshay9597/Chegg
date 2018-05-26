#include <stdio.h>
 
// Returns approximate value of e^x 
// using sum of first n terms of Taylor Series
float exponential(float x)
{
    float sum = 1.0f; // initialize sum of series
    float prev = 1.0f, new = 1.0f;
 	while(new-prev > 0.0001) {
    for (int i = n - 1; i > 0; --i )
    	prev = new;
        sum = 1 + x * sum / i;
        new = sum;
    }
 
    return sum;
}
 
// Driver program to test above function
int main()
{
    float x = 1.0f;
    printf("e^x = %f", exponential(x));
    return 0;
}
