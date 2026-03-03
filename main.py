import customtkinter as ctk
import random
from tkinter import messagebox

# Programmanyň dizaýn sazlamalary (Sport Dark Theme)
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green") 

class FootballPredictorAI(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Penjiräniň ady we ölçegi
        self.title("FOOTBALL PREDICTOR AI - Professional Edition")
        self.geometry("900x600")

        # --- Side Bar (Çep tarapdaky menýu) ---
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0, fg_color="#121212")
        self.sidebar.pack(side="left", fill="y")
        
        self.logo = ctk.CTkLabel(self.sidebar, text="⚽ AI STATS", font=("Orbitron", 26, "bold"), text_color="#2ecc71")
        self.logo.pack(pady=30)

        self.info_label = ctk.CTkLabel(self.sidebar, text="Version 1.0\nSystem: Online", text_color="gray", font=("Roboto", 12))
        self.info_label.pack(side="bottom", pady=20)

        # --- Esasy Panel (Sag tarap) ---
        self.main_panel = ctk.CTkFrame(self, corner_radius=15, fg_color="#1e1e1e")
        self.main_panel.pack(side="right", fill="both", expand=True, padx=20, pady=20)

        self.title_label = ctk.CTkLabel(self.main_panel, text="PROFESSIONAL MATCH ANALYZER", font=("Roboto", 22, "bold"))
        self.title_label.pack(pady=20)

        # --- Maglumat Girizilýän Bölüm ---
        self.input_frame = ctk.CTkFrame(self.main_panel, fg_color="transparent")
        self.input_frame.pack(pady=10)

        # Komanda atlaryny girizmek
        self.home_name = ctk.CTkEntry(self.input_frame, placeholder_text="Öý komandanyň ady", width=220, height=35)
        self.home_name.grid(row=0, column=0, padx=15, pady=15)

        self.away_name = ctk.CTkEntry(self.input_frame, placeholder_text="Myhman komandanyň ady", width=220, height=35)
        self.away_name.grid(row=0, column=1, padx=15, pady=15)

        # xG (Garaşylýan gol) statistikasyny girizmek
        self.home_xg = ctk.CTkEntry(self.input_frame, placeholder_text="Öý xG (Meselem: 1.8)", width=220, height=35)
        self.home_xg.grid(row=1, column=0, padx=15, pady=15)

        self.away_xg = ctk.CTkEntry(self.input_frame, placeholder_text="Myhman xG (Meselem: 1.1)", width=220, height=35)
        self.away_xg.grid(row=1, column=1, padx=15, pady=15)

        # Analiz Düwmesi
        self.btn_analyze = ctk.CTkButton(self.main_panel, text="ANALIZ ET WE PROGNOZ ÇYKAR", 
                                          fg_color="#27ae60", hover_color="#2ecc71", 
                                          font=("Roboto", 16, "bold"), height=50, width=300,
                                          command=self.analyze_match)
        self.btn_analyze.pack(pady=30)

        # --- Netije Görkezilýän Ekran ---
        self.result_display = ctk.CTkTextbox(self.main_panel, width=650, height=220, 
                                              font=("Consolas", 15), corner_radius=12, 
                                              fg_color="#2d3436", text_color="#ffffff", border_width=1, border_color="#2ecc71")
        self.result_display.pack(pady=10, padx=30)
        self.result_display.insert("0.0", "Maglumatlary giriziň we 'Analiz' düwmesine basyň...")

    def analyze_match(self):
        try:
            # Girizilen maglumatlary almak
            home = self.home_name.get() or "Öý Komanda"
            away = self.away_name.get() or "Myhman Komanda"
            h_xg = float(self.home_xg.get() or 0)
            a_xg = float(self.away_xg.get() or 0)

            # Statistiki ähtimallyk hasaplamasy (Poisson logic)
            total_xg = h_xg + a_xg + 0.01
            home_win_prob = round((h_xg / total_xg) * 100, 1)
            away_win_prob = round((a_xg / total_xg) * 100, 1)
            draw_prob = 15.0 # Deňme-deňlik ähtimallygy standart

            # Ähtimal hasap simulýasiýasy
            score_h = int(h_xg) if random.random() > 0.3 else int(h_xg) + 1
            score_a = int(a_xg) if random.random() > 0.4 else int(a_xg) + 1

            # Netijäni ekrana çykarmak
            result_text = (
                f"📊 MATCH ANALYSIS REPORT: {home.upper()} vs {away.upper()}\n"
                f"{'='*55}\n"
                f"⚽ AI Çaklamasy (Score): {score_h}:{score_a}\n"
                f"📈 Utuş Ähtimallygy: %{home_win_prob} ({home}) | %{away_win_prob} ({away})\n"
                f"⚖️ Deňme-deňlik (Draw): %{draw_prob}\n"
                f"{'='*55}\n"
                f"💡 AI MASLAHATY: "
            )

            if home_win_prob > 65:
                result_text += f"{home} utmaga örän ýakyn (W1)."
            elif h_xg + a_xg > 2.5:
                result_text += "Gollaryň köp bolmagyna garaşylýar (Total Over 2.5)."
            elif h_xg < 1.0 and a_xg < 1.0:
                result_text += "Az golly we goranyşly oýun (Total Under 2.5)."
            else:
                result_text += "Töwekgelçilikli oýun, janly (live) garaşyň."

            self.result_display.delete("0.0", "end")
            self.result_display.insert("0.0", result_text)

        except ValueError:
            messagebox.showerror("Ýalňyşlyk", "Lütfen, xG bölümlerine diňe san giriziň! (Meselem: 1.5)")

if __name__ == "__main__":
    app = FootballPredictorAI()
    app.mainloop()
  
