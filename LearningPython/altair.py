from altair import Chart, load_dataset

# load data as a pandas DataFrame
cars = load_dataset('cars')

Chart(cars).mark_point().encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color='Origin',
)