import tkinter as tk
import random

def run_turtle_prank():
    root = tk.Tk()
    root.title("System Update")
    root.attributes('-fullscreen', True)
    # Windows 10/11 Update Blue color: #0078D7
    root.configure(bg='#0078D7')

    # Main container frame
    frame = tk.Frame(root, bg='#0078D7')
    frame.place(relx=0.5, rely=0.5, anchor='center')

    # --- PHASE 1: Windows-Style Clean Update Screen ---
    title_label = tk.Label(frame, text="Working on updates", font=("Segoe UI", 28), fg="white", bg='#0078D7')
    title_label.pack(pady=10)
    
    sub_label = tk.Label(frame, text="0% complete", font=("Segoe UI", 16), fg="#d0e2ff", bg='#0078D7')
    sub_label.pack(pady=5)

    tip_label = tk.Label(frame, text="Don't turn off your PC. This will take a while.", font=("Segoe UI", 12), fg="#a6c8ff", bg='#0078D7')
    tip_label.pack(pady=20)

    update_steps = [
        (5, "15% complete"),
        (10, "34% complete"),
        (15, "58% complete"),
        (20, "79% complete"),
        (25, "94% complete")
    ]

    for sec, text in update_steps:
        root.after(sec * 1000, lambda t=text: sub_label.config(text=t))

    # --- PHASE 2: The Chaos Ransomware UI Transformation ---
    def trigger_chaos():
        for widget in frame.winfo_children():
            widget.destroy()

        root.configure(bg='black')
        frame.configure(bg='black')

        colors = ["#ff0000", "#00ff00", "#ffff00", "#ff00ff", "#00ffff", "#ffffff"]

        chaos_title = tk.Label(frame, text="⚠️ TURTLE.EXE ACTIVATED ⚠️", font=("Courier", 22, "bold"), bg='black')
        chaos_title.pack(pady=10)

        msg_label = tk.Label(frame, text="hahah idiot you got tricked by turtle.exe virus\nYOUR FILES ARE BEING ENCRYPTED", font=("Courier", 14, "bold"), fg="white", bg='black')
        msg_label.pack(pady=10)

        timer_label = tk.Label(frame, text="Time until wipe: 01:00", font=("Courier", 18, "bold"), fg="#ff0000", bg='black')
        timer_label.pack(pady=10)

        counter_var = tk.IntVar(value=20)
        counter_display = tk.Label(frame, text="Type 'turtle exe' 20 times to abort: 20", font=("Courier", 12), fg="yellow", bg='black')
        counter_display.pack(pady=10)

        entry = tk.Entry(frame, font=("Courier", 14), justify='center', width=25)
        entry.pack(pady=10)
        entry.focus_set()

        feedback = tk.Label(frame, text="", font=("Courier", 10), bg='black')
        feedback.pack(pady=5)

        # Countdown Timer (60 seconds)
        time_left = [60]
        def update_timer():
            if time_left[0] > 0:
                time_left[0] -= 1
                mins, secs = divmod(time_left[0], 60)
                timer_label.config(text=f"Time until wipe: {mins:02d}:{secs:02d}")
                root.after(1000, update_timer)
            else:
                timer_label.config(text="SYSTEM WIPED (Just kidding!)")
                root.after(2000, root.destroy)
        update_timer()

        # Flashing colors effect
        def flash_colors():
            chaos_title.config(fg=random.choice(colors))
            root.after(150, flash_colors)
        flash_colors()

        # Screen Invert Background Effect
        def invert_screen_effect():
            bg_color = random.choice(["black", "white", "#110000", "#001100"])
            root.configure(bg=bg_color)
            frame.configure(bg=bg_color)
            root.after(400, invert_screen_effect)
        invert_screen_effect()

        # Floating jumping windows
        def spawn_floating_popup():
            pop = tk.Toplevel(root)
            pop.overrideredirect(True)
            screen_w = pop.winfo_screenwidth()
            screen_h = pop.winfo_screenheight()
            rx = random.randint(50, screen_w - 300)
            ry = random.randint(50, screen_h - 150)
            pop.geometry(f"250x100+{rx}+{ry}")
            pop.configure(bg=random.choice(["red", "black", "blue"]))
            
            lbl = tk.Label(pop, text="ERROR: TURTLE.EXE\nFiles vanishing...", fg="white", bg=random.choice(["black", "red"]), font=("Courier", 10, "bold"))
            lbl.pack(expand=True, fill="both")
            
            pop.after(2000, pop.destroy)
            root.after(1500, spawn_floating_popup)

        spawn_floating_popup()

        # Input code verification
        def check_code(event=None):
            val = entry.get().strip().lower()
            current = counter_var.get()
            if val == "turtle exe":
                current -= 1
                counter_var.set(current)
                counter_display.config(text=f"Type 'turtle exe' 20 times to abort: {current}")
                entry.delete(0, tk.END)
                feedback.config(text="Decrypting block...", fg="green")
                if current <= 0:
                    feedback.config(text="ABORTED. Prank over!", fg="green")
                    root.after(1500, root.destroy)
            else:
                feedback.config(text="WRONG CODE!", fg="red")
                entry.delete(0, tk.END)

        entry.bind("<Return>", check_code)

    # Trigger transition after 30 seconds
    root.after(30000, trigger_chaos)

    # Emergency exit safeguard
    root.bind("<Escape>", lambda e: root.destroy())
    root.mainloop()

if __name__ == "__main__":
    run_turtle_prank()
