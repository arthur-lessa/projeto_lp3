from validate_docbr import CPF

cpf = CPF()

print(cpf.generate(True))
print(cpf.generate(False))

print(cpf.validate("955.813.849-59"))
print(cpf.validate("43064523449"))
print(cpf.validate("352413515"))

cpfs = [
    "458.413.028-09",
    "51677716339",
    "600.174.760-11",
    "73151358632",
    "5168531"
]

print(cpf.validate_list(cpfs))
