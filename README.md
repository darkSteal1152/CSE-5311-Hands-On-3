# CSE-5311-Hands-On-3
CSE 5311 Assignment 3

1. The runtime of the algorithm is mathematically shown in the python file function_runtime.py
2. The function is timed and plotted in the python file function_timer.py with the corresponding plot being in Figure 5. Additionally, the estimated equation is given below.

Estimated Function Equation:
2.422e-08 x^2 + 1.409e-05 x - 0.002331

3. O(n^2) provides the upper bound, while Omega(n^2) is the lower bound. Theta(n^2) represents the estimated function, as it is between the upper and lower bounds.
4. The approximate location of n_0 is around n = 800. After the point n_0 = 800, the curve of the observed values mimics more closely with the estimated graph, and continues as a quadratic equation. This is due to the speed of my processor computing lower values of n in almost no time, which staggers the first few input sizes at 0, while the curve, being quadratic, is calculating negative values, The two curves straighten more out after the point n_0 = 800. The plots can be seen as the zoom-in images of Figure 5, as Figure 6, Figure 7, and Figure 8.
5. The timing of the modified function is shown in the python file modified_function_timer.py, along with the corresponding plot in Figure 9. Additionally, the estimated equation is given below

Estimated Modified Function Equation:
4.007e-08 x^2 + 5.27e-06 x - 0.00208

6. While the timer codes do show a more lengthy time difference between the original and modified functions, the actual O notation of the functions or asymptotic complexity remains O(n^2). However, the calculations done within the loop are lenghtier, given two computations are done in the nested loop now, as opposed to one.
7. Merge sort is implemented and shown in the python file merge_sort.py. The output console of the code is shown below.

Output of merge_sort.py
[5, 2, 4, 7, 1, 3, 2, 6]
[1, 2, 2, 3, 4, 5, 6, 7]
Merge Sort returns a sorted array correctly
