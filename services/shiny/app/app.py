import matplotlib.pyplot as plt
from shiny import render, ui
from .data import get_data


def get_app_ui():
    app_ui = ui.page_fluid(  # Layout the UI with Layout Functions

        #  Add Inputs with ui.input_*() functions
        ui.input_slider(
            "n", "Number of coordinates", 1, 100, 20
        ),
        # Add Outputs with ui.ouput_*() functions
        ui.output_plot("map_with_coords")
    )
    return app_ui


def server(input, output, session):
    # For each output, define a function that generates the output
    @output  # Designate output functions with the @output decorator
    @render.plot  # Specify the type of output with a @render. decorator
    def map_with_coords():  # Use the output id as the function name
        # Call the values of UI inputs with input.<id>()
        return get_map_with_coords(input.n())


def get_map_with_coords(n_coords: int):
    df = get_data(n_results=n_coords)
    fig, ax = plt.subplots()
    plt.scatter(df["lon"], df["lat"])
    plt.xlim([-180, 180])
    plt.ylim([-90, 90])
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    return ax
