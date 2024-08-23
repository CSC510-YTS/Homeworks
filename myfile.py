team_members = {
    "Tanuj" : "tskulkar@ncsu.edu",
    "Shubham" : "stidke@ncsu.edu",
    "Yunfei" : "ychen267@ncsu.edu"
}

def team_member(name):
    if name in team_members:
        return f"{name}'s email is {team_members[name]}"
    else:
        return "This individual is not in our team"

print(team_member("Tanuj"))
print(team_member("Shubham"))
print(team_member("Yunfei"))
print(team_member("Dijkstra"))

team_members("WRONG METHOD NAME!")