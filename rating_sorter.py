students = []
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        student = {
            "name": row["name"],
            "score": int(row["score"])
        }
        students.append(student)
students.sort(key=lambda x: x["score"], reverse=True)

with open("rating.csv", "w", newline="") as file:
    fieldnames = ["rank", "name", "score"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()

    rank = 1
    for student in students:
        writer.writerow({
            "rank": rank,
            "name": student["name"],
            "score": student["score"]
        })
        rank += 1
