import tkinter as tk
import random

#By Moises De Arcos And Luis Ponce

#pygame.mixer.init()


class Game:
  state = {"remote_pressed": False}

  def __init__(self, root):
    global count
    self.count = 1
    global remote
    self.remote = False
    global correct_code
    self.correct_code = "2012"
    global lighters
    self.lighters = False
    global doorknobss
    self.doorknobss = False
    self.root = root
    self.load_sounds()
    self.first_room()
    self.second_room()
    self.third_room()
    self.place_1room()
    self.arrows()
    self.place_arrows()
    self.init_boxattributes()
    #self.play_background_music(1)

  def load_sounds(self):
    # Background music for each room
    self.room1_bg_music = "./sounds/firstroom.mp3"
    self.room2_bg_music = "./sounds/static.mp3"
    self.room3_bg_music = "./sounds/creepy.mp3"

    # Sound effects
    self.button_click_sound = "./sounds/click.mp3"
    self.door_unlock_sound = "./sounds/open.mp3"
    self.chest_open_sound = "./sounds/chest.mp3"
    self.drawer_open_sound = "./sounds/drawer.mp3"
    self.tv_on_sound = "./sounds/tvon.mp3"

    self.code_error_sound = "./sounds/wrongcode.mp3"

    self.current_bg_music = None

  #def play_sound(self, sound_file):

   # try:
    #  sound = pygame.mixer.Sound(sound_file)
   #   sound.play()
   # except:
    #  print(f"Error playing sound: {sound_file}")

 # def play_background_music(self, room_number):

 #   pygame.mixer.music.stop()

  #  if room_number == 1:
  #    bg_music = self.room1_bg_music
  #  elif room_number == 2:
  #    bg_music = self.room2_bg_music
  #  elif room_number == 3:
  #    bg_music = self.room3_bg_music

  ##  try:
  #    pygame.mixer.music.load(bg_music)
  #    pygame.mixer.music.play(-1)
  #    self.current_bg_music = bg_music
  #  except:
  #    print(f"Error loading background music: {bg_music}")

  def init_boxattributes(self):
    self.semicolon = tk.Label(self.root,
                              font=("Arial", 9),
                              text=":",
                              height=1,
                              width=1,
                              bg="#9d9b9c")

    picdown = tk.PhotoImage(file="Pictures/downarrow.png")
    self.downarrow = tk.Button(self.root,
                               image=picdown,
                               height=29,
                               width=29,
                               command=self.down_arrow)
    self.downarrow.image = picdown

    self.confirm = tk.Label(self.root, height=1, width=6, bg="#999999")

    self.confirm.bind("<Button-1>", self.confirms)

    global text1
    global text2
    global text3
    global text4
    self.text1 = "0"
    self.text2 = "0"
    self.text3 = "0"
    self.text4 = "0"

    self.number1 = tk.Label(self.root,
                            font=("Arial", 12),
                            text=self.text1,
                            height=1,
                            width=1,
                            bg="#bbbbbb")
    self.number1.bind("<Button-1>", self.num1)

    self.number2 = tk.Label(self.root,
                            font=("Arial", 12),
                            text=self.text2,
                            height=1,
                            width=1,
                            bg="#bbbbbb")
    self.number2.bind("<Button-1>", self.num2)

    self.number3 = tk.Label(self.root,
                            font=("Arial", 12),
                            text=self.text3,
                            height=1,
                            width=1,
                            bg="#bbbbbb")
    self.number3.bind("<Button-1>", self.num3)

    self.number4 = tk.Label(self.root,
                            font=("Arial", 12),
                            text=self.text4,
                            height=1,
                            width=1,
                            bg="#bbbbbb")
    self.number4.bind("<Button-1>", self.num4)

  def num1(self, event):
    #self.play_sound(self.button_click_sound)
    self.text1 = int(self.text1)
    if self.text1 == 9:
      self.text1 = 0
    else:
      self.text1 = self.text1 + 1
      self.text1 = str(self.text1)
    self.number1.config(text=self.text1)

  def num2(self, event):
    #self.play_sound(self.button_click_sound)
    self.text2 = int(self.text2)
    if self.text2 == 9:
      self.text2 = 0
    else:
      self.text2 = self.text2 + 1
      self.text2 = str(self.text2)
    self.number2.config(text=self.text2)

  def num3(self, event):
    #self.play_sound(self.button_click_sound)
    self.text3 = int(self.text3)
    if self.text3 == 9:
      self.text3 = 0
    else:
      self.text3 = self.text3 + 1
      self.text3 = str(self.text3)
    self.number3.config(text=self.text3)

  def num4(self, event):
    #self.play_sound(self.button_click_sound)
    self.text4 = int(self.text4)
    if self.text4 == 9:
      self.text4 = 0
    else:
      self.text4 = self.text4 + 1
      self.text4 = str(self.text4)
    self.number4.config(text=self.text4)

  def boxattributes(self):
    self.semicolon.place(x=396, y=245)
    self.downarrow.place(x=390, y=470)
    self.number1.place(x=345, y=243)
    self.number2.place(x=381, y=243)
    self.number3.place(x=418, y=243)
    self.number4.place(x=452, y=243)
    self.confirm.place(x=380, y=198)

  def boxattributes_forget(self):
    self.semicolon.place_forget()
    self.downarrow.place_forget()
    self.number1.place_forget()
    self.number2.place_forget()
    self.number3.place_forget()
    self.number4.place_forget()
    self.confirm.place_forget()
    self.description.place_forget()

  def confirms(self, event):
    #self.play_sound(self.button_click_sound)
    textcheck1 = int(self.text1)
    textcheck2 = int(self.text2)
    textcheck3 = int(self.text3)
    textcheck4 = int(self.text4)

    if textcheck1 == 0 and textcheck2 == 6 and textcheck3 == 1 and textcheck4 == 3:
      self.description.config(text="You got a lighter!", width=15)
      self.description.place(x=300, y=0)
      self.lighters = True
      #Make Chest Noise
      #self.play_sound(self.chest_open_sound)
    #else:
      #self.play_sound(self.code_error_sound)

  def doorknobs(self, event):
    #self.play_sound(self.button_click_sound)
    if self.doorknobss == True:
      self.description.config(text="You found a remote!")
      self.description.place(x=300, y=0)
      self.remote = True
      #Make Drawer Noise
      #self.play_sound(self.drawer_open_sound)

  def boxes(self, event):
    #self.play_sound(self.button_click_sound)
    self.secondroom.place_forget()
    self.box.place_forget()
    self.buttons.place_forget()
    self.tv.place_forget()
    self.leftarrow.place_forget()
    self.rightarrow.place_forget()

    self.Boxcode.place(x=-100, y=-250)
    self.boxattributes()

  def down_arrow(self):
    #self.play_sound(self.button_click_sound)
    self.Boxcode.place_forget()
    self.boxattributes_forget()

    self.place_2room()
    self.place_arrows()

  def buttonss(self, event):
    #self.play_sound(self.button_click_sound)
    if self.remote == True:
      self.tv.place(x=275, y=35)
      self.buttons.place_forget()
      #Make TV Noise
      #self.play_sound(self.tv_on_sound)

  def lighter(self, event):
    #self.play_sound(self.button_click_sound)
    if self.lighters == True:
      self.description.config(text="A doorknob spawned in your hand. ",
                              width=30)
      self.description.place(x=300, y=0)
      fireimage = tk.PhotoImage(file="Pictures/Fire.png")
      self.light.config(image=fireimage, height=65, width=56)
      self.light.image = fireimage
      self.doorknobss = True
      #Make Fire Noise

  def show_code_entry(self):
    #self.play_sound(self.button_click_sound)
    self.code_window = tk.Toplevel(self.root)
    self.code_window.title("Door Code")
    self.code_window.geometry("300x150")
    self.code_window.resizable(False, False)

    screen_width = self.root.winfo_screenwidth()
    screen_height = self.root.winfo_screenheight()
    x = (screen_width - 300) // 2
    y = (screen_height - 150) // 2
    self.code_window.geometry(f"300x150+{x}+{y}")

    code_frame = tk.Frame(self.code_window, padx=20, pady=20)
    code_frame.pack(fill="both", expand=True)

    label = tk.Label(code_frame, text="Enter the door code:")
    label.pack(pady=(0, 10))

    self.code_entry = tk.Entry(code_frame,
                               font=("Arial", 12),
                               justify="center",
                               show="*")
    self.code_entry.pack(pady=(0, 10))
    self.code_entry.focus_set()

    button_frame = tk.Frame(code_frame)
    button_frame.pack(fill="x")

    submit_button = tk.Button(button_frame,
                              text="Submit",
                              command=self.check_code)
    submit_button.pack(side="left", padx=(0, 5), expand=True, fill="x")

    cancel_button = tk.Button(button_frame,
                              text="Cancel",
                              command=self.code_window.destroy)
    cancel_button.pack(side="right", padx=(5, 0), expand=True, fill="x")

    self.code_entry.bind("<Return>", lambda event: self.check_code())

    self.code_window.transient(self.root)
    self.code_window.grab_set()
    self.root.wait_window(self.code_window)

  def check_code(self):

    entered_code = self.code_entry.get()
    if entered_code == self.correct_code:
      result_window = tk.Toplevel(self.root)
      result_window.title("Success!")
      result_window.geometry("250x100")

      screen_width = self.root.winfo_screenwidth()
      screen_height = self.root.winfo_screenheight()
      x = (screen_width - 250) // 2
      y = (screen_height - 100) // 2
      result_window.geometry(f"250x100+{x}+{y}")

      label = tk.Label(result_window,
                       text="Door unlocked! You escaped!",
                       font=("Arial", 12))
      label.pack(pady=20)

      self.code_window.destroy()
    else:
      self.code_entry.delete(0, tk.END)
      self.code_window.after(100,
                             lambda: self.code_entry.config(background="red"))
      self.code_window.after(
          300, lambda: self.code_entry.config(background="white"))

  #we can use this function to keep placing the firstroom
  def first_room(self):
    #FIRST ROOM
    picture = tk.PhotoImage(file="Pictures/Door.png")
    lock_img = tk.PhotoImage(file="Pictures/smart-lock.png")
    
    

    self.firstroom = tk.Label(self.root,
                              image=picture,
                              height=1000,
                              width=1000)
    self.firstroom.image = picture

    self.lock = tk.Button(
        self.root, image=lock_img,
        command=self.show_code_entry, height =100, width=100)  #add funtion to add number code
    self.lock.image = lock_img

    # we will set this for every pressable puzzle
    self.doorknob = tk.Label(self.root, height=1, width=1, bg="#737373")
    self.doorknob.bind("<Button-1>", self.doorknobs)

  def second_room(self):
    #SECOND ROOM
    picture1 = tk.PhotoImage(file="Pictures/TV.png")

    self.secondroom = tk.Label(self.root,
                               image=picture1,
                               height=1000,
                               width=1000)
    self.secondroom.image = picture1

    self.box = tk.Label(self.root, height=1, width=1, bg="#898989")
    self.box.bind("<Button-1>", self.boxes)

    button_text = "2023"

    button_text = str(random.randint(1000, 9999))
    self.correct_code = button_text
    self.buttons = tk.Label(self.root, height=10, width=30, bg="#efefef")
    self.buttons.bind("<Button-1>", self.buttonss)

    self.tv = tk.Label(self.root,
                       text=button_text,
                       height=10,
                       width=30,
                       bg="#efefef")

    Boximage = tk.PhotoImage(file="Pictures/Box.png")
    self.Boxcode = tk.Label(self.root, image=Boximage, height=1000, width=1000)
    self.Boxcode.image = Boximage

  def third_room(self):
    #THIRDROOM
    picture2 = tk.PhotoImage(file="Pictures/Clock.png")
    self.thirdroom = tk.Label(self.root,
                              image=picture2,
                              height=1000,
                              width=1000)
    self.thirdroom.image = picture2
    self.light = tk.Label(self.root, height=4, width=6, bg="#151515")
    self.light.bind("<Button-1>", self.lighter)

    self.description = tk.Label(self.root,
                                text="",
                                height=1,
                                width=30,
                                bg="#989898")

  def arrows(self):
    #ARROWS
    picture3 = tk.PhotoImage(file="Pictures/RightArrow.png")
    self.rightarrow = tk.Button(self.root,
                                image=picture3,
                                height=45,
                                width=65,
                                command=self.move_room_right)
    self.rightarrow.image = picture3

    picture4 = tk.PhotoImage(file="Pictures/LeftArrow.png")
    self.leftarrow = tk.Button(self.root,
                               image=picture4,
                               height=45,
                               width=65,
                               command=self.move_room_left)
    self.leftarrow.image = picture4

  def place_1room(self):
    #remove mini labels from other rooms
    self.box.place_forget()
    self.buttons.place_forget()
    self.light.place_forget()
    self.tv.place_forget()
    self.description.place_forget()

    self.firstroom.place(x=-100, y=-250)
    center_x = 800 // 2
    center_y = 600 // 2
    lock_x = center_x - 50
    lock_y = center_y - 120
    self.lock.place(x=lock_x, y=lock_y)
    self.doorknob.place(x=185, y=305)
    #self.play_background_music(1)

  def place_2room(self):
    #remove mini labels from other rooms
    self.doorknob.place_forget()
    self.lock.place_forget()
    self.light.place_forget()
    self.description.place_forget()

    self.secondroom.place(x=-100, y=-250)
    self.box.place(x=675, y=235)
    self.buttons.place(x=275, y=35)
    #self.play_background_music(2)

  def place_3room(self):
    #remove mini labels from other rooms
    self.box.place_forget()
    self.buttons.place_forget()
    self.doorknob.place_forget()
    self.lock.place_forget()
    self.tv.place_forget()
    self.description.place_forget()

    self.thirdroom.place(x=-100, y=-250)
    self.light.place(x=358, y=200)

    #self.play_background_music(3)

  def place_arrows(self):
    self.leftarrow.place(x=1, y=450)
    self.rightarrow.place(x=730, y=450)

  def move_room_right(self):
    #self.play_sound(self.button_click_sound)
    if self.count == 1:
      self.count += 1
      self.firstroom.place_forget()
      self.place_2room()

    elif self.count == 2:
      self.count += 1
      self.secondroom.place_forget()
      self.place_3room()

    elif self.count == 3:
      self.count = 1
      self.thirdroom.place_forget()
      self.light.place_forget()
      self.place_1room()

  def move_room_left(self):
    #self.play_sound(self.button_click_sound)
    if self.count == 1:
      self.count = 3
      self.firstroom.place_forget()
      self.place_3room()

    elif self.count == 2:
      self.count -= 1
      self.secondroom.place_forget()
      self.place_1room()

    elif self.count == 3:
      self.count -= 1
      self.thirdroom.place_forget()
      self.light.place_forget()
      self.place_2room()

  def runMe(self):
    self.root.mainloop()

  #def __del__(self):
  #  pygame.mixer.music.stop()
  #  pygame.mixer.quit()


if __name__ == "__main__":
  root = tk.Tk()
  root.title("Escape Room")
  root.geometry("800x600")

  #pygame.init()

  game = Game(root)
  game.runMe()

  #pygame.quit()
