"""Synthetic conversation-card projection. No storage, messaging or API access."""


def cards(films, recommendations):
    return [{"recommendation": r["id"], "person": r["person"],
             "title": films[r["film"]]["title"]}
            for r in recommendations
            if r.get("state") == "open"
            and films.get(r["film"], {}).get("watched") is True
            and r.get("confirmed_recommender") is True
            and r.get("offer_conversation") is True]
