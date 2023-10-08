import uuid

FIRST_NAME = [
    "nagy",
    "nemeth",
    "kovacs",
    "kis",
    "kiss",
    "szabo",
    "varga",
    "molnar",
    "toth",
    "racz",
    "feher",
    "molnar",
    "fekete",
    "torok",
    "papp"
]

LAST_NAME = [
    "maria",
    "erzsebet",
    "istvan",
    "eva",
    "ilona",
    "anna",
    "zsuzsanna",
    "andrea",
    "laszlo",
    "tibor",
    "dezso",
    "jozsef",
    "attila",
    "tamas",
    "vivien",
    "szilvia",
    "edina",
    "gyula"
]

FILE_PATH = "generated_username" + str(uuid.uuid4())[0:5] + ".txt"


def generate_username():
    for first_name in FIRST_NAME:
        for last_name in LAST_NAME:
            one_letter = first_name + last_name[0:1]
            two_letter = first_name + last_name[0:2]
            three_letter = first_name + last_name[0:3]
            four_letter = first_name + last_name[0:4]
            full_name = first_name + last_name
            full_name_point = first_name + "." + last_name
            with open(FILE_PATH, 'a') as file:
                file.write(one_letter)
                file.write('\n')
                file.write(two_letter)
                file.write('\n')
                file.write(three_letter)
                file.write('\n')
                file.write(four_letter)
                file.write('\n')
                file.write(full_name)
                file.write('\n')
                file.write(full_name_point)
                file.write('\n')


if __name__ == '__main__':
    generate_username()

