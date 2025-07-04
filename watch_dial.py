# -*- coding: utf-8 -*-
"""
Created on Tue May 19 23:42:50 2026

@author: patha
"""

import tkinter as tk
import math
import time

class WatchDial:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Horology Lab")
        self.root.geometry("500x500")
        self.root.configure(bg="#111111")
        
        # Dimensions
        self.width, self.height = 450, 450
        self.cx, self.cy = self.width // 2, self.height // 2
        self.r = 180  # Main dial radius
        
        # Canvas Setup
        self.canvas = tk.Canvas(root, width=self.width, height=self.height, bg="#111111", highlightthickness=0)
        self.canvas.pack(expand=True)
        
        self.build_dial_architecture()
        self.update_watch()

    def build_dial_architecture(self):
        """Draws the static luxury elements of the watch face."""
        # 1. Outer Bezel / Case Accent
        self.canvas.create_oval(self.cx - self.r - 8, self.cy - self.r - 8, 
                                self.cx + self.r + 8, self.cy + self.r + 8, 
                                outline="#8e7f54", width=3) # Muted gold outline
        
        # 2. Main Dial Face
        self.canvas.create_oval(self.cx - self.r, self.cy - self.r, 
                                self.cx + self.r, self.cy + self.r, 
                                fill="#1a1a24", outline="#2c2c35", width=2) # Deep midnight blue/matte black
        
        # 3. Sub-dial ring for Sweeping Seconds (at 6 o'clock position)
        self.sub_cx, self.sub_cy, self.sub_r = self.cx, self.cy + 85, 45
        self.canvas.create_oval(self.sub_cx - self.sub_r, self.sub_cy - self.sub_r,
                                self.sub_cx + self.sub_r, self.sub_cy + self.sub_r,
                                outline="#3a3a45", width=1)

        # 4. Generate Hour Indices & Micro-ticks
        for i in range(60):
            angle = math.radians(i * 6) # 360 degrees / 60 ticks = 6 degrees per tick
            
            if i % 5 == 0:  # Major Hour Markers
                # Draw circular luminescent-style plots
                x_pos = self.cx + (self.r - 15) * math.sin(angle)
                y_pos = self.cy - (self.r - 15) * math.cos(angle)
                self.canvas.create_oval(x_pos-4, y_pos-4, x_pos+4, y_pos+4, fill="#dfd5b6", outline="#8e7f54")
            else:  # Minor Minute/Second Ticks
                x1 = self.cx + (self.r - 8) * math.sin(angle)
                y1 = self.cy - (self.r - 8) * math.cos(angle)
                x2 = self.cx + self.r * math.sin(angle)
                y2 = self.cy - self.r * math.cos(angle)
                self.canvas.create_line(x1, y1, x2, y2, fill="#4a4a55", width=1)

        # 5. Date Window Aperture (at 3 o'clock position)
        self.canvas.create_rectangle(self.cx + 105, self.cy - 12, self.cx + 145, self.cy + 12, 
                                     fill="#111111", outline="#8e7f54", width=1)
        self.date_text = self.canvas.create_text(self.cx + 125, self.cy, fill="#dfd5b6", 
                                                 font=("Courier", 11, "bold"))

    def draw_hand(self, cx, cy, length, angle_rad, color, width, cap="round"):
        """Helper to project vectors and draw hands."""
        x = cx + length * math.sin(angle_rad)
        y = cy - length * math.cos(angle_rad)
        return self.canvas.create_line(cx, cy, x, y, fill=color, width=width, capstyle=cap)

    def update_watch(self):
        """Calculates time metrics and updates dynamic vectors."""
        # Clear dynamic elements from previous frame
        self.canvas.delete("dynamic")
        
        # Fetch high-precision system time
        t = time.time()
        local_time = time.localtime(t)
        
        hr = local_time.tm_hour
        mn = local_time.tm_min
        sc = local_time.tm_sec
        ms = t - int(t) # Used for a silky smooth, mechanical sweep effect
        
        # 1. Update Date Window Text
        self.canvas.itemconfig(self.date_text, text=f"{local_time.tm_mday:02d}")
        
        # 2. Angle Calculations
        # Continuous sweeping angles for ultra-smooth rendering
        sec_angle = math.radians((sc + ms) * 6)
        min_angle = math.radians((mn + sc/60.0) * 6)
        hour_angle = math.radians(((hr % 12) + mn/60.0) * 30)
        
        # 3. Draw Hour Hand (Thick, elegant sword profile archetype)
        self.draw_hand(self.cx, self.cy, 95, hour_angle, "#e5dec9", 5, "round")
        self.canvas.create_line(self.cx, self.cy, self.cx + 95 * math.sin(hour_angle), self.cy - 95 * math.cos(hour_angle), fill="#dfd5b6", width=5, tags="dynamic", capstyle="round")
        
        # 4. Draw Minute Hand (Slender baton)
        self.canvas.create_line(self.cx, self.cy, self.cx + 145 * math.sin(min_angle), self.cy - 145 * math.cos(min_angle), fill="#dfd5b6", width=3, tags="dynamic", capstyle="round")
        
        # 5. Draw Sweeping Seconds Sub-hand (Chronograph style counter weight)
        self.canvas.create_line(self.sub_cx, self.sub_cy, self.sub_cx + 35 * math.sin(sec_angle), self.sub_cy - 35 * math.cos(sec_angle), fill="#b93a3a", width=1.5, tags="dynamic")
        
        # 6. Center Pinion Cap (Covers hand junctions cleanly)
        self.canvas.create_oval(self.cx - 5, self.cy - 5, self.cx + 5, self.cy + 5, fill="#8e7f54", outline="#dfd5b6", tags="dynamic")
        self.canvas.create_oval(self.sub_cx - 3, self.sub_cy - 3, self.sub_cx + 3, self.sub_cy + 3, fill="#3a3a45", outline="#b93a3a", tags="dynamic")

        # Refresh canvas loop at ~60 FPS (16 milliseconds delay) to capture fluid motion
        self.root.after(16, self.update_watch)

if __name__ == "__main__":
    app_root = tk.Tk()
    dial = WatchDial(app_root)
    app_root.mainloop()
