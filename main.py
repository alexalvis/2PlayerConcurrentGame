import pickle
import Translate
import safetyGame
import reachabilityGame
from itertools import product

def reachAlmostSure():
    W = set()
    for p1, q1, p2, q2 in product(range(11), range(11), repeat= 2):
        if (p1, q1) == (9, 5) and (abs(p1-p2) + abs(q1 - q2)) > 1:
            W.add(((p1, q1),(p2, q2)))
    print(len(W))
    return W

def safeAlmostSure(reach):
    safeSet = set()
    for p1, q1, p2, q2 in product(range(11), range(11), repeat= 2):
        if ((p1, q1), (p2, q2)) not in reach:
            safeSet.add(((p1, q1), (p2, q2)))
    print ("length of safety set is:",len(safeSet))
    return safeSet

if __name__ == "__main__":
    # filename = input("filename")
    storeFlag = False
    filename = "filename_P_s1_a_s2.pkl"
    grf, actionSpaceP1, actionSpaceP2 = Translate.transferObj(filename)
    W_reach = reachAlmostSure()
    # W_reachAlmost, reachpolicy = reachabilityGame.reachabilityGameSolver(grf, W_reach, actionSpaceP1, actionSpaceP2)
    W_safe = safeAlmostSure(W_reach)
    W_safeAlmost = safetyGame.safetyGameSolver(grf, W_safe, actionSpaceP1, actionSpaceP2)
    filename = "testsafe.pkl"
    picklefile = open(filename, "wb")
    pickle.dump(W_safeAlmost, picklefile)
    picklefile.close()
    if storeFlag:
        filename = "grf.pkl"
        picklefile = open(filename, "wb")
        pickle.dump(grf, picklefile)
        picklefile.close()

        # filename = "testreach.pkl"
        # picklefile = open(filename, "wb")
        # pickle.dump(W_reachAlmost, picklefile)
        # picklefile.close()