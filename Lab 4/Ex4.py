# Try to append to a tuple. It won't work
#name: Ziling He
#date: Sep. 16, 2026

survey_repondents = (1012, 1035, 1021, 1053)
#survey_repondents.append(1054)  # This will raise an AttributeError because tuples are immutable

survey_repondents = survey_repondents + (1054,)  # This creates a new tuple with the additional element
print("Updated survey_respondents:", survey_repondents)