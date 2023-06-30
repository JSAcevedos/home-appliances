# home-appliances

You are the sales manager of a home appliances distributor. Finished products slide down a conveyor belt to be shipped as follows. As they arrive, they must be organized into groups, one group for each store. The products destined for the same store must be stacked in the order they arrive for later distribution.

The appliances must be distributed in the following order: first, stack the products for store 1 until the required quantity for that store is reached; then, stack the appliances for store 2 until the required quantity for that store is reached; and so on, continuing the process of organizing products store by store until all the orders are fulfilled.

You need to develop a program that reads from the console the order in which the different appliances arrive and the number of appliances that need to be sent to each store. Then, organize the groups of appliances for each store and print how each stack is arranged.

**Input**

The first line should contain an integer C, which represents the number of "cases" to be processed in a single execution. In other words, it is the number of times you, as the manager, need to distribute your production among a given number of stores. (Note: Each case works separately, and if there are remaining appliances in an iteration, they are discarded or donated to charity.)

The next line should contain an integer N, which represents the number of appliances to be distributed among the stores.

The following line should read N strings, representing the names of all the products that need to be processed. The first string in this input line represents the product located at the front of the production line (and thus should be the first to be processed), and the last string represents the product at the back of the conveyor belt (and thus should be the last to be processed). Use a queue for implementation.

The next line should read an integer T, indicating the number of stores to which the products should be sent.

Then, there should be a line with T integers (T1, T2, ..., Tx...) representing the number of products to be sent to each of the T stores, separated by a space as shown: T1 is the number of products to be sent to store 1, T2 is the number of products to be sent to store 2, and so on.

Very important: In the case that a stack of products for a particular store is empty, it should be printed as "[]" (without the quotation marks).

Constraints:

1 <= C <= 10^3

1 <= N <= 10^6

1 <= T <= 10^6

1 <= Ti <= 10^6


**Output**

The output should consist of L lines as follows:

The first line, L1, contains the elements of the stack of products to be sent to store 1.

The second line, L2, contains the elements of the stack of products to be sent to store 2.

The i-th line, Li, contains the elements of the stack of products to be sent to the i-th store.
