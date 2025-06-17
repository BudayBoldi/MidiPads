import mido, subprocess

with mido.open_input("Oxygen Pro Mini USB MIDI") as inport:
    for msg in inport:
        if msg.type == "note_on":
            print(msg)
            vol = msg.velocity / 100
            for i in range(41, 73):
                if msg.note == i:
                    subprocess.Popen(["ffplay", "-autoexit", "-nodisp", "-af", "aformat=channel_layouts=stereo,asetrate=44100*" + str(i) + "/50,atempo=50/" + str(i) + ",volume=" + str(vol), "./Sample.wav"], stdout=subprocess.PIPE)
                
            
        
    
