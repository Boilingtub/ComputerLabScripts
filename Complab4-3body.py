GlowScript 3.1 VPython

#initialisation
sun =    sphere(pos=vector(0,0,0),radius=1.5e10,color=color.yellow)
sun2 =   sphere(pos=vector(2e11,2e11,0),radius=1.5e10,color=color.orange)
planet = sphere(pos=vector(2e11,-2e11,0),radius=1.5e10,color=color.blue)

sun.M = 2e30
sun2.M = 2e30
planet.M = 2e30

G=6.67e-11

suninitialp = -sqrt(G*sun.M/mag(sun2.pos-sun.pos))
sun.p = sun.M*vector(0,suninitialp,0)
sun.trail = curve(pos=sun.pos , color=sun.color)

sun2initialp = sqrt(G*sun2.M/mag(sun2.pos-sun.pos))
sun2.p = sun2.M*vector(0,sun2initialp,0)
sun2.trail = curve(pos=sun2.pos , color=sun2.color)

planetinitialp = sqrt(G*planet.M/mag(planet.pos-sun.pos))
planet.p = planet.M*vector(0,planetinitialp,0)
planet.trail = curve(pos=planet.pos , color=planet.color)


t=0
dt=24*3600

scene.autoscale=1

while t < 10000*dt:
  rate(100)
  
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
