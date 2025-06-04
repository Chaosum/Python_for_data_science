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
    Main function to load data, process it, and plot life expectancy
    against income for a specific year.
    This function loads the income and life expectancy data,
    processes it to extract the relevant year, and then plots
    life expectancy against income on a logarithmic scale.
    The x-axis represents income (GDP per capita in PPP),
    and the y-axis represents life expectancy in years.
    The plot is displayed with the year as the title.
    """
    try:
        file_path = \
            'income_per_person_gdppercapita_ppp_inflation_adjusted.csv'
        income_data = load(file_path)
        file_path = 'life_expectancy_years.csv'
        life_expectancy_data = load(file_path)
        if income_data is None or life_expectancy_data is None:
            print("Failed to load data.")
            return
        year = 1900
        income_melted = income_data.melt(
            id_vars=["country"],
            var_name="Year",
            value_name="Income"
        )
        life_melted = life_expectancy_data.melt(
            id_vars=["country"],
            var_name="Year",
            value_name="Life Expectancy"
        )
        income_melted["Year"] = income_melted["Year"].apply(parse_number)
        income_melted["Year"] = income_melted["Year"].astype(int)
        life_melted["Year"] = life_melted["Year"].astype(int)

        income = income_melted[income_melted["Year"] == year]
        life = life_melted[life_melted["Year"] == year]
        if income.empty or life.empty:
            print(f"No data available for the year {year}.")
            return

        merged = income.merge(
                    life,
                    on=["country", "Year"]
        )
        x = merged['Income']
        y = merged['Life Expectancy']

        sorted_indices = x.argsort()
        # sort list with index prosition
        x = x.iloc[sorted_indices]
        y = y.iloc[sorted_indices]

        plt.figure(figsize=(10, 6))
        plt.scatter(x, y)
        plt.title(f"{year}")
        plt.ylabel("Life Expectancy")
        plt.xlabel("Gross domestic product")
        plt.xscale("log")
        plt.xticks([300, 1000, 10000])
        plt.gca().xaxis.set_major_formatter(FuncFormatter(millions_formatter))
        plt.show()
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    main()
