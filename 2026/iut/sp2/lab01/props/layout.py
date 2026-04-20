from manim import *
import numpy as np
import math

class Layout:
    def __init__(self, n):
        if n < 1: raise ValueError("n must be positive!")
        self.n = n
    
    def get_positions(self):
        return self._validate(self.normalize(self._generate_positions()))
    
    def _generate_positions(self):
        raise NotImplementedError
    
    def _validate(self, positions):
        if len(positions) != self.n:
            raise ValueError(f"Layout must return exactly n={self.n} positions!")

        return positions
    
    @staticmethod
    def normalize(positions):
        ara = np.array(positions, dtype=float)

        x_max = np.max(ara[:, 0])
        y_max = np.max(ara[:, 1])
        z_max = np.max(ara[:, 2])
        x_min = np.min(ara[:, 0])
        y_min = np.min(ara[:, 1])
        z_min = np.min(ara[:, 2])

        center = np.array([x_max + x_min, y_max + y_min, z_max + z_min]) / 2
        ara -= center

        x_range = x_max - x_min
        y_range = y_max - y_min
        z_range = z_max - z_min
        max_range = max(x_range, y_range, z_range) / 2
        if max_range > 0: ara = ara / max_range

        return [pos for pos in ara]
    
    @staticmethod
    def min_gap(positions):
        ara = np.array(positions, dtype=float)
        n = len(ara)

        max_dist = math.sqrt(12)
        if n < 2: return max_dist

        min_dist = max_dist

        for i in range(n):
            for j in range(i + 1, n):
                dist = np.linalg.norm(ara[i] - ara[j])
                if dist < min_dist: min_dist = dist
        
        return min_dist
    
    @staticmethod
    def max_length(positions):
        ara = np.array(positions, dtype=float)
        return np.max(np.linalg.norm(ara, axis=1))

class GridLayout(Layout):
    def __init__(self, n, rows=None):
        super().__init__(n)
        self.rows = rows or int(math.floor(math.sqrt(n)))
    
    def _generate_positions(self):
        positions = []
        cols = int(math.ceil(self.n / self.rows))

        for i in range(self.n):
            r = i // cols
            c = i % cols
            positions.append(np.array([c, -r, 0]))

        return positions

class RadialLayout(Layout):
    def __init__(
        self,
        n,
        rings=1,
        ring_sizes=None,
        angle_offsets=None,
        use_center=True
    ):
        super().__init__(n)
        self.rings = rings
        self.use_center = use_center

        m = n - 1 if self.use_center else n

        if ring_sizes is None: self.ring_sizes = self._default_ring_sizes(m)
        else: self.ring_sizes = ring_sizes

        if len(self.ring_sizes) != rings:
            raise ValueError(f"The length of ring_sizes must be exactly rings={rings}!")
        if sum(self.ring_sizes) != m:
            raise ValueError(f"The sum of ring_sizes must be exactly m={m}!")
        
        if angle_offsets is None: self.angle_offsets = [0] * rings
        else: self.angle_offsets = angle_offsets

        if len(self.angle_offsets) != rings:
            raise ValueError(f"The length of angle_offsets must be exactly rings={rings}!")
        
    def _default_ring_sizes(self, m):
        r = self.rings
        k = math.ceil(2 * m / (r * (r + 1)))

        ring_sizes = [k * (i + 1) for i in range(r)]
        
        total = sum(ring_sizes)
        extra = total - m

        for i in range(r - 1, -1, -1):
            temp = min(extra, ring_sizes[i])

            ring_sizes[i] -= temp
            extra -= temp

            if extra == 0: break
        
        return ring_sizes
    
    def _generate_positions(self):
        positions = []

        if self.use_center:
            positions.append(np.zeros(3))
        
        for i, (count, offset) in enumerate(zip(self.ring_sizes, self.angle_offsets)):
            if count == 0: continue
            
            radius = i + 1
            angles = np.linspace(0, TAU, count, endpoint=False) + offset

            ring = radius * np.stack(
                [np.cos(angles), np.sin(angles), np.zeros(count)],
                axis=1
            )

            positions.extend(ring)
        
        return positions

class TriangularLayout(Layout):
    def _generate_positions(self):
        positions = []

        i = 0
        remaining = self.n

        while remaining > 0:
            count = min(i + 1, remaining)
            remaining -= count

            x = np.linspace(-i, i, count) if count > 1 else np.zeros(1)
            y = -2 * i * np.ones(count)
            z = np.zeros(count)

            row = np.stack([x, y, z], axis=1)
            positions.extend(row)

            i += 1
        
        return positions