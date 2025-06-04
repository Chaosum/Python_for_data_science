import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from load_csv import load


def parse_number(val: str) -> float:
    """
    Parse a string representing a number with optional suffixes
    like 'M' for million, 'k' for thousand, or '%' for percentage.
    Args:
        val (str): The string to parse.
    Returns:
        float: The parsed number.
    """
    if val is None or not isinstance(val, str):
        raise ValueError(f"Unsupported type for parsing: {type(val)}")
    if isinstance(val, str):
        val = val.strip().replace(',', '')  # just in case
        if val.endswith('M'):
            return float(val[:-1]) * 1_000_000
        elif val.endswith('k'):
            return float(val[:-1]) * 1_000
        elif val.endswith('%'):
            return float(val[:-1])
        else:
            return float(val)
    return float(val)


def millions_formatter(x, pos):
    """
    Format the y-axis labels to show millions or thousands.
    Args:
        x (float): The value to format.
        pos (int): The tick position.
    Returns:
        str: The formatted string.
    """
    if x >= 1_000_000:
        return f'{x / 1_000_000:.1f}M'
    elif x >= 1_000:
        return f'{x / 1_000:.0f}K'
    else:
        return f'{x:.0f}'


def main():
    """
    Main function to load Population data
    and plot it for a specific country.
    """
    try:
        file_path = 'population_total.csv'
        data = load(file_path)
        if data is None:
            print("Failed to load data.")
            return

        first_country = 'Belgium'
        second_country = 'France'
        first_country_data = data[data['country'] == first_country]
        second_country_data = data[data['country'] == second_country]

        if first_country_data.empty:
            print(f"No data found for {first_country}.")
            return
        if first_country_data.empty:
            print(f"No data found for {second_country}.")
            return

        # Extract years and Population values
        first_melted = first_country_data.melt(
            id_vars=["country"],
            var_name="Year",
            value_name="Population"
        )
        try:
            first_melted["Population"] = \
                first_melted["Population"].apply(parse_number)
        except ValueError as e:
            print(f"Error parsing 'Population' column: {e}")
            return
        first_melted["Year"] = first_melted["Year"].astype(int)
        first_melted = \
            first_melted[first_melted["Year"].between(1800, 2050)]
        first_melted["Population"] = first_melted["Population"].astype(float)
        second_melted = second_country_data.melt(
            id_vars=["country"],
            var_name="Year",
            value_name="Population"
        )
        try:
            second_melted["Population"] = \
                second_melted["Population"].apply(parse_number)
        except ValueError as e:
            print(f"Error parsing 'Population' column: {e}")
            return
        second_melted["Year"] = second_melted["Year"].astype(int)
        second_melted = \
            second_melted[second_melted["Year"].between(1800, 2050)]
        second_melted["Population"] = second_melted["Population"].astype(float)

        plt.figure(figsize=(10, 6))
        plt.plot(
            first_melted["Year"],
            first_melted["Population"],
            label=first_country
        )
        plt.plot(
            second_melted["Year"],
            second_melted["Population"],
            label=second_country
        )
        plt.title("Population Projections")
        plt.xlabel("Year")
        plt.ylabel("Population")

        formatter = FuncFormatter(millions_formatter)
        plt.gca().yaxis.set_major_formatter(formatter)
        plt.legend()
        plt.show()
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    main()
