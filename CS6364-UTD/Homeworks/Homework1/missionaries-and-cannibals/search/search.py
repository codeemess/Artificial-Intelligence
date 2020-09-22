"""
Iterative deepening and depth limited search.

Source:
https://github.com/aimacode/aima-python/blob/master/search.py
"""

import sys
from node import Node
from utils import PriorityQueue
import numpy as np

def memoize(fn, slot=None, maxsize=32):
    """Memoize fn: make it remember the computed value for any argument list.
    If slot is specified, store result in that slot of first argument.
    If slot is false, use lru_cache for caching the values."""
    if slot:
        def memoized_fn(obj, *args):
            if hasattr(obj, slot):
                return getattr(obj, slot)
            else:
                val = fn(obj, *args)
                setattr(obj, slot, val)
                return val
    else:
        @functools.lru_cache(maxsize=maxsize)
        def memoized_fn(*args):
            return fn(*args)

    return memoized_fn

def iterative_deepening_search(problem):
    """Iteratively search greater depths of the search tree to find the goal state."""
    for depth in range(sys.getsizeof([None] * (2**20))):
        result = depth_limited_search(problem, depth)
        if result != 'cutoff':
            return result


def depth_limited_search(problem, limit=50):
    """Depth-first search with a limit.

    Depth-first search always expands the deepest node
    in the current frontier of the search tree.

    We apply a limit to prevent the algorithm from failing on
    problems with infinitely deep paths.

    Limit defaults to 50.
    """
    root = Node(problem.initial_state)
    return __recursive_dls(root, problem, limit)


def __recursive_dls(node, problem, limit):
    """Recursive helper function for depth limited search.

    Returns 'cutoff' if no solution was found within the specified limit.
    Otherwise returns the node containing the goal state.
    """
    if problem.is_goal_state(node.state):
        return node
    elif limit == 0:
        return 'cutoff'
    else:
        cutoff_occurred = False
        for child in node.expand(problem):
            result = __recursive_dls(child, problem, limit - 1)
            if result == 'cutoff':
                cutoff_occurred = True
            elif result is not None:
                return result
        return 'cutoff' if cutoff_occurred else None

def recursive_best_first_search(problem, h=None):
    """[Figure 3.26]"""
    h = memoize(h or problem.h, 'h')

    def RBFS(problem, node, flimit):
        if problem.is_goal_state(node.state.value):
            return node, 0  # (The second value is immaterial)
        successors = node.expand(problem)
        if len(successors) == 0:
            return None, np.inf
        for s in successors:
            s.f = max(s.path_cost() + h(s), node.f)
        while True:
            # Order by lowest f value
            successors.sort(key=lambda x: x.f)
            best = successors[0]
            if best.f > flimit:
                return None, best.f
            if len(successors) > 1:
                alternative = successors[1].f
            else:
                alternative = np.inf
            result, best.f = RBFS(problem, best, min(flimit, alternative))
            if result is not None:
                return result, best.f
        #print(successors)
    node = Node(problem.initial_state)
    node.f = h(node)
    result, bestf = RBFS(problem, node, np.inf)
    return result

def rbfs(problem):
    return recursive_best_first_search(problem, lambda n: problem.h(n.state))

def best_first_graph_search(problem, f, display=False):
    """Search the nodes with the lowest f scores first.
    You specify the function f(node) that you want to minimize; for example,
    if f is a heuristic estimate to the goal, then we have greedy best
    first search; if f is node.depth then we have breadth-first search.
    There is a subtlety: the line "f = memoize(f, 'f')" means that the f
    values will be cached on the nodes as they are computed. So after doing
    a best first search you can examine the f values of the path returned."""
    f = memoize(f, 'f')
    node = Node(problem.initial_state)
    frontier = PriorityQueue('min', f)
    frontier.append(node)
    explored = set()
    while frontier:
        print(frontier.heap) 
        print("***************")
        print(explored)
        print("\n")
        print("--------------")
        node = frontier.pop()
        if problem.is_goal_state(node.state):
            if display:
                print(len(explored), "paths have been expanded and", len(frontier), "paths remain in the frontier")
            return node
        explored.add(node.state)
        for child in node.expand(problem):
            if child.state not in explored and child not in frontier:
                frontier.append(child)
            elif child in frontier:
                if f(child) < frontier[child]:
                    del frontier[child]
                    frontier.append(child)
    return None


def uniform_cost_search(problem, display=False):
    """[Figure 3.14]"""
    return best_first_graph_search(problem, lambda node: node.path, display)


def astar_search(problem, h=None, display=False):
    """A* search is best-first graph search with f(n) = g(n)+h(n).
    You need to specify the h function when you call astar_search, or
    else in your Problem subclass."""
    h = memoize(h or problem.h, 'h')
    return best_first_graph_search(problem, lambda n: n.path_cost()+ problem.h(n.state), display)

def greedy_best_first_graph_search(problem,h=None,display=False):
    h = memoize(h or problem.h,'h') 
    return best_first_graph_search(problem, lambda n: problem.h(n.state),display)