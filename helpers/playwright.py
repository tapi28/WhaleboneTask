from typing import List, Dict, Union


def scrape_players_roster(page) -> List[Dict[str, Union[str, int]]]:
    # Roster is divided into three tables: Forwards, Defensemen, and Goalies
    roster_types = [
        {
            "selector": "#root > div.sc-giInvV.jbthWE > div > div > div:nth-child(2) > div > div > table",
            "type": "Forward",
        },
        {
            "selector": "#root > div.sc-giInvV.jbthWE > div > div > div:nth-child(3) > div > div > table",
            "type": "Defensemen",
        },
        {
            "selector": "#root > div.sc-giInvV.jbthWE > div > div > div:nth-child(4) > div > div > table",
            "type": "Goalie",
        },
    ]

    full_roster = []

    for roster_type in roster_types:
        # Wait for the roster table to be loaded
        page.wait_for_selector(roster_type["selector"])

        # Scrape the roster for this type of player
        roster = page.evaluate(
            f"""(selector) => {{
                const rosterTable = document.querySelector(selector);
                const rows = Array.from(rosterTable.querySelectorAll('tr'));
                const players = [];
                for (const row of rows.slice(1)) {{
                    const columns = row.querySelectorAll('td');
                    const name = columns[0].textContent.trim();
                    const number = columns[1].textContent.trim();
                    const position = columns[2].textContent.trim();
                    const shoot = columns[3].textContent.trim();
                    const height = columns[4].textContent.trim();
                    const weight = columns[5].textContent.trim();
                    const born = columns[6].textContent.trim();
                    const birthplace = columns[7].textContent.trim();
                    players.push({{name, number, position, shoot, height, weight, born, birthplace}});
                }}
                return players;
            }}""",
            roster_type["selector"],
        )
        full_roster.extend(roster)
    return full_roster
