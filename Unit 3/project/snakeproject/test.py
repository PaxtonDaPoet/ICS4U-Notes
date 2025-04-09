students = { 
    "Ben" = 15,
    "A" = 12,
    "D" = 17, 
    "C" = 17,
    "H" = 18,
    "L" = 19,
    "T" = 18,
    "U" = 19,
    "N" = 13, 
    "P" = 15
    "N" = 14
}
eligible = []
not_eligible = []
for name, age in students.items():
if age > = 16: 
    eligible.append((name,age))
else: 
    not_eligible.append((name,age))
