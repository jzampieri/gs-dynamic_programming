from typing import List, Tuple

def boundary_points(polygon: List[Tuple[int, int]]) -> int:
    def points(x1, y1, x2, y2):
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        return dx + dy - (dx, dy)
    
    B = 0
    n = len(polygon)
    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % n]
        B += abs(x2 - x1) + abs(y2 - y1) - 1
    return B + n

def interior_points(polygon: List[Tuple[int, int]]) -> int:
    n = len(polygon)
    area_twice = 0
    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % n]
        area_twice += (x1 * y2) - (y1 * x2)
    
    area = abs(area_twice) // 2
    B = boundary_points(polygon)
    
    I = area - (B // 2) + 1
    return I

def pick_theorem_area(polygon: List[Tuple[int, int]]) -> float:
    I = interior_points(polygon)
    B = boundary_points(polygon)
    A = I + (B / 2) - 1
    return A

#repasse de valores
polygon = [(0, 0), (6, 0), (7, 3), (0, 9)]
area = pick_theorem_area(polygon)
print(f"A área marinha é: {area}km²")
