import json

team_file = open('csv_file.txt', 'r')
team_array = [line.strip() for line in team_file.readlines()]
team_file.close()

parsed_team_array = [
    {
        "club": team.split(',')[0],
        "country": team.split(',')[2],
        "city": team.split(',')[1]
    }
    for team in team_array
]

print(parsed_team_array)

json_output = open('json_file.json', 'w')
json.dump(parsed_team_array, json_output, indent=2)
json_output.close()
