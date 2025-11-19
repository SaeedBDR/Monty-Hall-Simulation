"""
Streamlit UI for Monty Hall simulation.

This module provides a minimal user interface to visualize
the running win rate of switching vs. not switching in
the Monty Hall problem.
"""

import streamlit as st
from main import simulate_monty_hall


def main() -> None:
    """
    Render the Monty Hall simulation dashboard using Streamlit.

    Allows the user to specify the number of simulations and
    displays two live-updating line charts:
    - Win rate without switching
    - Win rate with switching
    """
    st.title("Monty Hall Simulation")

    num_of_simulations = int(
        st.number_input(
            "Enter the number of simulations:",
            min_value=100,
            max_value=10000,
            value=100,
            step=100
        )
    )

    col1, col2 = st.columns(2)

    col1.subheader("Win rate WITHOUT switching")
    chart_without = col1.line_chart(height=400)

    col2.subheader("Win rate WITH switching")
    chart_with = col2.line_chart(height=400)

    wins_without = 0
    wins_with = 0

    for i in range(num_of_simulations):
        win_without, win_with = simulate_monty_hall(1)

        wins_without += win_without
        wins_with += win_with

        avg_without = wins_without / (i + 1)
        avg_with = wins_with / (i + 1)

        chart_without.add_rows([[avg_without]])
        chart_with.add_rows([[avg_with]])


if __name__ == "__main__":
    main()
