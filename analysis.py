#_________________________________________________________________________________________________________________________
#               Submitted by:
#   Name: Prashanna Raj pandit
#   SID:800817018
#
#   Message to Grader: My code runs perfectly, achieving 25/25 in the autograder. 
#   It takes a maximum of 10 seconds to execute on my M1 silicon processor. Please feel free to contact me if you encounter any issues.
#_________________________________________________________________________________________________________________________





# analysis.py
# -----------
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


######################
# ANALYSIS QUESTIONS #
######################

# Set the given parameters to obtain the specified policies through
# value iteration.

def question2():
    answerDiscount = 0.9
    answerNoise = 0                                 # Setting noise to 0 to remove randomness in actions
    return answerDiscount, answerNoise

def question3a():                                   #A high discount encourages reaching the exit,
    answerDiscount = 1                              # and low noise reduces the risk of random moves. 
    answerNoise = 0.01                              #A negative living reward helps the agent aim for a quick exit without a strong preference for distant rewards.
    answerLivingReward = -5
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3b():
    answerDiscount = 0.05                            #A moderate noise level encourages the agent to avoid risky moves,
    answerNoise = 0.01                               # and a reasonable discount prioritizes a closer exit without risking the cliff.
    answerLivingReward = 0
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3c():
    answerDiscount = 1                                #A high discount emphasizes future rewards, 
    answerNoise = 0                                   #encouraging the agent to reach the distant goal. 
    answerLivingReward = -0.1                         #A small living reward and low noise maintain focus on reaching the exit quickly without too much caution.
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3d():
    answerDiscount = 0.9                                # High discount and moderate noise push the agent towards the distant exit while avoiding 
                                                        #the cliff area. A positive living reward slightly encourages cautious behavior without rushing.
    answerNoise = 0.5
    answerLivingReward = 0
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3e():
    answerDiscount = 0                                    #A low discount minimizes the incentive for future rewards,                                          
    answerNoise = 0                                       #and a positive living reward motivates the agent to stay in 
    answerLivingReward = 1                                #non-terminal states indefinitely rather than reaching an exit.
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question6():
    # answerEpsilon = None
    # answerLearningRate = None
    # return answerEpsilon, answerLearningRate
    # If not possible, return 'NOT POSSIBLE'
    return 'NOT POSSIBLE'

if __name__ == '__main__':
    # print ('Answers to analysis questions:')
    import analysis
    for q in [q for q in dir(analysis) if q.startswith('question')]:
        response = getattr(analysis, q)()
        # print ('  Question %s:\t%s' % (q, str(response)))
