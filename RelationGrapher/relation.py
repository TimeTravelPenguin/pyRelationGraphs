"""
Author: Phillip Smith c3322845
Contact: c3322845@uon.edu.au
Will I do your homework? No.
"""

import itertools
from typing import *

from RelationGrapher.proposition import Proposition


def cart_prod(array: Set) -> Set[Tuple[Any, Any]]:
    return set([s for s in itertools.product(array, array)])


class Relation:
    def __init__(self, proposition: str) -> None:
        self._proposition = proposition

    def relation_expression(self) -> str:
        return self._proposition

    def relateOver(self, values: Set) -> Set[Tuple[Any, Any]]:
        """
        Find the valid relations held over a particular set
        :rtype: object
        :param values: A set of values to apply the relation to
        :rtype: Set
        :return: Returns a set of all elements that hold under the relation
        """

        related = set()
        prop = Proposition(self._proposition)
        for (a, b) in cart_prod(values):
            if prop.compile(a, b):
                related.add((a, b))

        return related

    # R(a, a) for all a
    def isReflexiveOver(self, values: Set) -> bool:
        prop = Proposition(self._proposition)
        return all([prop.compile(i, i) for i in values])

    # R(a, b) implies R(b, a)
    def isSymmetricOver(self, values: Set) -> bool:
        prop = Proposition(self._proposition)
        return all([prop.compile(a, b) for (b, a) in self.relateOver(values)])

    # R(a, b) & R(b, a) implies a = b
    def isAntisymmetricOver(self, values: Set) -> bool:
        prop = Proposition(self._proposition)
        return all([
            (a == b) for (a, b) in self.relateOver(values)
            if (prop.compile(a, b) and prop.compile(b, a))
        ])

    # R(a, b) & R(b, c) implies R(a, c)
    def isTransitiveOver(self, values: Set) -> bool:
        prop = Proposition(self._proposition)
        relations = self.relateOver(values)
        isTransitive = True
        for (a, b) in relations:
            bc = [(B, C) for (B, C) in relations if B == b]
            isTransitive *= all(prop.compile(a, c) for (b, c) in bc)

        return bool(isTransitive)
