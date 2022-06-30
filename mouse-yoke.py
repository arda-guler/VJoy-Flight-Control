from pyvjoystick import vjoy
import mouse
import keyboard
import time

screen_x = 1360
screen_y = 768

j = vjoy.VJoyDevice(1)
j.set_axis(vjoy.HID_USAGE.X, 32768)

active = True
running = True

def center_mouse():
    mouse.move(screen_x/2,screen_y/2,True)

def toggle_active():
    global active
    active = not active

center_mouse()
mouse.on_middle_click(toggle_active)
    
while running:
    if active:
        m_pos = mouse.get_position()
        yoke_y = m_pos[1]/screen_y * 32768
        yoke_x = m_pos[0]/screen_x * 32768
        j.set_axis(vjoy.HID_USAGE.X, int(yoke_x))
        j.set_axis(vjoy.HID_USAGE.Y, int(yoke_y))

    if keyboard.is_pressed("N"):
        center_mouse()

    time.sleep(0.05)
        
