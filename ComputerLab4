##EARTH ORBITING SUN
GlowScript 3.1 VPython

#initialisation
sun = sphere(pos=vector(0,0,0),radius=1.5e10,color=color.yellow)
earth = sphere(pos=vector(1.5e11,0,0),radius=6.4e9,color=color.blue)

sun.M=2e30
earth.M=6e24
G=6.67e-11

earth.p = earth.M*vector(0,sqrt(G*sun.M/mag(earth.pos-sun.pos)),0)
earth.trail = curve(pos=earth.pos , color=earth.color)

sun.p = sun.M*vector(0,0,0)
sun.trail = curve(pos=sun.pos , color=sun.color)

t=0
dt=24*3600

scene.autoscale=1

while t < 10000*dt:
  rate(50)
  R = earth.pos-sun.pos
  force = -G*sun.M*earth.M*R/mag(R)**3
  
  earth.p = earth.p+force*dt
  earth.pos = earth.pos+(earth.p/earth.M)*dt
  earth.trail.append(pos=earth.pos)
  
  sun.p = sun.p-force*dt
  sun.pos = sun.pos+(sun.p/sun.M)*dt
  sun.trail.append(pos=sun.pos)
  
  t = t+dt
########################################################
#3 suns
GlowScript 3.1 VPython

#initialisation
sun =    sphere(pos=vector(0,0,0),radius=1.5e10,color=color.yellow)
sun2 =   sphere(pos=vector(2e11,2e11,0),radius=1.5e10,color=color.orange)
planet = sphere(pos=vector(2e11,-2e11,0),radius=1.5e10,color=color.blue)

sun.M = 2e30
sun2.M = 2e30
planet.M = 2e30

G=6.67e-11

suninitialp = 0*-sqrt(G*sun.M/mag(sun2.pos-sun.pos))/2
sun.p = sun.M*vector(0,suninitialp,0)
sun.trail = curve(pos=sun.pos , color=sun.color)

sun2initialp = 0*sqrt(G*sun2.M/mag(sun2.pos-sun.pos))/2
sun2.p = sun2.M*vector(0,sun2initialp,0)
sun2.trail = curve(pos=sun2.pos , color=sun2.color)

planetinitialp = 0*sqrt(G*planet.M/mag(planet.pos-sun.pos))*1.5
planet.p = planet.M*vector(0,planetinitialp,0)
planet.trail = curve(pos=planet.pos , color=planet.color)


t=0
dt=24*3600

scene.autoscale=1

while t < 10000*dt:
  rate(50)
  
  RSunSun2 = sun.pos-sun2.pos
  FSunSun2 = -G*sun.M*sun2.M*RSunSun2/mag(RSunSun2)**3
  
  RSunPlanet = sun.pos-planet.pos
  FSunPlanet = -G*sun.M*planet.M*RSunPlanet/mag(RSunPlanet)**3
  
  RSun2Planet = sun2.pos-planet.pos
  FSun2Planet = -G*sun2.M*planet.M*RSun2Planet/mag(RSun2Planet)**3
  
  sun.p = sun.p+(FSunSun2 + FSunPlanet)*dt
  sun.pos = sun.pos+(sun.p/sun.M)*dt
  sun.trail.append(pos=sun.pos)
  
  sun2.p = sun2.p+(-FSunSun2 + FSun2Planet)*dt
  sun2.pos = sun2.pos+(sun2.p/sun2.M)*dt
  sun2.trail.append(pos=sun2.pos)
  
  planet.p = planet.p+(-FSunPlanet-FSun2Planet)*dt
  planet.pos = planet.pos+(planet.p/planet.M)*dt
  planet.trail.append(pos=planet.pos)
  
  t = t+dt
