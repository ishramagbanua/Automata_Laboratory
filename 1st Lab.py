# ======================
# Problem 1 DFA
# ======================

def dfa_problem1(string):
    # States: a (start), b, 1 (final)
    state = 'a'  
    
    for ch in string:
        if state == 'a':
            if ch == '0':
                state = 'a'
            elif ch == '1':
                state = 'b'
        elif state == 'b':
            if ch == '0':
                state = '1'
            elif ch == '1':
                state = 'a'
        elif state == '1':  # final state
            if ch == '0':
                state = '1'
            elif ch == '1':
                state = '1'
    
    return state == '1'


# Accepted and Rejected examples
accepted_p1 = ["1110001", "101001", "111000"]
rejected_p1 = ["11011011", "1100011", "11111101"]


print("===== Problem 1 DFA =====")
for s in accepted_p1:
    print(f"{s:8} -> {'Accepted' if dfa_problem1(s) else 'Rejected'}")
for s in rejected_p1:
    print(f"{s:8} -> {'Accepted' if dfa_problem1(s) else 'Rejected'}")






# ======================
# Problem 2 DFA
# ======================

def dfa_problem2(string):
    # States: q0 (start, final), q1, q2, q3 (final)
    state = 'q0'
    
    for ch in string:
        if state == 'q0':
            if ch == 'a':
                state = 'q1'
            elif ch == 'b':
                state = 'q2'
        elif state == 'q1':
            if ch == 'a':
                state = 'q0'
            elif ch == 'b':
                state = 'q3'
        elif state == 'q2':
            if ch == 'a':
                state = 'q3'
            elif ch == 'b':
                state = 'q0'
        elif state == 'q3':
            if ch == 'a':
                state = 'q2'
            elif ch == 'b':
                state = 'q1'
    
    return state in ['q0', 'q3']  # Accepting states


# 8 Accepted and 8 Rejected examples
accepted_p2 = ["aabbab", "abababab", "baababba"]
rejected_p2 = ["bbaabb", "aabbaabb", "bbaabbba"]

print("\n===== Problem 2 DFA =====")
print("Accepted Examples:")
for s in accepted_p2:
    print(f"{s:8} -> Accepted")

print("\nRejected Examples:")
for s in rejected_p2:
    print(f"{s:8} -> Rejected")
