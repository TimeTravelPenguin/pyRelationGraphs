"""
Author: Phillip Smith c3322845
Contact: c3322845@uon.edu.au
Will I do your homework? No.
"""

import RelationGrapher as rg

# For a set S = {x: f(x)} and a relation R(a,b) for a,b in S, plot a graph of the relations
if __name__ == "__main__":
    rg.plot_relation("(a+b)*(a-b)>a*b", {3, 4, 5, 6, 7, 8})
