# Solving-Markov-Chain-Stable-State-Probability

When Markov Chain path probabilities are in the form a non-negative sqaure matrix. 
The probability of reaching a stable state(through a feedback or not) could found.

The attached images can contain the examples of simple markov chain structures.

The inputs for this python script were in a nxn matrix (LIST - in python terms) format.
- State - 0 is expected to be be parent or initial state.
Child states with no further childs or paths possible further state transitions are known as the stable states.

#The probability of reaching a stable state from state - 0 is found using this code.

The path traversed to a stable state may or may not contain a loop or feedback.

- The concepts Probabilities and Stochastic processes were used.
- If no loop present. The probabilites of reaching stable state are independent and can be multiplied.
- If there is a loop. Then geometric progression concepts were used to determine the probability of reaching the stable state. 


#The inputs can be given in this way.
m1 = [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]

m2 = [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

m3 = [[0, 2, 1, 0, 0, 0], [0, 0, 0, 3, 4, 0], [0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]

m4 = [[0, 2, 1, 0, 0], [1, 0, 0, 2, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

m5 = [[0, 1, 0, 0, 0, 2], [4, 0, 0, 3, 0, 0], [0, 0, 0, 0, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]

Loops are present in m1, m3, m4 and m5

No loop in m2.



