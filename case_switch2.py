from random import choice
import PySimpleGUI as sg
import pyperclip

sg.theme("Topanga")
sg.set_options(font=('Georgia', 12))
#choose directory to work use pathlib.Path().home() 
#os.chdir(pathlib.Path().home().joinpath('Desktop'))
text1="""
THE RANSOM OF RED CHIEF[11]

It looked like a good thing: but wait till I tell you. “We were down South, in Alabama—Bill Driscoll and myself—when this kidnapping idea struck us. It was, as Bill afterward expressed it, “during a moment of temporary mental apparition”; but we didn’t find that out till later.

There was a town down there, as flat as a flannel-cake, and called Summit, of course. It contained inhabitants of as undeleterious and self-satisfied a class of peasantry as ever clustered around a Maypole.

Bill and me had a joint capital of about six hundred dollars, and we needed, just two thousand dollars more to pull off a fraudulent town-lot scheme in Western Illinois with. We talked it over on the front steps of the hotel. Philoprogenitiveness, says we, is strong in semirural communities; therefore, and for other reasons, a kidnapping project ought to do better there than in the radius of newspapers that send reporters out in plain clothes to stir up talk about such things. We knew that Summit couldn’t get after us with anything stronger than constables and, maybe, some lackadaisical bloodhounds and a diatribe or two in the Weekly Farmers’ Budget. So, it looked good.

We selected for our victim the only child of a prominent citizen named Ebenezer Dorset. The father was respectable and tight, a mortgage fancier and a stern, upright collection-plate passer and forecloser. The kid was a boy of ten, with bas-relief freckles, and hair the color of[146] the cover of the magazine you buy at the news-stand when you want to catch a train. Bill and me figured that Ebenezer would melt down for a ransom of two thousand dollars to a cent. But wait till I tell you.

About two miles from Summit was a little mountain, covered with a dense cedar brake. On the rear elevation of this mountain was a cave. There we stored provisions.

One evening after sundown, we drove in a buggy past old Dorset’s house. The kid was in the street, throwing rocks at a kitten on the opposite fence.

“Hey, little boy!” says Bill, “would you like to have a bag of candy and a nice ride?”

The boy catches Bill neatly in the eye with a piece of brick.

“That will cost the old man an extra five hundred dollars,” says Bill, climbing over the wheel.

That boy put up a fight like a welter-weight cinnamon bear; but, at last, we got him down in the bottom of the buggy and drove away. We took him up to the cave, and I hitched the horse in the cedar brake. After dark I drove the buggy to the little village, three miles away, where we had hired it, and walked back to the mountain.

Bill was pasting court-plaster over the scratches and bruises on his features. There was a fire burning behind the big rock at the entrance of the cave, and the boy was watching a pot of boiling coffee, with two buzzard tail-feathers stuck in his red hair. He points a stick at me when I come up, and says:

“Ha! cursed paleface, do you dare to enter the camp of Red Chief, the terror of the plains?”

“He’s all right now,” says Bill, rolling up his trousers and examining some bruises on his shins. “We’re playing Indian. We’re making Buffalo Bill’s show look[147] like magic-lantern views of Palestine in the town hall. I’m Old Hank, the Trapper, Red Chief’s captive, and I’m to be scalped at daybreak. By Geronimo! that kid can kick hard.”

Yes, sir, that boy seemed to be having the time of his life. The fun of camping out in a cave had made him forget that he was a captive himself. He immediately christened me Snake-eye, the Spy, and announced that, when his braves returned from the warpath, I was to be broiled at the stake at the rising of the sun.
"""



layout = [
#     [sg.Listbox(data, size=(max(map(len, data))+2, 10), key='LISTBOX')],
    [sg.Multiline(text1,size=(42,20), key='-LINES-', )],
    [sg.Button("Make Title", key="-TITLE-", size=(10,1)), sg.Button("Upper Case", key="-UPPER-",size=(10,1)), sg.Button("Lower case", key="-LOWER-",size=(10,1))],
    [sg.Button("Copy", key="-COPY-",size=(10,1)), sg.Button("Paste", key="-PASTE-",size=(10,1)),sg.Button("Clear", key="-CLEAR-",size=(10,1)),],
    [sg.Button("Exit", key="-OK-",size=(30,1))], 
]

window = sg.Window('Title', layout)
#listbox = window['LISTBOX']

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event=="-OK-":
        break
    
    if event == "-TITLE-":
        text=values['-LINES-']
        text= text.title()
        #sg.popup(text)
        window['-LINES-'].update(text)
        continue
    
    if event == "-UPPER-":
        text=values['-LINES-']
        text= text.upper()
        #sg.popup(text)
        window['-LINES-'].update(text)
        continue
    
    if event == "-LOWER-":
        text=values['-LINES-']
        text= text.lower()
        #sg.popup(text)
        window['-LINES-'].update(text)
        continue
    
    if event == "-COPY-":
        text=values['-LINES-']
        if text is None: continue
        pyperclip.copy(text)
        continue
    
    if event == "-CLEAR-":
        window['-LINES-'].update("")
        continue
    
    if event == "-PASTE-":
        text=pyperclip.paste()
        if text is None: continue
        window['-LINES-'].update(text)
        continue
window.close()

