import sys
import data
import build_data
import county_demographics
from data import CountyDemographics

fd = build_data.get_data()


# part 1: Calculate the total population of a list of counties
def population_total(counties: list[CountyDemographics]) -> int:
    total = 0
    for county in counties:
        total += county.population.get("2014 Population", 0)
    return total


# part 2: Filter counties by a specified state
def filter_by_state(counties: list[CountyDemographics], state: str) -> list[CountyDemographics]:
    returning_list = []
    for county in counties:
        if county.state == state:
            returning_list.append(county)
    return returning_list


# part 3: Calculate the number of people with a specific education level across counties
def population_by_education(counties: list[CountyDemographics], education_level: str) -> float:
    total = 0
    for county in counties:
        population = county.population.get('2014 Population', 0)
        if education_level in county.education:
            percent = county.education[education_level]
            sub_population = population * (percent / 100)
            total += sub_population
    return total


# Calculate the number of people of a specific ethnicity across counties
def population_by_ethnicity(counties: list[CountyDemographics], ethnicity: str) -> float:
    total_population = 0.0
    for county in counties:
        if ethnicity in county.ethnicities:
            population = county.population.get('2014 Population', 0)
            percentage = county.ethnicities[ethnicity]
            sub_population = population * (percentage / 100)
            total_population += sub_population
    return total_population


# Calculate the number of people below the poverty level across counties
def population_below_poverty_level(counties: list[CountyDemographics]) -> float:
    total = 0
    for county in counties:
        if "Persons Below Poverty Level" in county.income:
            poverty_percentage = county.income["Persons Below Poverty Level"]
            population = county.population.get("2014 Population", 0)
            total += (population * poverty_percentage) / 100
    return total


# part 4: Calculate the percentage of a sub-population with a specific education level across counties
def percent_by_education(counties: list[CountyDemographics], education_level: str) -> float:
    total_population = 0
    total_education_population = 0
    for county in counties:
        if education_level in county.education:
            total_population += county.population['2014 Population']
            total_education_population += (
                    county.population['2014 Population'] * county.education[education_level] / 100)

    if total_population == 0:
        return 0

    education_percentage = (total_education_population / total_population) * 100
    return education_percentage


# Calculate the percentage of a sub-population by ethnicity across counties
def percent_by_ethnicity(counties: list[CountyDemographics], ethnicity: str) -> float:
    total_population = 0
    total_ethnic_population = 0
    for county in counties:
        if ethnicity in county.ethnicities:
            total_population += county.population['2014 Population']
            total_ethnic_population += (
                    county.population['2014 Population'] * county.ethnicities[ethnicity] / 100)

    if total_population == 0:
        return 0

    ethnic_percentage = (total_ethnic_population / total_population) * 100
    return ethnic_percentage


# Calculate the percentage of the total population below the poverty level across counties
def percent_below_poverty_level(counties: list[CountyDemographics]) -> float:
    total_population = 0
    total_below_poverty_population = 0

    for county in counties:
        total_population += county.population['2014 Population']
        total_below_poverty_population += (
                county.population['2014 Population'] * county.income['Persons Below Poverty Level'] / 100)

    if total_population == 0:
        return 0

    poverty_percentage = (total_below_poverty_population / total_population) * 100
    return poverty_percentage

# the purpose of this function is to filter and return all counties where the specified ethnicity key is greater than the threshold
# input is a list of CountyDemographics objects that represent different counties and their demographics data
# input 2 is a string representing the ethnicity key of interest (e.g., 'Hispanic or Latino')
# input 3 is a float representing the threshold value for comparison
# output is a list of CountyDemographics objects where the specified ethnicity level is greater than the threshold

def education_less_than(counties: list[CountyDemographics], education_key: str, threshold: float) -> list[
    CountyDemographics]:

    result = []

    for county in counties:
        if county.education.get(education_key, 0) < threshold:
            result.append(county)

    return result

# the purpose of this function is to filter and return all counties where the specified education key is greater than the threshold
# input is a list of CountyDemographics objects that represent different counties and their demographics data
# input 2 is a string representing the education key of interest (e.g., "Bachelor's Degree or Higher")
# input 3 is a float representing the threshold value for comparison
# output is a list of CountyDemographics objects where the specified education level is greater than the threshold

def education_greater_than(counties: list[CountyDemographics], education_key: str, threshold: float) -> list[
    CountyDemographics]:
    result = []
    for county in counties:
        if education_key in county.education and county.education[education_key] > threshold:
            result.append(county)
    return result




# part 5: Various filtering functions remain unchanged

