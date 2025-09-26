from fastapi import FastAPI
from typing import List, Dict
import uvicorn

app = FastAPI()

# Dummy tennis player data
tennis_players = [
	{"id": 1, "name": "Novak Djokovic", "country": "Serbia", "ranking": 1},
	{"id": 2, "name": "Carlos Alcaraz", "country": "Spain", "ranking": 2},
	{"id": 3, "name": "Jannik Sinner", "country": "Italy", "ranking": 3},
	{"id": 4, "name": "Daniil Medvedev", "country": "Russia", "ranking": 4},
	{"id": 5, "name": "Stefanos Tsitsipas", "country": "Greece", "ranking": 5},
	{"id": 6, "name": "Andrey Rublev", "country": "Russia", "ranking": 6},
	{"id": 7, "name": "Alexander Zverev", "country": "Germany", "ranking": 7},
	{"id": 8, "name": "Holger Rune", "country": "Denmark", "ranking": 8},
	{"id": 9, "name": "Hubert Hurkacz", "country": "Poland", "ranking": 9},
	{"id": 10, "name": "Roger Federer", "country": "Switzerland", "ranking": 10},
]

@app.get("/players", response_model=List[Dict])
def get_players():
	"""Return all tennis players."""
	return tennis_players

@app.get("/players/{player_id}", response_model=Dict)
def get_player(player_id: int):
	"""Return a single tennis player by ID."""
	for player in tennis_players:
		if player["id"] == player_id:
			return player
	return {"error": "Player not found"}

@app.get("/top-player", response_model=Dict)
def get_top_player():
	"""Return the top ranked tennis player."""
	top_player = min(tennis_players, key=lambda p: p["ranking"])
	return top_player

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000)