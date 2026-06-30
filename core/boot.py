import customtkinter as ctk

class BootScreen(ctk.CTkFrame):
    def __init__(self, master, on_finish=None):
        super().__init__(master)
        self.pack(fill="both", expand=True)

        self.on_finish = on_finish

        self.title = ctk.CTkLabel(
            self,
            text="NOVA CYBER OS",
            font=("Consolas", 40, "bold"),
            text_color="#00ff66"
        )
        self.title.pack(pady=80)

        self.status = ctk.CTkLabel(
            self,
            text="Initializing AI Core...",
            font=("Consolas", 20),
            text_color="white"
        )
        self.status.pack()

        self.progress = ctk.CTkProgressBar(
            self,
            width=700,
            progress_color="#00ff66"
        )
        self.progress.pack(pady=30)

        self.progress.set(0)

        self.value = 0

        self.loading()

    def loading(self):

        self.value += 1

        self.progress.set(self.value/100)

        if self.value < 20:
            self.status.configure(text="Initializing AI Core...")

        elif self.value < 40:
            self.status.configure(text="Loading Security Modules...")

        elif self.value < 60:
            self.status.configure(text="Checking Hardware...")

        elif self.value < 80:
            self.status.configure(text="Connecting Camera...")

        elif self.value < 100:
            self.status.configure(text="Launching NOVA...")

        else:
            self.status.configure(text="SYSTEM READY")

            if self.on_finish:
                self.after(1000, self.on_finish)
            return

        self.after(40, self.loading)