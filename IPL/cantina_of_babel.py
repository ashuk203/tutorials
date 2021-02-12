num_chars = int(input())

adjacency_list = {}

# Adds a directed edge from l1 to l2
def add_edge(l1, l2):
    if l1 not in adjacency_list.keys():
        adjacency_list[l1] = []

    if l2 not in adjacency_list[l1]:
        adjacency_list[l1].append(l2)


# Checks whether there is a directed edge from l1 to l2
def check_edge(l1, l2):
    if l1 in adjacency_list.keys():
        return l2 in adjacency_list[l1]

    return False


# To keep track of the number of speakers that speak a certain language
num_speakers = {}
def incr_count(language):
    if language not in num_speakers.keys():
        num_speakers[language] = 0

    num_speakers[language] += 1


# Read in input
for c in range(num_chars):
    char_info = input().split(" ")

    char_speak = char_info[1]
    incr_count(char_speak)

    for c_understand in range(2, len(char_info)):
        add_edge(c_understand, char_speak)



# Find strongly connected components in graph
