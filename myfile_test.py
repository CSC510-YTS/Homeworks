import pytest
from myfile import team_member

def test_success_cases():
     assert team_member("Tanuj")=="Tanuj's email is tskulkar@ncsu.edu"
     assert team_member("Shubham")=="Shubham's email is stidke@ncsu.edu"
     assert team_member("Yunfei")=="Yunfei's email is ychen267@ncsu.edu"

def test_failure_cases():
     assert team_member("Dr.Tim")=="I am Batman"


print(team_member("Tanuj"))
print(team_member("Shubham"))
print(team_member("Yunfei"))
print(team_member("Dijkstra"))

# team_members("WRONG METHOD NAME!")