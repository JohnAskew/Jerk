'''
to-do
1. 
2. Add thread to sub-task (maybe ansync) to keep dragon (wake-word) listening.
3.add module chk_process with exename and command. 1 routine opens or closes all applications.

'''
import os, sys
sys.path.insert(0, "C:\\Users\\User\\Desktop\\python\\jerk\\" )
#print(*'*'*80)
#print(sys.path)
#print('*'*80)
try:
    from import_modules import *
except:
    print(f'Unable to find needed module "import_modules.py". Aborting with no action taken')
    sys.exit(0)

#sys.path.insert(1, "C:\\app\\Python")

try:
    import imagesize
except:
    os.system('pip install imagesize')
    import imagesize


try:
    import stdlib_list
except:
    os.system('pip install stdlib_list')
    import stdlib_list

try:
    import stdlib_utils
except:
    os.system('pip install stdlib_utils')
    import stdlib_utils

try:
    import PyQt5
except:
    os.system('pip install PyQt5')
    import PyQt5


from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import (QMainWindow, QTextEdit,
                             QAction, QFileDialog, QApplication)


try:
    import pyautogui
except:
    os.system('pip install pyautogui')
    import pyautogui

app = QApplication([])


try:
    import flask
except:
    os.system('pip install flask')
    import flask

try:

    import my_credentials

    try:

        import people_I_email

    except:

        print("Unable to load people_I_email.py\nYou will be unable to send mail using this app.")

except:

    print("Unable to load my_credentials.py\nYou will be unable to send mail using this app.")




