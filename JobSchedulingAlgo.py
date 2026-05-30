def job_scheduling(jobs):
    # sort by profit descending
    jobs.sort(key=lambda x: x[2], reverse=True)

    max_deadline = max(job[1] for job in jobs)
    slots = [-1] * max_deadline  # time slots

    total_profit = 0

    for job in jobs:
        job_id, deadline, profit = job

        # try to place job in latest free slot
        for i in range(deadline - 1, -1, -1):
            if slots[i] == -1:
                slots[i] = job_id
                total_profit += profit
                break

    print("Selected Jobs:", [j for j in slots if j != -1])
    print("Total Profit:", total_profit)


# 🔹 Input
n = int(input("Enter number of jobs: "))
jobs = []

print("Enter job_id deadline profit:")
for _ in range(n):
    job_id, deadline, profit = input().split()
    jobs.append((job_id, int(deadline), int(profit)))

# 🔹 Run
job_scheduling(jobs)