import sys
import data
import build_data
import county_demographics
from data import CountyDemographics

fd = build_data.get_data()
#part 1

#The purpose of the function is to calculate the total population of a county or counties
# input a list of CountyDemographic objects
# output an integer representing the population

def population_total(counties: list[CountyDemographics]) -> int:
    total = 0
    for county in counties:
        total += county.population.get("2014 Population", 0)
    return total

#part 2
# the purpose of this function is to iterate through a list of counties and return only those that are within the searched staet
# input is a list of CountyDemographics objects
# input 2 is a string that represents the filter is what state it is
#outputs a list of CountyDemographics objects from the input list from the specified state
def filter_by_state(counties:list[CountyDemographics],state:str) -> list[CountyDemographics]:
    returning_list = []
    for county in counties:
        if county.state == state:
            returning_list.append(county)
    return returning_list

#part 3
# the purpose of this function is to return the number of people that are of a certain level of education across a list of counties
# input is the list of counties as a list
# input is the education level
# output is the number of people

def population_by_education(counties: list[CountyDemographics], education_level:str) -> float:

    total = 0
    for county in counties:
        population = county.population.get('2014 Population',0)
        if education_level in county.education:
            percent = county.education[education_level]
            sub_population = population * (percent/100)
            total += sub_population

    return total

# the purpose of this function is to return the number of people that are of a certain ethnicity across a list of counties
# input is the list of counties as a list
# input is the ethnicities
# output is the number of people
def population_by_ethnicity(counties: list[CountyDemographics], ethnicity: str) -> float:
    total_population = 0.0

    for county in counties:
        if ethnicity in county.ethnicities:
            population = county.population.get('2014 Population', 0)
            percentage = county.ethnicities[ethnicity]
            sub_population = population * (percentage / 100)
            total_population += sub_population

    return total_population

# the purpose of this function is to return the number of people that are of below the poverty line across a list of counties
# input is the list of counties as a list
# output is the number of people
def population_below_poverty_level(counties: list[CountyDemographics]) -> float:
    total = 0
    for county in counties:
        if "Persons Below Poverty Level" in county.income:
            poverty_percentage = county.income["Persons Below Poverty Level"]
            population = county.population.get("2014 Population", 0)
            total += (population * poverty_percentage) / 100

    return total

#part 4
# the purpose of this function is to calculate the specified sub-population by education as a percentage of the total population
# input is a list of CountyDemographics objects that represent different counties and their demographics data
# input 2 is a string representing the education key of interest (e.g., "Bachelor's Degree or Higher")
# output is a float representing the percentage of the total population with the specified education level across the counties
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


# the purpose of this function is to calculate the specified sub-population by ethnicity as a percentage of the total population
# input is a list of CountyDemographics objects that represent different counties and their demographics data
# input 2 is a string representing the ethnicity key of interest (e.g., 'Two or More Races')
# output is a float representing the percentage of the total population with the specified ethnicity across the counties

def percent_by_ethnicity(counties: list[CountyDemographics], ethnicity: str) -> float:
    total_population = 0
    total_ethnic_population = 0
    for county in counties:
        if ethnicity in county.ethnicities:
            total_population += county.population['2014 Population']
            total_ethnic_population += (county.population['2014 Population'] * county.ethnicities[ethnicity] / 100)

    if total_population == 0:
        return 0

    ethnic_percentage = (total_ethnic_population / total_population) * 100
    return ethnic_percentage


# the purpose of this function is to calculate the percentage of the total population below the poverty level across the counties
# input is a list of CountyDemographics objects that represent different counties and their demographics data
# output is a float representing the percentage of the total population below the poverty level across the counties

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

#Part 5
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

# the purpose of this function is to filter and return all counties where the specified ethnicity key is greater than the threshold
# input is a list of CountyDemographics objects that represent different counties and their demographics data
# input 2 is a string representing the ethnicity key of interest (e.g., 'Hispanic or Latino')
# input 3 is a float representing the threshold value for comparison
# output is a list of CountyDemographics objects where the specified ethnicity level is greater than the threshold

