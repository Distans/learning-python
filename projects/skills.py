#!/data/data/com.termux/files/usr/bin/python3

skills = {'Python', 'HTML', 'SQL', 'C++', 'Java', 'Scala'}
job_skills = {'HTML', 'CSS', 'JS', 'C#', 'NodeJS'}
match = skills & job_skills
print(''.join(match))

