# Jody Bailey
# 09/21/2018
# Intro to Algorithms
# This program takes in a pre-generated maze and traverses the left side
# to find the entrance. Once it finds the entrance, it will create a node
# and start building a tree looking for possible paths to the exit. Every
# move that it makes, it replaces the 'P' with a '*' to indicate the path
# that it traveled. When it is complete, the maze is printed to the screen
# and the full path is printed below.

from subpkg.BreadthFirst import BreadthSearch
from subpkg.DepthFirst import DepthSearch


class MainProgram:

    # Method to perform the breadth first search.
    # Calls the method run() defined in the BreadthSearch class.
    def breadthFirst(self):
        # Run the Breadth First search
        print('Breadth First Search\n')
        search1 = BreadthSearch()
        search1.run()

    # Method to perform the depth first search.
    # Calls the method run() defined in the DepthSearch class
    def depthFirst(self):
        # Run the Depth First search
        print('Depth First Search\n')
        search2 = DepthSearch()
        search2.run()

    # Main method that calls both the breadth first and
    # depth first searches.
    def main(self):
        self.breadthFirst()
        print()
        self.depthFirst()


# Instantiates an instance of the main class
program = MainProgram()

# Calls the main method of the class
program.main()
