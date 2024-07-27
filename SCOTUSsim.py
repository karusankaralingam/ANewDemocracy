from itertools import product
import copy
import matplotlib.pyplot as plt

# Initial data of the Supreme Court justices
justices = [
    {"Name": "Roberts", "Ideology": "Conservative", "Age": 69},
    {"Name": "Thomas", "Ideology": "Conservative", "Age": 76},
    {"Name": "Alito", "Ideology": "Conservative", "Age": 74},
    {"Name": "Gorsuch", "Ideology": "Conservative", "Age": 56},
    {"Name": "Kavanaugh", "Ideology": "Conservative", "Age": 59},
#    {"Name": "Barrett", "Ideology": "Conservative", "Age": 52},
    {"Name": "Barrett*", "Ideology": "Liberal", "Age": 52},
    {"Name": "Sotomayor", "Ideology": "Liberal", "Age": 70},
    {"Name": "Kagan", "Ideology": "Liberal", "Age": 64},
    {"Name": "Jackson", "Ideology": "Liberal", "Age": 53}
]

# Function to simulate the aging of justices and appointments
def simulate_appointments(election_results):
    liberal_leaning = 0
    cons_super_majority = 0 
    n_terms = 0
    current_justices = copy.deepcopy(justices)
    president_ideology = {"D": "Liberal", "R": "Conservative"}
    court_compositions = {"Liberal": 0, "Conservative": 0}
    for i in justices:
        court_compositions[ i['Ideology'] ] += 1
#    print(court_compositions)
   
    prev_liberal = 0
    liberal_streak = 0
    max_liberal_streak = 0
    ret_array = []
    for term, result in enumerate(election_results):
        n_terms += 1
        for justice in current_justices:
            justice["Age"] += 4
            if justice["Age"] >= 81 and justice["Ideology"] == president_ideology[result]:
                print(f"Term {term + 1}: President {result} appoints a new {justice['Ideology']} justice replacing {justice['Name']} who retired at age {justice['Age']}.")
                justice["Age"] = 53
                justice["Name"] = justice["Name"] + "-succ-" + president_ideology[result]
                # Print the retirement and replacement event
            if justice["Age"] >= 85 and justice["Ideology"] != president_ideology[result]:
                court_compositions[ justice["Ideology"] ] -= 1
                justice["Ideology"] = president_ideology[result]
                print(f"Term {term + 1}: President {result} appoints a new {justice['Ideology']} justice replacing {justice['Name']} who died at age {justice['Age']}.")
                justice["Age"] = 53
                justice["Name"] = justice["Name"] + "-succ-" + president_ideology[result]
                court_compositions[ president_ideology[result]] += 1
            if justice["Age"] >= 85 and justice["Ideology"] == president_ideology[result]:
                print("UNHANDLED")
        if (court_compositions['Liberal'] >= 5):
            liberal_leaning += 1
            if prev_liberal == 1:
                liberal_streak += 1
            else:
                liberal_streak = 1
                prev_liberal = 1
        else:
            prev_liberal = 0
        if liberal_streak > max_liberal_streak:
            max_liberal_streak = liberal_streak
        if (court_compositions['Liberal'] <= 3):
            cons_super_majority += 1
        print(term, court_compositions, max_liberal_streak, court_compositions['Liberal'] >= 5, court_compositions['Liberal'] <= 3)
        ret_array.append(court_compositions)
    
    return ret_array, current_justices, liberal_leaning, n_terms, cons_super_majority, max_liberal_streak

def has_consecutive(lst, C):
    count = 0
    for symbol in lst:
        if symbol == C:
            count += 1
            if count >= 3:
                return True
        else:
            count = 0
    return False

# Generate all possible combinations for 20 presidential terms
years = range(2024, 2081, 4)
num_terms = len(years)
combinations = product("DR", repeat=num_terms)

# Simulate each combination and print the resulting Supreme Court composition
n_sims = 0
n_liberal_leaning = 0
n_cons_super_majority = 0
n_cons_permanent_super_majority = 0
L = 0
COMP_BY_TERM = []
for i in range(num_terms):
    l = []
    COMP_BY_TERM.append( l )

for combo in combinations:
    if (has_consecutive(combo, "D") or has_consecutive(combo, "R")):
        print("Ignoring")
        continue
    print(f"---Election results: {''.join(combo)}", end=" ")
    A, final_justices, x, y, z, streak = simulate_appointments(combo)
    for i,j in enumerate(A):
#        print('ret-val', i,j)
        COMP_BY_TERM[i].append(j['Liberal'])
#        print(COMP_BY_TERM[i])
    n_liberal_leaning += x 
    n_sims += y 
    n_cons_super_majority += z 
    print(f"---NO LOG Election results: {''.join(combo)}", end=" ")
    if (x < 0.01):
        print(" consecutive ", end=' ')
        n_cons_permanent_super_majority += 1 
    print(x/y, z/y, streak) 
    L = L + 1
    for justice in final_justices:
        print(f"{justice['Name']}: {justice['Ideology']}, Age: {justice['Age']}")
    print("\n")
print("NO LOG Election total", "Liberal-frac", n_liberal_leaning/n_sims, 'cons-super-maj-frac', n_cons_super_majority/n_sims, 'frac-perm-majority', n_cons_permanent_super_majority/L)
# Note: Printing all possible combinations will generate a lot of output.

for i in COMP_BY_TERM:
    dist = [0]*10
    for y in i:
        dist[y] += 1
    z = sum(dist)
    for i in range(10):
        dist[i] = dist[i]/z
    print(dist)
    break
#    print(i)
s = 0
for i in dist:
    s = s+i
    print(s)
x_labels = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
plt.bar(x_labels, dist, color='blue', edgecolor='black')

# Adding title and labels
plt.title('Histogram of # Liberal Justices')
plt.xlabel('# Liberal Justices')
plt.ylabel('Probability')
plt.xticks(x_labels)
plt.savefig('histogram.png')
# Display the plot
plt.show()
