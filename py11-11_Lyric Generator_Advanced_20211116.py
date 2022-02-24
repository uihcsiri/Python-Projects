#Lyrics generator

def get_name():
    singer = input("Please enter the singer you would like to search:")
    singer_lower = singer.lower()

    singer_list = ["ed", "sheeran", "taylor", "swift", "katy", "perry", "ariana", "grande", "chainsmoker", "oasis"]
    result = []
    for name in singer_list:
        if name in singer_lower:
            result.append(singer_list.index(name))
     
    if (result ==[]):
        print("Sorry. We don't have "+ singer + "'s song.")
        print("Or please check if there is typo in your input.")
    return result #list type


def search_song(result):
    song_dict ={
        1: "1. Perfect by Ed Sheeran",
        2: "2. Thinking Out Loud by Ed Sheeran",
        3: "3. Everything Has Changed by Taylor Swift feat.Ed Sheeran",
        4: "4. Wide awake by Katy Perry",
        5: "5. Califonia girls by Katy Perry",
        6: "6. Never really over by Katy Perry",
        7: "7. No tears left to cry by Ariana Grande",
        8: "8. Closer by The Chainsmoker",
        9: "9. Don't look back in anger by Oasis"
    }


    flag = 0 #to avoid double showing 
    ava = []
    for word in result:
        if (word == 0 or word == 1):#ed
            if (flag == 0):
                print(song_dict[1])
                print(song_dict[2])
                print(song_dict[3])
                ava.append(1)
                ava.append(2)
                ava.append(3)
                flag += 1
            else:
                flag -= 1
                continue
                
        if (word == 2 or word == 3):#taylor
            if (flag == 0):
                print(song_dict[3])
                flag += 1
                ava.append(3)
            else:
                flag -= 1
                continue
                
        if (word == 4 or word == 5):#katy
            if (flag == 0):
                print(song_dict[4])
                print(song_dict[5])
                print(song_dict[6])
                ava.append(4)
                ava.append(5)
                ava.append(6)
                flag += 1
            else:
                flag -= 1
                continue                  
        if (word == 6 or word == 7):#ariana
            if (flag == 0):
                print(song_dict[7])
                ava.append(7)
                flag += 1
            else:
                flag -= 1
                continue
        if (word == 8):#chainsmoker
            print(song_dict[8])
            ava.append(8)
            
        if (word == 9):#oasis
            print(song_dict[9])
            ava.append(9)

    while True:
        user = input("Please enter a numer to choose the song:")
        try:
            user = int(user)
            if user in ava:
                return user
            else:
                print("Invalid input! Please key again.")
                
        except(ValueError):
            print("Error! Please try again.\n")
            continue

    



