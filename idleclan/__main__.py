import json

with open('config.json') as f:
    config = json.load(f)

print(config['jobs'])
for jobs in config['jobs']:
    print(jobs)
    for job in config['jobs'][jobs]:
        with open(f"{jobs}/{job}.json", 'w') as files:
            files.write('{}')