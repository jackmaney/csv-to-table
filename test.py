from typeguesser import TypeGuesser

tg = TypeGuesser("test.csv", True)

tg.guessTypes()

print tg.getCreateStatement()
