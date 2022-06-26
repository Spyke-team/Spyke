import spyke

while True:
    text = input('SPYKE >> ')
    result, error = spyke.run('<stdin>', text)

    if error: print(error.as_string())
    else: print(result)