# US States Game: Python Dictionary vs. Pandas DataFrame Approaches

This repository hosts two Python implementations (`solution_1` and `solution_2`) of the US States Game, an interactive educational application designed to help users learn US states in an engaging way. Both versions employ similar functionalities with a subtle difference in the data structure and initial presentation.

## Table of Contents
- [General Information](#general-information)
- [Similarities](#similarities)
- [Differences](#differences)
- [Advantages and Disadvantages](#advantages-and-disadvantages)
  - [`solution_1`](#solution_1)
  - [`solution_2`](#solution_2)
  
## General Information
The US States Game is a Python-based interactive application that leverages the turtle library for GUI and pandas library for data handling in `solution_2`. The game challenges users to name all the US states, displaying correctly guessed states on a map.

## Similarities
- **Core Functionality**: Both solutions fulfill the same primary objective of the game, which involves guessing and visualizing US states.
- **Libraries**: Usage of `turtle` for GUI components.
- **Progress Tracking**: Both `solution_1` and `solution_2` track the user's learning progress and save it to a specified path.
- **User Interaction**: Both solutions employ similar mechanisms for user input and feedback.

## Differences
- **Data Handling**:
  - `solution_1`: Uses a Python dictionary to handle and process game data.
  - `solution_2`: Utilizes a Pandas DataFrame for data handling, offering robust data manipulation capabilities.
- **Initial Presentation**:
  - `solution_1`: Features an initial text title, potentially providing a more guided start.
  - `solution_2`: Directly starts the game without an initial text title.

## Advantages and Disadvantages

### `solution_1`
- **Advantages**:
  - Simplicity and potentially faster performance due to native Python data structures.
  - Initial text title may provide a clearer introduction to the game.
- **Disadvantages**:
  - Limited data manipulation capabilities compared to Pandas.
  - May not scale as well with larger or more complex datasets.

### `solution_2`
- **Advantages**:
  - Robust data manipulation and analysis capabilities with Pandas.
  - May handle larger datasets and more complex operations more efficiently.
- **Disadvantages**:
  - Slightly more overhead and potentially slower performance for small datasets due to the use of Pandas.
  - Lack of an initial text title might make the game start less guided.
