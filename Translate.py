import pickle
import networkx as nx

"""
This is the file used to transfer the transition system to a netowrkX object
The transition system should in the form of:
P[startState][jointAction][endState] = Probability
This one is based on the concurrent 2 player game version.
"""

def transferObj(filename):
    with open(filename, "rb") as f:
        proDict = pickle.load(f)
    grf = nx.MultiDiGraph()
    actionSpaceP1 = []
    actionSpaceP2 = []
    for state in proDict.keys():
        grf.add_node(state)
    # for startState in proDict.keys():
    #     for endState in proDict[startState].keys():
    #         for jointAction, pro in proDict[startState][endState].items():
    #             if jointAction[0] not in actionSpaceP1:
    #                 actionSpaceP1.append(jointAction[0])
    #             if jointAction[1] not in actionSpaceP2:
    #                 actionSpaceP2.append(jointAction[1])
    #             grf.add_edge(startState, endState, action = jointAction, probability = pro)
    for startState in proDict.keys():
        for jointAction in proDict[startState].keys():
            for endState, pro in proDict[startState][jointAction].items():
                if jointAction[0] not in actionSpaceP1:
                    actionSpaceP1.append(jointAction[0])
                if jointAction[1] not in actionSpaceP2:
                    actionSpaceP2.append(jointAction[1])
                grf.add_edge(startState, endState, action = jointAction, probability = pro)
    return grf, actionSpaceP1, actionSpaceP2


if __name__ == "__main__":
    filename = "test.pkl"
    net, actSpaceP1, actSpaceP2 = transferObj(filename)