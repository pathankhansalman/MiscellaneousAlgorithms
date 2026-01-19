# -*- coding: utf-8 -*-
"""
Created on Sat Jun 06 2026

@author: Antigravity
"""

import math
from typing import List, Tuple

Point = Tuple[float, float]

def orientation(p: Point, q: Point, r: Point) -> int:
    """
    Finds the orientation of ordered triplet (p, q, r).
    
    Returns:
         0 -> p, q and r are collinear
         1 -> Clockwise
         2 -> Counterclockwise
    """
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return 2

def distance_sq(p1: Point, p2: Point) -> float:
    """
    Returns the squared Euclidean distance between p1 and p2.
    """
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

def graham_scan(points: List[Point]) -> List[Point]:
    """
    Computes the Convex Hull of a set of 2D points using the Graham Scan algorithm.
    
    Args:
        points: A list of (x, y) coordinate tuples.
        
    Returns:
        A list of points representing the convex hull in counterclockwise order.
    """
    n = len(points)
    if n < 3:
        return points  # Convex hull is not well-defined for less than 3 points
        
    # Find the bottom-most point (leftmost in case of tie)
    pivot = min(points, key=lambda p: (p[1], p[0]))
    
    # Custom sort key using polar angle relative to pivot
    # If angles are equal, sort by distance to pivot
    def polar_angle_key(p: Point) -> Tuple[float, float]:
        if p == pivot:
            return -math.inf, 0.0
        # Calculate polar angle
        angle = math.atan2(p[1] - pivot[1], p[0] - pivot[0])
        # Calculate distance
        dist = distance_sq(pivot, p)
        return angle, dist

    sorted_points = sorted(points, key=polar_angle_key)
    
    # If two or more points make same angle with pivot, we should only keep the farthest one.
    # However, for a simple implementation, we can just process them and let orientation check remove them.
    # To be fully robust, let's keep the stack approach.
    stack: List[Point] = []
    stack.append(sorted_points[0])
    stack.append(sorted_points[1])
    stack.append(sorted_points[2])
    
    for i in range(3, n):
        while len(stack) > 1 and orientation(stack[-2], stack[-1], sorted_points[i]) != 2:
            stack.pop()
        stack.append(sorted_points[i])
        
    return stack

if __name__ == "__main__":
    # Test cases: Set of 2D points
    test_points = [(0, 3), (1, 1), (2, 2), (4, 4), (0, 0), (1, 2), (3, 1), (3, 3)]
    
    print("Running Graham Scan Convex Hull algorithm test...")
    hull = graham_scan(test_points)
    print(f"Input points: {test_points}")
    print(f"Convex Hull: {hull}")
