import os
from datetime import datetime

def make_commits(num_commits: int):
    current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    for i in range(num_commits):
        with open('data.txt', 'a') as file:
            file.write(f'Commit {i + 1} on {current_date}\n')

        os.system('git add data.txt')
        os.system(f'git commit --date="{current_date}" -m "Commit {i + 1}"')

    os.system('git push')

make_commits(15)