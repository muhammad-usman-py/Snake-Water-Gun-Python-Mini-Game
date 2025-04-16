# 🐍 Snake Water Gun Game (Python)

A fun little terminal-based Snake-Water-Gun game built using Python.  
Inspired by the classic game like Rock-Paper-Scissors, but with a twist!

---

## 🎮 Game Rules

- **S** for Snake  
- **W** for Water  
- **G** for Gun

> 🐍 Snake drinks Water  
> 💧 Water douses Gun  
> 🔫 Gun shoots Snake

|              | Snake (S) | Water (W) | Gun (G) |
|--------------|------------|-----------|---------|
| **Snake (S)**| Tie        | Win       | Lose    |
| **Water (W)**| Lose       | Tie       | Win     |
| **Gun (G)**  | Win        | Lose      | Tie     |

---

## 💻 How It Works

- The **user** inputs a choice (S, W, or G).
- The **computer** randomly selects its own.
- The result is displayed — You Win, Lose, or Tie.
- Game asks if you want to play again.

---

## 🧠 Technologies Used

- Python 3
- `random` module for computer choice
- Loop and conditionals for game logic

---

## ▶️ How to Run

1. Clone the repository or copy the code.
2. Make sure you have Python 3 installed.
3. Run the script:

```bash
python snake_water_gun.py
