from typing import List, Dict, Any

from helpers import playwright


def test_count_of_teams_is_32(nhl_teams: List[Dict[str, Any]]) -> None:
    assert len(nhl_teams) == 32, "Expected 32 teams in the response."


def test_oldest_team_is_canadiens(nhl_teams: List[Dict[str, Any]]) -> None:
    oldest_team = min(nhl_teams, key=lambda x: x["firstYearOfPlay"])
    assert (
        oldest_team["name"] == "Montreal Canadiens"
    ), "Expected Montreal Canadiens to be the oldest team"


def test_city_with_more_than_one_team(nhl_teams: List[Dict[str, Any]]) -> None:
    cities = [team["location"] for team in nhl_teams]
    city_counts = {city: cities.count(city) for city in set(cities)}

    # Collect dict containing cities with more than one team and their counts
    multi_team_cities = {
        city: count for city, count in city_counts.items() if count > 1
    }
    assert multi_team_cities, "No cities with more than one team found"

    # Collect names of teams in cities with more than one team
    teams_in_city = []
    for city, count in multi_team_cities.items():
        teams_in_city = [team["name"] for team in nhl_teams if team["location"] == city]

    expected_team_names = {"New York Islanders", "New York Rangers"}

    assert expected_team_names == set(
        teams_in_city
    ), f"I found these teams {teams_in_city}, but these were expected {expected_team_names}."


def test_there_are_eight_teams_in_the_metropolitan_division(
    nhl_teams: List[Dict[str, Any]]
) -> None:
    metropolitan_teams = [
        team for team in nhl_teams if team["division"]["name"] == "Metropolitan"
    ]
    assert (
        len(metropolitan_teams) == 8
    ), "Expected 8 teams in the Metropolitan division."

    expected_team_names = [
        "Carolina Hurricanes",
        "Columbus Blue Jackets",
        "New Jersey Devils",
        "New York Islanders",
        "New York Rangers",
        "Philadelphia Flyers",
        "Pittsburgh Penguins",
        "Washington Capitals",
    ]

    for team in metropolitan_teams:
        assert (
            team["name"] in expected_team_names
        ), f"Unexpected team in Metropolitan division: {team['name']}"


def test_montreal_canadiens_have_more_canadian_players_than_players_from_usa(
    browser,
) -> None:
    page = browser.new_page()
    page.goto("https://www.nhl.com/canadiens/roster")
    full_roster = playwright.scrape_players_roster(page)

    # Count the number of Canadian and American players
    canadian_players = sum(1 for player in full_roster if "CAN" in player["birthplace"])
    american_players = sum(1 for player in full_roster if "USA" in player["birthplace"])

    # Assert that there are more Canadian players than American players
    assert (
        canadian_players > american_players
    ), "There are NOT more Canadian players than American players in the roster!"
