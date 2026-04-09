import pandas as pd

last_two_digit_of_student_id = 24

input_rpm = 1800 + last_two_digit_of_student_id
output_rpm = 180
target_ratio = input_rpm / output_rpm

min_teeth = 13
max_teeth = 85
max_mesh_ratio = 3.0
tolerance = 0.01

def solve_gear_train():
    solutions = []
    
    for t1 in range(min_teeth, max_teeth + 1):
        for t2 in range(min_teeth, max_teeth + 1):
            r1 = t2 / t1
            if r1 > max_mesh_ratio or t1 == t2: continue
            
            for t3 in range(min_teeth, max_teeth + 1):
                for t4 in range(min_teeth, max_teeth + 1):
                    for t5 in range(min_teeth, max_teeth + 1):
                        for t6 in range(min_teeth, max_teeth + 1):
                            used = {t1, t2, t3, t4, t5, t6}
                            if len(used) < 6: continue
                            
                            r2 = t4 / t3
                            r3 = t6 / t5
                            if r2 > max_mesh_ratio or r3 > max_mesh_ratio: continue
                            
                            calc_ratio = r1 * r2 * r3
                            if abs(calc_ratio - target_ratio) < tolerance:
                                solutions.append([t1, t2, t3, t4, t5, t6, round(calc_ratio, 4)])
                                if len(solutions) >= 10:
                                    return solutions
    return solutions

columns = ['T1 (In)', 'T2', 'T3', 'T4', 'T5', 'T6 (Out)', 'Calculated Ratio']
results = solve_gear_train()
df = pd.DataFrame(results, columns=columns)

print("\nTop 10 Candidate Gear Combinations:")
print(df.to_string(index=False))