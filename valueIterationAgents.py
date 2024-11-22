#_________________________________________________________________________________________________________________________
#               Submitted by:
#   Name: Prashanna Raj pandit
#   SID:800817018
#
#   Message to Grader: My code runs perfectly, achieving 25/25 in the autograder. 
#   It takes a maximum of 10 seconds to execute on my M1 silicon processor. Please feel free to contact me if you encounter any issues.
#_________________________________________________________________________________________________________________________




# valueIterationAgents.py
# -----------------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


import mdp, util
import sys
from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0
        
        
        "*** YOUR CODE HERE ***"
        
        """
        The ValueIterationAgent class performs value iteration,
        a dynamic programming technique to compute the optimal value
        function and optimal policy for an MDP. It iteratively updates the estimated 
        values of states until they converge, then uses these values to determine the best actions for any given state.

        """
        # Performing value iteration using a while loop

        iteration = 0                                               # Initialize iteration count
        while iteration < self.iterations:                          # Run until the number of iterations is reached
            next_values = util.Counter()                            # Temporary counter for updated values

            for state in mdp.getStates():                           # Iterating through all states
                if self.mdp.isTerminal(state):                      # Skipping terminal states
                    next_values[state] = 0
                    continue

                                                                    # Compute the maximum Q-value over all actions
                max_q_value = float('-inf')                         # initializing to -ve infinity
                for action in mdp.getPossibleActions(state):        # Loop through possible actions
                    q_value = self.computeQValueFromValues(state, action)
                    max_q_value = max(max_q_value, q_value)

                next_values[state] = max_q_value                    # Update the value of the state in the temporary counter

            self.values = next_values                               # Update the stored values with the new computed values
            iteration += 1                                          # going to next iteration by incrementing counbter by 1

    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]

    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        "*** YOUR CODE HERE ***"

        q_value = 0                                                                         # Initializing the Q-value
        for next_state, probability in self.mdp.getTransitionStatesAndProbs(state, action): # getting next state S' and transition probability from state S taking action a.
            reward = self.mdp.getReward(state, action, next_state)                          # Reward for transitioning to the next state
            q_value += probability * (reward + self.discount * self.values[next_state])     # Bellman equation: Add contribution of this transition
        return q_value

    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        "*** YOUR CODE HERE ***"
        if self.mdp.isTerminal(state):                                          # Checks if the given state is a terminal state.
            return None                                                         #Terminal states have no valid actions, so the function immediately returns None.

        best_action = None                                                      #This variable will store the action with the highest Q-value.
        max_q_value = float('-inf')                                             # racks the highest Q-value found so far. It is initialized to negative infinity because any valid Q-value will be greater than this.

        actions = self.mdp.getPossibleActions(state)                            # Get possible actions for the state
        index = 0                                                               

        while index < len(actions):                                             # Iterate through all actions
            action = actions[index]
            q_value = self.computeQValueFromValues(state, action)               # The Q-value for the current action, computed using the computeQValueFromValues method.

            if q_value > max_q_value:                                           # Compares the current action's Q-value (q_value) with the highest Q-value found so far (max_q_value).
                                                                                # If q_value is higher: Updates max_q_value and sets best_action to the current action.
                max_q_value = q_value
                best_action = action

            index += 1                                                          # Increment the index for the next action

        return best_action

    def getPolicy(self, state):
        """
          Return the best action to take in a state (the policy).
        """
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        """
          Return the Q-value of a state-action pair.
        """
        return self.computeQValueFromValues(state, action)


