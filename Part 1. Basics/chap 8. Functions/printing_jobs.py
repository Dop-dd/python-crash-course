
def jobs_todo(uncompleted_jobs, completed_jobs):

    while uncompleted_jobs:
        current_job = uncompleted_jobs.pop()
        print(f"current job being done: {current_job}")
        completed_jobs.append(current_job)

def show_jobs_done(completed_jobs):

    print("\nAll jobs done so far: ")
    for completed_job in completed_jobs:
        print(completed_job)

uncompleted_jobs = ['kortrijk', 'menen', 'beveren', 'gent']
completed_jobs = []

jobs_todo(uncompleted_jobs[:], completed_jobs)
show_jobs_done(completed_jobs)
