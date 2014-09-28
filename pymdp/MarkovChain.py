import numpy as np

class MarkovChain(object):
    def __init__(self, P):
        self.P = P
        self.num_states = P.shape[0]
        self.states = np.arange(self.num_states)

    def start(self, p = None):
        self.s = np.random.choice(self.states, p=p)

    def step(self):
        self.s = np.random.choice(self.states, p=self.P[:, self.s])
        return self.s

    def solveValueFn(self, gamma, R):
        return np.linalg.solve( np.eye(self.num_states) - gamma*self.P.T, R)

class MarkovChainWithReward(MarkovChain):
    def __init__(self, P, R):
        super(MarkovChainWithReward, self).__init__(P)
        self.R = R
        
    def solve(self, gamma):
        return np.linalg.solve( np.eye(self.num_states) - gamma*self.P.T, self.R)

class MCSequenceGenerator(object):
    def __init__(self, P, maxlength, **argk):
        self.MC = MarkovChain(P)
        self.maxlength = maxlength

    def getsequence(self):
        sequence = [self.MC.start()]
        return sequence + [self.MC.step() for i in xrange(self.maxlength)]