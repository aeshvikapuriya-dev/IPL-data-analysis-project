import pandas as pd

def load_data():
    matches = pd.read_csv("data/matches.csv")
    deliveries = pd.read_csv("data/deliveries.csv")
    return matches, deliveries


def top_batsmen(deliveries):
    return deliveries.groupby('batter')['batsman_runs'] \
        .sum().sort_values(ascending=False).head(10)


def top_bowlers(deliveries):
    wickets = deliveries[deliveries['dismissal_kind'] != "run out"]
    return wickets.groupby('bowler')['player_dismissed'] \
        .count().sort_values(ascending=False).head(10)


def win_percentage(matches):
    played = pd.concat([matches['team1'], matches['team2']]).value_counts()
    won = matches['winner'].value_counts()
    return (won / played * 100).sort_values(ascending=False)


def toss_impact(matches):
    toss_win_match = matches[matches['toss_winner'] == matches['winner']]
    return round(len(toss_win_match) / len(matches) * 100, 2)