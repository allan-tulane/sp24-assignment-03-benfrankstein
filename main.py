import math, queue
from collections import Counter

####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'), ('relev--ant','-ele-phant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    # TO DO - modify to account for insertions, deletions and substitutions
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
    else:
        if (S[0] == T[0]):
            return(MED(S[1:], T[1:]))
        else:
            return(1 + min(MED(S, T[1:]), MED(S[1:], T)))


def fast_MED(S, T, MED={}):
    if (S, T) in MED:
        return MED[(S, T)]

    if S == "":
        return len(T)

    elif T == "":
        return len(S)
    elif S[0] == T[0]:
        result = fast_MED(S[1:], T[1:], MED)
    else:
        insert = fast_MED(S, T[1:], MED)
        delete = fast_MED(S[1:], T, MED)
        result = 1 + min(insert , delete)
        MED[(S, T)] = result
    return result

def fast_align_MED(S, T, MED={}):
    if (S, T) in MED:
        return MED[(S, T)]
    elif S == "":
        MED[(S, T)] = ("-" * len(T), T)
        return MED[(S, T)]
    elif T == "":
        MED[(S, T)] = (S, "-" * len(S))
        return MED[(S, T)]
  
    else:
        if S[0] == T[0]:
            SA, TA = fast_align_MED(S[1:], T[1:], MED)
            MED[(S, T)] = (S[0] + SA, T[0] + TA)
        else:
            SI, TI = fast_align_MED(S, T[1:], MED)
            SD, TD = fast_align_MED(S[1:], T, MED)

            insertcost = 1 + len(SI)
            deletecost = 1 + len(SD)

            if insertcost <= deletecost:
                MED[(S, T)] = ("-" + SI, T[0] + TI)
            else:
                MED[(S, T)] = (S[0] + SD, "-" + TD)
    print(MED[(S,T)])
    return MED[(S, T)]
