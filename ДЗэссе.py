inp = input('Если хотите увидеть краткий рассказ обо мне,то введите:"Да" ')
MyName = 'Всем привет, меня зовут Михаил Костин.'
mycity = 'Я живу в Великом Новгороде.'
myage = 'Мне 17 лет и я учусь в'
myStudyBuilding = 'строительном колледже.'
DopPer = 'Обычная пара длится'
lengthPair =  1.5
forLengthP = 'часа.'
turnLength = 'Обычная пара в колледже составляет - 10 минут, а большая - '
turnBigLength = 30
street = 'В городе, я проживаю на улице Коровникова.'
population = 'Население нашего города составляет примерно 200.000 человек.'
specialty = ' Я обучаюсь по специальности информационные системы по отраслям.'
profession = 'Я пошёл на эту специальность, потому что меня заинтересовала профессия программиста.'
trueProfession = 'Но поняв, что и как работает в мире IT я захотел работать тестировщиком.'
goodbye = 'Спасибо за внимание, это был краткий рассказ обо мне:-)'
if inp=='Да' or inp=='да':   
    print(MyName, mycity, myage,myStudyBuilding,DopPer,lengthPair,forLengthP,'\n',turnLength,turnBigLength,'.',street,population,specialty,profession,trueProfession,goodbye )
else:
    print("Ну и ладно, не очень то и хотелось!!!")