/**
 * CSCI-665: Foundations of Algorithms
 * Homework 3 - Problem 4
 *
 * This program is to find the best value we can get when we have some
 * certain items with some items and costs and 2 backpacks with some
 * items. We have to find the maximum value we can get using dynamic
 * programming.
 */

import java.util.Scanner;

public class DoubleKnapsack {

    private int number_of_weights;
    private int weight_1, weight_2 = 0;
    private int[][] items;

    /**
     * Main function to take input and find the best weight for the
     * 2 backpack knapsack problem
     */
    public static void main(String[] args) {

        // create an object of DoubleKnapsack
        DoubleKnapsack knapsack = new DoubleKnapsack();

        // take all the user input and initialize values
        knapsack.takeUserInput();

        // solve the problem using dynamic programming
        int weight = knapsack.solveKnapsack();

        // display the result
        System.out.println(weight);
    }

    /**
     * Function to get input from user and initialize all the
     * necessary parameters like the items array
     */
    private void takeUserInput() {

        // initialize the scanner to take input through command
        // line parameters
        Scanner sc = new Scanner(System.in);

        // read first line and split it by spaces
        String[] input_line = sc.nextLine().split(" ");

        // save the values of the number of items and the weight
        // of the 2 backpacks
        number_of_weights = Integer.parseInt(input_line[0]);
        weight_1 = Integer.parseInt(input_line[1]);
        weight_2 = Integer.parseInt(input_line[2]);

        // initialize the items array
        items = new int[number_of_weights][2];

        // take the data from the command line using the scanner and put
        // into the items array, which has weight and cost.
        for (int i = 0; i < number_of_weights; i++) {
            input_line = sc.nextLine().split(" ");
            items[i][0] = Integer.parseInt(input_line[0]);
            items[i][1] = Integer.parseInt(input_line[1]);
        }
    }

    /**
     * Use dynamic programming to solve the double knapsack problem
     *
     * @return the maximum cost we can carry using the 2 backpacks
     */
    private int solveKnapsack() {

        // initialize the dynamic programming array
        int[][][] S = new int[number_of_weights + 1][weight_1 + 1][weight_2 + 1];

        // base case - when there is are all items and only no backpack,
        // the max value is 0
        for (int i = 0; i < number_of_weights; i++) {
            S[i][0][0] = 0;
        }

        // using the base cases we start filling gup our dp array

        for (int j = 1; j < number_of_weights + 1; j++) {
            for (int v1 = 0; v1 < weight_1 + 1; v1++) {
                for (int v2 = 0; v2 < weight_2 + 1; v2++) {
                    // weight and cost of current item in consideration
                    int Wj = items[j - 1][0];
                    int Cj = items[j - 1][1];

                    // prefill the current value as the one before considering
                    // this weight
                    S[j][v1][v2] = S[j - 1][v1][v2];

                    // initialize value1, value2 to 0 - used to check adding
                    // item to which backpack gives us maximum value
                    int value1 = 0, value2 = 0;

                    // if the item can be added to both the backpacks
                    if (Wj <= v1 && Wj <= v2) {

                        // find the value when it is added to backpack 1 and
                        // backpack based on the previously filled dp array, ie
                        // which gives maximum value adding it to not
                        // including it
                        value1 = maxOf(S[j - 1][v1 - Wj][v2]
                                + Cj, S[j][v1][v2]);
                        value2 = maxOf(S[j - 1][v1][v2 - Wj]
                                + Cj, S[j][v1][v2]);

                        // use the value which is maximum of two values
                        S[j][v1][v2] = maxOf(value1, value2);
                    }
                    // if the item can only be added to 1st backpack
                    else if (Wj <= v1) {
                        // find which gives the best value, adding the weight
                        // to the backpack or not including it
                        S[j][v1][v2] = maxOf(S[j - 1][v1 - Wj][v2]
                                + Cj, S[j][v1][v2]);
                    } else if (Wj <= v2) {
                        S[j][v1][v2] = maxOf(S[j - 1][v1][v2 - Wj]
                                + Cj, S[j][v1][v2]);
                    }
                }
            }
        }
        // return the result back , which represents the maximum value we
        // can get by using the given items and having 2 backpacks
        // with the certain capacities
        return S[number_of_weights][weight_1][weight_2];
    }

    /**
     * Function to find the maximum of the 2 input values
     *
     * @param value1 - one value to find max
     * @param value2 - another value to find the max
     * @return - the maximum of the two input values
     */
    private static int maxOf(int value1, int value2) {
        //if value 1 is larger return it else return value 2
        if (value1 > value2)
            return value1;
        else
            return value2;
    }
}
