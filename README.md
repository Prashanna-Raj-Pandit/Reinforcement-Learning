# CS 590 - Advanced AI - Project 3: Reinforcement Learning

**Author: Prashanna Raj Pandit**
<img src="output.gif"></img>
### Overview
In this project, you will implement **Value Iteration** and **Q-Learning** agents, and apply them to complete the following tasks:

1. **Value Iteration** — Implement an offline planner using the batch version of Value Iteration.  
2. **Bridge Crossing Analysis** — Adjust parameters to encourage crossing a risky bridge.  
3. **Policies** — Adjust discount, noise, and living reward to produce specific policies.  
4. **Q-Learning** — Implement core Q-learning methods.  
5. **Epsilon-Greedy** — Implement exploration in Q-learning.  
6. **Bridge Crossing Revisited** — Analyze parameter effects on learning success.  
7. **Q-Learning & Pacman** — Train and test Pacman with your Q-learning agent.  
8. **Approximate Q-Learning** — Implement function approximation for scalable learning.

---

## Requiment

``
Python 2.7.18
``

## ▶️ Running the Code

```bash
python autograder.py
```
```
Question q1
===========

*** PASS: test_cases/q1/1-tinygrid.test
*** PASS: test_cases/q1/2-tinygrid-noisy.test
*** PASS: test_cases/q1/3-bridge.test
*** PASS: test_cases/q1/4-discountgrid.test

### Question q1: 6/6 ###


Question q2
===========

*** PASS: test_cases/q2/1-bridge-grid.test

### Question q2: 1/1 ###


Question q3
===========

*** PASS: test_cases/q3/1-question-3.1.test
*** PASS: test_cases/q3/2-question-3.2.test
*** PASS: test_cases/q3/3-question-3.3.test
*** PASS: test_cases/q3/4-question-3.4.test
*** PASS: test_cases/q3/5-question-3.5.test

### Question q3: 5/5 ###


Question q4
===========

*** PASS: test_cases/q4/1-tinygrid.test
*** PASS: test_cases/q4/2-tinygrid-noisy.test
*** PASS: test_cases/q4/3-bridge.test
*** PASS: test_cases/q4/4-discountgrid.test

### Question q4: 5/5 ###


Question q5
===========

*** PASS: test_cases/q5/1-tinygrid.test
*** PASS: test_cases/q5/2-tinygrid-noisy.test
*** PASS: test_cases/q5/3-bridge.test
*** PASS: test_cases/q5/4-discountgrid.test

### Question q5: 3/3 ###


Question q6
===========

*** PASS: test_cases/q6/grade-agent.test

### Question q6: 1/1 ###


Question q7
===========

Beginning 2000 episodes of Training
Reinforcement Learning Status:
        Completed 100 out of 2000 training episodes
        Average Rewards over all training: -510.46
        Average Rewards for last 100 episodes: -510.46
        Episode took 0.48 seconds
Reinforcement Learning Status:
        Completed 200 out of 2000 training episodes
        Average Rewards over all training: -511.25
        Average Rewards for last 100 episodes: -512.03
        Episode took 0.67 seconds
Reinforcement Learning Status:
        Completed 300 out of 2000 training episodes
        Average Rewards over all training: -485.30
        Average Rewards for last 100 episodes: -433.41
        Episode took 0.82 seconds
Reinforcement Learning Status:
        Completed 400 out of 2000 training episodes
        Average Rewards over all training: -442.13
        Average Rewards for last 100 episodes: -312.64
        Episode took 0.98 seconds
Reinforcement Learning Status:
        Completed 500 out of 2000 training episodes
        Average Rewards over all training: -422.14
        Average Rewards for last 100 episodes: -342.17
        Episode took 1.33 seconds
Reinforcement Learning Status:
        Completed 600 out of 2000 training episodes
        Average Rewards over all training: -403.44
        Average Rewards for last 100 episodes: -309.91
        Episode took 1.06 seconds
Reinforcement Learning Status:
        Completed 700 out of 2000 training episodes
        Average Rewards over all training: -392.92
        Average Rewards for last 100 episodes: -329.81
        Episode took 1.06 seconds
Reinforcement Learning Status:
        Completed 800 out of 2000 training episodes
        Average Rewards over all training: -360.10
        Average Rewards for last 100 episodes: -130.35
        Episode took 1.35 seconds
Reinforcement Learning Status:
        Completed 900 out of 2000 training episodes
        Average Rewards over all training: -332.11
        Average Rewards for last 100 episodes: -108.17
        Episode took 2.04 seconds
Reinforcement Learning Status:
        Completed 1000 out of 2000 training episodes
        Average Rewards over all training: -307.57
        Average Rewards for last 100 episodes: -86.77
        Episode took 0.98 seconds
Reinforcement Learning Status:
        Completed 1100 out of 2000 training episodes
        Average Rewards over all training: -277.33
        Average Rewards for last 100 episodes: 25.13
        Episode took 0.88 seconds
Reinforcement Learning Status:
        Completed 1200 out of 2000 training episodes
        Average Rewards over all training: -244.54
        Average Rewards for last 100 episodes: 116.14
        Episode took 0.91 seconds
Reinforcement Learning Status:
        Completed 1300 out of 2000 training episodes
        Average Rewards over all training: -212.11
        Average Rewards for last 100 episodes: 177.08
        Episode took 0.97 seconds
Reinforcement Learning Status:
        Completed 1400 out of 2000 training episodes
        Average Rewards over all training: -177.86
        Average Rewards for last 100 episodes: 267.37
        Episode took 1.06 seconds
Reinforcement Learning Status:
        Completed 1500 out of 2000 training episodes
        Average Rewards over all training: -147.48
        Average Rewards for last 100 episodes: 277.78
        Episode took 0.90 seconds
Reinforcement Learning Status:
        Completed 1600 out of 2000 training episodes
        Average Rewards over all training: -124.69
        Average Rewards for last 100 episodes: 217.24
        Episode took 1.08 seconds
Reinforcement Learning Status:
        Completed 1700 out of 2000 training episodes
        Average Rewards over all training: -109.32
        Average Rewards for last 100 episodes: 136.62
        Episode took 1.04 seconds
Reinforcement Learning Status:
        Completed 1800 out of 2000 training episodes
        Average Rewards over all training: -96.27
        Average Rewards for last 100 episodes: 125.43
        Episode took 1.26 seconds
Reinforcement Learning Status:
        Completed 1900 out of 2000 training episodes
        Average Rewards over all training: -84.06
        Average Rewards for last 100 episodes: 135.79
        Episode took 0.92 seconds
Reinforcement Learning Status:
        Completed 2000 out of 2000 training episodes
        Average Rewards over all training: -63.01
        Average Rewards for last 100 episodes: 336.87
        Episode took 0.96 seconds
Training Done (turning off epsilon and alpha)
---------------------------------------------
Pacman emerges victorious! Score: 503
Pacman emerges victorious! Score: 499
Pacman emerges victorious! Score: 503
Pacman emerges victorious! Score: 499
Pacman emerges victorious! Score: 503
Pacman emerges victorious! Score: 499
Pacman emerges victorious! Score: 495
Pacman emerges victorious! Score: 503
Pacman emerges victorious! Score: 503
Pacman emerges victorious! Score: 499
Pacman emerges victorious! Score: 499
Pacman emerges victorious! Score: 495
Pacman emerges victorious! Score: 503
Pacman emerges victorious! Score: 503
Pacman emerges victorious! Score: 499
Pacman emerges victorious! Score: 495
Pacman emerges victorious! Score: 503
Pacman emerges victorious! Score: 495
Pacman emerges victorious! Score: 495
Pacman emerges victorious! Score: 495
Pacman emerges victorious! Score: 499
Pacman emerges victorious! Score: 503
Pacman emerges victorious! Score: 495
Pacman emerges victorious! Score: 499
Pacman emerges victorious! Score: 499
Pacman emerges victorious! Score: 503
Pacman emerges victorious! Score: 503
Pacman emerges victorious! Score: 495
Pacman emerges victorious! Score: 503
Pacman emerges victorious! Score: 503
Pacman emerges victorious! Score: 503
Pacman emerges victorious! Score: 503
Pacman emerges victorious! Score: 503
Pacman emerges victorious! Score: 503
Pacman emerges victorious! Score: 503
Pacman emerges victorious! Score: 503
Pacman emerges victorious! Score: 503
Pacman emerges victorious! Score: 503
Pacman emerges victorious! Score: 495
Pacman emerges victorious! Score: 495
Pacman emerges victorious! Score: 503
Pacman emerges victorious! Score: 503
Pacman emerges victorious! Score: 503
Pacman emerges victorious! Score: 503
Pacman emerges victorious! Score: 503
Pacman emerges victorious! Score: 499
Pacman emerges victorious! Score: 503
Pacman emerges victorious! Score: 499
Pacman emerges victorious! Score: 503
Pacman emerges victorious! Score: 495
Pacman emerges victorious! Score: 495
Pacman emerges victorious! Score: 503
Pacman emerges victorious! Score: 503
Pacman emerges victorious! Score: 503
Pacman emerges victorious! Score: 499
Pacman emerges victorious! Score: 503
Pacman emerges victorious! Score: 495
Pacman emerges victorious! Score: 499
Pacman emerges victorious! Score: 503
Pacman emerges victorious! Score: 503
Pacman emerges victorious! Score: 503
Pacman emerges victorious! Score: 503
Pacman emerges victorious! Score: 503
Pacman emerges victorious! Score: 503
Pacman emerges victorious! Score: 503
Pacman emerges victorious! Score: 495
Pacman emerges victorious! Score: 503
Pacman emerges victorious! Score: 495
Pacman emerges victorious! Score: 503
Pacman emerges victorious! Score: 503
Pacman emerges victorious! Score: 503
Pacman emerges victorious! Score: 503
Pacman emerges victorious! Score: 499
Pacman emerges victorious! Score: 503
Pacman emerges victorious! Score: 499
Pacman emerges victorious! Score: 503
Pacman emerges victorious! Score: 495
Pacman emerges victorious! Score: 503
Pacman emerges victorious! Score: 495
Pacman emerges victorious! Score: 495
Pacman emerges victorious! Score: 503
Pacman emerges victorious! Score: 495
Pacman emerges victorious! Score: 503
Pacman emerges victorious! Score: 495
Pacman emerges victorious! Score: 503
Pacman emerges victorious! Score: 495
Pacman emerges victorious! Score: 499
Pacman emerges victorious! Score: 495
Pacman emerges victorious! Score: 503
Pacman emerges victorious! Score: 499
Pacman emerges victorious! Score: 503
Pacman emerges victorious! Score: 495
Pacman emerges victorious! Score: 503
Pacman emerges victorious! Score: 503
Pacman emerges victorious! Score: 503
Pacman emerges victorious! Score: 503
Pacman emerges victorious! Score: 503
Pacman emerges victorious! Score: 503
Pacman emerges victorious! Score: 503
Pacman emerges victorious! Score: 503
Reinforcement Learning Status:
        Completed 100 test episodes
        Average Rewards over testing: 500.48
        Average Rewards for last 100 episodes: 500.48
        Episode took 0.98 seconds
Average Score: 500.48
Scores:        503.0, 499.0, 503.0, 499.0, 503.0, 499.0, 495.0, 503.0, 503.0, 499.0, 499.0, 495.0, 503.0, 503.0, 499.0, 495.0, 503.0, 495.0, 495.0, 495.0, 499.0, 503.0, 495.0, 499.0, 499.0, 503.0, 503.0, 495.0, 503.0, 503.0, 503.0, 503.0, 503.0, 503.0, 503.0, 503.0, 503.0, 503.0, 495.0, 495.0, 503.0, 503.0, 503.0, 503.0, 503.0, 499.0, 503.0, 499.0, 503.0, 495.0, 495.0, 503.0, 503.0, 503.0, 499.0, 503.0, 495.0, 499.0, 503.0, 503.0, 503.0, 503.0, 503.0, 503.0, 503.0, 495.0, 503.0, 495.0, 503.0, 503.0, 503.0, 503.0, 499.0, 503.0, 499.0, 503.0, 495.0, 503.0, 495.0, 495.0, 503.0, 495.0, 503.0, 495.0, 503.0, 495.0, 499.0, 495.0, 503.0, 499.0, 503.0, 495.0, 503.0, 503.0, 503.0, 503.0, 503.0, 503.0, 503.0, 503.0
Win Rate:      100/100 (1.00)
Record:        Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win, Win
*** PASS: test_cases/q7/grade-agent.test (1 of 1 points)
***     Grading agent using command:  python pacman.py -p PacmanQAgent -x 2000 -n 2100 -l smallGrid -q -f --fixRandomSeed
***     100 wins (1 of 1 points)
***         Grading scheme:
***          < 70:  0 points
***         >= 70:  1 points

### Question q7: 1/1 ###


Question q8
===========

*** PASS: test_cases/q8/1-tinygrid.test
*** PASS: test_cases/q8/2-tinygrid-noisy.test
*** PASS: test_cases/q8/3-bridge.test
*** PASS: test_cases/q8/4-discountgrid.test
*** PASS: test_cases/q8/5-coord-extractor.test

### Question q8: 3/3 ###


Finished at 17:51:05

Provisional grades
==================
Question q1: 6/6
Question q2: 1/1
Question q3: 5/5
Question q4: 5/5
Question q5: 3/3
Question q6: 1/1
Question q7: 1/1
Question q8: 3/3
------------------
Total: 25/25
```