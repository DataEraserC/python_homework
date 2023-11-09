import random

def estimate_pi(num_points):
    inside_circle = 0
    for _ in range(num_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        distance = x**2 + y**2
        if distance <= 1:
            inside_circle += 1
    return 4 * (inside_circle / num_points)

num_points = 1000000  # 可根据需要调整生成的随机点数量
pi_estimate = estimate_pi(num_points)
print(f"Estimated value of pi: {pi_estimate}")
