# Monty-Hall-Simulation
An interactive Monty Hall problem simulator implemented in Python with a Streamlit dashboard, allowing users to visualize and compare win rates for switching versus staying with the initial choice.
This project provides a simple and clear implementation of the Monty Hall problem, along with an interactive Streamlit dashboard to visualize win rates for the two strategies:

- **Staying with the initial choice**
- **Switching after the host opens a goat door**

The simulation demonstrates the classic counter-intuitive result:  
**Switching doors yields a significantly higher chance of winning the car.**

---

## 📂 Project Structure

├── main.py                     # Core Monty Hall simulation logic
├── app.py                      # Streamlit UI
└── README.md                   # Project documentation


## Features
- Clean and correct implementation of the Monty Hall problem
- Real-time chart updates of win rates using Streamlit
- Fully type-annotated code with detailed docstrings
- Adjustable number of simulation runs (100 to 10,000)
- Side-by-side comparison of switching vs not switching


## How It Works
For each simulation:
1. Three doors are created: two goats, one car.
2. The player selects a random door.
3. The host opens one of the remaining doors that contains a goat.
4. Depending on the strategy:
   - Stay → player keeps the original door.
   - Switch → player switches to the only remaining closed door.
5. The program records whether the player won the car.
This process repeats for as many trials as the user requests.


## Running the Simulation (CLI)
If you only want to run the simulation in the terminal:
```
python main.py
```

## Running the Streamlit Dashboard
To launch the interactive UI:
```
streamlit run app.py
```
This will open a browser window showing:
- A numeric input for the number of simulations
- Two real-time line charts:
  - Win rate without switching
  - Win rate with switching


  ## Expected Results
With large numbers of simulations, you should observe:
- ~33% win rate if you do not switch  
- ~66% win rate if you do switch  
This matches the mathematically proven solution to the Monty Hall problem.

## Requirements
Install dependencies using pip:
```
pip install streamlit
```
(No additional external libraries are required.)


## License
This project is released under the MIT License.

## Contributions
Pull requests and improvements are welcome, as long as they preserve the clarity and educational value of the project.


