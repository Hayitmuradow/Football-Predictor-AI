import customtkinter as ctk
import requests  # Onlaýn maglumat çekmek üçin (SoloLearn-de öwrenen kitaphananyň biri)
from tkinter import messagebox
import threading

# 1. DIZAÝN: Reňkler we Görünüş
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue") # Reňki has döwrebap "Sport Blue" etdik

class FootballPredictorAI(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("PRO-BET AI ROBOT v3.0")
        self.geometry("1000x700")

        # API Sazlamalary (Bärde hakyky onlaýn robotyň işleýiş gurluşy bar)
        self.api_key = "SENIN_API_ACHARYN" # Bura geljekde hakyky açar goýlar
        self.api_url = "https://v3.football.api-sports.io/fixtures?live=all"

        # 2. PYTHON DARSLERI: Sözlükler (Dictionary) we Diller
        self.languages = {
            "Turkmen": {
                "title": "⚽ ONLAÝN FUTBOL ANALIZI",
                "btn_live": "JANLY MAGLUMATY ÇEK",
                "btn_manual": "EL BILEN ANALIZ ET",
                "status": "Ulgam: Onlaýn",
                "placeholder_home": "Öý komandasy",
                "placeholder_away": "Myhman komandasy"
            },
            "English": {
                "title": "⚽ ONLINE FOOTBALL ANALYSIS",
                "btn_live": "FETCH LIVE DATA",
                "btn_manual": "MANUAL ANALYSIS",
                "status": "System: Online",
                "placeholder_home": "Home Team",
                "placeholder_away": "Away Team"
            },
            "Russian": {
                "title": "⚽ ОНЛАЙН АНАЛИЗ ФУТБОЛА",
                "btn_live": "ПОЛУЧИТЬ ДАННЫЕ",
                "btn_manual": "РУЧНОЙ АНАЛИЗ",
                "status": "Система: Онлайн",
                "placeholder_home": "Хозяева",
                "placeholder_away": "Гости"
            }
        }
        self.current_lang = "Turkmen"

        # --- UI DIZAÝN BÖLÜMLERI ---
        # Çep Menýu
        self.sidebar = ctk.CTkFrame(self, width=220, corner_radius=0, fg_color="#0f172a")
        self.sidebar.pack(side="left", fill="y")
        
        self.logo = ctk.CTkLabel(self.sidebar, text="SPORT AI", font=("Orbitron", 28, "bold"), text_color="#38bdf8")
        self.logo.pack(pady=30)

        self.lang_menu = ctk.CTkOptionMenu(self.sidebar, values=["Turkmen", "English", "Russian"], command=self.change_language)
        self.lang_menu.pack(pady=10, padx=20)

        # Sag Esasy Panel
        self.main_panel = ctk.CTkScrollableFrame(self, corner_radius=15, fg_color="#1e293b")
        self.main_panel.pack(side="right", fill="both", expand=True, padx=20, pady=20)

        self.header = ctk.CTkLabel(self.main_panel, text=self.languages["Turkmen"]["title"], font=("Roboto", 24, "bold"))
        self.header.pack(pady=20)

        # API DÜWMESI (Hakyky Robot)
        self.btn_api = ctk.CTkButton(self.main_panel, text="JANLY MAGLUMATY ÇEK", fg_color="#0284c7", 
                                     hover_color="#0ea5e9", height=45, command=self.fetch_api_data)
        self.btn_api.pack(pady=10, fill="x", padx=100)

        # Analiz Netije Meýdançasy
        self.result_box = ctk.CTkTextbox(self.main_panel, height=300, font=("Consolas", 14), fg_color="#0f172a")
        self.result_box.pack(pady=20, fill="x", padx=20)

    # 3. HAKYKY API BIRIKDIRMEK: Funksiýa
    def fetch_api_data(self):
        self.result_box.insert("end", "\n[ROBOT]: Onlaýn maglumatlar çekilýär, garaşyň...\n")
        
        # Bu ýerde threading ulanýarys (Programma doňmazlygy üçin - Advanced Python)
        def thread_request():
            try:
                # Hakyky API Baglanyşygy
                headers = {'x-rapidapi-key': self.api_key, 'x-rapidapi-host': "v3.football.api-sports.io"}
                # response = requests.get(self.api_url, headers=headers) # API açaryňyz bar bolsa açyň
                
                # Simulýasiýa Netijesi (API jogaby ýaly)
                data_preview = "⚽ Barselona 2-1 Real Madrid (Live)\n📊 xG: 2.45 - 1.20\n🔥 Hüjüm: %65 - %35"
                self.result_box.delete("1.0", "end")
                self.result_box.insert("end", f"--- JANLY NETIJELER ---\n{data_preview}")
            except Exception as e:
                messagebox.showerror("Error", f"API Baglanyşyk ýalňyşlygy: {e}")

        threading.Thread(target=thread_request).start()

    def change_language(self, new_lang):
        self.current_lang = new_lang
        l = self.languages[new_lang]
        self.header.configure(text=l["title"])
        self.btn_api.configure(text=l["btn_live"])

if __name__ == "__main__":
    app = FootballPredictorAI()
    app.mainloop()
    
