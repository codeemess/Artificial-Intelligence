from missionaries_and_cannibals import MissionariesAndCannibals
from search import *

def main():
    problem = MissionariesAndCannibals()
    result = search.uniform_cost_search(problem)
    print(result)
    print_path(result.path())

def print_path(path):
    for node in path:
        print(node.state.value)

if __name__ == '__main__':
    main()
