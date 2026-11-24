def get_performers():
    global performers
    performers = {}
    while True:
        # Key = Performer name, Value = What instrument they play (e.g Macauley: Bass, Joshua: Lead Guitar)
        performer = input("Please input name of performer, or input 'stop': ")
        
        if performer == "stop":
            break
        instrument = input("Please state what intstrument they play: ")
        
        # Double checks whether the band has a duplicate of the instrument or not
        # Helps detect duplicate errors if they already got someone on that instrument and dont want a dupe
        if instrument in performers.values():
            dupe_check = input("You already have this instrument, do you want another person on this instrument? (y/n): ")
            
            #If they know and want a dupe, add instrument
            if dupe_check.lower() == "y":
                performers[performer] = instrument
                continue
            
            #Otherwise just continue
            continue
        
        #If no dupe is detected, immediately add instrument
        performers[performer] = instrument
        continue
    print(performers)
    return performers

def band_and_genre_dict(name, genre):
    band = {}
    band[name] = genre
    return band

contacts = {}

def contact_details():
    global contacts, performers
    
    for performer in performers:
        contacts[performer] = input("Please input contact details of " + performer + ": ")
    return contacts

def banner():
    print("""
    -----------------------------------------
            Performer Management
        Collection of band information
    -----------------------------------------
    """)

def main():
    banner()
    band_name = input("Please state your band name: ")
    genre = input("Please input your genre: ")
    band_performing = band_and_genre_dict(band_name, genre)
    
    get_performers()
    contact_details()
    
    print(band_performing)

if __name__ == "__main__":
    main()