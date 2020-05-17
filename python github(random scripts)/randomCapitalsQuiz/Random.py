#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.

import random

capitals = {'Albania':'Tirana',
'Andorra':'Andorra la Vella',
'Armenia':'Yerevan',
'Austria':'Vienna',
'Azerbaijan':'Baku',
'Belarus':'Minsk',
'Belgium':'Brussels',
'Bosnia and Herzegovina':'Sarajevo',
'Bulgaria':'Sofia',
'Croatia':'Zagreb',
'Cyprus':'Nicosia',
'Czechia':'Prague',
'Denmark':'Copenhagen',
'Estonia':'Tallinn',
'Finland':'Helsinki',
'France':'Paris',
'Georgia':'Tbilisi',
'Germany':'Berlin',
'Greece':'Athens',
'Hungary':'Budapest',
'Iceland':'Reykjavik',
'Ireland':'Dublin',
'Italy':'Rome',
'Kazakhstan':'Nur-Sultan',
'Kosovo':'Pristina',
'Latvia':'Riga',
'Liechtenstein':'Vaduz',
'Lithuania':'Vilnius',
'Luxembourg':'Luxembourg',
'Malta':'Valletta',
'Moldova':'Chisinau',
'Monaco':'Monaco',
'Montenegro':'Podgorica',
'Netherlands':'Amsterdam',
'Macedonia':'Skopje',
'Norway':'Oslo',
'Poland':'Warsaw',
'Portugal':'Lisbon',
'Romania':'Bucharest',
'Russia':'Moscow',
'San Marino':'San Marino',
'Serbia':'Belgrade',
'Slovakia':'Bratislava',
'Slovenia':'Ljubljana',
'Spain':'Madrid',
'Sweden':'Stockholm',
'Switzerland':'Bern',
'Turkey':'Ankara',
'Ukraine':'Kiev',
'United Kingdom':'London',
'Vatican City': 'Vatican City'}

for quizNum in range(2):
    # Create the quiz and answer key files.
    quizFile = open('CapitalsQuiz%s.txt' % (quizNum + 1), 'w')
    answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')

    # Write out the header for the quiz.
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')

    countries = list(capitals.keys())
    random.shuffle(countries)


    for questionNum in range(50):
        correctAnswer = capitals[countries[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)


        quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1, countries[questionNum]))
        for i in range(4):
            quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')


        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
quizFile.close()
answerKeyFile.close()
