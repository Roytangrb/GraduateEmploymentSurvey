'''
career report by faculty
'''

import requests

progCode = input("Programme Code: ")
for year in range (1997, 2018):
    '''year = input("Report year: ")'''
    url = "http://www.cedars.hku.hk/sections/careersplacement/GraduateEmploymentSurvey/leaflet/" + str(year) + "/UG/"+ progCode + ".pdf"

    response = requests.get(url)

    with open ('../' + progCode + "/"+ progCode + str(year) + '.pdf', 'wb') as f:
        f.write(response.content)
