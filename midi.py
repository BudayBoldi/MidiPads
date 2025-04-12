import mido, subprocess

with mido.open_input("Oxygen Pro Mini Mackie/HUI") as inport:
    for msg in inport:
        if msg.type == "note_on":
            print(msg)
            match msg.note:
                case 40:
                    subprocess.Popen(["ffplay", "-autoexit", "-nodisp", "./Kick.wav"], stdout=subprocess.PIPE)
                case 41:
                    subprocess.Popen(["ffplay", "-autoexit", "-nodisp", "./Kick2.wav"], stdout=subprocess.PIPE)
                case 42:
                    subprocess.Popen(["ffplay", "-autoexit", "-nodisp", "./Kick3.wav"], stdout=subprocess.PIPE)
                case 43:
                    subprocess.Popen(["ffplay", "-autoexit", "-nodisp", "./Snare.wav"], stdout=subprocess.PIPE)
                case 48:
                    subprocess.Popen(["ffplay", "-autoexit", "-nodisp", "./HHat.wav"], stdout=subprocess.PIPE)
                case 49:
                    subprocess.Popen(["ffplay", "-autoexit", "-nodisp", "./HHat2.wav"], stdout=subprocess.PIPE)
                case 50:
                    subprocess.Popen(["ffplay", "-autoexit", "-nodisp", "./Crash.wav"], stdout=subprocess.PIPE)
                case 51:
                    subprocess.Popen(["ffplay", "-autoexit", "-nodisp", "./Crash2.wav"], stdout=subprocess.PIPE)
                case _:
                    print("ERROR!")
                
            
        
    
