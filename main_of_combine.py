

import tkinter
import tkinter.messagebox
import customtkinter
from random import randint,choice
import PIL.Image as image
import webbrowser
import os
from functions import *

#Theme setting
customtkinter.set_default_color_theme("dark-blue")


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
         
        #We need to do with image input and number of image expected (important)
        self.input_image_dir = "./documentation_images/group5.jpg" #default img show group name
        self.number_Expected = 1
        

        # configure window
        self.title("Image Augmentation")
        self.geometry(f"{1100}x{580}")

        # configure grid layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure(1, weight=1)




        #Show group information (Not important)
        self.sidebar_frame = customtkinter.CTkFrame(self, 
                                                    width=140, 
                                                    corner_radius=0)
        
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)


        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame,
                                                 text="Image\n\nAugmentation",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))


        #Git hub button
        self.github_button = customtkinter.CTkButton(self.sidebar_frame, 
                                                        command=self.click_gitHub,
                                                        text = "Git Hub")
        self.github_button.grid(row=1, column=0, padx=20, pady=10)


        #Facebook button
        self.facebook_button = customtkinter.CTkButton(self.sidebar_frame, 
                                                        command=self.click_facebook,
                                                        text = "Facebook")
        self.facebook_button.grid(row=2, column=0, padx=20, pady=10)
        


        
        
        
        #Run button (IMPPORTANT)
        self.RunButton = customtkinter.CTkButton(self.sidebar_frame,    
                                                        width=120, 
                                                        height=80,
                                                        text="Run",
                                                        font=customtkinter.CTkFont(size=30),
                                                        command=self.run_button) 

        self.RunButton.grid(row=6, column=0)





        # create tabview to show the input image
        self.input_image = customtkinter.CTkTabview(self, width=250)
        self.input_image.grid(row=0, column=1, padx=(
            10, 0), pady=(20, 0), sticky="nsew")

        self.random_num_image = customtkinter.CTkButton(self.input_image, text="Choose a image:",
                                                        command=self.choose_image_event)
        self.random_num_image.grid(row=1, column=0)

        self.input_dir = customtkinter.CTkEntry(self.input_image,
                                                placeholder_text="Input image directory",
                                                )
        self.input_dir.grid(row=2, column=0, columnspan=2,
                            padx=10, pady=5, sticky="nsew")

        # Show a loading img (if there's no image)
        
       
        img = image.open("./documentation_images/group5.jpg")
        resized_img = img.resize((200, 200))
        ctk_img = customtkinter.CTkImage(resized_img, size=(200, 200))
        self.original_img = customtkinter.CTkLabel(
            self.input_image, image=ctk_img, text="")
        self.original_img.grid(row=3, column=0, columnspan=2,
                               padx=10, pady=5, sticky="nsew")


    # create tabview to ask user how many image is enough

        self.num_frame = customtkinter.CTkFrame(self)
        self.num_frame.grid(row=0, column=2, sticky="nsew",padx=(20,0), pady=(20,0))
        self.num_frame.grid_rowconfigure(2, weight=1) 
        self.num_frame.grid_columnconfigure(0, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.num_frame,
                                                 text="How many image?",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=1, column=0, padx=20, pady=(20, 20))
        self.num_frame.grid_rowconfigure(4, weight=1)
        

        
        self.random_num_image = customtkinter.CTkButton(self.num_frame,
                                                        text="Random a number",
                                                        command=self.random_number_event)
        self.random_num_image.grid(row=4, column=0)
        
        self.nums_show = customtkinter.CTkEntry(self.num_frame,
                                                placeholder_text="Number expect",
                                                )
        self.nums_show.grid(row=5, column=0, columnspan=2,
                            padx=10, pady=(20, 20), sticky="nsew")



        #The frame show the random output (Important)

        self.res_frame = customtkinter.CTkFrame(self)
        self.res_frame.grid(row=1, column=1, rowspan=4, sticky="nsew",padx=( 10, 0), pady=(20, 0))
        self.res_frame.grid_rowconfigure(2, weight=1) 
        self.res_frame.grid_columnconfigure(0, weight=1)

        self.logo_label = customtkinter.CTkLabel(self.res_frame,
                                                 text="Your result here",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=2, column=0, padx=20, pady=(20, 20))
        self.res_frame.grid_rowconfigure(4, weight=1)

        
        
        #Show a "result picture" first
        img = image.open("./documentation_images/result.jpg")
        resized_img = img.resize((200, 200))
        ctk_img = customtkinter.CTkImage(resized_img, size=(250, 250))
        self.random_img = customtkinter.CTkLabel(
            self.res_frame, image=ctk_img, text="")
        self.random_img.grid(row=3, column=0, columnspan=2,
                               padx=10, pady=5, sticky="nsew")

        
        self.randomimgbutton = customtkinter.CTkButton(self.res_frame, text="Click here to random one",
                                                        command=self.show_random_img)
        self.randomimgbutton.grid(row=4,padx = (20,20) , pady = (20,20))
    
    
    
    
        #Create switch for SETTING OPTIONS
        self.scrollable_frame = customtkinter.CTkScrollableFrame(
            self, label_text="Image Processing Options")
        self.scrollable_frame.grid(row=1, column=2, padx=(
            20, 0), pady=(20, 0), sticky="nsew")
        self.scrollable_frame.grid_columnconfigure(0, weight=1)
        self.scrollable_frame_switches = []
        #Make options
        switch_texts = {0:"Crop", 
                        1:"Flip",
                        2:"Rotate",
                        3:"Blur",
                        4:"Filter",
                        5: "Gray Scale",
                        6 : "Edge Detection"  
                        }   #A dictionary save the options
        for i in range(7):
            switch = customtkinter.CTkSwitch(
                master=self.scrollable_frame, text=f"{switch_texts[i]}")
            switch.grid(row=i, column=0, padx=10, pady=(0, 20))
            self.scrollable_frame_switches.append(switch)
            
    
    #The last col show the information of the picture (text box)
        self.image_informations_tag = customtkinter.CTkTextbox(self, 
                                                               width=250,
                                                               font=customtkinter.CTkFont(size=15))
        self.image_informations_tag.grid(row=0, column=3, padx=(20, 5), pady=(20, 5), sticky="nsew")
        self.textbox2 = customtkinter.CTkTextbox(self, width=250)
        self.textbox2.grid(row=1, column=3, padx=(20, 5), pady=(20, 5), sticky="nsew")
        self.textbox2.insert("0.0","User manual\n\n1. Choose the image's directory\n\n2.Choose the number of images expect\n\n3.Choose options\n\n4.Choose the output folder directory\n\n5.Click Run\n\n6.Click 'Random one' to show a random ouput image")






    #______________________________________________________________FUNC_____________________________________________________
    #Show a random result image
    def show_random_img(self):
        #Get Paths
        all_output_img_path = os.path.join(os.getcwd(), "./output") 
        files = os.listdir(all_output_img_path)
        rd_img_name = choice(files)
        rd_img_path = os.path.join(all_output_img_path, rd_img_name)
        
        #Show img
        img = image.open(rd_img_path)
        resized_img = img.resize((200, 200))
        ctk_img = customtkinter.CTkImage(resized_img, size=(250, 250))
        self.random_img = customtkinter.CTkLabel(
            self.res_frame, image=ctk_img, text="")
        self.random_img.grid(row=3, column=0, columnspan=2,
                               padx=10, pady=5, sticky="nsew")


    #Browse a image
    def choose_image_event(self):
        #Show file directory
        self.input_dir.delete(0,tkinter.END)
        image_path = tkinter.filedialog.askopenfilename()
        self.input_dir.insert(0, image_path)
        
        # Show the original img
        img = image.open(image_path)
        img_name = image_path.split("/")[-1]
        width,height = img.size
        img_format = img.format
        resized_img = img.resize((200, 200))
        ctk_img = customtkinter.CTkImage(resized_img, size=(200, 200))
        self.original_img.configure(image=ctk_img)
        self.input_image_dir = image_path
        
        #Show img infomations
        self.image_informations_tag.delete("0.0",tkinter.END)
        self.image_informations_tag.insert("0.0",str(img_name)+"\n\nSize:"+str(width)+' x '+ str(height) + "\n\nFormat:" + str(img_format))

        




    #Get the number of output image
    def random_number_event(self):
        random_number = randint(0, 20)
        self.nums_show.delete(0, tkinter.END)
        self.nums_show.insert(0, str(random_number))
        self.number_Expected = random_number  # assign it to the number_Expected



   
    #Everything start when click run button
    def run_button(self):
        #Get number expect ,default = 5
        try:

            self.number_Expected = int(self.nums_show.get())
        except :
            self.number_Expected = 5
            
        
        #Delete Old Things
        for file in os.listdir("./output"):
            os.remove(os.path.join("./output", file))



        #Save the status of editting buttons 1: On 0:Off
        statuses = []
        for i in range(7):
            if self.scrollable_frame_switches[i].get():
                statuses.append(1)
            else:
                statuses.append(0)



        #Make changes for each images and save it (IMPORTANT)
        for i in range(self.number_Expected):

            #Open image
            self.input_image_dir = self.input_dir.get()
            
            img = cv2.imread(self.input_image_dir)
            if img is None:
                self.show_popup_error("CAN NOT OPEN THIS PATH!!!")
                break
            #Changes
            if statuses[0] == 1 : #Crop
                img = crop_image(img)
                
            if statuses[1] == 1 : #Flip
                img = flip_image(img)
                
            if statuses[2] == 1 : #Rotate
                img = rotate_image(img)
                
            if statuses[3] == 1 : #Blur
                img = blur_image(img)
                
            if statuses[4] == 1 : #Filter

                try:
                    img = change_color_image(img)
                except:
                    
                    self.show_popup_error("A RANDOM FILTER CAN NOT RUN WITH THIS IMAGE")
                    continue


                
            if statuses[5] == 1 : #Gray Scale
                img = gray_scale(img)
                
            if statuses[6] == 1 : #Edge Detection
                img = find_edge(img)

            

        try:
            #Show the first output image
            all_output_img_path = os.path.join(os.getcwd(), "./output") 
            files = os.listdir(all_output_img_path)
            rd_img_name = choice(files)
            rd_img_path = os.path.join(all_output_img_path, rd_img_name)
            #Show img
            img = image.open(rd_img_path)
            resized_img = img.resize((200, 200))
            ctk_img = customtkinter.CTkImage(resized_img, size=(250, 250))
            self.random_img = customtkinter.CTkLabel(
                self.res_frame, image=ctk_img, text="")
            self.random_img.grid(row=3, column=0, columnspan=2,
                                padx=10, pady=5, sticky="nsew")
        except Exception as e :
            self.show_popup_error(e)


            
        


    #Click some in4 of coder
    def click_gitHub(self):
        webbrowser.open("https://github.com/sinhvienfpt")
    
    def click_facebook(self):

        webbrowser.open("https://www.facebook.com/nghoangziet/")
        
    def show_popup_error(self,s):
        if str(s) == "Cannot choose from an empty sequence":
            s = "There's nothing in the output folder. Maybe you forgot to choose an option!"
        dialog = customtkinter.CTkInputDialog(
            text=s, title="NOTIFICATION")

if __name__ == "__main__":
    output_path = os.path.join(os.getcwd(), "./output")
    # make a folder output if it doesn't exist
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    app = App()

    app.mainloop()
