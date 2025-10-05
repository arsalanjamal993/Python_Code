class programmer:
    company = "Microsoft"
    def __init__(self, name , salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin


p = programmer("arsalan", 120000, 75421)
print(p.name, p.salary, p.pin)
q = programmer("bill", 130000, 25431)
print(q.name, q.salary, q.pin)
r = programmer("jibes", 150000, 35431)
print(r.name, r.salary, r.pin)

