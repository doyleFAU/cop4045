

def main() -> None:
    print('Part a)')
    part_a = [
        (a, b, c, d)
        for a in range(1, 11)
        for b in range(1, 11)
        for c in range(1, 11)
        for d in range(1, 11)
        if len({a, b, c, d}) == 4
        if a * a + b * b == c * c + d * d

    ]
    print(part_a)
    print('Part b)')
    words = ['One', 'SEVEN', 'three', 'two', 'Ten']
    part_b = [(word.lower(), len(word)) for word in words if len(word) < 5]
    print(part_b)

    print('Part c)')
    names = ['Christopher Ashton Kutcher', 'Elizabeth Stamatina Fey']
    part_c = [
        name.split()[0] + ' ' + name.split()[1][0] + '. ' + name.split()[2]
        for name in names
    ]
    print(part_c)

    print('Part d)')
    lst1 = ["Spam", "Trams", "Elbows", "Tops", "Astral"]
    lst2 = ["Bowels", "Sample", "Altars", "Stop", "Course", "Smart"]
    part_d = [
        (w1, w2)
        for w1 in lst1
        for w2 in lst2
        if sorted(w1.lower()) == sorted(w2.lower())

    ]
    print(part_d)

    print('Part e)')
    s = ['one', 'two', 'three']
    part_e = {word: len(word) for word in s}
    print(part_e)

    print('Part f)')
    text = "Hello World"

    part_f = {
        i: text[i]
        for i in range(len(text))
        if text[i].lower() in 'aeiou'

    }
    print(part_f)

if __name__ == '__main__':
    main()