import mido, subprocess

lista = []

with mido.open_input("Oxygen Pro Mini USB MIDI") as inport:
    for msg in inport:
        if msg.type == "note_on":
            print(msg)
            vol = msg.velocity / 100
            new = subprocess.Popen(["ffplay", "-autoexit", "-nodisp", "-af", "aformat=channel_layouts=stereo,asetrate=44100*" + str(msg.note) + "/50,atempo=50/" + str(msg.note) + ",volume=" + str(vol), "./Sample.wav"], stdout=subprocess.PIPE)
            lista.append(new)
        else:
            for l in lista:
                l.kill()
                lista.remove(l)
            
        
    
