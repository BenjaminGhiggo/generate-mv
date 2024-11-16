from pyo import *

# Iniciar el servidor de audio
s = Server().boot()
s.start()

# Crear un ritmo base utilizando un generador de pulsos
beat = Metro(time=0.25).play()

# Generar una envolvente para el ritmo
env = TrigEnv(beat, table=HannTable(), dur=0.1, mul=0.5)

# Oscilador de bajo
bass_freq = 55  # Frecuencia base para el bajo
bass = Sine(freq=bass_freq, mul=env).out()

# Añadir un arpegiador
arp_notes = [110, 220, 330, 440]
arp = TrigChoice(beat, choice=arp_notes)
arp_env = TrigEnv(beat, table=HannTable(), dur=0.1, mul=0.3)
lead = Sine(freq=arp, mul=arp_env).out()

# Añadir un efecto de delay
delay = Delay(lead, delay=[0.1, 0.2], feedback=0.5).out()

# Mantener el script corriendo
s.gui(locals())
