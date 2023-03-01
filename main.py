import tkinter as tk
import pyvjoy
import pynput as pp
import codecs
import os

gears_id = ['']*9
vjoy_device = 1
bg_def = '#3E3E3E'
fg_def = '#DADADA'
gray = '#9C9C9C'
white = '#FFFFFF'

def release_keys():
    for key in range(1, 9):
        vjoy.set_button(key, 0)

def on_press(key):
    #if type(key) == "<class 'pynput.keyboard._win32.KeyCode'>":
    if isinstance(key, type(pp.keyboard.KeyCode(char='1'))):
        '''if key.char == '1':
            release_keys()
            vjoy.set_button(1, 1)
        elif key.char == '2':
            release_keys()
            vjoy.set_button(2, 1)
        elif key.char == '3':
            release_keys()
            vjoy.set_button(3, 1)
        elif key.char == '4':
            release_keys()
            vjoy.set_button(4, 1)
        elif key.char == '5':
            release_keys()
            vjoy.set_button(5, 1)
        elif key.char == '6':
            release_keys()
            vjoy.set_button(6, 1)
        elif key.char == '7':
            release_keys()
            vjoy.set_button(7, 1)
        elif key.char == '`':
            release_keys()
            vjoy.set_button(8, 1)
        elif key.char == 'q':
            release_keys()'''
        if key.char in gears_id:
            release_keys()
            if gears_id.index(key.char)+1 != 9:
                vjoy.set_button(gears_id.index(key.char)+1, 1)
    else:
        print('no!')

def start_listening():
    global listener
    listener = pp.keyboard.Listener(on_press=on_press)
    listener.start()
    startButton.configure(text='End', command = stop_listening)

def stop_listening():
    global listener
    #pp.keyboard.Listener.stop(listener)
    release_keys()
    listener.stop()
    startButton.configure(text='Start', command=start_listening)

def start(*args):
    global vjoy
    vjoy = pyvjoy.VJoyDevice(vjoy_device)
    start_listening()


def save_settings(*args):
    global gears_id, vjoy_device
    error_flag = False
    for i in range(0, 9):
        var = gears[i].entry.get()
        if len(var) == 1:
            gears_id[i] = var
            if error_flag is False:
                errorLabel.configure(text='')
        else:
            error_flag = True
            errorLabel.configure(text='Variable with length != 1 is not saved')

    var = vjoyEntry.get()
    if len(var) != 0:
        vjoy_device = int(var)
    else:
        errorLabel.configure(text='Please set up vJoy device')

    new_settings = f'''vJoy device:{vjoy_device}
1st gear:{gears_id[0]}
2nd gear:{gears_id[1]}
3rd gear:{gears_id[2]}
4th gear:{gears_id[3]}
5th gear:{gears_id[4]}
6th gear:{gears_id[5]}
7th gear:{gears_id[6]}
reverse gear:{gears_id[7]}
neutral gear:{gears_id[8]}'''
    with codecs.open(os.getcwd() + "\settings.txt", "w", encoding='utf-8') as a:
        a.write(new_settings)

def get_value(var, settings):
    output = ''

    i = settings.find(var)+len(var)
    while True:
        if i < len(settings):
            if settings[i] != '\n':
                output += settings[i]
                i += 1
            else:
                break
        else:
            break
    #print(var, output)
    output = output.replace(' ', '')
    return output

def import_settings(*args):
    global gears_id, vjoy_device
    with codecs.open(os.getcwd() + "\settings.txt", "r", encoding='utf-8') as a:
        settings = a.read()
        b = settings.split('\r')
        settings = ''
        for i in b:
            settings += i

    vjoy_device = int(get_value('vJoy device:', settings))
    gears_id[0] = get_value('1st gear:', settings)
    gears_id[1] = get_value('2nd gear:', settings)
    gears_id[2] = get_value('3rd gear:', settings)
    gears_id[3] = get_value('4th gear:', settings)
    gears_id[4] = get_value('5th gear:', settings)
    gears_id[5] = get_value('6th gear:', settings)
    gears_id[6] = get_value('7th gear:', settings)
    gears_id[7] = get_value('reverse gear:', settings)
    gears_id[8] = get_value('neutral gear:', settings)

def set_value(setting, value):
    if setting.entry.get() != '':
        setting.entry.delete(0, len(setting.entry.get()))
    setting.entry.insert(0, value)

if "settings.txt" in os.listdir(os.getcwd()):
    import_settings()
else:
    with codecs.open(os.getcwd() + "\settings.txt", "w", encoding='utf-8') as a:
        a.write('''vJoy device:1
1st gear:1
2nd gear:2
3rd gear:3
4th gear:4
5th gear:5
6th gear:6
7th gear:7
reverse gear:`
neutral gear:q''')
    import_settings()


app = tk.Tk()

app.configure(width=400, height=200, background=bg_def)
app.resizable(0, 0)
app.title('H-Shifter for AC')


if "dont_steal_this.ico" in os.listdir(os.getcwd()):
    app.iconbitmap(os.getcwd() +"\dont_steal_this.ico")


gearFrame = tk.Frame(app, highlightthickness=1, highlightcolor=white, highlightbackground=gray,
                     width=322, height=77, bg=bg_def)
gearFrame.place(x=40, y=50)

class Gear:
    def __init__(self, id):
        frame = tk.Frame(gearFrame,
                         width=80, height=25, bg=bg_def)
        label = tk.Label(frame, text='{0}:'.format(id),
                         bg=bg_def, fg=fg_def)
        self.entry = tk.Entry(frame, bg=bg_def, fg=white)

        label.place(x=14, y=0, height=18)
        self.entry.place(x=35, y=0, height=18, width=20)
        if id == 'R':
            self.entry.insert(0, str(gears_id[7]))
            frame.place(x=240, y=25)
        elif id == 'N':
            self.entry.insert(0, str(gears_id[8]))
            frame.place(x=0, y=50)
        else:
            self.entry.insert(0, str(gears_id[id-1]))
            frame.place(x=(id-1)//2*80, y=(id-1)%2*25)

gears = []
for i in range(1, 8):
    gears.append(Gear(i))
gears.append(Gear('R'))
gears.append(Gear('N'))

vjoyFrame = tk.Frame(app, highlightthickness=1, highlightcolor=white, highlightbackground=gray,
                     width=100, height=25, bg=bg_def)
vjoyLabel = tk.Label(vjoyFrame, text='vJoy device:',
                     bg=bg_def, fg=fg_def)
vjoyEntry = tk.Entry(vjoyFrame, bg=bg_def, fg=white)
vjoyEntry.insert(0, vjoy_device)
vjoyFrame.place(x=40, y=13)
vjoyLabel.place(x=3, y=3, height=18)
vjoyEntry.place(x=70, y=3, height=18, width=20)

errorLabel = tk.Label(gearFrame, bg=bg_def, fg='red',)
errorLabel.place(x=80, y=50, width=240, height=25)

saveButton = tk.Button(app, command=save_settings, text='Save settings',
                       bg=bg_def, fg=fg_def)
saveButton.place(x=40, y=150, height=25, width=80)

startButton = tk.Button(app, text='Start', command = start,
                        bg=bg_def, fg=fg_def)
startButton.place(x=280, y=150, height=25, width=80)

app.mainloop()