def education_less_than(counties: list[CountyDemographics], education_key: str, threshold: float) -> list[
    CountyDemographics]:

    result = []

    for county in counties:

        if education_key in county.education and county.education[education_key] < threshold:
            result.append(county)
    return result

# the purpose of this function is to filter and return all counties where the specified ethnicity key is greater than the threshold
# input is a list of CountyDemographics objects that represent different counties and their demographics data
# input 2 is a string representing the ethnicity key of interest (e.g., 'Hispanic or Latino')
# input 3 is a float representing the threshold value for comparison
# output is a list of CountyDemographics objects where the specified ethnicity level is greater than the threshold

def ethnicity_greater_than(counties: list[CountyDemographics], ethnicity_key: str, threshold: float) -> list[
    CountyDemographics]:
    result = []

    for county in counties:
        if county.ethnicities.get(ethnicity_key, 0) > threshold:
            result.append(county)

    return result
# the purpose of this function is to filter and return all counties where the specified ethnicity key is less than the threshold
# input is a list of CountyDemographics objects that represent different counties and their demographics data
# input 2 is a string representing the ethnicity key of interest (e.g., 'Hispanic or Latino')
# input 3 is a float representing the threshold value for comparison
# output is a list of CountyDemographics objects where the specified ethnicity level is less than the threshold

def ethnicity_less_than(counties: list[CountyDemographics], ethnicity: str, threshold: float) -> list[
    CountyDemographics]:
    result = []
    for county in counties:
        if county.ethnicities.get(ethnicity, 0) < threshold:
            result.append(county)


    return result

# the purpose of this function is to filter and return all counties where the percentage of the population below poverty level is greater than the threshold
# input is a list of CountyDemographics objects that represent different counties and their demographics data
# input 2 is a float representing the threshold value for comparison
# output is a list of CountyDemographics objects where the percentage of the population below poverty level is greater than the threshold



def below_poverty_level_greater_than(counties: list[CountyDemographics], threshold: float) -> list[CountyDemographics]:

    result = []

    for county in counties:
        if county.income.get('Persons Below Poverty Level', 0) > threshold:
            result.append(county)

    return result

# the purpose of this function is to filter and return all counties where the percentage of the population below poverty level is less than the threshold
# input is a list of CountyDemographics objects that represent different counties and their demographics data
# input 2 is a float representing the threshold value for comparison
# output is a list of CountyDemographics objects where the percentage of the population below poverty level is less than the threshold

def below_poverty_level_less_than(counties: list[CountyDemographics], threshold: float) -> list[CountyDemographics]:

    result = []

    for county in counties:
        if county.income['Persons Below Poverty Level'] < threshold:
            result.append(county)

    return result

