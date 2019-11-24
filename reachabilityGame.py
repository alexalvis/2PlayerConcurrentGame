import networkx as nx
import pickle
"""
This is used to calculate the reachability game, for reachability game, please check some reference. We are calculating P1's almost-sure winning set
You should provide:
    a graph: grf, which you can get from Translate file
    a set of state: W, which you want to get the safety set
    actionSpace of agent1: actSpaceP1
    actionSpace of agent2: actSpaceP2
    Call the function reachabilityGameSolver(grf, W, actSpaceP1, actSpaceP2), will return the almost-sure winning region of P1: W and action policy: policy
"""

policy = {}
def reachabilityGameSolver(grf, W, actSpaceP1, actSpaceP2):
    W_formal = W
    W_temp = getPreReachability(grf, W, actSpaceP1, actSpaceP2)
    W = W.union(W_temp)
    index = 1
    while (W_formal != W):
        print(str(index) + "st iteration")
        W_formal = W
        W_temp = getPreReachability(grf, W, actSpaceP1, actSpaceP2)
        W = W.union(W_temp)
        index += 1
    return W, policy

def getPreReachability(grf, W, actSpaceP1, actSpaceP2):
    W_temp = set()
    for state in W:
        predecessor = grf.predecessors(state)
        while True:
            try:
                pre = next(predecessor)
                if pre in W:
                    continue
                for actionP1 in actSpaceP1:
                    tempset = set()
                    for actionP2 in actSpaceP2:
                        dst = transfer(grf, pre, (actionP1,actionP2))
                        if dst != None:
                            tempset = tempset.union(dst)
                    if tempset.issubset(W) and len(tempset) != 0:
                        #file.write("node is: " + str(pre) + "  the action can ensure reaching the set in one step is: " + action_r.__name__ + "\n")
                        if pre not in policy:
                            policy[pre] = actionP1
                        W_temp.add(pre)
                        break
            except StopIteration:
                break;
    print ("W_temp size is", len(W_temp))
    return W_temp

def transfer(grf, state, action):
    tempset = set()
    for dst in grf[state]:
        for label in grf[state][dst]:
            action_temp = grf[state][dst][label]["action"]
            if action == action_temp and grf[state][dst][label]["probability"] > 1e-5:
                tempset.add(dst)
    return tempset