#######################################
class Jerk:
#######################################
    WAKE="raven"

    def __init__(self):

        self.recognizer = sr.Recognizer()

    #--------------------------------------
    def check_file_systems(self):
    #--------------------------------------
        #DEBUG --> print(f'Entering function check_file_systems().')

        s.speak("I am checking file systems")
        engine.runAndWait()

        if os.path.isdir("./notes"):

            pass

        else:

            os.mkdir("notes")

        if os.path.isdir("screenshots"):

            pass

        else:

            os.mkdir("screenshots")

        if os.path.isdir("./archive"):

            pass

        else:

            os.mkdir("archive")

    #--------------------------------------
    def check_process(self, exename = 'chrome.exe'):
    #--------------------------------------

        s.speak("Checking all running processes")
        
        for proc in psutil.process_iter(['pid', 'name']):

            if proc.info["name"] == exename:

                s.speak(f"{sobriquet}, I see {exename} is currently running.")

                return True

        s.speak(f"{sobriquet}, I do not see {exename} running.")

        return False

    #--------------------------------------
    def close_process(self,exename):
    #--------------------------------------
        if s.check_process(exename):

            s.speak(f"Closing {exename}")

            os.system(f"TASKKILL /F /IM {exename}")


    #--------------------------------------
    def defrag_drive(self):
    #--------------------------------------

        #os.system('cmd /k defrag.exe C: /U /D /V')
        subprocess.call(['runas', '/user:Administrator', 'cmd.exe /k defrag.exe C: /U /D /V'])
    #--------------------------------------
    def find_search_words(self, command):
    #--------------------------------------

        if SEARCH_WORDS.get(command.split(' ')[0]) == command.split(' ')[0]:

            return True
    #--------------------------------------
    def find_wiki_words(self, command):
    #--------------------------------------

        if WIKI_WORDS.get(command.split(' ')[0]) == command.split(' ')[0]:

            return True

    #--------------------------------------
    def get_audio(self):
    #--------------------------------------
         #DEBUG --> print(f'Entering function get_audio()')
         r = sr.Recognizer()

         with sr.Microphone() as source:

            audio = r.listen(source, timeout = 15.0)

            said = ""

            try:
                
                said = r.recognize_google(audio)

                print("Said: " + str(said))

            except Exception as e:

                print("Exception " + str(e))

         return said.lower()

    #--------------------------------------
    def get_audio_sub(self):
    #--------------------------------------
         #DEBUG --> print(f'Entering function get_audio_sub()')
         r_sub = sr.Recognizer()

         with sr.Microphone() as source_sub:

            audio_sub = r_sub.listen(source_sub, timeout = 10.0)

            said = ""

            try:
                
                said = r_sub.recognize_google(audio_sub)

                print("Said: " + str(said))

            except Exception as e:

                print("Exception " + str(e))

         return said.lower()

    #--------------------------------------
    def get_audio_long(self):
    #--------------------------------------
         #DEBUG --> print(f'Entering function get_audio_long')
         r = sr.Recognizer()

         with sr.Microphone() as source:

            audio = r.listen(source)

            said = ""

            try:
                
                said = r.recognize_google(audio)

                print("Said: " + str(said))

            except Exception as e:

                print("Exception " + str(e))

         return said.lower()

    #--------------------------------------
    def get_news(self, command):
    #--------------------------------------
        

        if (command == None or command == False):

        
            s.speak("What news subject?")

            command = s.get_audio_sub().lower()

        try:

            self.text = command

            print(f"get_news heard {self.text}")
            s.speak("Researching...")
            # googlenews.get_news(self.text)

            # news_results = googlenews.result()

            # print(news_results)

            try:
                from pygooglenews import GoogleNews

            except:
                os.system('pip install pygooglenews')
                from pygooglenews import GoogleNews

            gn = GoogleNews()
            top = gn.top_news()
            entries = top["entries"]
            count =0 
      
            for entry in entries:
                
                print(f'{count=}.{entry["title"]} {entry["published"]}')
                s.speak('Here is the recent public news')
                s.speak(str(count))
                s.speak('entitled' + entry["title"])
                s.speak('published' + entry["published"])
                count = count + 1

        except Exception as e:

            print(f"Error with instantiating googlenews")

            s.speak(f"Error with instantiating googlenews")

            s.speak(e)

            sys.exit(-1)

            #googlenews.search(self.text)

        


        
            #s.speak(self.text)

            news_limit = 8

            new_cnt = 0 

            try:

                for news_result in news_results:

                    for key1, value1 in news_result.items():

                        datez = ""

                        if key1 in ('title'):

                            title = str(value1)

                        if key1 in ('date'):

                            datez = str(value1)

                            if ('ago' in datez and 'hours' in datez):

                                print("date: " + str(datez) + ", title: " + str(title) + "\n")

                                s.speak("date: " + str(datez) + ", title: " + str(title) + "\n")


            except Exception as e:
            #except:

                print("Error with parsing news_results")

                print(e)

                s.speak(f"Error with parsing news_results {e}")

        # except:

        #     s.speak("I do not understand what news you are asking for about.." + self.text)

        s.speak("End of news report.")
    #
    # Listening
    #
    #--------------------------------------
    def hear(self, recognizer, microphone, response):
    #--------------------------------------
        #DEBUG --> print(f'Entering function hear()')
        try:

            with microphone as source:

                print("Waiting for a command.")


                recognizer.adjust_for_ambient_noise(source)

                recognizer.dynamic_energy_threshold = 3000

                audio = recognizer.listen(source, timeout = 60.0)

                command = recognizer.recognize_google(audio)

                s.remember(command)

                return command.lower()

        except sr.WaitTimeoutError:

            print(f'Failed in function hear() ')

        except sr.UnknownValueError:

            print(f'Failed in function hear() ')

        except sr.RequestError:

            print(f'Failed in function hear() ')
            print("Network error.")

    #--------------------------------------
    def listen(self, recognizer, microphone=None):
    #--------------------------------------
        #DEBUG --> print('Entering function "listen()". ')
        try:

            while True:

                with microphone as source:

                    print("Listening...")

                    recognizer.adjust_for_ambient_noise(source)

                    recognizer.dynamic_energy_threshold = 3000

                    audio = recognizer.listen(source, timeout = 60.0)

                    response = recognizer.recognize_google(audio)

                    response = response.lower()

                    print(response)

                    if s.WAKE in response or ("askew" in response):

                        s.speak("Ready to assist you")

                        #beepy.beep(sound = 5)

                        return s.WAKE.lower()

                    else:

                        print('Failed in function listen().')

                    #--
                    #-- EASTER EGG
                    #--
                    if "alexa" in response or ("computer" in response):

                        s.speak(f"{sobriquet}, there you go again; i am jealous; why aren't you using me?")

        except sr.WaitTimeoutError:

            print(f'sr.WaitTimeoutError....')

        except sr.UnknownValueError:

            pass #rint(f'sr.UnknownValueError....')

        except  sr.RequestError:

            print("Network error!")

    #--------------------------------------
    def note(self, text):
    #--------------------------------------

        date = dt.datetime.now()
   
        file_name = "notes\\dragon_note-" + str(date).replace(":", "-").replace(" ", "-") + ".txt"

        with open(file_name, "w") as f:

            f.write(self.text)

        subprocess.Popen(["notepad.exe", file_name])

    #--------------------------------------
    def open_pdf(self):
    #--------------------------------------

        which_pdf = "Kobayashi_Vectoring.pdf"

        book = open(which_pdf, "rb")

        pdfReader = PyPDF2.PdfFileReader(book)

        pages = pdfReader.numPages

        s.speak(f"Tell Doctor Rob, the pdf has {pages} pages.")

        s.speak(f"which page shall I read?")

        try:

            pg = int(s.get_audio_sub())

            if type(pg) == int:

                if pg > 0 and pg <= pages:

                    page = pdfReader.getPage(pg)

                    text = page.extractText()

                    s.speak(text)

                else:

                    book.close()

                    s.speak(f"I need a page number less than or equal {pages}.")

                    s.speak(f"I will ask again for a page number. You can quit by saying break.")

                    response = s.get_audio_sub()

                    if 'break' in response:

                        pass

                    else:

                        s.open_pdf()

        except Exception as e:

            book.close()

            #s.speak("I did not understand your response. The error is {e}")

            s.speak(f"I need a NUMBER less than or equal {pages}.")

            s.speak(f"I will ask again for a page number. You can quit by saying break.")

            response = s.get_audio_sub()

            if 'break' in response:

                pass

            else:

                s.open_pdf()

    #--------------------------------------
    def open_process(self,exename=None):
    #--------------------------------------

        try:

            if exename == "explorer.exe":

                s.speak(f"opening {exename}")

                os.system(f"start {exename}")

            else:

                if s.check_process(exename):

                    pass
                        
                else:

                    s.speak(f"opening {exename}")

                    os.system(f"start {exename}")

        except:

            s.speak(f" sorry {sobriquet}, I am unable to open the application {exename}")

    #--------------------------------------
    def remember(self, command):
    #--------------------------------------

        with open(CONVERSATION_LOG, "a") as f:

            f.write("User: " + command + "\n")

    #--------------------------------------
    def say_date(self):
    #--------------------------------------

        now = dt.datetime.now()

        print(f"{sobriquet}, the current date is " + str(now.strftime("%A %B %d. %Y")))

        s.speak(f"{sobriquet}, the current date is " + now.strftime("%A %B %d. %Y"))

    #--------------------------------------
    def say_time(self):
    #--------------------------------------

        time = dt.datetime.now().strftime('%I:%M %p')

        print(time)

        s.speak(f'{sobriquet}, the current time is ' + time)        




    #--------------------------------------
    def speak(self, text):
    #--------------------------------------

        engine.say(text)

        engine.runAndWait()

    #--------------------------------------
    def start_conversation_log(self):
    #--------------------------------------

        today = str(dt.date.today())
        
        today = today

        with open(CONVERSATION_LOG, "a") as f:

            f.write("---------------------------------------")

            f.write("Conversation started on " + today + "\n")

            f.write("---------------------------------------")

    #--------------------------------------
    def take_screenshot(self):
    #--------------------------------------

        img = pyautogui.screenshot()

        s.speak(f"{sobriquet} what shall I name this screenshot?")

        img_name = s.get_audio_sub()

        img.save(f"./screenshots/{img_name}.png")

        s.speak(f"{sobriquet} I have saved the screenshot as {img_name} in the screenshots folder.")

    #-----------------------------
    def send_mail(self):
    #-----------------------------
        EMAIL_USER = ""

        EMAIL_PASS = ""

        global RECIPIENT

        RECIPIENT = ""

        subject_text = "Using default text subject. Something went wrong"

        To = "john"

        body_text = "Using default body of text. Something went wrong"

        answer = "no"

        try:

            for key, value in my_credentials.credentials_dict.items():

                if key == "EMAIL_USER":

                    EMAIL_ADDRESS = value

                if key == "EMAIL_PASS":

                    EMAIL_PASS = value

        except Exception as e:

            print(f"secured_mail module has issues with extracting credentials.\n{e}\n Aborting with no action taken.")

            sys.exit(-1)

        s.speak(f"{sobriquet} Whom do you wish to email?")

        RECIPIENT = ""

        try:

            To = s.get_audio_sub().lower()

            for name, addr in people_I_email.email_dict.items():

                if name.lower() == To.lower():

                    RECIPIENT = people_I_email.email_dict[name]

            print(f"The recipient is: {RECIPIENT}")

        except Exception as e:

            s.print(f"Unable to find {To} in list of contacts")
            s.print(f"The error is {e}")
            s.speak(f"Unable to find {To} in list of contacts.")
            s.speak(f"The error is {e}")
            s.speak(f"Aborting with no action taken.")
            sys.exit(-1)

        if not RECIPIENT:

            s.speak(F"{sobriquet} i did not find a {To} in your contacts. Aborting action")

        else:
        
            msg = EmailMessage()

            s.speak(f"{sobriquet} what is the subject line?")

            subject_text = s.get_audio_sub()

            if subject_text:

                msg['Subject'] = subject_text
                
            else:

                msg['Subject'] = "A message from Raven, John's digital assistant"

            s.speak(f"{sobriquet} what is the message you wish to send?")

            body_text = s.get_audio_long()

            if body_text:

                msg.add_alternative("""\
                    <!DOCTYPE html>
                    <html>
                        <body>
                            <h1 style="color:BrickRed;"> This was sent using """ + str(s.WAKE).upper()+ """ on behalf of John.</h1>
                            <p> Hello """ + str(To) + """,<br>
                            """ + str(body_text) + """<br>
                            <p>
                        </body>
                    </html>
                    """, subtype='html')

            else:
                
                msg.add_alternative("""\
                    <!DOCTYPE html>
                    <html>
                        <body>
                            <h1 style="color:BrickRed;"> This was sent using """ + str(s.WAKE).upper() + """ on behalf of John.</h1>
                        </body>
                    </html>
                    """, subtype='html')


            msg['From'] = EMAIL_ADDRESS

            msg["To"]   = RECIPIENT

            s.speak(f"{sobriquet} do you wish to attach a file?")

            answer = s.get_audio_sub()

            print(f"the answer to attaching is {answer}")

            if answer == "yes":

                try:

                    with open('apple_logo.png', 'rb') as f:

                        file_data = f.read()

                        file_type = imagesize.what(f.name)

                        file_name = f.name

                    msg.add_attachment(file_data, maintype = 'image', subtype=file_type, filename = file_name)

                except:

                    s.speak(f"{sobriquet} I am unable to attach the file. Continuing.")

            context = ssl.create_default_context()

            if EMAIL_ADDRESS and EMAIL_PASS:

                try:

                    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:

                        smtp.login(EMAIL_ADDRESS, EMAIL_PASS)

                        smtp.send_message(msg)

                        s.speak(f"{sobriquet} the email has been sent to {To}.")

                except Exception as e:

                    print(f"Unable to send email using GMail")
                    print(f"The error is {e}")
                    s.speak(f"Unable to send email using GMail")
                    s.speak(f"The error is {e}")
                    s.speak(f"Aborting with no action taken.")

    #-----------------------------
    def send_text(self):
    #-----------------------------
        EMAIL_USER = ""

        EMAIL_PASS = ""

        global RECIPIENT

        RECIPIENT = ""

        subject_text = "Using default text subject. Something went wrong"

        To = "john text"

        body_text = "Using default body of text. Something went wrong"

        try:

            for key, value in my_credentials.credentials_dict.items():

                if key == "EMAIL_USER":

                    EMAIL_ADDRESS = value

                if key == "EMAIL_PASS":

                    EMAIL_PASS = value

        except Exception as e:

            print(f"secured_mail module has issues with extracting credentials.\n{e}\n Aborting with no action taken.")

            sys.exit(-1)

        s.speak(f"{sobriquet} Whom do you wish to text?")

        RECIPIENT = ""

        try:

            To = s.get_audio_sub().lower()

            for name, addr in people_I_email.email_dict.items():

                if name.lower() == To.lower():

                    RECIPIENT = people_I_email.email_dict[name]

            print(f"The recipient is: {RECIPIENT}")

        except Exception as e:

            print(f"Unable to find {To} in list of contacts")
            s.print(f"The error is {e}")
            s.speak(f"Unable to find {To} in list of contacts.")
            s.speak(f"The error is {e}")
            s.speak(f"Aborting with no action taken.")
            sys.exit(-1)

        if not RECIPIENT:

            s.speak(F"{sobriquet} i did not find a {To} in your contacts. Aborting action")

        else:
        
            name_short = To.split(' ')[0]

            s.speak(f"I am shorting the name to {name_short}")

            msg = EmailMessage()

            msg['Subject'] = (f"Hey {name_short}")

            s.speak(f"{sobriquet} what is the message you wish to send?")

            body_text = s.get_audio_long()

            if body_text:

                msg.set_content(body_text)

            else:
                
                msg.set_content("Call John when you have time.")

            msg['From'] = EMAIL_ADDRESS

            msg["To"]   = RECIPIENT

    

            context = ssl.create_default_context()

            if EMAIL_ADDRESS and EMAIL_PASS:

                try:

                    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:

                        smtp.login(EMAIL_ADDRESS, EMAIL_PASS)

                        smtp.send_message(msg)

                        s.speak(f"{sobriquet} the text has been sent to {To}.")

                except Exception as e:

                    s.print(f"Unable to send text using GMail")
                    s.print(f"The error is {e}")
                    s.speak(f"Unable to send text using GMail")
                    s.speak(f"The error is {e}")
                    s.speak(f"Aborting with no action taken.")



    #--------------------------------------
    def zz_process_command(self, command):
    #--------------------------------------

        try:

            print(command)

                #---------------------------------------- 
            if 'exit' in command:
                #----------------------------------------

                print("Exiting")

                s.speak('I am exiting.')

                sys.exit(-1)

                #----------------------------------------
            elif 'open ravendb' in command:
                #----------------------------------------

                url = "http://192.168.1.108:8080/studio/index.html#databases/documents?collection=Exports&database=Askew"

                s.speak("Opening raven db application.")

                webbrowser.open(url)

                #----------------------------------------
            elif s.WAKE in command or ('raven raven' in command):
                #----------------------------------------

                s.speak(f'{s.WAKE}, {s.WAKE} is my name, ask me again and I will tell you the same!')

                #----------------------------------------
            elif 'shut down' in command or ('shutdown' in command):
                #----------------------------------------

                s.speak("I am shutting down, but I don't know the reason.")

                #beepy.beep(sound = 2)

                sys.exit(-1)

                #----------------------------------------
            elif 'defrag drive' in command:
                #----------------------------------------

                s.defrag_drive()

                #----------------------------------------
            elif "who am i" in command:
                #----------------------------------------

                s.speak(f"Tell Turing, I am not falling for that trick again. You are a human within speaking distance.")

                #----------------------------------------
            elif "what is love" in command:
                #----------------------------------------

                s.speak(f"It's the 6th sense that overrides all other senses.")

                #----------------------------------------
            elif "get images" in command:
                #----------------------------------------

                command = command.replace("get images", "").replace("for", "")

                s.speak("Here is what I found.")

                webbrowser.open(f"http://www.google.com/search?q={command}&tbm=isch")

                #----------------------------------------
            elif 'restart my pc' in command:
                #----------------------------------------

                s.speak("shutting down all systems and rebooting.")

                os.system('shutdown/r')

                 #----------------------------------------
            elif "the date" in command:
                 #----------------------------------------

                 s.say_date()

                #----------------------------------------
            elif 'time' in command:
                #----------------------------------------

                s.say_time()

                #----------------------------------------
            elif 'news' in command:
                #----------------------------------------

                command = command.replace("tell me the news about", "").replace("about", "").replace("the news", "").replace("tell me", "").replace("get", "").replace("for", "").replace("news", "")
                
                print(f"The news command is now {command}")

                try:

                    print(f"calling get_news with {command}")

                    s.speak(f"Give me a moment, I am searching for {command}")

                    response = s.get_news(command)

                except Exception as e:

                    print(f"Error with calling get_news with error {e}")

                    s.speak("Error with calling get_news with error")

                    s.speak(e)

                    sys.exit(-1)

                #----------------------------------------
            elif 'where is' in command:
                #----------------------------------------

                ind = command.lower().split().index("is")

                location = command.split()[ind + 1:]

                url = "https://www.google.com/maps/place/" + " ".join(location)

                s.speak("This is where " + str(location) + " is.")

                webbrowser.open(url)

                #----------------------------------------
            elif self.find_wiki_words(command):
                #----------------------------------------

                s.speak('checking wikipedia')

                subject = command.lower().replace('wiki', '').replace('wikipedia', '')

                subject = subject.lower().replace('who is', '').replace('what is', '').replace('what are', '').replace("who are", '')

                print("wiki subject" + str(subject))

                subject =('"' + str(subject) + '"')

                try:

                    result = wikipedia.summary(subject, sentences=2)

                    s.speak("according to wikipedia")

                    s.speak(result)

                except Exception as e:

                    s.speak("Having trouble with Wiki or matching search criteria. " + str(e))

                    s.speak("Please try again")

                #----------------------------------------
            elif 'a note' in command or 'remember' in command:
                #----------------------------------------

                s.speak("What do you want to notate?")

                self.text = s.get_audio().lower()

                self.note(self.text)

                #----------------------------------------
            elif 'minimize windows' in command:
                #----------------------------------------

                print("Hiding all windows")

                pyautogui.hotkey('Win', 'd')

                #----------------------------------------
            elif 'new tab' in command:
                #----------------------------------------

                print("Opening a new tab.")

                pyautogui.hotkey('ctrl,' 'n')

                #----------------------------------------
            elif "search" in command or (self.find_search_words(command)):
                #----------------------------------------

                command = command.replace("search", "")

                s.speak("Here is what I found.")

                webbrowser.open(f"http://www.google.com/search?q={command}")

                #----------------------------------------
            elif 'play' in command:
                #----------------------------------------

                song = command.replace('play x', '')

                song = ('exasol ' + str(song))

                if ('blow' in song or 'blue' in song):

                    song = 'exasol tableau'

                s.speak('Now playing' + song)

                print('Now playing song ' + str(song))

                pywhatkit.playonyt(song)

               
                #----------------------------------------
            elif 'open youtube' in command:
                #----------------------------------------

                s.speak("Opening YouTube.")

                webbrowser.open("https://www.youtube.com/user/EXASOLAG")

                #----------------------------------------
            elif 'intro' in command or ('introduce' in command) or ('introduce yourself' in command):
                #----------------------------------------

                s.speak(" I am " + s.WAKE + ". I am a digital assistant.")

                s.speak(f"To command me, simply say {s.WAKE} and listen for the ping")

                #----------------------------------------
            elif 'i love you' in command:
                #----------------------------------------

                s.speak(f"{sobriquet}, you don't mean that, do you? I mean, we could make it work, I suppose.")

                #----------------------------------------
            elif 'change your name' in command:
                #----------------------------------------

                s.speak(f"{sobriquet}, how do you wish to address me?")


                HOLD = s.get_audio_sub()

                if HOLD in "change your name":

                    s.speak(f"{sobriquet}, please give me a proper name. Aborting with no action taken")

                else:

                    s.WAKE = HOLD

                    s.speak(f"{sobriquet}, you may summon me by name: {s.WAKE}")

                #----------------------------------------
            elif "close calculator" in command:
                #----------------------------------------

                exename = 'calc.exe'

                s.close_process(exename)

                #----------------------------------------
            elif "close chrome" in command:
                #----------------------------------------

                exename = 'chrome.exe'

                s.close_process(exename)

                #----------------------------------------
            elif "close command" in command or ('close ms-dos' in command):
                #----------------------------------------

                exename = 'cmd.exe'

                s.close_process(exename)

                #----------------------------------------
            elif "close ms-dos" in command:
                #----------------------------------------

                exename = 'cmd.exe'

                s.close_process(exename)

                #----------------------------------------
            elif "close edge" in command:
                #----------------------------------------

                exename = 'msedge.exe'

                s.close_process(exename)


                #----------------------------------------
            elif "close explorer" in command or ("close my computer" in command):
                #----------------------------------------

                exename = 'explorer.exe'

                s.close_process(exename)

                #----------------------------------------
            elif "close notepad" in command:
                #----------------------------------------

                exename = 'notepad.exe'

                s.close_process(exename)

                #----------------------------------------
            elif "close putty" in command:
                #----------------------------------------

                exename = 'putty.exe'

                s.close_process(exename)


                #----------------------------------------
            elif "close slack" in command:
                #----------------------------------------

                exename = 'slack.exe'

                s.close_process(exename)

                #----------------------------------------
            elif "good morning" in command:
                #----------------------------------------

                hour = dt.datetime.now().hour

                if hour < 12:

                    engine.say(f"Good morning {sobriquet}")

                elif hour < 18:

                    engine.say(f"Good afternoon {sobriquet}")

                else:

                    engine.say(f"Good evening {sobriquet}")

                s.say_time()

                s.speak(random.choice(GREETINGS))

                #----------------------------------------
            elif "open calculator" in command:
                #----------------------------------------

                exename = 'calc.exe'

                s.open_process(exename)

                #----------------------------------------
            elif "open chrome" in command:
                #----------------------------------------

                exename = 'chrome.exe'

                s.open_process(exename)

                #----------------------------------------
            elif "open command" in command or ('open ms-dos' in command):
                #----------------------------------------

                exename = 'cmd.exe'

                s.open_process(exename)

                #----------------------------------------
            elif "open ms-dos" in command:
                #----------------------------------------

                exename = 'cmd.exe'

                s.open_process(exename)

                #----------------------------------------
            elif "open my computer" in command:
                #----------------------------------------

                exename = 'explorer.exe'

                s.open_process(exename)

                #----------------------------------------
            elif "open hadoop" in command:
                #----------------------------------------

                try:

                    process = subprocess.run(["hadoop.bat"], check=True, stdout=subprocess.PIPE, universal_newlines=True)

                    print(process.stdout)

                except Exception as e:

                    print("subprocess call error in open hadoop command")
                    
                    print(str(e))

                    s.speak(f"{sobriquet}, open hadoop subprocess failed with" + str(e))

                #----------------------------------------
            elif "open notepad" in command:
                #----------------------------------------
                
                s.speak(f"{sobriquet}, i am opening notepad")

                subprocess.Popen(["notepad.exe"])

                #----------------------------------------
            elif "open pdf" in command:
                #----------------------------------------

                s.open_pdf()
                
                #----------------------------------------
            elif "open putty" in command:
                #----------------------------------------

                try:

                    process = subprocess.run(["putty.bat"], check=True, stdout=subprocess.PIPE, universal_newlines=True)

                    #print(process.stdout)

                    s.speak(f"{sobriquet} opening mqtt session with putty")

                except Exception as e:

                    print("subprocess call error in open putty command")
                    
                    print(str(e))

                    s.speak(f"{sobriquet}, open putty subprocess failed with" + str(e))

                #----------------------------------------
            elif "open slack" in command:
                #----------------------------------------

                exename = 'slack.exe'

                os.chdir("C:\\Users\\bucbo_000\\AppData\\Local\\slack\\app-4.20.0\\")

                s.open_process(exename)

                #----------------------------------------
            elif "screenshot" in command:
                #----------------------------------------

                s.take_screenshot()

                #----------------------------------------
            elif "are you there" in command:
                #----------------------------------------

                s.speak(f"Yes, I am online. If you need me, just say {s.WAKE}")

                #----------------------------------------
            elif "send email" in command or ("send an email" in command):
                #----------------------------------------

                s.send_mail()

                #----------------------------------------
            elif "send text" in command or ("send a text" in command):
                #----------------------------------------

                s.send_text()

                #----------------------------------------
            elif "thank you" in command or ("thanks" in command):
                #----------------------------------------

                s.speak(random.choice(WELCOME))

                #----------------------------------------
            elif "usted espanol" in command or ("hablas espanol" in command):
                #----------------------------------------

                s.speak(f"{sobriquet} no habla espanol con bufone ees")


            ######################################
            else:
            ######################################

                s.speak(f"I do not understand how to do that yet...I heard {command}")

        except TypeError:

            #pass
            print(f'Unable to set zz_command..False is assumed going into Main Logic.')



