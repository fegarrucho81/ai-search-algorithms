# Fundamentals of AI – Search Algorithms

This repository contains the implementation of three classic search and optimization problems developed as part of a university assignment for the **Fundamentals of Artificial Intelligence** course.

## 📌 Assignment Overview

The goal was to apply different types of search strategies to solve specific problems using Python. The project includes:

### 1. Dijkstra's Algorithm

- **Purpose:** Find the shortest paths from a source vertex to all other vertices in a graph.
- **Approach:** Uses a priority queue (min-heap) to always expand the node with the smallest accumulated cost.
- **Result:** Outputs the shortest distances from the starting node to each node in the graph.

### 2. Tabu Search for Optimization

- **Purpose:** Maximize the function `f(x1, x2) = -sin(x1) - cos(x2)` with constraints on `x1` and `x2`.
- **Approach:** Uses a local search algorithm with a Tabu list to avoid cycles and explore new solutions.
- **Result:** Displays the best solution found after a fixed number of iterations.

### 3. Search Strategies: Greedy Best-First Search vs. Uniform Cost Search

- **Purpose:** Compare three search strategies to find a path between two points in a graph.
- **Greedy Best-First Search:** Uses only the heuristic function to decide which node to expand.
- **Uniform Cost Search:** Considers the total cost from the start node to the current node (ignores heuristics).
- **A-Star Search:** Combines both the path cost and the heuristic (f(n) = g(n) + h(n)), balancing between cost-so-far and estimated cost-to-goal to find the optimal path efficiently.
- **Result:** Shows the path found by each strategy from node `A` to node `I`.

## 🛠️ Technologies

- Python 3.x
- Standard libraries: `heapq`, `math`, `random`

## 📚 Academic Context

This project was developed as part of the "Fundamentals of Artificial Intelligence" course. It aimed to provide practical experience with different search techniques commonly used in AI problem-solving.
