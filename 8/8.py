import math

class Point:
    def __init__(self, id: int, x: int, y: int, z: int, next: list[any] = None):
        self.id = id
        self.x = x
        self.y = y
        self.z = z
        self.next = next

    def distance_from_point(self, other_point) -> float:
        return math.dist((self.x, self.y, self.z), (other_point.x, other_point.y, other_point.z))
    
    def __repr__(self):
        return f"Point(id={self.id}, {self.x}, {self.y}, {self.z})"
    
    def __eq__(self, other_point) -> bool:
        return self.id == other_point.id

    def connected_to(self, other_point) -> bool:
        return other_point in self.next if self.next else False
    
    
def find_nearest_unconnected_point(points: list[Point]):
    # returns the two closest not already connected points
    min_distance = float('inf')
    closest_pair = (None, None)
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            # if points already connected, skip
            if points[i].connected_to(points[j]):
                continue
            distance = points[i].distance_from_point(points[j])
            if distance < min_distance:
                min_distance = distance
                closest_pair = (points[i], points[j])
    return closest_pair


def find_farthest_point(points: list[Point]):
    min_distance = -1
    farthest_pair = (None, None)
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            distance = points[i].distance_from_point(points[j])
            if distance > min_distance:
                min_distance = distance
                farthest_pair = (points[i], points[j])
    return farthest_pair

class DistancePoints:
    def __init__(self, distance: float, points: list[tuple[Point, Point]]):
        self.distance = distance
        self.points = points

    def __repr__(self):
        return f"DistancePoints(distance={self.distance}, points={self.points})"


def pair_points(points: list[Point]):
    distance_points = []
    last_connected = (None, None)
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            if points[i].connected_to(points[j]):
                continue
            if points[i].next == None:
                points[i].next = []
            if points[j].next == None:
                points[j].next = []
            points[i].next.append(points[j])
            points[j].next.append(points[i])
            last_connected = (points[i], points[j])
            distance = points[i].distance_from_point(points[j])
            distance_points.append(DistancePoints(distance, [(points[i], points[j])]))

    # points_sorted = sorted(points, key=lambda point: point.id)
    # return points_sorted

    distance_points.sort(key=lambda distancePoint: distancePoint.distance)
    return distance_points, last_connected


def get_circuits(points: list[Point]):
    circuits = []
    visited = set()
    for point in points:
        if point.id in visited:
            continue
        circuit = []
        stack = [point]
        while stack:
            current = stack.pop()
            if current.id in visited:
                continue
            visited.add(current.id)
            circuit.append(current)
            if current.next:
                for n in current.next:
                    if n.id not in visited:
                        stack.append(n)
        circuits.append(circuit)
    return circuits


def run():
    points = []
    with open("testinput.txt") as f:
        for i, line in enumerate(f):
            coords = line.strip().split(",")
            point = Point(id=i, x=int(coords[0]), y=int(coords[1]), z=int(coords[2]), next=None)
            points.append(point)

    connections = 0
    while connections < 1000:
        p1, p2 = find_nearest_unconnected_point(points)
        if p1.next is None:
            p1.next = []
        if p2.next is None:
            p2.next = []
        p1.next.append(p2)
        p2.next.append(p1)
        connections += 1
        print(f"Connected {p1} to {p2} on connection {connections}")

    # print("Final connections:")
    # for point in points:
    #     print(f"{point} connected to {point.next}")

    circuits = get_circuits(points)

    print(f"Total circuits found: {len(circuits)}")
    circuits.sort(key=len, reverse=True)
    answer = 1
    for circuit_idx in range(0, 3):
        answer *= len(circuits[circuit_idx])

    print(f"Answer: {answer}")

# this solution is bad and takes forever, but it worked in the end. 
# run_2_2 is meant to be better, but I didnt get it working 
def run_2():
    points = []
    with open("input.txt") as f:
        for i, line in enumerate(f):
            coords = line.strip().split(",")
            point = Point(id=i, x=int(coords[0]), y=int(coords[1]), z=int(coords[2]), next=None)
            points.append(point)

    connections = 0
    last_circuits_connected = (None, None)
    # circuits = get_circuits(points)
    while len(get_circuits(points)) > 1:
        p1, p2 = find_nearest_unconnected_point(points)
        if p1.next is None:
            p1.next = []
        if p2.next is None:
            p2.next = []
        p1.next.append(p2)
        p2.next.append(p1)
        last_circuits_connected = (p1, p2)
        connections += 1
        circuits = get_circuits(points)
        print(f"Connected {p1} to {p2} on connection {connections}")

    answer = last_circuits_connected[0].x * last_circuits_connected[1].x
    print(f"Answer: {answer} from connecting {last_circuits_connected[0]} and {last_circuits_connected[1]}")


def run_2_2():
    points = []
    with open("testinput.txt") as f:
        for i, line in enumerate(f):
            coords = line.strip().split(",")
            point = Point(id=i, x=int(coords[0]), y=int(coords[1]), z=int(coords[2]), next=None)
            points.append(point)

    connections = 0
    distance_points = pair_points(points)
    all_points = []
    for dp in distance_points:
        all_points.extend([p[0] for p in dp.points])
        all_points.extend([p[1] for p in dp.points])
    last_connected = (None, None)
    while len(get_circuits(all_points)) > 1:
        distance_points, last_connected = pair_points(points)

        all_points = []
        for dp in distance_points:
            all_points.extend([p[0] for p in dp.points])
            all_points.extend([p[1] for p in dp.points])
        connections += 1
        print(f"Connection attempt {connections}")

    print(f"Last connected points: {last_connected}")
    
    print(f"Final connections made: {connections}")
    for point in distance_points:
        print(f"{point} connected to {point.next}")

if __name__ == "__main__":
    run_2()



    # circuits: list[list[Point]] = []
    # for p in points:
    #     circuits.append([p])

    # max_distance = 99999999
    # for point in points:
    #     for p2 in range(1, len(points)):
    #         distance = point.distance_from_point(points[p2])
    #         if distance < max_distance:
    #             print(f"New max distance found: {distance} between {point} and {points[p2]}")
    #             max_distance = distance
    #             circuits.append([point, points[p2]])