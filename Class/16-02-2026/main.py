# name = 'Istomin Sasha'
# print(name[0], name[1], name[11], name[3], name[2], sep='')
# print(name[1], name[11], name[9], name[2], sep='')
# print(name[10], name[11], name[8], name[9], name[5], name[2], sep='')

# text = """
# With a velvety growl, Maul himself invites you to look more closely at a galaxy reshaped by the Empire in Star Wars: Maul – Shadow Lord. Today, the first teaser trailer and poster for the animated series arrived, giving fans our first glimpse at the world of Janix and the machinations of the underworld playing out in an era near the beginning of Emperor Palpatine’s reign.
#
# Beginning with a two-episode premiere on Disney+ April 6, 2026, and two episodes each week leading to a finale on Star Wars Day, May the 4th, Star Wars: Maul – Shadow Lord picks up after the events of Star Wars: The Clone Wars, for a pulpy adventure that finds Maul plotting to rebuild his criminal syndicate on a planet untouched by the Empire. There, he crosses paths with a disillusioned young Jedi Padawan who may just be the apprentice he is seeking to aid him in his relentless pursuit for revenge.
#
# The voice cast is led by Sam Witwer — who also lent his voice to Maul in Star Wars: The Clone Wars, Star Wars Rebels, and beyond — as Maul, Gideon Adlon as Devon Izara, recent Golden Globe® winner and Oscar® nominee Wagner Moura as Brander Lawson, and Richard Ayoade as Two-Boots; the latter duo will also feature in a Marvel Comics prequel series set on Janix beginning this March.
#
# The series features stylized animation emblematic of the gritty new cityscape locale of Janix combined with old-school filmmaking methods to capture painterly brushstrokes on glass and other physical elements.
#
# Star Wars: Maul – Shadow Lord teaser poster
# “Cinematography Lighting & VFX Director Joel Aron really took it up a notch with going back to the practical ways of capturing brush strokes by painting them on glass, shooting them then strategically placing them in shots,” says Executive Producer and Vice President of Lucasfilm Animation Athena Portillo. "He even went back to establishing matte paintings on canvas. There's always different challenges with every show that we do, but this one in particular raised the bar. We also wanted the animation body mechanics and the facial to be more fluid from our previous work and animation director Keith Kellogg worked closely with CGCG and our internal animation team to upgrade the performances of our main characters."
#
# With 10 episodes arriving over five weeks, Star Wars: Maul – Shadow Lord will take a serialized approach to Star Wars storytelling. “This show is highly serialized, very connected all the way through,” Executive Producer and Supervising Director Brad Rau says.
#
# “And it’s a super fast-paced series,” adds Executive Producer Matt Michnovetz. “We wanted to create an action-packed thrill ride, something that had the rush of a roller coaster, so we do a lot of homages to the classic serials of the day, which gave George Lucas the inspiration for Star Wars. And we've got the perfect character to drive us through this in Maul.”
# """
# print('Task 1')
#
# word = "M"
# count = 0
# for i in range(len(text)):
#     if word == text[i]:
#         count += 1
#
# print(count)
# print(text.count("M"))


# text = "0123456789abcdef"
# digits = '0123456789'
# leters = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
# countL = 0
# countD = 0
#
# for elem in text:
#     if elem.isdigit():
#         countD += 1
#     if elem.isalpha():
#         countL += 1
#
# print(f"l: {countL}, d: {countD}")

text = input("Enter text: ")
sim = input("Enter similarity: ")
num = 0
for i in text:
    if i.count(sim):
        num += 1
print(num)