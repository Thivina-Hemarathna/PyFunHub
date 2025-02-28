
path = "../Mail Merge Project Start/Output/ReadyToSend/"

with open("../Mail Merge Project Start/Input/Names/invited_names.txt",mode="r") as file:
    names=file.readlines()

for name in names:
    use=name.strip()
    with open (f"{path}letter_for_{use}.txt",mode="w") as invite:
        with open ("../Mail Merge Project Start/Input/Letters/starting_letter.txt",mode="a+") as reader:
            reader.seek(0)
            contents = reader.read()
            new_contents = contents.replace("[name]", f"{use}")
            invite.write(new_contents)