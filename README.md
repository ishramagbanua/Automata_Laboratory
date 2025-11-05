# CS13A – Automata Theory and Formal Languages  
## Lab 2 – Final Term (1st Sem 2025–2026)

### Problem
Draw the Mealy Machine and the converted Moore Machine for the given transition table.  
Write the code for the converted Moore Machine that can process the following inputs:
`00110`, `11001`, `1010110`, `1011111`.

---

# Mealy Machine
<img width="968" height="666" alt="Mealy png" src="https://github.com/user-attachments/assets/aa85129e-8432-4c2f-9be3-cfe5425907ec" />


---

# Moore Machine
<img width="1140" height="905" alt="Moore png" src="https://github.com/user-attachments/assets/57e43015-5824-4643-8ecb-7273bb991152" />


---

### 🧠 Moore Machine Simulation
```python
# ---------------------------------
# Moore Machine Simulation
# ---------------------------------

moore = {
    "A/A": {"0": "A/A", "1": "B/B"},
    "B/B": {"0": "C/A", "1": "D/B"},
    "C/A": {"0": "D/C", "1": "B/B"},
    "C/B": {"0": "D/B", "1": "B/B"},
    "C/C": {"0": "D/C", "1": "B/B"},
    "D/B": {"0": "B/B", "1": "C/B"},
    "D/C": {"0": "B/B", "1": "C/C"},
    "E/C": {"0": "D/C", "1": "E/C"}
}

def process(input_str, start="A/A"):
    state = start
    output = state.split("/")[1]  # initial output
    for i in input_str:
        state = moore[state][i]
        output += state.split("/")[1]
    return output

inputs = ["00110", "11001", "1010110", "1011111"]

print("Input  →  Output")
for inp in inputs:
    print(f"{inp}  →  {process(inp)}")



