# exercise 1
LIMIT = 5
distances = []
total = 0

for number in range(LIMIT):
    distance_travelled = float(input("Enter distance travelled:"))
    distances.append(distance_travelled)
    total += distance_travelled
print("-------------------------------------------------------")
# average
average = total / len(distances)
print("Average:", average, "km.")

# longest and shortest distance
max_distance = max(distances)
min_distance = min(distances)

print("Longest distance", max_distance, "km.")
print("Shortest distance", min_distance, "km.")
print("-------------------------------------------------------")

# exercise 2
numbers = []
for _ in range(5):
    number = int(input("Enter a number:"))
    numbers.append(number)

# Increment each number by 1
incremented_numbers = [num + 1 for num in numbers]

print("Original list:", numbers)
print("List after incrementing each number by 1:", incremented_numbers)
print("-------------------------------------------------------")

# exercise 3
num_trainees = int(input("Number of trainees:"))
trainee_results = []

for trainee in range(4000, 4000 + num_trainees):
    results = [float(input(f"Result for exam {exam} for trainee {trainee}: ")) for exam in range(1, 4)]
    average_result = round(sum(results) / len(results), 2)
    trainee_results.append((trainee, average_result))

average_all_trainees = round(sum(result[1] for result in trainee_results) / len(trainee_results), 2)
max_average = max(trainee_results)
min_average = min(trainee_results)
below_50_count = sum(1 for result in trainee_results if result[1] < 50)
print("-------------------------------------------------------")
# trainee results
print("\nTrainee Results:")
for trainee, avg_result in trainee_results:
    print(f"Trainee {trainee}: Average Result - {avg_result}")
print(f"\nAverage result: {average_all_trainees}")
print(f"Maximum average: Trainee {max_average[0]} with {max_average[1]}")
print(f"Minimum average: Trainee {min_average[0]} with {min_average[1]}")
print(f"Number of low average results: {below_50_count}")


