import os
import random
import datetime

# Configuration
start_date = datetime.date(2023, 1, 1)  # Start date for commits
end_date = datetime.date(2024, 6, 30)  # End date for commits
repo_path = r"C:\Users\conta\booster2"  # Path to your new repo
commit_message = r"Automated commit"
author_name = r"Haadesx"
author_email = r"contactvaresh@gmail.com"

def generate_commit(date, commit_time):
    with open(os.path.join(repo_path, "README.md"), "a") as file:
        file.write(f"Commit for {date} at {commit_time}\n")
    
    os.system(f'cd {repo_path} && git add README.md')
    os.system(f'cd {repo_path} && git commit --date="{date} {commit_time}" -m "{commit_message}" --author="{author_name} <{author_email}>"')

def get_random_commit_days(start_date, end_date):
    current_date = start_date
    total_commits = 0
    max_commits = 600
    days_per_week = random.randint(2, 3)
    max_commits_per_week = (max_commits // (days_per_week * 52)) + 1  # Max commits per week to stay under 600

    while current_date <= end_date and total_commits < max_commits:
        week_days = random.sample(range(7), days_per_week)  # Randomly select 2 or 3 days in the week
        total_commits_this_week = 0

        for day in week_days:
            commit_date = current_date + datetime.timedelta(days=day)
            if commit_date > end_date or total_commits >= max_commits:
                break

            remaining_commits = max_commits - total_commits
            commit_count = min(random.randint(1, 3), remaining_commits, max_commits_per_week)
            total_commits_this_week += commit_count
            total_commits += commit_count

            for _ in range(commit_count):
                commit_hour = random.randint(8, 22)  # Commit during typical working hours
                commit_minute = random.randint(0, 59)
                commit_second = random.randint(0, 59)
                commit_time = f"{commit_hour:02d}:{commit_minute:02d}:{commit_second:02d}"
                generate_commit(commit_date, commit_time)

            if total_commits >= max_commits:
                break

        current_date += datetime.timedelta(days=7)  # Move to the next week

get_random_commit_days(start_date, end_date)
