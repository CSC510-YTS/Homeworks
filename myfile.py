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