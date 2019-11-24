import networkx as nx
import pickle

"""
This is used to calculate the safety game, for safety game, please check some reference. We are computing for P2's safety game
You should provide:
    a graph: grf, which you can get from Translate file
    a set of state: W, which you want to get the safety set
    actionSpace of agent1: actSpaceP1
    actionSpace of agent2: actSpaceP2
    Call the function safetyGameSolver(grf, W, actSpaceP1, actSpaceP2)
"""
def safetyGameSolver(grf, W, actSpaceP1, actSpaceP2):
    W_temp = getPreSafety(grf, W, actSpaceP1, actSpaceP2)
    W_temp = W.intersection(W_temp)
    index = 1
    while (W!=W_temp):
        print(str(index) + "st iteration")
        W = W_temp
        W_temp = getPreSafety(grf, W, actSpaceP1, actSpaceP2)
        W_temp = W.intersection(W_temp)
        index += 1
    return W

def getPreSafety(grf, W, actSpaceP1, actSpaceP2):
    W_temp = set()
    for state in W:
        endStateDict =getDictEndstate(grf, state)
        for actionP2 in actSpaceP2:
            flag = checkInWSafety(W, actionP2, actSpaceP1, endStateDict, state)
            if flag == True:
                #file.write("node is: " + str(node) + "  the action can remain in set is: " + action_e.__name__ + "\n")
                W_temp.add(state)
                break
    print ("length of W_temp is:", len(W_temp))
    return W_temp

def checkInWSafety(W, actionP2, actSpaceP1, endStateDict, state):
    for actionP1 in actSpaceP1:
        for key, value in endStateDict[state][(actionP1, actionP2)].items():
            if value > 1e-5 and key not in W:
                return False
    return True


def getDictEndstate(grf, state):
    stateDict = {}
    stateDict[state] = {}
    for endState in grf[state]:
        for label in grf[state][endState]:
            action = grf[state][endState][label]['action']
            pro = grf[state][endState][label]['probability']
            if action not in stateDict[state]:
                stateDict[state][action] = {}
            stateDict[state][action][endState] = pro
    return stateDict