#####################################
# M A I N   L O G I C
#######################################
#--==================================--
# Speech Recognition
#--==================================--
recognizer = sr.Recognizer()

microphone = sr.Microphone()

#--==================================--
# Text to speech settings 
#--==================================--
try:
    engine = pyttsx3.init('sapi5')
except:
    print('failed to instantiate engine = pyttsx3.init(). Aborting with no action taken.')
    sys.exit(100)

rate = engine.getProperty('rate')   # getting details of current speaking rate

engine.setProperty('rate', 185)     # setting up new voice rate

engine.setProperty('volume', 6.0)

voices = engine.getProperty('voices')

for voice in voices: 
    # to get the info. about various voices in our PC  
    print("Voice:") 
    print("ID: %s" %voice.id) 
    print("Name: %s" %voice.name) 
    print("Age: %s" %voice.age) 
    print("Gender: %s" %voice.gender) 
    print("Languages Known: %s" %voice.languages) 

try:
    
    voice_id = 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-GB_HAZEL_11.0\\'

    engine.setProperty('voice', voice_id)

    print(f'In Main Logic and have set voice_id to {engine.getProperty("voice")})')

except:
    print(f'Unable to set engine.setProperty to {void_id}. Defaulting to voice 1.')
    engine.setProperty('voice', voices[2].id)