def main():
    try:
        with open("inputs/"+sys.argv[1],"r") as file:
            line = file.readline()
            print(line)
            print("Records:", len(fd))
            cali_data = filter_by_state(fd, "CA")

            second = ""
            file_contents = file.readlines()
            count = 0
            while line:

                line = line.strip()

                print(line)


                if line == "filter-gt:Education.Bachelor's Degree or Higher:60":
                    print("Bachelor's Degree or Higher: ", education_greater_than(fd, "Bachelor's Degree or Higher", 60))

                elif line == "filter-lt:Education.High School or Higher:60":
                    print("High School or Higher: ", education_less_than(fd, "High School or Higher", 60))


                elif line == "percent:Education.Bachelor's Degree or Higher":

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
                    print("Income.Persons Below Poverty Level percent: ",
                          percent_below_poverty_level(fd))


                elif line == "population-total":
                    print("Population in 2014: ", population_total(fd))

                elif line == "population:Education.Bachelor's Degree or Higher":
                    print("For 2014 ...")
                    print("Education.Bachelor's Degree or Higher: ", population_by_education(fd, "Bachelor's Degree or Higher"))
                    print("Education.High School or Higher population: ", population_by_education(fd, "High School or Higher"))
                    print("Ethnicities.American Indian and Alaska Native Alone population: ", population_by_ethnicity(fd, "American Indian and Alaska Native Alone"))
                    print("Ethnicities.Asian Alone population: ", population_by_ethnicity(fd, "Asian Alone"))
                    print("Ethnicities.Black Alone population: ", population_by_ethnicity(fd, "Black Alone"))
                    print("Ethnicities.Hispanic or Latino population: ", population_by_ethnicity(fd, "Hispanic or Latino"))
                    print("Ethnicities.Native Hawaiian and Other Pacific Islander Alone population: ", population_by_ethnicity(fd, "Native Hawaiian and Other Pacific Islander Alone"))
                    print("Ethnicities.Two or More Races population: ", population_by_ethnicity(fd, "Two or More Races"))
                    print("Ethnicities.White Alone population: ", population_by_ethnicity(fd, "White Alone"))
                    print("Ethnicities.White Alone, not Hispanic or Latino population: ",
                          population_by_ethnicity(fd, "White Alone, not Hispanic or Latino"))
                    print("Income.Persons Below Poverty Level population: ",
                          population_below_poverty_level(fd))

                elif line == "filter-lt:Education.High School or Higher:80":

                    filtered_counties = education_less_than(fd,"High School or Higher", 80)
                    print(percent_below_poverty_level(filtered_counties))
                elif line == "filter-gt:Education.Bachelor's Degree or Higher:40":

                    filtered_counties = education_greater_than(fd, "Bachelor's Degree or Higher", 40)
                    print(percent_below_poverty_level(filtered_counties))
                elif line == "filter-gt:Ethnicities.Asian Alone:60":
                    filtered_counties = ethnicity_greater_than(fd, "Asian Alone", 40)
                    print(percent_below_poverty_level(filtered_counties))

                elif line == "filter-lt:Ethnicities.Asian Alone:60":
                    filtered_counties = ethnicity_less_than(fd, "Asian Alone", 40)
                    print(percent_below_poverty_level(filtered_counties))

                elif line == "filter-state:CA":


                    if sys.argv[1] == "ca.ops":
                        print("For 2014 ...")
                        print("Population in 2014: ", population_total(filter_by_state(fd,"CA")))
                        print("Education.Bachelor's Degree or Higher: ", percent_by_education(cali_data, "Bachelor's Degree or Higher"))
                        print("Education.High School or Higher percent: ", percent_by_education(cali_data, "High School"))
                        print("Ethnicities.American Indian and Alaska Native Alone percent: ",percent_by_ethnicity(cali_data, "American Indian and Alaska Native Alone") )
                        print("Ethnicities.Asian Alone percent: ", percent_by_ethnicity(cali_data, "Asian Alone"))
                        print("Ethnicities.Black Alone percent: ", percent_by_ethnicity(cali_data, "Black Alone"))
                        print("Ethnicities.Hispanic or Latino percent: ", percent_by_ethnicity(cali_data, "Hispanic or Latino"))
                        print("Ethnicities.Native Hawaiian and Other Pacific Islander Alone percent: ", percent_by_ethnicity(cali_data, "Native Hawaiian and Other Pacific Islander Alone"))
                        print("Ethnicities.Two or More Races percent: ", percent_by_ethnicity(cali_data, "Two or More Races"))
                        print("Ethnicities.White Alone percent: ", percent_by_ethnicity(cali_data, "White Alone"))
                        print("Ethnicities.White Alone, not Hispanic or Latino percent: ", percent_by_ethnicity(cali_data, "White Alone, not Hispanic or Latino"))
                        print("Income.Persons Below Poverty Level percent: ", percent_by_ethnicity(cali_data, "Persons Below Poverty Level"))
                    else:
                        print("Filter: state == CA(58 entries)")
                        print(cali_data)
                else:
                    print("File not found")

                line = file.readline()
    except Exception as e:
        print(e)




if __name__ == "__main__":
    try:
        main()
    except FileNotFoundError:
        print("error")

