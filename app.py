def some():
    yield "daniel"

result=None
for row in some():
    result=row
    
print(result)