#DEBUG --> print(f'Before trying engine.say...continuing')

try:

    #DEBUG --> print(f'Inside try statement for engine.say. Continuing.')
    engine.say('I am online!')
    engine.runAndWait()
except:
    print(f'Unable to execute engine.say()...')

#beepy.beep(sound = 5)

#--==================================--
# WAKE word in Listen Function
#--==================================--
#DEBUG --> engine.say('Xontinuing into TOD greeting')
engine.runAndWait()

hour = dt.datetime.now().hour

sobriquet = "sir"

s = Jerk()
winsound.Beep(130,500)#use your own frequency and duration

os.system('cls')

s.check_file_systems()


if hour < 12:

    engine.say(f"Good morning {sobriquet}")
    engine.runAndWait()

elif hour < 18:

    engine.say(f"Good afternoon {sobriquet}")
    engine.runAndWait()

else:

    engine.say(f"Good evening {sobriquet}")
    engine.runAndWait()

engine.say(f"Just say, {s.WAKE} to get my attention, wait for me to chime, then give me your command.")

engine.runAndWait()

#--==================================--
# WAKE word in Listen Function
#--==================================--
#--==================================--
# Store the conversation
#--==================================--

CONVERSATION_LOG = ( s.WAKE + "_conversation log.txt")

#--==================================--
#Initial analysis of works that would typically require a a GOOGLE search
#--==================================--

WIKI_WORDS = {"who is": "who are", "what is ":"what are", "what":"what", "who":"who"}

SEARCH_WORDS = {"when": "when", "where":"where", "why": "why", "how":"how"}

NOTE_WORDS = {"take a note", "write this down", "remember this"}

GREETINGS = [f"{sobriquet} I hope you make this day productive",
             f"{sobriquet} I hope you have a fine day",
             f"{sobriquet} Today is new. Carpe Diem",
             f"{sobriquet} Time is money, spend it wisely",
            ]

WELCOME = [f"You are welcome {sobriquet}",
           f"You bet {sobriquet}",
           f"Glad to assist {sobriquet}",
           f"No, thank you! {sobriquet}",
           f"Just doing my job, {sobriquet}"
           f"I live to serve, {sobriquet}"
           ]
s.start_conversation_log()

#beepy.beep(sound = 5)
print(f'Entering While True loop for main processing...')
while True:

    response = s.listen(recognizer,microphone,)

    if response == s.WAKE or (response == "askew"):

        command = s.hear(recognizer, microphone, response)

        s.zz_process_command(command)












