#_________________________________________________________________________________________________________________________
#               Submitted by:
#   Name: Prashanna Raj pandit
#   SID:800817018
#
#   Message to Grader: My code runs perfectly, achieving 25/25 in the autograder. 
#   It takes a maximum of 10 seconds to execute on my M1 silicon processor. Please feel free to contact me if you encounter any issues.
#_________________________________________________________________________________________________________________________



# qlearningAgents.py
# ------------------
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

from game import *
from learningAgents import ReinforcementAgent
from featureExtractors import *

import random, util, math


class QLearningAgent(ReinforcementAgent):
    """
      Q-Learning Agent

      Functions you should fill in:
        - computeValueFromQValues
        - computeActionFromQValues
        - getQValue
        - getAction
        - update

      Instance variables you have access to
        - self.epsilon (exploration prob)
        - self.alpha (learning rate)
        - self.discount (discount rate)

      Functions you should use
        - self.getLegalActions(state)
          which returns legal actions for a state
    """

    def __init__(self, **args):
        "You can initialize Q-values here..."
        ReinforcementAgent.__init__(self, **args)
        # Initialize Q-values as a Counter for easy default values
        self.q_values = util.Counter()

    def getQValue(self, state, action):
        """
          Returns Q(state,action)
          Should return 0.0 if we have never seen a state
          or the Q node value otherwise
        """
        "*** YOUR CODE HERE ***"
        return self.q_values[(state, action)]                        # Directly return Q-value for (state, action) from q_values with a default of 0.0

    def computeValueFromQValues(self, state):
        """
          Returns max_action Q(state,action)
          where the max is over legal actions.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return a value of 0.0.
        """
        "*** YOUR CODE HERE ***"
        actions = self.getLegalActions(state)                        # Get the list of legal actions for the given state
        if not actions:                                              # Check if there are no legal actions (e.g., terminal state)
            return 0.0                                               # Return 0.0 if no legal actions are available

        
        max_q_value = max(self.getQValue(state, action) for action in actions)     # Calculate max Q-value for all legal actions in the given state 
        return max_q_value                                           # Return the maximum Q-value among all actions

    def computeActionFromQValues(self, state):
        """
          Compute the best action to take in a state.  Note that if there
          are no legal actions, which is the case at the terminal state,
          you should return None.
        """
        "*** YOUR CODE HERE ***"
        actions = self.getLegalActions(state)                       # Get the list of legal actions for the given state
        if not actions:                                             # Check if there are no legal actions (e.g., terminal state)
            return None                                             # Return None if there are no legal actions

                                                                    # Determine the best action based on Q-values
        best_action = max(actions, key=lambda action: self.getQValue(state, action))
        return best_action                                          # Return the action with the highest Q-value

    def getAction(self, state):
        """
          Compute the action to take in the current state.  With
          probability self.epsilon, we should take a random action and
          take the best policy action otherwise.  Note that if there are
          no legal actions, which is the case at the terminal state, you
          should choose None as the action.

          HINT: You might want to use util.flipCoin(prob)
          HINT: To pick randomly from a list, use random.choice(list)
        """
        legal_actions = self.getLegalActions(state)                 # Get the list of legal actions for the given state
        if not legal_actions:                                       # Check if there are no legal actions (e.g., terminal state)
            return None                                             # Return None if no legal actions are available

        "*** YOUR CODE HERE ***"
        if util.flipCoin(self.epsilon):                              # Explore with probability epsilon
            return random.choice(legal_actions)                      # Explore by choosing a random action
        else:
            return self.computeActionFromQValues(state)              # Exploit by choosing the best action based on Q-values

    def update(self, state, action, nextState, reward):
        """
          The parent class calls this to observe a
          state = action => nextState and reward transition.
          You should do your Q-Value update here

          NOTE: You should never call this function,
          it will be called on your behalf
        """
        "*** YOUR CODE HERE ***"
        
        sample = reward + self.discount * self.computeValueFromQValues(nextState)  # Calculate the sample (reward + gamma * max Q-value of next state)
        
        
        self.q_values[(state, action)] = (1 - self.alpha) * self.getQValue(state, action) + self.alpha * sample   # Update Q-value using the learning rate (alpha) and the sample

    def getPolicy(self, state):
        return self.computeActionFromQValues(state)

    def getValue(self, state):
        return self.computeValueFromQValues(state)


class PacmanQAgent(QLearningAgent):
    "Exactly the same as QLearningAgent, but with different default parameters"

    def __init__(self, epsilon=0.05, gamma=0.8, alpha=0.2, numTraining=0, **args):
        """
        These default parameters can be changed from the pacman.py command line.
        For example, to change the exploration rate, try:
            python pacman.py -p PacmanQLearningAgent -a epsilon=0.1

        alpha    - learning rate
        epsilon  - exploration rate
        gamma    - discount factor
        numTraining - number of training episodes, i.e. no learning after these many episodes
        """
        args['epsilon'] = epsilon
        args['gamma'] = gamma
        args['alpha'] = alpha
        args['numTraining'] = numTraining
        self.index = 0  # This is always Pacman
        QLearningAgent.__init__(self, **args)

    def getAction(self, state):
        """
        Simply calls the getAction method of QLearningAgent and then
        informs parent of action for Pacman.  Do not change or remove this
        method.
        """
        action = QLearningAgent.getAction(self, state)
        self.doAction(state, action)
        return action


class ApproximateQAgent(PacmanQAgent):
    """
       ApproximateQLearningAgent

       You should only have to overwrite getQValue
       and update.  All other QLearningAgent functions
       should work as is.
    """

    def __init__(self, extractor='IdentityExtractor', **args):
        self.featExtractor = util.lookup(extractor, globals())()
        PacmanQAgent.__init__(self, **args)
        # Initialize weights as a Counter for easy default values
        self.weights = util.Counter()

    def getWeights(self):
        return self.weights

    def getQValue(self, state, action):
        """
          Should return Q(state,action) = w * featureVector
          where * is the dotProduct operator
        """
        "*** YOUR CODE HERE ***"
                                                                  # Compute Q-value as the dot product of weights and features
        features = self.featExtractor.getFeatures(state, action)  # Extract features for the (state, action) pair
        q_value = sum(self.weights[feature] * value for feature, value in features.items())  # Calculate dot product of weights and feature values
        return q_value                                            # Return the computed Q-value

    def update(self, state, action, nextState, reward):
        """
           Should update your weights based on transition
        """
        "*** YOUR CODE HERE ***"
                                                        
        difference = (reward + self.discount * self.computeValueFromQValues(nextState)) - self.getQValue(state, action) # Calculate the correction term (difference) for updating weights
        
                                                                    # Update weights based on the difference and feature values
        features = self.featExtractor.getFeatures(state, action)    # Extract features for the (state, action) pair
        for feature, value in features.items():                     # Update each weight based on the feature's value
            self.weights[feature] += self.alpha * difference * value  # Apply Q-learning update rule for weights

    def final(self, state):
        "Called at the end of each game."
        # call the super-class final method
        PacmanQAgent.final(self, state)

        # did we finish training?
        if self.episodesSoFar == self.numTraining:
            # you might want to print your weights here for debugging
            "*** YOUR CODE HERE ***"
            # print("Weights after training:", self.weights)
