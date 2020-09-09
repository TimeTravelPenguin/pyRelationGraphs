from numbers import Number
from typing import Set, Dict, Tuple

import matplotlib.pyplot as plt
import numpy as np
from RelationGrapher.pltpoint import Point
from RelationGrapher.proposition import Proposition
from RelationGrapher.relation import Relation
from matplotlib import patheffects


def plot_relation(relation: str, values: Set, print_details=True):
    rel = Relation(relation)

    if print_details:
        print_relation_properties(rel, values)

    fig, ax = plt.subplots()

    relations = list(rel.relateOver(values))

    vertexes: Dict[Number, Tuple] = dict()
    c = 1
    total = len(values)

    for i in values:
        if i not in vertexes:
            val = 2 * np.pi * c / total
            vertexes[i] = (np.cos(val), np.sin(val))
            txt = plt.text(*vertexes[i], i, size=12, color='white')
            txt.set_path_effects([patheffects.withStroke(linewidth=3, foreground='black')])
            plt.scatter(*vertexes[i])
            c += 1

    for a, b in relations:
        p1 = Point(*vertexes[a])
        p2 = Point(*vertexes[b])
        p1.connectToPoint(p2)

    title = "aRb iff " + rel.relation_expression()
    fig.suptitle(title)
    plt.axis("off")
    plt.show()


def print_relation_properties(relation: Relation, values: Set):
    rel = list(relation.relateOver(values))
    print("Relation:", relation.relation_expression())
    print("Set:", values)
    print("(a, b) in R:", rel)
    print("Reflexive:", relation.isReflexiveOver(values))
    print("Symmetric:", relation.isSymmetricOver(values))
    print("Antisymmetric:", relation.isAntisymmetricOver(values))
    print("Transitive:", relation.isTransitiveOver(values))
