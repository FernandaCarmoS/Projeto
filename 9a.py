import emoji
print("Vamos descobrir se você é a minha alma gêmea? ")
a = input(str('Me diga o seu nome que eu te responderei! '))
print(emoji.emojize('Eu te amo {} :sparkling_heart:'.format(a), language='alias'))