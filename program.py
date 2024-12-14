import tkinter as tk
from tkinter import filedialog, messagebox
from pyscreenrec import ScreenRecorder
import os
import time
import threading
from PIL import ImageGrab
import webbrowser


class ScreenRecorderApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Simple Screen Recorder")
        self.master.geometry("600x600")
        self.master.resizable(False, False)

        self.recorder = ScreenRecorder()
        self.file_path = ""
        self.screenshot_folder = "Screenshots"
        os.makedirs(self.screenshot_folder, exist_ok=True)
        self.is_recording = False
        self.start_time = None

        self.create_widgets()

    def create_widgets(self):
        """Create and organize the GUI components."""
        # Title Label
        title_label = tk.Label(
            self.master,
            text="Simple Screen Recorder",
            font=("Arial", 28, "bold"),
            bg="#3B4D5C",
            fg="#FFFFFF",
        )
        title_label.pack(pady=40)

        # Path Selection Frame
        path_frame = tk.Frame(self.master, bg="#3B4D5C")
        path_frame.pack(pady=5, padx=20, fill="x")

        self.path_entry = tk.Entry(
            path_frame, font=("Arial", 12), width=40, bg="#F1F1F1", fg="#333333", relief="solid", bd=1
        )
        self.path_entry.pack(side="left", padx=20, pady=15)

        browse_button = tk.Button(
            path_frame,
            text="Path",
            command=self.browse_file,
            bg="#6C7C8A",
            fg="#FFFFFF",
            font=("Arial", 12, "bold"),
            relief="solid",
            cursor="hand2",
        )
        browse_button.pack(side="right", padx=10, pady=5)

        # FPS Slider Frame
        fps_frame = tk.Frame(self.master, bg="#3B4D5C")
        fps_frame.pack(pady=10)
        fps_label = tk.Label(fps_frame, text="Select FPS  :", font=("Arial", 12), bg="#3B4D5C", fg="#FFFFFF")
        fps_label.pack(side="left", padx=10)
        self.fps_slider = tk.Scale(fps_frame, from_=5, to=60, orient="horizontal", bg="#F1F1F1", fg="#333333", length=300, font=("Arial", 10))
        self.fps_slider.set(20)
        self.fps_slider.pack(side="left", padx=10)

        # Buttons Frame
        buttons_frame = tk.Frame(self.master, bg="#3B4D5C")
        buttons_frame.pack(pady=20)

        self.start_button = tk.Button(
            buttons_frame,
            text="Start Recording",
            command=self.start_recording,
            bg="#3498DB",
            fg="#FFFFFF",
            font=("Arial", 14, "bold"),
            width=16,
            relief="solid",
            cursor="hand2",
        )
        self.start_button.grid(row=0, column=0, padx=10, pady=10)

        self.stop_button = tk.Button(
            buttons_frame,
            text="Stop Recording",
            command=self.stop_recording,
            bg="#E74C3C",
            fg="#FFFFFF",
            font=("Arial", 14, "bold"),
            width=16,
            relief="solid",
            state="disabled",
            cursor="hand2",
        )
        self.stop_button.grid(row=0, column=1, padx=10, pady=10)

        screenshot_button = tk.Button(
            buttons_frame,
            text="Capture Screenshot",
            command=self.capture_screenshot,
            bg="#F39C12",
            fg="#FFFFFF",
            font=("Arial", 14, "bold"),
            width=16,
            relief="solid",
            cursor="hand2",
        )
        screenshot_button.grid(row=1, column=0, padx=10, pady=10)

        preview_button = tk.Button(
            buttons_frame,
            text="Preview Recording",
            command=self.preview_recording,
            bg="#2ECC71",
            fg="#FFFFFF",
            font=("Arial", 14, "bold"),
            width=16,
            relief="solid",
            cursor="hand2",
        )
        preview_button.grid(row=1, column=1, padx=10, pady=10)

        theme_button = tk.Button(
            self.master,
            text="Toggle Theme",
            command=self.toggle_theme,
            bg="#9B59B6",
            fg="#FFFFFF",
            font=("Arial", 12, "bold"),
            width=15,
            relief="solid",
            cursor="hand2",
        )
        theme_button.pack(pady=10)

         # Footer
        footer_label = tk.Label(root, text="Developed by Hassan Ahmed", font=("Helvetica", 10), bg="#e5e5e5", fg="#7F8C8D")
        footer_label.pack(pady=20)

        # Timer Label
        self.timer_label = tk.Label(
            self.master,
            text="00:00:00",
            font=("Arial", 14, "bold"),
            bg="#3B4D5C",
            fg="#FFFFFF",
        )
        self.timer_label.pack(pady=5)

    def browse_file(self):
        """Open file dialog to select save path."""
        self.file_path = filedialog.asksaveasfilename(
            defaultextension=".mp4", filetypes=[("MP4 Files", "*.mp4")]
        )
        if self.file_path:
            self.path_entry.delete(0, tk.END)
            self.path_entry.insert(0, self.file_path)

    def start_recording(self):
        """Start screen recording."""
        self.file_path = self.path_entry.get().strip()
        if not self.file_path:
            messagebox.showerror("Error", "Please select a file path.")
            return
        try:
            fps = self.fps_slider.get()
            self.recorder.start_recording(self.file_path, fps=fps)
            self.is_recording = True
            self.start_time = time.time()
            self.update_ui(started=True)
            threading.Thread(target=self.update_timer, daemon=True).start()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to start recording: {e}")

    def stop_recording(self):
        """Stop screen recording."""
        try:
            self.recorder.stop_recording()
            self.is_recording = False
            self.update_ui(started=False)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to stop recording: {e}")

    def capture_screenshot(self):
        """Capture a screenshot."""
        try:
            screenshot_path = os.path.join(
                self.screenshot_folder, f"screenshot_{int(time.time())}.png"
            )
            screenshot = ImageGrab.grab()
            screenshot.save(screenshot_path)
            messagebox.showinfo("Screenshot", f"Screenshot saved at {screenshot_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to capture screenshot: {e}")

    def preview_recording(self):
        """Preview the last recording."""
        if self.file_path and os.path.exists(self.file_path):
            webbrowser.open(self.file_path)
        else:
            messagebox.showerror("Error", "No recording found to preview.")

    def toggle_theme(self):
        """Toggle between light and dark themes."""
        current_bg = self.master.cget("bg")
        if current_bg == "#3B4D5C":
            self.master.configure(bg="#ECF0F1")
        else:
            self.master.configure(bg="#3B4D5C")

    def update_ui(self, started):
        """Update UI buttons based on recording state."""
        if started:
            self.start_button.config(state="disabled")
            self.stop_button.config(state="normal")
        else:
            self.start_button.config(state="normal")
            self.stop_button.config(state="disabled")

    def update_timer(self):
        """Update the timer during recording."""
        while self.is_recording:
            elapsed_time = int(time.time() - self.start_time)
            hrs, mins, secs = elapsed_time // 3600, (elapsed_time % 3600) // 60, elapsed_time % 60
            self.timer_label.config(text=f"{hrs:02}:{mins:02}:{secs:02}")
            time.sleep(1)


if __name__ == "__main__":
    root = tk.Tk()
    app = ScreenRecorderApp(root)
    root.mainloop()
