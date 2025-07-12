import os
try:
    import webvtt
except ImportError:
    os.system("pip install webvtt-py")
    import webvtt
base_dir = os.path.dirname(__file__)
formatted_folder = os.path.join(base_dir, "formatted_transcripts")
os.makedirs(formatted_folder, exist_ok=True)
def write_text(txt_folder,vtt_name):
    try:
        read_vtt = webvtt.read(vtt_folder_single)
    except Exception as e1:
        print("❌ "+ vtt_name +" file/folder not found, check spelling. If it is a single file, include .vtt at the end. (Ex. 2432_transcript_FP.vtt) ❌")
        exit()
    txt_name = vtt_name[:-4]+".txt"
    txt_directory = os.path.join(txt_folder, txt_name)
    open(txt_directory, "w").close()
    f = open(txt_directory, "w")
    prev_speaker = ""
    for caption in read_vtt:
        cutoff = caption.text.find(":")
        speaker = caption.text[:cutoff]
        talking = caption.text[(cutoff+1):]
        if speaker == prev_speaker:
            f.write(talking)
        else:
            if prev_speaker:
                f.write("\n\n")
            f.write("("+caption.start+")"+"\n"+speaker+":"+talking)
        prev_speaker = speaker
    f.close()
vtt_file = input("\n"+"Enter the name of the VTT file or a folder with all the VTT files (include .vtt at the end if single file): ")
if vtt_file.endswith(".vtt"):
    vtt_folder_single = os.path.join(base_dir, vtt_file)
    write_text(formatted_folder,vtt_file)
else: 
    vtt_folder = os.path.join(base_dir, vtt_file)
    try:
        vtt_list = os.listdir(vtt_folder)
    except Exception as e2:
        print("❌ "+ vtt_file +" file/folder not found, check spelling. If it is a single file, include .vtt at the end. (Ex. 2432_transcript_FP.vtt) ❌")
        exit()
    for filename in vtt_list:
        if filename.endswith(".vtt"):
            vtt_folder_single = os.path.join(vtt_folder, filename)
            write_text(formatted_folder,filename)