# Define a Job class
class Job:
    def __init__(self, id, deadline, profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit

def job_sequencing(jobs):
    # Sort jobs by decreasing order of profit
    jobs.sort(key=lambda x: x.profit, reverse=True)

    n = max(job.deadline for job in jobs)
    result = [None] * n  # Time slots
    slot_taken = [False] * n

    for job in jobs:
        # Find a free slot before or on the job's deadline
        for i in range(min(n, job.deadline) - 1, -1, -1):
            if not slot_taken[i]:
                result[i] = job.id
                slot_taken[i] = True
                break

    # Remove None slots and return scheduled job IDs
    return [job_id for job_id in result if job_id]

# Example usage
jobs = [
    Job('a', 2, 100),
    Job('b', 1, 19),
    Job('c', 2, 27),
    Job('d', 1, 25),
    Job('e', 3, 15)
]

scheduled_jobs = job_sequencing(jobs)
print("Scheduled jobs to maximize profit:", scheduled_jobs)
