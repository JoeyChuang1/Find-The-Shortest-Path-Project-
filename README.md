# Find The Shortest Path Project

This project implements an efficient A* pathfinding algorithm in Python to navigate between any two points on a grid-based map. It leverages heuristic functions to prioritize promising paths, leading to faster route discovery. A video demonstration showcases the functionality.

Demo Here: https://www.youtube.com/watch?v=_d5AuspKe3o

## 🚀 Features

- **A* Pathfinding Algorithm**: Utilizes the A* algorithm for optimal pathfinding on grid-based maps.
- **Performance Optimization**: Achieved an average performance improvement of 71% through:
  - **Multiprocessing**: Distributes computations across multiple cores to accelerate pathfinding.
  - **Heurispy Library Integration**: Incorporates pre-defined heuristic functions optimized for various scenarios.
- **Pygame Visualization**: Employs Pygame for efficient visualization of the pathfinding process, aiding in debugging and understanding.

## 📹 Demonstration

A video demonstration showcasing the functionality is available [here](#).

## 🛠️ Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/JoeyChuang1/Find-The-Shortest-Path-Project-.git
   cd Find-The-Shortest-Path-Project-

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt

## 🧪 Usage

To run the pathfinding visualization:

    ```bash
    python main.py
  

Follow the on-screen instructions to set the start and end points, and observe the algorithm in action.

## 📁 Project Structure

    ```bash
    Find-The-Shortest-Path-Project-/
    ├── main.py                 # Entry point for the application
    ├── pathfinding/
    │   ├── a_star.py           # Implementation of the A* algorithm
    │   ├── heuristics.py       # Heuristic functions utilizing heurispy
    │   └── multiprocessing.py  # Multiprocessing utilities for performance
    ├── visualization/
    │   └── pygame_visual.py    # Pygame-based visualization components
    ├── requirements.txt        # List of project dependencies
    └── README.md               # Project documentation

## 📚 Dependencies
  Python 3.x

  Pygame

  Heurispy

  Multiprocessing (standard Python library)

Install all dependencies using:
  ```bash
    pip install -r requirements.txt

## 📈 Performance Optimization Details
The algorithm's performance was enhanced through:

Multiprocessing: By distributing computations across multiple cores, the algorithm explores a larger search space concurrently, accelerating pathfinding.

Heurispy Integration: Utilizes optimized heuristic functions tailored for various pathfinding scenarios, ensuring efficient exploration strategies.

These optimizations collectively contributed to a 71% improvement in performance.