def main():
    file = "inputs/" + sys.argv[1]

    try:
        with open(file, 'r') as infile:
            print(file)
            print("Records:", len(fd))
            cali_data = filter_by_state(fd, "CA")

            for line in infile:
                if line.strip() == "filter-gt:Education.Bachelor's Degree or Higher:60":
                    print("Bachelor's Degree or Higher: ",
                          education_greater_than(fd, "Bachelor's Degree or Higher", 60))

                elif line.strip() == "filter-state:CA\npopulation-total":
                    print("For 2014 ...")
                    print("Population in 2014: ", population_total(filter_by_state(fd, "CA")))
                    print("Education.Bachelor's Degree or Higher: ",
                          percent_by_education(cali_data, "Bachelor's Degree or Higher"))
                    print("Education.High School or Higher percent: ", percent_by_education(cali_data, "High School"))
                    print("Ethnicities.American Indian and Alaska Native Alone percent: ",
                          percent_by_ethnicity(cali_data, "American Indian and Alaska Native Alone"))
                    print("Ethnicities.Asian Alone percent: ", percent_by_ethnicity(cali_data, "Asian Alone"))
                    print("Ethnicities.Black Alone percent: ", percent_by_ethnicity(cali_data, "Black Alone"))
                    print("Ethnicities.Hispanic or Latino percent: ",
                          percent_by_ethnicity(cali_data, "Hispanic or Latino"))
                    print("Ethnicities.Native Hawaiian and Other Pacific Islander Alone percent: ",
                          percent_by_ethnicity(cali_data, "Native Hawaiian and Other Pacific Islander Alone"))
                    print("Ethnicities.Two or More Races percent: ",
                          percent_by_ethnicity(cali_data, "Two or More Races"))
                    print("Ethnicities.White Alone percent: ", percent_by_ethnicity(cali_data, "White Alone"))
                    print("Ethnicities.White Alone, not Hispanic or Latino percent: ",
                          percent_by_ethnicity(cali_data, "White Alone, not Hispanic or Latino"))
                    print("Income.Persons Below Poverty Level percent: ", percent_below_poverty_level(cali_data))

                elif line.strip() == "filter-lt:Education.High School or Higher:60":
                    print("High School or Higher: ", education_less_than(fd, "High School", 60))

                elif line.strip() == "filter-state:CA":
                    print(cali_data)

                elif line.strip() == "percent:Education.Bachelor's Degree or Higher":
                    print("For 2014 ...")
                    print("Education.Bachelor's Degree or Higher: ",
                          percent_by_education(fd, "Bachelor's Degree or Higher"))
                    print("Education.High School or Higher percent: ", percent_by_education(fd, "High School"))
                    print("Ethnicities.American Indian and Alaska Native Alone percent: ",
                          percent_by_ethnicity(fd, "American Indian and Alaska Native Alone"))
                    print("Ethnicities.Asian Alone percent: ", percent_by_ethnicity(fd, "Asian Alone"))
                    print("Ethnicities.Black Alone percent: ", percent_by_ethnicity(fd, "Black Alone"))
                    print("Ethnicities.Hispanic or Latino percent: ", percent_by_ethnicity(fd, "Hispanic or Latino"))
                    print("Ethnicities.Native Hawaiian and Other Pacific Islander Alone percent: ",
                          percent_by_ethnicity(fd, "Native Hawaiian and Other Pacific Islander Alone"))
                    print("Ethnicities.Two or More Races percent: ", percent_by_ethnicity(fd, "Two or More Races"))
                    print("Ethnicities.White Alone percent: ", percent_by_ethnicity(fd, "White Alone"))
                    print("Ethnicities.White Alone, not Hispanic or Latino percent: ",
                          percent_by_ethnicity(fd, "White Alone, not Hispanic or Latino"))
                    print("Income.Persons Below Poverty Level percent: ", percent_below_poverty_level(fd))

                elif line.strip() == "population-total":
                    print("Population in 2014: ", population_total(fd))

                elif line.strip() == "population:Education.Bachelor's Degree or Higher":
                    print("For 2014 ...")
                    print("Education.Bachelor's Degree or Higher: ", percent_by_education(fd, "High School"))
                    print("Education.High School or Higher population: ", population_by_education(fd, "High School"))
                    print("Ethnicities.American Indian and Alaska Native Alone population: ",
                          population_by_ethnicity(fd, "American Indian and Alaska Native Alone"))
                    print("Ethnicities.Asian Alone population: ", population_by_ethnicity(fd, "Asian Alone"))
                    print("Ethnicities.Black Alone population: ", population_by_ethnicity(fd, "Black Alone"))
                    print("Ethnicities.Hispanic or Latino population: ",
                          population_by_ethnicity(fd, "Hispanic or Latino"))
                    print("Ethnicities.Native Hawaiian and Other Pacific Islander Alone population: ",
                          population_by_ethnicity(fd, "Native Hawaiian and Other Pacific Islander Alone"))
                    print("Ethnicities.Two or More Races population: ",
                          population_by_ethnicity(fd, "Two or More Races"))
                    print("Ethnicities.White Alone population: ", population_by_ethnicity(fd, "White Alone"))
                    print("Ethnicities.White Alone, not Hispanic or Latino population: ",
                          population_by_ethnicity(fd, "White Alone, not Hispanic or Latino"))
                    print("Income.Persons Below Poverty Level population: ", population_below_poverty_level(fd))

    except Exception as e:
        print(f"Error occurred: {str(e)}")
        sys.exit(1)