def lyric_generator(choice):

    lyric_perfect = """
    ------- Perfect by Ed Sheeran ------------
    [Verse 1]
    I found a love for me
    Oh darling, just dive right in and follow my lead
    Well, I found a girl, beautiful and sweet
    Oh, I never knew you were the someone waiting for me
    'Cause we were just kids when we fell in love
    Not knowing what it was
    I will not give you up this time
    But darling, just kiss me slow, your heart is all I own
    And in your eyes, you're holding mine

    [Chorus]
    Baby, I'm dancing in the dark with you between my arms
    Barefoot on the grass, listening to our favourite song
    When you said you looked a mess, I whispered underneath my breath
    But you heard it, darling, you look perfect tonight

    [Verse 2]
    Well I found a woman, stronger than anyone I know
    She shares my dreams, I hope that someday I'll share her home
    I found a love, to carry more than just my secrets
    To carry love, to carry children of our own
    We are still kids, but we're so in love
    Fighting against all odds
    I know we'll be alright this time
    Darling, just hold my hand
    Be my girl, I'll be your man
    I see my future in your eyes
    [Chorus 2]
    Baby, I'm dancing in the dark, with you between my arms
    Barefoot on the grass, listening to our favorite song
    When I saw you in that dress, looking so beautiful
    I don't deserve this, darling, you look perfect tonight
    """

    lyric_thinking_out = """
    ------- Thinking out loud by Ed Sheeran ------------
    [Verse 1]
    When your legs don't work like they used to before
    And I can't sweep you off of your feet
    Will your mouth still remember the taste of my love?
    Will your eyes still smile from your cheeks?
    And darling, I will be loving you till we're seventy
    And baby, my heart could still fall as hard at twenty-three
    And I'm thinking 'bout how

    [Pre-Chorus 1]
    People fall in love in mysterious ways
    Maybe just the touch of a hand
    Well me, I fall in love with you every single day
    I just wanna tell you I am

    [Chorus]
    So honey, now, take me into your loving arms
    Kiss me under the light of a thousand stars
    Place your head on my beating heart, I'm thinking out loud
    And maybe we found love right where we are
    """

    lyric_everything_has_changed = """
    ------- Everything has changed by Taylor Swift feat. Ed Sheeran ------------
    [Verse 1: Taylor Swift]
    All I knew this morning when I woke
    Is I know something now
    Know something now I didn't before
    And all I've seen since 18 hours ago
    Is green eyes and freckles and your smile
    In the back of my mind, making me feel like

    [Pre-Chorus: Taylor Swift & Ed Sheeran]
    I just wanna know you better
    Know you better, know you better now
    I just wanna know you better
    Know you better, know you better now
    I just wanna know you better
    Know you better, know you better now
    I just wanna know you, know you, know you

    [Chorus: Taylor Swift & Ed Sheeran]
    'Cause all I know is we said, "Hello"
    And your eyes look like coming home
    All I know is a simple name
    Everything has changed
    All I know is you held the door
    You'll be mine and I'll be yours
    All I know since yesterday
    Is everything has changed
    """

    lyric_wide_awake= """
    ------- Wide awake by Katy Perry ------------
    [Intro]
    I'm wide awake
    I'm wide awake
    I'm wide awake

    [Verse 1]
    Yeah, I was in the dark
    I was falling hard
    With an open heart (I'm wide awake)
    How did I read the stars so wrong? (I'm wide awake)
    And now it's clear to me
    That everything you see
    Ain't always what it seems (I'm wide awake)
    Yeah, I was dreaming for so long

    [Pre-Chorus]
    I wish I knew then, what I know now
    Wouldn't dive in, wouldn't bow down
    Gravity hurts, you made it so sweet
    'Til I woke up on, on the concrete

    [Chorus]
    Falling from cloud nine
    Crashing from the high
    I'm letting go tonight
    Yeah, I'm falling from cloud nine
    """

    lyric_california_girls = """
    ------- California girls by Katy Perry ------------
    [Intro: Snoop Dogg]
    Greetings, loved ones
    Let's take a journey

    [Verse 1: Katy Perry]
    I know a place where the grass is really greener
    Warm, wet and wild
    There must be something in the water
    Sipping gin and juice
    Laying underneath the palm trees (Undone)
    The boys break their necks
    Tryna creep a little sneak peek (At us)

    [Pre-Chorus: Katy Perry]
    You could travel the world
    But nothing comes close to the golden coast
    Once you party with us
    You'll be falling in love
    Oh-oh-oh-oh-oh-oh-oh

    [Chorus: Katy Perry]
    California girls, we're unforgettable
    Daisy Dukes, bikinis on top
    Sun-kissed skin so hot, we'll melt your popsicle
    Oh-oh-oh-oh-oh, oh-oh-oh-oh-oh-oh-oh
    California girls, we're undeniable
    Fine, fresh, fierce, we got it on lock
    West Coast represent, now put your hands up
    Oh-oh-oh-oh-oh, oh-oh-oh-oh-oh-oh-oh
    """
    lyric_never_really = """
    ------- Never really over by Katy Perry ------------
    [Verse 1]
    I'm losing my self-control
    Yeah, you’re starting to trickle back in
    But I don't wanna fall down the rabbit hole
    Cross my heart, I won't do it again

    [Pre-Chorus]
    I tell myself, tell myself, tell myself, "Draw the line"
    And I do, I do
    But once in a while, I trip up, and I cross the line
    And I think of you

    [Chorus]
    Two years, and just like that
    My head still takes me back
    Thought it was done, but I
    Guess it’s never really over
    Oh, we were such a mess
    But wasn't it the best?
    Thought it was done, but I
    Guess it's never really over

    [Post-Chorus]
    Just because it's over doesn't mean it's really over
    And if I think it over, maybe you'll be coming over again
    And I'll have to get over you all over again
    Just because it’s over doesn’t mean it's really over
    And if I think it over, maybe you’ll be coming over again
    And I'll have to get over you all over again
    """
    
    lyric_no_tears = """
    ------- No tears left to cry by Ariana Grande ------------
    [Intro]
    Right now, I'm in a state of mind
    I wanna be in like all the time
    Ain't got no tears left to cry
    So I'm pickin' it up, pickin' it up
    I'm lovin', I'm livin', I'm pickin' it up
    I'm pickin' it up, pickin' it up (Yeah)
    I'm lovin', I'm livin', I'm pickin' it up (Oh, yeah)

    [Refrain]
    I'm pickin' it up (Yeah), pickin' it up (Yeah)
    Lovin', I'm livin', so we turnin' up
    Yeah, we turnin' it up

    [Verse 1]
    Ain't got no tears in my body
    I ran out, but boy, I like it, I like it, I like it
    Don't matter how, what, where, who tries it
    We out here vibin', we vibin', we vibin'

    [Pre-Chorus]
    Comin' out, even when it's rainin' down
    Can't stop now, can't stop so shut your mouth
    Shut your mouth, and if you don't know
    Then now you know it, babe
    Know it, babe, yeah

    [Chorus]
    Right now, I'm in a state of mind
    I wanna be in like all the time
    Ain't got no tears left to cry
    So I'm pickin' it up, pickin' it up (Oh yeah)
    I'm lovin', I'm livin', I'm pickin' it up
    Oh, I just want you to come with me
    We're on another mentality
    Ain't got no tears left to cry (To cry)
    So I'm pickin' it up, pickin' it up (Oh yeah)
    I'm lovin', I'm livin', I'm pickin' it up
    """
    lyric_closer = """
    ------- Closer by The Chainsmoker ------------
    [Verse 1: Andrew Taggart]
    Hey, I was doing just fine before I met you
    I drink too much
    And that's an issue, but I'm okay
    Hey, you tell your friends
    It was nice to meet them
    But I hope I never see them again

    [Pre-Chorus: Andrew Taggart]
    I know it breaks your heart
    Moved to the city in a broke-down car
    And four years, no calls
    Now you're lookin' pretty in a hotel bar
    And I-I-I can't stop
    No, I-I-I can't stop

    [Chorus: Andrew Taggart]
    So, baby, pull me closer
    In the backseat of your Rover
    That I know you can't afford
    Bite that tattoo on your shoulder
    Pull the sheets right off the corner
    Of the mattress that you stole
    From your roommate back in Boulder
    We ain't ever getting older
    [Post-Chorus: Andrew Taggart]
    We ain't ever getting older
    We ain't ever getting older
    """
    
    lyric_dont_look_back = """
    ------- Don't look back in anger by Oasis ------------
    [Verse 1]
    Slip inside the eye of your mind
    Don't you know you might find
    A better place to play?
    You said that you'd never been
    But all the things that you've seen
    Slowly fade away

    [Pre-Chorus]
    So I start a revolution from my bed
    'Cause you said the brains I had went to my head
    Step outside, summertime's in bloom
    Stand up beside the fireplace
    Take that look from off your face
    You ain't ever gonna burn my heart out

    [Chorus]
    And so, Sally can wait
    She knows it's too late as we're walking on by
    Her soul slides away
    But don't look back in anger, I heard you say
    """
    
 
    lyric_dict= {
        1: lyric_perfect,
        2: lyric_thinking_out,
        3: lyric_everything_has_changed,
        4: lyric_wide_awake,
        5: lyric_california_girls,
        6: lyric_never_really,
        7: lyric_no_tears,
        8: lyric_closer,
        9: lyric_dont_look_back
        
    }

    print(lyric_dict[choice])

def playagain():
    print("Press * to search again")
    again = input()
    if (again == "*"):
        return 1
    else:
        return 0


def main():
    while True:
        result = get_name()
        if (result == []):
            re = playagain()
            if re == 0:
                break
            else:
                continue
            
        else:
            user_choice = search_song(result)
            lyric_generator(user_choice)
            re = playagain()
            if re == 0:
                break
            else:
                continue
        
main()
