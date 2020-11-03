"""
You are given a 2d grid of `"1"`s and `"0"`s that represents a "map". The
`"1"`s represent land and the `"0"s` represent water.

You need to write a function that, given a "map" as an argument, counts the
number of islands. Islands are defined as adjacent pieces of land that are
connected horizontally or vertically. You can also assume that the edges of the
map are surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""
# from collections import deque


# UPER:
# input: 2D array (list of lists)
# output: integer

# What kind of graph is it?
# Unidirectional because we have connections in both ways
# What are the verticies of this graph?
# -- Each value in the 2D array is a vertex (think coordinates)
# What are the edges / when do we have an edge?
# -- Edges are moving up / down / left / right between bits of land ('1's)

# Want to check up / down / left / right to see if it's land or water

# Start at a 1 (land) and move out in all directions until we hit water
# --> Traversal of the land graph. Can do breadth first or depth first.

def numIslands(grid):
  
  # PLAN
  # Start at [0][0]
  # check the value at [0][0]
  # if it's a '1' (land):
    # kick off of the BFS
    # why do we want to find all of the locations connected to the current one?
      # to see if you can skip the next one?
      # we want to maek the connected locations as patr of the same island so we can skip it / not double count it
      # store the connected locations in a "visited array"
    # increment our island count
      
  # if it's a '0' (water):
    # Don't do anything, check the next spot
  # repeat for every location in the grid
  # as we repeat, if the new location has already been visited, that means it's part of an island we've already counted
    # --> skip it!
    
  for row_idx in range(len(grid)):
    for col_idx in range(len(grid[row_idx])):
      # if it's visited, skip TODO
      if grid[row_idx][col_idx] == 0:
        # skip it
        continue
      
      if grid[row_idx][col_idx] == 1:
        bfs(...) #TODO
        # need to add it to visited
        num_islands += 1  
    
  # Return the number of islands
  
  
  # row is the first index (into the outer array)
  # col is the second index (into the inner array)
  

def bfs(grid, starting_location)
# starting location is a tuple (row_idx, col_idx)
# From starting location, go out in each direction and add to visited array
  pass
  # need a q and a visited array
  queue = []
  visited = set()
  # Add the current node to queue
  queue.append(starting_location)
  # while the queue is not empty:
  while len(queue) > 0:
    # pop off the queue
    cur_loc = queue.pop(0)
    # process it / visit it
    visit.add(cur_loc)
    # add the node's children to the queue
    row, col = cur_loc # assign the first value of the tuple to row, and second to col
    
    # possible edges go up, down, left, or right:
    # need to check if the edge actyualy exists before we add it to the queue
    queue.append(row - 1, col)
    # up: [row - 1[col]
    # down: [row + 1][col]
    # left: [row][col -1]
    # right: [row + 1][col 1]
    
    
def isLocationValid(grid, row, col):
  if not (0 < row < len(grid)):
    return False
  
  if not (0)
  return True