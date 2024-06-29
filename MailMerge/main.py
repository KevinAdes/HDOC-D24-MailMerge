names = []

with open("./Input/Names/invited_names.txt", encoding='utf-8-sig') as invited_names:
    for name in invited_names.readlines():
        names.append(name.removesuffix("\n"))


with open("./Input/Letters/starting_letter.txt", encoding='utf-8-sig') as starting_letter:
    lettercopy = starting_letter.read()
    for invitee in names:
        with open(f"./Output/ReadyToSend/LetterFor{invitee}", mode="x") as invitation:
            invitation.write(lettercopy.replace("[NAME]", invitee))