import random
#capitals of european countries
euCapitals = {'Albania': 'Tirana', 'Andorra': 'Andorra la Vella', 'Armenia': 'Yerevan', 'Austria': 'Vienna',
              'Azerbaijan': 'Baku', 'Belarus': 'Minsk', 'Belgium': 'Brussels', 'Bosnia and Herzegovina': 'Sarajevo',
              'Bulgaria': 'Sofia', 'Croatia': 'Zagreb', 'Cyprus': 'Nicosia', 'Czechia': 'Prague', 'Denmark': 'Copenhagen',
              'Estonia': 'Tallinn', 'Finland': 'Helsinki', 'France': 'Paris', 'Georgia': 'Tbilisi', 'Germany': 'Berlin',
              'Greece': 'Athens', 'Hungary': 'Budapest', 'Iceland': 'Reyjkavik', 'Ireland': 'Dublin', 'Italy': 'Rome',
              'Kazakhstan': 'Nur-Sultan', 'Kosovo': 'Pristina', 'Latvia': 'Riga', 'Liechtenstein': 'Vaduz',
              'Lithuania': 'Vilnius', 'Luxembourg': 'Luxembourg', 'Malta': 'Valletta', 'Moldova': 'Chisinau',
              'Monaco': 'Monaco', 'Montenegro': 'Podgorica', 'Netherlands': 'Amsterdam', 'North Macedonia': 'Skopje',
              'Norway': 'Oslo', 'Poland': 'Warsaw', 'Portugal': 'Lisbon', 'Romania': 'Bucharest', 'Russia': 'Moscow',
              'San Marino': 'San Marino', 'Serbia': 'Belgrade', 'Slovakia': 'Bratislava', 'Slovenia': 'Ljubljana',
              'Spain': 'Madrid', 'Sweden': 'Stockholm', 'Switzerland': 'Bern', 'Turkey': 'Ankara', 'Ukraine': 'Kiev',
              'United Kingdom': 'London', 'Vatican City': 'Vatican City'}

#generate 30 quiz files
for quizNum in range(30):
    # quiz file and answers file
    quizFile = open('.\\quiz\\eucapitalsquiz%s.txt' % (quizNum + 1), 'w')
    answerKeyFile = open('.\\quiz\\capitalsquizanswers%s.txt' % (quizNum + 1), 'w')

    #write out the header for the quiz
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + 'Capitals of Europe quiz (Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')

    # shuffle order of countries
    countries = list(euCapitals.keys())
    random.shuffle(countries)

    # loop through 51 countries making question for every one
    for questionNum in range(51):
        correctAnswer = euCapitals[countries[questionNum]]
        wrongAnswers = list(euCapitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

    # questions and answer options in a file
        quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1, countries[questionNum]))
        for i in range(4):
            quizFile.write(' %s. %s\n' %('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')

    # writing answers key to a file
        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
    quizFile.close()
    answerKeyFile.close()
