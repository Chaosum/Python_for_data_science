import matplotlib.pyplot as plt
from load_csv import load


def main():
    """
    Main function to load life expectancy data
    and plot it for a specific country.
    """
    file_path = 'life_expectancy_years.csv'
    data = load(file_path)
    if data is None:
        print("Failed to load data.")
        return
    country = 'France'  # Example: Replace with your campus country
    country_data = data[data['country'] == country]  # mask boolean indexing

    if country_data.empty:
        print(f"No data found for {country}.")
        return

    # Extract years and life expectancy values
    melted = country_data.melt(
        id_vars=["country"],
        var_name="Year",
        value_name="Life Expectancy"
    )
    melted["Year"] = melted["Year"].astype(int)
    melted["Life Expectancy"] = melted["Life Expectancy"].astype(float)

    plt.figure(figsize=(10, 6))
    plt.plot(
        melted["Year"],
        melted["Life Expectancy"],
        label=country
    )
    plt.title(f"Life Expectancy in {country} Over the Years")
    plt.xlabel("Year")
    plt.ylabel("Life Expectancy")
    plt.show()


if __name__ == '__main__':
    main()
