from typeguesser import TypeGuesser

tg = TypeGuesser("test.csv", header=True)

tg.guessTypes()

print tg.getCreateStatement()
