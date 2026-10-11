for s in 2021 2022 2023 2024 2025 2026; do for w in $(seq 1 18); do
 for k in projections stats; do f=$k-$s-$w.json; [ -s $f ] || curl -s "https://api.sleeper.app/$k/nfl/$s/$w?season_type=regular&position[]=QB&position[]=RB&position[]=WR&position[]=TE" -o $f & done; done; wait; done
curl -sL https://github.com/nflverse/nfldata/raw/master/data/games.csv -o games.csv
curl -s https://api.sleeper.app/v1/players/nfl -o players.json
for s in 2021 2022 2023 2024 2025 2026; do curl -sL https://github.com/nflverse/nflverse-data/releases/download/injuries/injuries_$s.csv -o inj_$s.csv; done
